#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ra_verifier.py: execute the integrity analyses
#
# Copyright (C) 2014 Politecnico di Torino, Italy
#                    TORSEC group -- http://security.polito.it
#
# Author: Roberto Sassu <roberto.sassu@polito.it>
#         Tao Su <tao.su@polito.it>
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

import os
import sys
import getopt
import string
import traceback
from connection import *
from log import *
from graph import *
from structs import *
from output import *
from statistics import *
from aggregation import *
from action import *
from analysis import *
import networkx as nx
from suds.client import Client
from parser import IRParser


# if graph type is 'auto', RA Verifier determines the best choice depending
# on available information from IMA measurements list
graph_types = ['auto', 'digests', 'lsm', 'lsm+inode', 'lsm+selinux']

def main(argv):
    host = 'localhost:9160'
    keyspace = 'PackagesDB'
    distro = 'Fedora19'
    analysis = 'load-time'
    graph_type = 'auto'
    selinux = False
    log_file = None
    selinux_policy_path = None
    results_dir = '.'
    log_dir = '/var/www/html/OAT/unknown_log'

    # parse command line
    try:
        opts, args = getopt.getopt(argv, "hH:K:i:q:vl:a:g:s:r:",
                                   ["help", "host=", "keyspace=",
                                   "ima-list=", "distribution=",
                                   "verbose", "log_file=", "analysis=",
                                   "graph_type=", "selinux_policy_path="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt in ("-H", "--host"):
            host = arg
        elif opt in ("-K", "--keyspace"):
            keyspace = arg
        elif opt in ("-i", "--ima-list"):
            measure_list = arg
        elif opt in ("-q", "--distribution"):
            distro = arg
        elif opt in ("-v", "--verbose"):
            set_verbose_mode(True)
        elif opt in ("-l", "--log_file"):
            log_file = arg
        elif opt in ("-a", "--analysis"):
            analysis = arg
        elif opt in ("-g", "--graph_type"):
            if arg not in graph_types:
                print 'Unknown graph type %s' % arg
            graph_type = arg
        elif opt in ("-s", "--selinux_policy_path"):
            selinux_policy_path = arg
        elif opt in ("-r", "--results_dir"):
            results_dir = arg


    distro = os.environ.get('OS', distro)
    analysis = os.environ.get('ANALYSIS', analysis)
    report_url = os.environ.get('URL')
    report_id = int(os.environ.get('IR', 0))

    # check log file exists or not
    log_file = '%s/unknown_log_%s' %(log_dir,report_id);
    if os.path.exists(log_file) is False:
        set_verbose_mode(True);
    else:
        log_file = None;

    log_init(log_file)
    Statistics.start_timer()

    try:
        if report_url is not None and report_id != 0:
            client = Client(report_url)
            report_str = client.service.fetchReport(report_id)
        else:
            fd = open(measure_list, 'r')
            report_str = fd.read()
            fd.close()

        IRParser(report_str)
    except Exception as e:
        log_error('Error opening IR, %s' % e)
        sys.exit(2)

    Statistics.set_elapsed_time('time_parse_ima_list')

    graph = nx.DiGraph()
    conn = DBConnection(keyspace, [host])

    lsm_fields = ['subj', 'obj', 'bprm-subj']
    lsm_inode_fields = lsm_fields + ['lw']

    if 'check-cert' in analysis:
        for item in analysis.split(','):
            if item.startswith('cert_digest'):
                add_known_digest(item.split('=')[1])
                break

    if graph_type == 'auto':
        if IMARecord.default_template() in ['ima', 'ima-ng']:
            graph_type = 'digests'
        elif IMARecord.default_template_contains_fields(lsm_inode_fields):
            graph_type = 'lsm+inode'
        elif IMARecord.default_template_contains_fields(lsm_fields):
            graph_type = 'lsm'

    if graph_type == 'auto':
        print 'Graph type cannot be determined, exiting.'
        sys.exit(2)

    if graph_type == 'digests':
        FileTypeAggregation(conn, distro, graph)
        DBLibrariesAction(conn, distro, graph)
        # no distinction is possible between code and data
    elif graph_type == 'lsm':
        LSMLabelAggregation(conn, distro, graph)
        LSMLabelLoadAction(conn, distro, graph)

        LSMLabelAggregationRunTime(conn, distro, graph)
        LSMLabelFlowAction(conn, distro, graph)
    elif graph_type == 'lsm+inode':
        LSMLabelInodeAggregation(conn, distro, graph)
        LSMLabelLoadAction(conn, distro, graph)
        LSMLabelInodeFlowAction(conn, distro, graph)
    elif graph_type == 'lsm+selinux':
        LSMLabelAggregation(conn, distro, graph)
        LSMLabelSELinuxAction(conn, distro, graph, selinux_policy_path)

    Statistics.set_elapsed_time('time_build_graph')

    # string format: analysis name,analysis parameters
    #  - analysis name: load-time or run-time or load-time+run-time
    #  - analysis parameters:
    #     - both: tcb=subj1|...|subjN
    #     - both: target=subj
    #     - both: draw_graph=True or False (default: False)
    #     - both: priv_check=True or False (default: True)
    #     - load-time: l_params=integrity level|operator
    #                  l_topic=code or data or code+data
    #                  l_prop_only=True or False
    #     - run-time: no other parameters needed
    global_result = True
    analysis_name = analysis.split(',')[0]
    analysis_params = analysis[len(analysis_name) + 1:]
    load_time_requirement = []
    load_time_topic = 'code'
    load_time_prop_only = True
    draw_graph = False
    priv_processes_check = True
    target = ''
    tcb = []
    priv_processes = []
    cert_digest = None

    if analysis_name not in ['load-time', 'run-time', 'load-time+run-time', 'check-cert', 'load-time+check-cert']:
        log_error('Unknown analysis %s' % analysis_name)
        sys.exit(2)

    for item in analysis_params.split(','):
        offset = len(item.split('=')[0]) + 1
        if item.startswith('tcb='):
            tcb = item[offset:].split('|')
        elif item.startswith('target='):
            target = item[offset:]
        elif item.startswith('draw_graph='):
            draw_graph = eval(item[offset:])
        elif item.startswith('priv_check='):
            priv_processes_check = eval(item[offset:])
        elif item.startswith('l_req='):
            load_time_requirement = item[offset:].split('|')
        elif item.startswith('l_topic='):
            load_time_topic = item[offset:]
        elif item.startswith('l_prop_only='):
            load_time_prop_only = eval(item[offset:])
        elif item.startswith('cert_digest='):
            cert_digest = item[offset:]
        else:
            log_error('Unknown parameter %s' % item)
            sys.exit(2)

#   TCB for graph built with LSM labels and last write information
    tcb_init_t_inode = ['sendmail_t', 'initrc_t', 'chronyd_t', 'udev_t',
                        'systemd_tmpfiles_t', 'getty_t', 'NetworkManager_t']


#   TCB for graph build with LSM labels only and open events
    tcb_init_t_lsm = tcb_init_t_inode + ['crond_t', 'system_dbusd_t']

#   TCB for graph build with LSM labels from execution events and
#   interactions inferred from the SELinux policy
    tcb_init_t_selinux = tcb_init_t_lsm + ['insmod_t', 'fsadm_t',
        'kernel_t', 'mount_t', 'setfiles_t', 'iptables_t', 'netutils_t',
        'chkpwd_t', 'ifconfig_t', 'auditctl_t', 'audisp_t', 'policykit_t']

    for item in tcb:
        if 'demo_inode' in tcb:
            tcb.remove('demo_inode')
            tcb += tcb_init_t_inode
        elif 'demo_lsm'in tcb:
            tcb.remove('demo_lsm')
            tcb += tcb_init_t_lsm
        elif 'demo_selinux' in tcb:
            tcb.remove('demo_selinux')
            tcb += tcb_init_t_selinux
        elif 'predecessors' in tcb:
            tcb.remove('predecessors')
            if len(target) == 0:
                log_error('Missing target parameter')
                sys.exit(2)
            try:
                a = ProcTransAnalysis(conn, distro, graph, target = target)
                tcb += list(a.get_predecessors(target))
                if draw_graph:
                    a.view_graph()
            except Exception as e:
                print e
                sys.exit(2)

    # Perform the ProcWrite analysis to see if some processed changed their
    # context or that of the next execve(). If one or more processes are found
    # different actions are done depending on the analyses to be executed.
    # For the load-time analysis, perform the propagation with topic code+data
    # (the configuration files affect the context written to /proc). For the
    # run-time analysis, processes are added to the chosen tcb to detect whether
    # an untrusted process tried to compromise their integrity. Further, if
    # a requirement has been provided for the load-time analysis, this is
    # concatenated with a new requirement on privileged processes: their
    # severity level must be 'ok' because otherwise it would be not possible
    # to correctly associate the code executed and configuration files read
    # to subject labels (privileged processes can take an arbitrary context).
    if priv_processes_check and graph_type != 'digests':
        a = ProcWriteAnalysis()
        priv_processes = a.get_subj_list()
        if (len(target) > 0 or len(tcb) > 0) and target not in priv_processes \
                and len(set(tcb) & set(priv_processes)) == 0:
            tcb.extend(priv_processes)

    error_message = {}
    if 'load-time' in analysis_name:
        try:
            a = LoadTimeAnalysis(conn, distro, graph,
                                 target = target, tcb = tcb,
                                 results_dir = results_dir,
                                 report_id = report_id)

            a.propagate_errors(load_time_topic)
            if len(priv_processes) > 0 and 'data' not in load_time_topic:
                a.propagate_errors('data', priv_processes)

        except Exception as e:
            print e
            traceback.print_exc()
            sys.exit(2)

        if len(load_time_requirement) > 0:
            global_result &= a.satisfies_requirement(load_time_requirement,
                                                     error_message)

            if len(priv_processes) > 0:
                global_result &= a.satisfies_requirement_priv(priv_processes,
                                                              error_message)
#        a.view_statistics()
        if draw_graph:
            a.view_graph(only_prop_true = load_time_prop_only)

        Statistics.set_elapsed_time('time_load_time_analysis')

    if 'run-time' in analysis_name:
        if IMARecord.default_template() in ['ima', 'ima-ng']:
            log_error('Run-time analysis is not supported for template %s' %
                      IMARecord.default_template())
            sys.exit(2)

        if len(tcb) == 0 and len(target) == 0:
            log_error('Missing parameters (tcb, target) for run-time analysis')
            sys.exit(2)

        try:
            a = RunTimeAnalysis(conn, distro, graph, target = target,
                                tcb = tcb, results_dir = results_dir,
                                report_id = report_id)
        except Exception as e:
            print e
            sys.exit(2)

        global_result &= a.satisfies_requirement(error_message)

#        a.view_statistics()
        if draw_graph:
            a.view_graph()

        Statistics.set_elapsed_time('time_run_time_analysis')
    if 'check-cert' in analysis_name:
        result = cert_digest in Digest.digests_dict.keys()
        if not result:
            error_message['cert'] = ['not found']
        global_result &= result

    Statistics.set_current_time('time_total')
    log_info('%s (%s/%s)\n%s (%s/%s)\n%s\n%s\n' %(Statistics.get_stat('n_meas_code'),
                                 Statistics.get_stat('n_meas_code_known'),
                                 Statistics.get_stat('n_meas_code') - Statistics.get_stat('n_meas_code_known'),
                                 Statistics.get_stat('n_meas_struct_data'),
                                 Statistics.get_stat('n_meas_struct_data_known'),
                                 Statistics.get_stat('n_meas_struct_data') - Statistics.get_stat('n_meas_struct_data_known'),
                                 Statistics.get_stat('n_tot_meas') - \
                                 Statistics.get_stat('n_meas_code') - \
                                 Statistics.get_stat('n_meas_struct_data'),
                                 Statistics.get_stat('n_tot_meas')))
    log_info('%s\n%s\n%s\n%s\n%s\n%s' %(Statistics.get_stat('time_parse_ima_list'),
                                        Statistics.get_stat('time_build_graph'),
                                        Statistics.get_stat('time_exec_query'),
                                        Statistics.get_stat('time_load_time_analysis'),
                                        Statistics.get_stat('time_run_time_analysis'),
                                        Statistics.get_stat('time_total')))

    print '\n'.join([key + ') ' + '; '.join(error_message[key]) \
        for key in error_message])
    log_info( '\n'.join([key + ') ' + '; '.join(error_message[key]) for key in error_message]))
    log_end()

    return global_result

if __name__ == '__main__':
    result = main(sys.argv[1:])
    if result is False:
        sys.exit(1)

    sys.exit(0)
