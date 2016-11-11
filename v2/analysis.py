#!/usr/bin/env python
# -*- coding: utf-8 -*-

# analysis.py: perform the integrity analyses
#
# Copyright (C) 2014 Politecnico di Torino, Italy
#                    TORSEC group -- http://security.polito.it
#
# Author: Roberto Sassu <roberto.sassu@polito.it>
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library.  If not, see
# <http://www.gnu.org/licenses/>.

from graph import *
from structs import *
from util import *

# Node types for information flow analysis
SUBJ_TCB = 1
SUBJ_NO_TCB = 2
SUBJ_TARGET = 4
OBJ_R_TARGET = 8
OBJ_R_HIGH = 16
OBJ_R_LOW = 32
OBJ_W_TARGET = 64
OBJ_W_HIGH = 128
OBJ_W_LOW = 256


class Analysis(object):
    analysis_list = []

    @classmethod
    def analysis_is_supported(cls, analysis_name):
        return analysis_name in cls.analysis_list

    def __init__(self, analysis_name = None):
        Analysis.analysis_list.append(analysis_name)


class LoadTimeAnalysis(Analysis):
    # possible topics: code, data, code+data
    def edges_types_by_topic(self, topic):
        edge_types = ['pkg', 'digest']
        for item in topic.split('+'):
            if item == 'code':
                edge_types += ['exec']
            elif item == 'data':
                edge_types += ['data_read']

        return edge_types

    def __init__(self, conn, distro, graph, target = '', tcb = [],
                 results_dir = '.', report_id = 0):
        Analysis.__init__(self, 'load-time')
        self.graph = graph
        self.target = target
        self.tcb = tcb
        self.results_dir = results_dir
        self.report_id = report_id

        Digest.execute_digests_query(conn, distro)
        Digest.execute_packages_query(conn, distro)
        Statistics.set_elapsed_time('time_exec_query')

        # digests stats
        self.n_digests_ok = 0
        self.n_digests_not_found = 0
        self.n_digests_fake_lib = 0

        # packages stats
        self.n_packages_ok = 0
        self.n_packages_security = 0
        self.n_packages_not_security = 0
        self.n_packages_unknown = 0

        if len(target) > 0 and len([l for l in Subject.subj_label_dict.keys()
                if selinux_type(l) == target]) == 0:
            raise Exception('Target not found')

        if len(tcb) > 0 and len([l for l in Subject.subj_label_dict.keys()
                if selinux_type(l) in tcb]) != len(tcb):
            raise Exception('One or more TCB subjects not found')

        for digest_obj in Digest.digests_dict.values():
            digest_obj.severity_level = 'ok'

            if digest_obj.is_fake:
                digest_obj.severity_level = 'fake-lib'
                log_info('Fake library %s' % digest_obj.digest_string)
                self.n_digests_fake_lib += 1
                continue

            if digest_obj.event_type == '':
                digest_obj.severity_level = 'not-found'
                self.n_digests_not_found += 1

