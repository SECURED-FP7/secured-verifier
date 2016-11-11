# ./ir_simple_parser.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:054711f851318b45ad8144ee159e4ecdbeae047a
# Generated 2014-02-06 17:58:58.706141 by PyXB version 1.2.3
# Namespace http://www.trustedcomputinggroup.org/XML/SCHEMA/Simple_Object_v1_0#

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:ef3b1b0a-8f4f-11e3-a96a-000ffe77a6bc')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.3'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import _ds as _ImportedBinding__ds
import pyxb.binding.datatypes
import _core as _ImportedBinding__core

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(u'http://www.trustedcomputinggroup.org/XML/SCHEMA/Simple_Object_v1_0#', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, unicode):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Complex type {http://www.trustedcomputinggroup.org/XML/SCHEMA/Simple_Object_v1_0#}ValuesType with content type ELEMENT_ONLY
class ValuesType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.trustedcomputinggroup.org/XML/SCHEMA/Simple_Object_v1_0#}ValuesType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ValuesType')
    _XSDLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Simple_Object_v1_0.xsd', 5, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.trustedcomputinggroup.org/XML/SCHEMA/Simple_Object_v1_0#}Hash uses Python identifier Hash
    __Hash = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Hash'), 'Hash', '__httpwww_trustedcomputinggroup_orgXMLSCHEMASimple_Object_v1_0_ValuesType_httpwww_trustedcomputinggroup_orgXMLSCHEMASimple_Object_v1_0Hash', True, pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Simple_Object_v1_0.xsd', 7, 3), )

    
    Hash = property(__Hash.value, __Hash.set, None, None)

    
    # Attribute ID uses Python identifier ID
    __ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ID'), 'ID', '__httpwww_trustedcomputinggroup_orgXMLSCHEMASimple_Object_v1_0_ValuesType_ID', pyxb.binding.datatypes.ID)
    __ID._DeclarationLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Simple_Object_v1_0.xsd', 9, 2)
    __ID._UseLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Simple_Object_v1_0.xsd', 9, 2)
    
    ID = property(__ID.value, __ID.set, None, None)

    
    # Attribute Name uses Python identifier Name
    __Name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Name'), 'Name', '__httpwww_trustedcomputinggroup_orgXMLSCHEMASimple_Object_v1_0_ValuesType_Name', pyxb.binding.datatypes.normalizedString)
    __Name._DeclarationLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Simple_Object_v1_0.xsd', 10, 2)
    __Name._UseLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Simple_Object_v1_0.xsd', 10, 2)
    
    Name = property(__Name.value, __Name.set, None, None)

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Type'), 'Type', '__httpwww_trustedcomputinggroup_orgXMLSCHEMASimple_Object_v1_0_ValuesType_Type', pyxb.binding.datatypes.anySimpleType)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Simple_Object_v1_0.xsd', 11, 2)
    __Type._UseLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Simple_Object_v1_0.xsd', 11, 2)
    
    Type = property(__Type.value, __Type.set, None, None)

    
    # Attribute Ref uses Python identifier Ref
    __Ref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Ref'), 'Ref', '__httpwww_trustedcomputinggroup_orgXMLSCHEMASimple_Object_v1_0_ValuesType_Ref', pyxb.binding.datatypes.anyURI)
    __Ref._DeclarationLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Simple_Object_v1_0.xsd', 12, 2)
    __Ref._UseLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Simple_Object_v1_0.xsd', 12, 2)
    
    Ref = property(__Ref.value, __Ref.set, None, None)

    
    # Attribute Image uses Python identifier Image
    __Image = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Image'), 'Image', '__httpwww_trustedcomputinggroup_orgXMLSCHEMASimple_Object_v1_0_ValuesType_Image', pyxb.binding.datatypes.base64Binary)
    __Image._DeclarationLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Simple_Object_v1_0.xsd', 13, 2)
    __Image._UseLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Simple_Object_v1_0.xsd', 13, 2)
    
    Image = property(__Image.value, __Image.set, None, None)

    
    # Attribute LocalRef uses Python identifier LocalRef
    __LocalRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'LocalRef'), 'LocalRef', '__httpwww_trustedcomputinggroup_orgXMLSCHEMASimple_Object_v1_0_ValuesType_LocalRef', pyxb.binding.datatypes.IDREF)
    __LocalRef._DeclarationLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Simple_Object_v1_0.xsd', 14, 2)
    __LocalRef._UseLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Simple_Object_v1_0.xsd', 14, 2)
    
    LocalRef = property(__LocalRef.value, __LocalRef.set, None, None)

    _ElementMap.update({
        __Hash.name() : __Hash
    })
    _AttributeMap.update({
        __ID.name() : __ID,
        __Name.name() : __Name,
        __Type.name() : __Type,
        __Ref.name() : __Ref,
        __Image.name() : __Image,
        __LocalRef.name() : __LocalRef
    })
Namespace.addCategoryObject('typeBinding', u'ValuesType', ValuesType)