#            for r in digest_obj.ima_records:
#                hook = int(r.get_data(HOOK_ID_FIELD))
#                mask = int(r.get_data(HOOK_MASK_FIELD))
#                lastwrite = int(r.get_data(LASTWRITE_FIELD))
#
#                if ima_hooks[hook] in ['BPRM_CHECK', 'FILE_MMAP']:
#                    Statistics.inc_stat('n_meas_code')
#                    if digest_obj.severity_level == 'ok':
#                        Statistics.inc_stat('n_meas_code_known')
#                elif ima_hooks[hook] == 'RDWR_VIOLATION_CHECK':
#                    Statistics.inc_stat('n_meas_violation')
#                elif lastwrite == 0 and mask == MAY_READ:
#                    Statistics.inc_stat('n_meas_struct_data')
#                    if digest_obj.severity_level == 'ok':
#                        Statistics.inc_stat('n_meas_struct_data_known')

            if digest_obj.severity_level == 'not-found':
                continue

            self.n_digests_ok += 1
            for pkg_name in digest_obj.pkg_history:
                if digest_obj.pkg_history[pkg_name] is None:
                    pkg = Package.get(pkg_name, None)
                    pkg.update_type = 'unknown'
                    pkg.severity_level = 'unknown'
                    self.graph.add_edge(pkg, digest_obj, edge_tag_pkg = True)
                    continue

                pkg_history = digest_obj.pkg_history[pkg_name]
                severity_level = 'ok'

                for pkg_ver in pkg_history:
                    update_type = pkg_history[pkg_ver]['updatetype']
                    if pkg_ver in digest_obj.pkgs[pkg_name]:
                        pkg = Package.get(pkg_name, pkg_ver)
                        pkg.update_type = update_type
                        pkg.severity_level = severity_level
                        if update_type == 'testing':
                            pkg.severity_level = 'ok'
                        self.graph.add_edge(pkg, digest_obj,
                                            edge_tag_pkg = True)
                        break

                    if propagation_rule(severity_level, update_type) == True:
                        severity_level = update_type

        for package_obj in Package.pkg_dict.values():
            if package_obj.severity_level == 'ok':
                self.n_packages_ok += 1
            elif package_obj.severity_level == 'security':
                self.n_packages_security += 1
            elif package_obj.severity_level == 'unknown':
                self.n_packages_unknown += 1
            else:
                self.n_packages_not_security += 1

        self.starting_nodes = [obj for obj in Digest.digests_dict.values()
                          if obj.severity_level != 'ok']
        self.starting_nodes += Package.pkg_dict.values()

    def propagate_errors(self, topic = 'code+data', target_subjs = None):
        LOAD_TIME_EDGES = self.edges_types_by_topic(topic)

        fake_node = GenericNode()
        for node in self.starting_nodes:
            self.graph.add_edge(fake_node, node, edge_tag_fake_edge = True)

        for parent, child in bfs(self.graph, fake_node,
                LOAD_TIME_EDGES + ['fake_edge']):
            if parent != None and parent != fake_node:
                if parent.severity_level == 'error':
                    break
                if isinstance(child, Subject) and target_subjs is not None and \
                        selinux_type(child.label) not in target_subjs:
                    continue
                if 'propagation' not in self.graph[parent][child]:
                    self.graph[parent][child]['propagation'] = False
                if propagation_rule(child.severity_level,
                        parent.severity_level) == True:
                    child.severity_level = parent.severity_level
                    self.graph[parent][child]['propagation'] = True

        self.graph.remove_node(fake_node)

    def subj_is_selected(self, subj):
        if len(self.target) == 0 and len(self.tcb) == 0:
            return True

        return (len(self.target) > 0 and \
            selinux_type(subj.label) == self.target) or \
            (len(self.tcb) > 0 and selinux_type(subj.label) in self.tcb)

    def view_statistics(self):
        print 'Statistics:'
        print ' - %d Digests: (%d ok, %d not found, %d fake libraries)' % \
            (len(Digest.digests_dict.values()), self.n_digests_ok,
            self.n_digests_not_found, self.n_digests_fake_lib)
        print ' - %d Packages: ' \
            '(%d ok, %d security, %d not security, %d unknown)' % \
            (len(Package.pkg_dict.values()), self.n_packages_ok,
            self.n_packages_security, self.n_packages_not_security,
            self.n_packages_unknown)

    def view_graph(self, only_prop_true = True):
        LOAD_TIME_EDGES = self.edges_types_by_topic('code+data')
        fake_node = GenericNode()
        edges_list = []

        for subj in Subject.subj_label_dict.values():
            if not self.subj_is_selected(subj):
                continue

            subj.draw = True
            self.graph.add_edge(subj, fake_node)
            self.graph[subj][fake_node]['edge_tag_fake_edge'] = True
            self.graph[subj][fake_node]['propagation'] = True

        for parent, child in bfs(self.graph.reverse(), fake_node,
                LOAD_TIME_EDGES + ['fake_edge'], True, only_prop_true):
            if parent != None and parent != fake_node and \
                    hasattr(parent, 'draw'):
                if only_prop_true is True and \
                        parent.severity_level != child.severity_level:
                    continue
                child.draw = True
                edges_list.append((child, parent))

        self.graph.remove_node(fake_node)

#        if subj_list is None and len(edges_list) == 0:
#            edges_list = self.graph.edges()

        g = AGraph(self.graph)
        g.draw('%s/graph-load-time-%d.svg' % (self.results_dir, self.report_id),
               edge_types = LOAD_TIME_EDGES, graph_edges = edges_list)

    def extract_level(self, level):
        return level[1:].split('_')[0]

    def satisfies_requirement(self, requirement, msg = {}):
        level, op = requirement
        severity_level = 'ok'

        for subj in Subject.subj_label_dict.values():
            if not self.subj_is_selected(subj):
                continue

            if subj.severity_level < 0:
                return False

            if propagation_rule(severity_level, subj.severity_level) == True:
                severity_level = subj.severity_level

        if propagation_rule(severity_level, 'name-mismatch'):
            current_level = 'l4_ima_all_ok'
        elif propagation_rule(severity_level, 'security'):
            current_level = 'l3_ima_pkg_not_security_updates'
        elif propagation_rule(severity_level, 'not-found'):
            current_level = 'l2_ima_pkg_security_updates'
        else:
            current_level = 'l1_ima_digest_notfound'

        result = eval('%s %s %s' % (self.extract_level(current_level), op,
            self.extract_level(level)))
        if not result:
            msg['load'] = ['level %s, req %s%s' % \
                (self.extract_level(current_level), op,
                self.extract_level(level))]

        return result

    def satisfies_requirement_priv(self, priv_processes = [], msg = {}):
        result = True
        for subj in Subject.subj_label_dict.values():
            if selinux_type(subj.label) in priv_processes and \
                    subj.severity_level != 'l4_ima_all_ok':
                result = False
                break

        if not result:
            if 'load' not in msg:
                msg['load'] = []
            msg['load'].append('priv check FAIL')

        return result


class RunTimeAnalysis(Analysis):
    def __init__(self, conn, distro, graph, target = '', tcb = '',
                 results_dir = '.', report_id = 0):
        Analysis.__init__(self, 'run-time')
        self.graph = graph
        self.RUN_TIME_EDGES = ['flow']
        self.results_dir = results_dir
        self.report_id = report_id

        self.r = {}
        self.r['s_target'] = set([s for s in Subject.subj_label_dict.values() \
            if selinux_type(s.label) == target])

        if len(target) > 0 and len(self.r['s_target']) != 1:
            raise Exception('Target subject not found')

        self.r['s_tcb'] = set([s for s in Subject.subj_label_dict.values() \
            if selinux_type(s.label) in tcb])

        if len(self.r['s_tcb']) < len(tcb):
            raise Exception('One or more TCB subjects not found')

        self.r['s_no_tcb'] = set([s for s in Subject.subj_label_dict.values() \
            if s not in self.r['s_target'] and s not in self.r['s_tcb']])

        self.r['s_no_tcb']
        flow_edges = [(u, v) for (u, v, d) in self.graph.edges(data = True) \
                      if 'edge_tag_flow' in d]

        self.r['o_target'] = set([v for (u, v) in flow_edges \
            if type(v) == Object and u in self.r['s_target']])
        self.r['o_tcb'] = set([v for (u, v) in flow_edges \
            if type(v) == Object and u in self.r['s_tcb']])
        self.r['o_no_tcb'] = set([v for (u, v) in flow_edges \
            if type(v) == Object and u in self.r['s_no_tcb']])
        self.r['o_target_conflict'] = set([u for (u, v) in flow_edges \
            if type(u) == Object and u in self.r['o_no_tcb'] and \
            v in self.r['s_target']])
        self.r['o_tcb_conflict'] = set([u for (u, v) in flow_edges \
            if type(u) == Object and u in self.r['o_no_tcb'] and \
            v in self.r['s_tcb']])

        conflict_subjs = set()
        conflict_objs = self.r['o_tcb_conflict'] | self.r['o_target_conflict']
        conflicts_sources = self.r['s_no_tcb']
        conflicts_targets = self.r['s_tcb'] | self.r['s_target']

        self.edges_list = []

        # display just one conflict
        for conflict_source in conflicts_sources:
            for conflict_target in conflicts_targets:
                a = set([v for (u, v) in flow_edges if u == conflict_source])
                b = set([u for (u, v) in flow_edges if v == conflict_target])
                c = a & b & conflict_objs

                if len(c) > 0:
                    conflict_subjs.add(conflict_source)
                    self.edges_list.append((conflict_source, list(c)[0]))
                    self.edges_list.append((list(c)[0], conflict_target))

        suggested_subjs = '|'.join([s.label.split(':')[2]
                                    for s in conflict_subjs])
        log_info('Conflicting subjects: %s' % suggested_subjs)

        #self.edges_list.extend([(u, v) for (u, v) in flow_edges \
            #if u in conflicts_sources and v in conflict_objs])
        #self.edges_list.extend([(u, v) for (u, v) in flow_edges \
            #if u in conflict_objs and v in conflicts_targets])

    def satisfies_requirement(self, msg = {}):
        result = (len(self.r['o_tcb_conflict']) == 0 and \
            len(self.r['o_target_conflict']) == 0)
        if not result:
            msg['run'] = ['conflicts: %d TCB, %d target' % \
                (len(self.r['o_tcb_conflict']),
                len(self.r['o_target_conflict']))]

        return result

    def view_graph(self):
        g = AGraph(self.graph)

        clusters = []
        clusters.append((self.r['s_target'],
                         'cluster_TARGET', 'Target'))
        clusters.append((self.r['s_tcb'],
                         'cluster_TCB', 'TCB'))
        clusters.append((self.r['s_no_tcb'],
                         'cluster_OUTSIDE_TCB', 'Outside TCB'))
        clusters.append((self.r['o_tcb_conflict'] | self.r['o_target_conflict'],
                         'cluster_CONFLICTS', 'Conflicts'))

        g.draw('%s/graph-run-time-%d.svg' % (self.results_dir, self.report_id),
               edge_types = self.RUN_TIME_EDGES, graph_edges = self.edges_list,
               clusters = clusters)

    def view_statistics(self):
        print 'Statistics:'
        print ' - %d conflicts: (%d TCB, %d target)' % \
            (len(self.r['o_tcb_conflict']) + len(self.r['o_target_conflict']),
            len(self.r['o_tcb_conflict']), len(self.r['o_target_conflict']))