# Complex type {http://www.trustedcomputinggroup.org/XML/SCHEMA/Simple_Object_v1_0#}SimpleObjectType with content type ELEMENT_ONLY
class SimpleObjectType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.trustedcomputinggroup.org/XML/SCHEMA/Simple_Object_v1_0#}SimpleObjectType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SimpleObjectType')
    _XSDLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Simple_Object_v1_0.xsd', 16, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.trustedcomputinggroup.org/XML/SCHEMA/Simple_Object_v1_0#}CompositeHash uses Python identifier CompositeHash
    __CompositeHash = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'CompositeHash'), 'CompositeHash', '__httpwww_trustedcomputinggroup_orgXMLSCHEMASimple_Object_v1_0_SimpleObjectType_httpwww_trustedcomputinggroup_orgXMLSCHEMASimple_Object_v1_0CompositeHash', True, pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Simple_Object_v1_0.xsd', 18, 3), )

    
    CompositeHash = property(__CompositeHash.value, __CompositeHash.set, None, None)

    
    # Element {http://www.trustedcomputinggroup.org/XML/SCHEMA/Simple_Object_v1_0#}TransformMethod uses Python identifier TransformMethod
    __TransformMethod = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'TransformMethod'), 'TransformMethod', '__httpwww_trustedcomputinggroup_orgXMLSCHEMASimple_Object_v1_0_SimpleObjectType_httpwww_trustedcomputinggroup_orgXMLSCHEMASimple_Object_v1_0TransformMethod', True, pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Simple_Object_v1_0.xsd', 19, 3), )

    
    TransformMethod = property(__TransformMethod.value, __TransformMethod.set, None, None)

    
    # Element {http://www.trustedcomputinggroup.org/XML/SCHEMA/Simple_Object_v1_0#}DigestMethods uses Python identifier DigestMethods
    __DigestMethods = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'DigestMethods'), 'DigestMethods', '__httpwww_trustedcomputinggroup_orgXMLSCHEMASimple_Object_v1_0_SimpleObjectType_httpwww_trustedcomputinggroup_orgXMLSCHEMASimple_Object_v1_0DigestMethods', True, pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Simple_Object_v1_0.xsd', 20, 3), )

    
    DigestMethods = property(__DigestMethods.value, __DigestMethods.set, None, None)

    
    # Element {http://www.trustedcomputinggroup.org/XML/SCHEMA/Simple_Object_v1_0#}Objects uses Python identifier Objects
    __Objects = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Objects'), 'Objects', '__httpwww_trustedcomputinggroup_orgXMLSCHEMASimple_Object_v1_0_SimpleObjectType_httpwww_trustedcomputinggroup_orgXMLSCHEMASimple_Object_v1_0Objects', True, pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Simple_Object_v1_0.xsd', 21, 3), )

    
    Objects = property(__Objects.value, __Objects.set, None, None)

    
    # Attribute Id uses Python identifier Id
    __Id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Id'), 'Id', '__httpwww_trustedcomputinggroup_orgXMLSCHEMASimple_Object_v1_0_SimpleObjectType_Id', pyxb.binding.datatypes.ID)
    __Id._DeclarationLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Simple_Object_v1_0.xsd', 23, 2)
    __Id._UseLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Simple_Object_v1_0.xsd', 23, 2)
    
    Id = property(__Id.value, __Id.set, None, None)

    _ElementMap.update({
        __CompositeHash.name() : __CompositeHash,
        __TransformMethod.name() : __TransformMethod,
        __DigestMethods.name() : __DigestMethods,
        __Objects.name() : __Objects
    })
    _AttributeMap.update({
        __Id.name() : __Id
    })
Namespace.addCategoryObject('typeBinding', u'SimpleObjectType', SimpleObjectType)


SimpleObject = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SimpleObject'), SimpleObjectType, location=pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Simple_Object_v1_0.xsd', 25, 1))
Namespace.addCategoryObject('elementBinding', SimpleObject.name().localName(), SimpleObject)



ValuesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Hash'), _ImportedBinding__core.DigestValueType, scope=ValuesType, location=pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Simple_Object_v1_0.xsd', 7, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ValuesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Hash')), pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Simple_Object_v1_0.xsd', 7, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ValuesType._Automaton = _BuildAutomaton()




SimpleObjectType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CompositeHash'), _ImportedBinding__core.HashType, scope=SimpleObjectType, location=pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Simple_Object_v1_0.xsd', 18, 3)))

SimpleObjectType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TransformMethod'), _ImportedBinding__ds.TransformType, scope=SimpleObjectType, location=pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Simple_Object_v1_0.xsd', 19, 3)))

SimpleObjectType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DigestMethods'), _ImportedBinding__core.DigestMethodType, scope=SimpleObjectType, location=pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Simple_Object_v1_0.xsd', 20, 3)))

SimpleObjectType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Objects'), ValuesType, scope=SimpleObjectType, location=pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Simple_Object_v1_0.xsd', 21, 3)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Simple_Object_v1_0.xsd', 18, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Simple_Object_v1_0.xsd', 19, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Simple_Object_v1_0.xsd', 20, 3))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleObjectType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CompositeHash')), pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Simple_Object_v1_0.xsd', 18, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleObjectType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TransformMethod')), pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Simple_Object_v1_0.xsd', 19, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleObjectType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DigestMethods')), pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Simple_Object_v1_0.xsd', 20, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SimpleObjectType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Objects')), pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Simple_Object_v1_0.xsd', 21, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SimpleObjectType._Automaton = _BuildAutomaton_()