class ProcTransAnalysis(Analysis):
    def __init__(self, conn, distro, graph, target = '',
                 results_dir = '.', report_id = 0):
        self.graph = graph
        self.results_dir = results_dir
        self.report_id = report_id

        for r in IMARecord.records:
            hook = int(r.get_data(HOOK_ID_FIELD))
            if ima_hooks[hook] != 'BPRM_CHECK':
                continue

            parent_subj = Subject.get(r.get_data(SUBJ_CTX_FIELD))
            child_subj = Subject.get(r.get_data(TARGET_SUBJ_CTX_FIELD))

            if parent_subj == child_subj:
                continue

            graph.add_edge(parent_subj, child_subj, edge_tag_proc_trans = True)

    def get_predecessors(self, subj_label):
        subj_list = [subj for subj in Subject.subj_label_dict.values() \
                if selinux_type(subj.label) == subj_label]
        if len(subj_list) == 0:
            raise Exception('Subject %s not found' % subj_label)

        subj_label_predecessors = set()

        for subj in subj_list:
            for parent, child in bfs(self.graph.reverse(), subj,
                                     ['proc_trans']):
                if parent != None:
                    subj_label_predecessors.add(selinux_type(child.label))

        return subj_label_predecessors

    def view_graph(self, report_id = 0):
        g = AGraph(self.graph)
        
        g.draw('%s/graph-proc-trans-%d.svg' % (self.results_dir,
            self.report_id), edge_types = ['proc_trans'], prog = 'dot')


class ProcWriteAnalysis(Analysis):
    def __init__(self):
        self.subj_list = set()

        for r in IMARecord.records:
            path = r.entry['event_name']
            if path.startswith('/proc/') and \
                    (path.endswith('/current') or path.endswith('/exec')):
                self.subj_list.add(selinux_type(r.subj.label))

    def get_subj_list(self):
        return list(self.subj_list)
