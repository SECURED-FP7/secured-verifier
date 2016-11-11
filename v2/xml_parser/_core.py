# ./_core.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:0535f8587f0130beb518ca33e00ce1b8d692b87e
# Generated 2014-02-06 17:58:58.705770 by PyXB version 1.2.3
# Namespace http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1# [xmlns:core]

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

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(u'http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_ds = _ImportedBinding__ds.Namespace
_Namespace_ds.configureCategories(['typeBinding', 'elementBinding'])

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


# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.normalizedString):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 120, 4)
    _Documentation = None
STD_ANON._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4L))
STD_ANON._InitializeFacetMap(STD_ANON._CF_maxLength)

# Complex type {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}AssertionType with content type ELEMENT_ONLY
class AssertionType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}AssertionType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'AssertionType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 6, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Id uses Python identifier Id
    __Id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Id'), 'Id', '__httpwww_trustedcomputinggroup_orgXMLSCHEMACore_Integrity_v1_0_1_AssertionType_Id', pyxb.binding.datatypes.ID)
    __Id._DeclarationLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 10, 2)
    __Id._UseLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 10, 2)
    
    Id = property(__Id.value, __Id.set, None, None)

    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Id.name() : __Id
    })
Namespace.addCategoryObject('typeBinding', u'AssertionType', AssertionType)


# Complex type {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}ComponentIDType with content type ELEMENT_ONLY
class ComponentIDType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}ComponentIDType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ComponentIDType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 12, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}VendorID uses Python identifier VendorID
    __VendorID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'VendorID'), 'VendorID', '__httpwww_trustedcomputinggroup_orgXMLSCHEMACore_Integrity_v1_0_1_ComponentIDType_httpwww_trustedcomputinggroup_orgXMLSCHEMACore_Integrity_v1_0_1VendorID', False, pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 14, 3), )

    
    VendorID = property(__VendorID.value, __VendorID.set, None, None)

    
    # Attribute Id uses Python identifier Id
    __Id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Id'), 'Id', '__httpwww_trustedcomputinggroup_orgXMLSCHEMACore_Integrity_v1_0_1_ComponentIDType_Id', pyxb.binding.datatypes.ID, required=True)
    __Id._DeclarationLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 16, 2)
    __Id._UseLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 16, 2)
    
    Id = property(__Id.value, __Id.set, None, None)

    
    # Attribute SimpleName uses Python identifier SimpleName
    __SimpleName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'SimpleName'), 'SimpleName', '__httpwww_trustedcomputinggroup_orgXMLSCHEMACore_Integrity_v1_0_1_ComponentIDType_SimpleName', pyxb.binding.datatypes.normalizedString)
    __SimpleName._DeclarationLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 17, 2)
    __SimpleName._UseLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 17, 2)
    
    SimpleName = property(__SimpleName.value, __SimpleName.set, None, None)

    
    # Attribute ModelName uses Python identifier ModelName
    __ModelName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ModelName'), 'ModelName', '__httpwww_trustedcomputinggroup_orgXMLSCHEMACore_Integrity_v1_0_1_ComponentIDType_ModelName', pyxb.binding.datatypes.normalizedString)
    __ModelName._DeclarationLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 18, 2)
    __ModelName._UseLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 18, 2)
    
    ModelName = property(__ModelName.value, __ModelName.set, None, None)

    
    # Attribute ModelNumber uses Python identifier ModelNumber
    __ModelNumber = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ModelNumber'), 'ModelNumber', '__httpwww_trustedcomputinggroup_orgXMLSCHEMACore_Integrity_v1_0_1_ComponentIDType_ModelNumber', pyxb.binding.datatypes.normalizedString)
    __ModelNumber._DeclarationLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 19, 2)
    __ModelNumber._UseLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 19, 2)
    
    ModelNumber = property(__ModelNumber.value, __ModelNumber.set, None, None)

    
    # Attribute ModelSerialNumber uses Python identifier ModelSerialNumber
    __ModelSerialNumber = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ModelSerialNumber'), 'ModelSerialNumber', '__httpwww_trustedcomputinggroup_orgXMLSCHEMACore_Integrity_v1_0_1_ComponentIDType_ModelSerialNumber', pyxb.binding.datatypes.normalizedString)
    __ModelSerialNumber._DeclarationLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 20, 2)
    __ModelSerialNumber._UseLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 20, 2)
    
    ModelSerialNumber = property(__ModelSerialNumber.value, __ModelSerialNumber.set, None, None)

    
    # Attribute ModelSystemClass uses Python identifier ModelSystemClass
    __ModelSystemClass = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ModelSystemClass'), 'ModelSystemClass', '__httpwww_trustedcomputinggroup_orgXMLSCHEMACore_Integrity_v1_0_1_ComponentIDType_ModelSystemClass', pyxb.binding.datatypes.normalizedString)
    __ModelSystemClass._DeclarationLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 21, 2)
    __ModelSystemClass._UseLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 21, 2)
    
    ModelSystemClass = property(__ModelSystemClass.value, __ModelSystemClass.set, None, None)

    
    # Attribute VersionMajor uses Python identifier VersionMajor
    __VersionMajor = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'VersionMajor'), 'VersionMajor', '__httpwww_trustedcomputinggroup_orgXMLSCHEMACore_Integrity_v1_0_1_ComponentIDType_VersionMajor', pyxb.binding.datatypes.integer)
    __VersionMajor._DeclarationLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 22, 2)
    __VersionMajor._UseLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 22, 2)
    
    VersionMajor = property(__VersionMajor.value, __VersionMajor.set, None, None)

    
    # Attribute VersionMinor uses Python identifier VersionMinor
    __VersionMinor = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'VersionMinor'), 'VersionMinor', '__httpwww_trustedcomputinggroup_orgXMLSCHEMACore_Integrity_v1_0_1_ComponentIDType_VersionMinor', pyxb.binding.datatypes.integer)
    __VersionMinor._DeclarationLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 23, 2)
    __VersionMinor._UseLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 23, 2)
    
    VersionMinor = property(__VersionMinor.value, __VersionMinor.set, None, None)

    
    # Attribute VersionBuild uses Python identifier VersionBuild
    __VersionBuild = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'VersionBuild'), 'VersionBuild', '__httpwww_trustedcomputinggroup_orgXMLSCHEMACore_Integrity_v1_0_1_ComponentIDType_VersionBuild', pyxb.binding.datatypes.integer)
    __VersionBuild._DeclarationLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 24, 2)
    __VersionBuild._UseLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 24, 2)
    
    VersionBuild = property(__VersionBuild.value, __VersionBuild.set, None, None)

    
    # Attribute VersionString uses Python identifier VersionString
    __VersionString = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'VersionString'), 'VersionString', '__httpwww_trustedcomputinggroup_orgXMLSCHEMACore_Integrity_v1_0_1_ComponentIDType_VersionString', pyxb.binding.datatypes.normalizedString)
    __VersionString._DeclarationLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 25, 2)
    __VersionString._UseLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 25, 2)
    
    VersionString = property(__VersionString.value, __VersionString.set, None, None)

    
    # Attribute MfgDate uses Python identifier MfgDate
    __MfgDate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'MfgDate'), 'MfgDate', '__httpwww_trustedcomputinggroup_orgXMLSCHEMACore_Integrity_v1_0_1_ComponentIDType_MfgDate', pyxb.binding.datatypes.dateTime)
    __MfgDate._DeclarationLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 26, 2)
    __MfgDate._UseLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 26, 2)
    
    MfgDate = property(__MfgDate.value, __MfgDate.set, None, None)

    
    # Attribute PatchLevel uses Python identifier PatchLevel
    __PatchLevel = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'PatchLevel'), 'PatchLevel', '__httpwww_trustedcomputinggroup_orgXMLSCHEMACore_Integrity_v1_0_1_ComponentIDType_PatchLevel', pyxb.binding.datatypes.normalizedString)
    __PatchLevel._DeclarationLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 27, 2)
    __PatchLevel._UseLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 27, 2)
    
    PatchLevel = property(__PatchLevel.value, __PatchLevel.set, None, None)

    
    # Attribute DiscretePatches uses Python identifier DiscretePatches
    __DiscretePatches = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'DiscretePatches'), 'DiscretePatches', '__httpwww_trustedcomputinggroup_orgXMLSCHEMACore_Integrity_v1_0_1_ComponentIDType_DiscretePatches', pyxb.binding.datatypes.NMTOKENS)
    __DiscretePatches._DeclarationLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 28, 2)
    __DiscretePatches._UseLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 28, 2)
    
    DiscretePatches = property(__DiscretePatches.value, __DiscretePatches.set, None, None)

    _ElementMap.update({
        __VendorID.name() : __VendorID
    })
    _AttributeMap.update({
        __Id.name() : __Id,
        __SimpleName.name() : __SimpleName,
        __ModelName.name() : __ModelName,
        __ModelNumber.name() : __ModelNumber,
        __ModelSerialNumber.name() : __ModelSerialNumber,
        __ModelSystemClass.name() : __ModelSystemClass,
        __VersionMajor.name() : __VersionMajor,
        __VersionMinor.name() : __VersionMinor,
        __VersionBuild.name() : __VersionBuild,
        __VersionString.name() : __VersionString,
        __MfgDate.name() : __MfgDate,
        __PatchLevel.name() : __PatchLevel,
        __DiscretePatches.name() : __DiscretePatches
    })
Namespace.addCategoryObject('typeBinding', u'ComponentIDType', ComponentIDType)


# Complex type {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}ComponentRefType with content type ELEMENT_ONLY
class ComponentRefType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}ComponentRefType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ComponentRefType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 30, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}ComponentID uses Python identifier ComponentID
    __ComponentID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ComponentID'), 'ComponentID', '__httpwww_trustedcomputinggroup_orgXMLSCHEMACore_Integrity_v1_0_1_ComponentRefType_httpwww_trustedcomputinggroup_orgXMLSCHEMACore_Integrity_v1_0_1ComponentID', False, pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 32, 3), )

    
    ComponentID = property(__ComponentID.value, __ComponentID.set, None, None)

    
    # Element {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}ComponentIDREF uses Python identifier ComponentIDREF
    __ComponentIDREF = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ComponentIDREF'), 'ComponentIDREF', '__httpwww_trustedcomputinggroup_orgXMLSCHEMACore_Integrity_v1_0_1_ComponentRefType_httpwww_trustedcomputinggroup_orgXMLSCHEMACore_Integrity_v1_0_1ComponentIDREF', False, pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 39, 3), )

    
    ComponentIDREF = property(__ComponentIDREF.value, __ComponentIDREF.set, None, None)

    
    # Attribute ComponentLoc uses Python identifier ComponentLoc
    __ComponentLoc = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ComponentLoc'), 'ComponentLoc', '__httpwww_trustedcomputinggroup_orgXMLSCHEMACore_Integrity_v1_0_1_ComponentRefType_ComponentLoc', pyxb.binding.datatypes.anyURI)
    __ComponentLoc._DeclarationLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 41, 2)
    __ComponentLoc._UseLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 41, 2)
    
    ComponentLoc = property(__ComponentLoc.value, __ComponentLoc.set, None, None)

    _ElementMap.update({
        __ComponentID.name() : __ComponentID,
        __ComponentIDREF.name() : __ComponentIDREF
    })
    _AttributeMap.update({
        __ComponentLoc.name() : __ComponentLoc
    })
Namespace.addCategoryObject('typeBinding', u'ComponentRefType', ComponentRefType)


# Complex type {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}ConfidenceValueType with content type EMPTY
class ConfidenceValueType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}ConfidenceValueType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ConfidenceValueType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 43, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Score uses Python identifier Score
    __Score = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Score'), 'Score', '__httpwww_trustedcomputinggroup_orgXMLSCHEMACore_Integrity_v1_0_1_ConfidenceValueType_Score', pyxb.binding.datatypes.integer, required=True)
    __Score._DeclarationLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 44, 2)
    __Score._UseLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 44, 2)
    
    Score = property(__Score.value, __Score.set, None, None)

    
    # Attribute Basis uses Python identifier Basis
    __Basis = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Basis'), 'Basis', '__httpwww_trustedcomputinggroup_orgXMLSCHEMACore_Integrity_v1_0_1_ConfidenceValueType_Basis', pyxb.binding.datatypes.integer, required=True)
    __Basis._DeclarationLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 45, 2)
    __Basis._UseLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 45, 2)
    
    Basis = property(__Basis.value, __Basis.set, None, None)

    
    # Attribute Authority uses Python identifier Authority
    __Authority = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Authority'), 'Authority', '__httpwww_trustedcomputinggroup_orgXMLSCHEMACore_Integrity_v1_0_1_ConfidenceValueType_Authority', pyxb.binding.datatypes.anyURI)
    __Authority._DeclarationLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 46, 2)
    __Authority._UseLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 46, 2)
    
    Authority = property(__Authority.value, __Authority.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Score.name() : __Score,
        __Basis.name() : __Basis,
        __Authority.name() : __Authority
    })
Namespace.addCategoryObject('typeBinding', u'ConfidenceValueType', ConfidenceValueType)


# Complex type {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}HashedURIType with content type ELEMENT_ONLY
class HashedURIType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}HashedURIType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'HashedURIType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 64, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}UriHash uses Python identifier UriHash
    __UriHash = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'UriHash'), 'UriHash', '__httpwww_trustedcomputinggroup_orgXMLSCHEMACore_Integrity_v1_0_1_HashedURIType_httpwww_trustedcomputinggroup_orgXMLSCHEMACore_Integrity_v1_0_1UriHash', True, pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 66, 3), )

    
    UriHash = property(__UriHash.value, __UriHash.set, None, None)

    
    # Attribute UriValue uses Python identifier UriValue
    __UriValue = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'UriValue'), 'UriValue', '__httpwww_trustedcomputinggroup_orgXMLSCHEMACore_Integrity_v1_0_1_HashedURIType_UriValue', pyxb.binding.datatypes.anyURI, required=True)
    __UriValue._DeclarationLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 68, 2)
    __UriValue._UseLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 68, 2)
    
    UriValue = property(__UriValue.value, __UriValue.set, None, None)

    _ElementMap.update({
        __UriHash.name() : __UriHash
    })
    _AttributeMap.update({
        __UriValue.name() : __UriValue
    })
Namespace.addCategoryObject('typeBinding', u'HashedURIType', HashedURIType)


# Complex type {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}IntegrityManifestType with content type ELEMENT_ONLY
class IntegrityManifestType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}IntegrityManifestType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'IntegrityManifestType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 77, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}ComponentID uses Python identifier ComponentID
    __ComponentID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ComponentID'), 'ComponentID', '__httpwww_trustedcomputinggroup_orgXMLSCHEMACore_Integrity_v1_0_1_IntegrityManifestType_httpwww_trustedcomputinggroup_orgXMLSCHEMACore_Integrity_v1_0_1ComponentID', False, pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 79, 3), )

    
    ComponentID = property(__ComponentID.value, __ComponentID.set, None, None)

    
    # Element {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}SignerInfo uses Python identifier SignerInfo
    __SignerInfo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'SignerInfo'), 'SignerInfo', '__httpwww_trustedcomputinggroup_orgXMLSCHEMACore_Integrity_v1_0_1_IntegrityManifestType_httpwww_trustedcomputinggroup_orgXMLSCHEMACore_Integrity_v1_0_1SignerInfo', False, pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 80, 3), )

    
    SignerInfo = property(__SignerInfo.value, __SignerInfo.set, None, None)

    
    # Element {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}ConfidenceValue uses Python identifier ConfidenceValue
    __ConfidenceValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ConfidenceValue'), 'ConfidenceValue', '__httpwww_trustedcomputinggroup_orgXMLSCHEMACore_Integrity_v1_0_1_IntegrityManifestType_httpwww_trustedcomputinggroup_orgXMLSCHEMACore_Integrity_v1_0_1ConfidenceValue', False, pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 81, 3), )

    
    ConfidenceValue = property(__ConfidenceValue.value, __ConfidenceValue.set, None, None)

    
    # Element {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}Collector uses Python identifier Collector
    __Collector = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Collector'), 'Collector', '__httpwww_trustedcomputinggroup_orgXMLSCHEMACore_Integrity_v1_0_1_IntegrityManifestType_httpwww_trustedcomputinggroup_orgXMLSCHEMACore_Integrity_v1_0_1Collector', False, pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 82, 3), )

    
    Collector = property(__Collector.value, __Collector.set, None, None)

    
    # Element {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}TransformMethod uses Python identifier TransformMethod
    __TransformMethod = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'TransformMethod'), 'TransformMethod', '__httpwww_trustedcomputinggroup_orgXMLSCHEMACore_Integrity_v1_0_1_IntegrityManifestType_httpwww_trustedcomputinggroup_orgXMLSCHEMACore_Integrity_v1_0_1TransformMethod', True, pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 83, 3), )

    
    TransformMethod = property(__TransformMethod.value, __TransformMethod.set, None, None)

    
    # Element {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}DigestMethod uses Python identifier DigestMethod
    __DigestMethod = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'DigestMethod'), 'DigestMethod', '__httpwww_trustedcomputinggroup_orgXMLSCHEMACore_Integrity_v1_0_1_IntegrityManifestType_httpwww_trustedcomputinggroup_orgXMLSCHEMACore_Integrity_v1_0_1DigestMethod', True, pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 84, 3), )

    
    DigestMethod = property(__DigestMethod.value, __DigestMethod.set, None, None)

    
    # Element {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}Values uses Python identifier Values
    __Values = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Values'), 'Values', '__httpwww_trustedcomputinggroup_orgXMLSCHEMACore_Integrity_v1_0_1_IntegrityManifestType_httpwww_trustedcomputinggroup_orgXMLSCHEMACore_Integrity_v1_0_1Values', True, pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 85, 3), )

    
    Values = property(__Values.value, __Values.set, None, None)

    
    # Element {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}AssertionInfo uses Python identifier AssertionInfo
    __AssertionInfo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'AssertionInfo'), 'AssertionInfo', '__httpwww_trustedcomputinggroup_orgXMLSCHEMACore_Integrity_v1_0_1_IntegrityManifestType_httpwww_trustedcomputinggroup_orgXMLSCHEMACore_Integrity_v1_0_1AssertionInfo', True, pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 86, 3), )

    
    AssertionInfo = property(__AssertionInfo.value, __AssertionInfo.set, None, None)

    
    # Element {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}PlatformClass uses Python identifier PlatformClass
    __PlatformClass = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'PlatformClass'), 'PlatformClass', '__httpwww_trustedcomputinggroup_orgXMLSCHEMACore_Integrity_v1_0_1_IntegrityManifestType_httpwww_trustedcomputinggroup_orgXMLSCHEMACore_Integrity_v1_0_1PlatformClass', False, pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 87, 3), )

    
    PlatformClass = property(__PlatformClass.value, __PlatformClass.set, None, None)

    
    # Element {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}SubComponents uses Python identifier SubComponents
    __SubComponents = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'SubComponents'), 'SubComponents', '__httpwww_trustedcomputinggroup_orgXMLSCHEMACore_Integrity_v1_0_1_IntegrityManifestType_httpwww_trustedcomputinggroup_orgXMLSCHEMACore_Integrity_v1_0_1SubComponents', True, pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 88, 3), )

    
    SubComponents = property(__SubComponents.value, __SubComponents.set, None, None)

    
    # Attribute Id uses Python identifier Id
    __Id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Id'), 'Id', '__httpwww_trustedcomputinggroup_orgXMLSCHEMACore_Integrity_v1_0_1_IntegrityManifestType_Id', pyxb.binding.datatypes.ID, required=True)
    __Id._DeclarationLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 90, 2)
    __Id._UseLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 90, 2)
    
    Id = property(__Id.value, __Id.set, None, None)

    
    # Attribute RevLevel uses Python identifier RevLevel
    __RevLevel = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'RevLevel'), 'RevLevel', '__httpwww_trustedcomputinggroup_orgXMLSCHEMACore_Integrity_v1_0_1_IntegrityManifestType_RevLevel', pyxb.binding.datatypes.integer, required=True)
    __RevLevel._DeclarationLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 91, 2)
    __RevLevel._UseLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 91, 2)
    
    RevLevel = property(__RevLevel.value, __RevLevel.set, None, None)

    _ElementMap.update({
        __ComponentID.name() : __ComponentID,
        __SignerInfo.name() : __SignerInfo,
        __ConfidenceValue.name() : __ConfidenceValue,
        __Collector.name() : __Collector,
        __TransformMethod.name() : __TransformMethod,
        __DigestMethod.name() : __DigestMethod,
        __Values.name() : __Values,
        __AssertionInfo.name() : __AssertionInfo,
        __PlatformClass.name() : __PlatformClass,
        __SubComponents.name() : __SubComponents
    })
    _AttributeMap.update({
        __Id.name() : __Id,
        __RevLevel.name() : __RevLevel
    })
Namespace.addCategoryObject('typeBinding', u'IntegrityManifestType', IntegrityManifestType)


# Complex type {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}PlatformClassType with content type EMPTY
class PlatformClassType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}PlatformClassType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'PlatformClassType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 93, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Class uses Python identifier Class
    __Class = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Class'), 'Class', '__httpwww_trustedcomputinggroup_orgXMLSCHEMACore_Integrity_v1_0_1_PlatformClassType_Class', pyxb.binding.datatypes.anyURI)
    __Class._DeclarationLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 94, 2)
    __Class._UseLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 94, 2)
    
    Class = property(__Class.value, __Class.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Class.name() : __Class
    })
Namespace.addCategoryObject('typeBinding', u'PlatformClassType', PlatformClassType)


# Complex type {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}SignerInfoType with content type ELEMENT_ONLY
class SignerInfoType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}SignerInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SignerInfoType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 96, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}SigningComponent uses Python identifier SigningComponent
    __SigningComponent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'SigningComponent'), 'SigningComponent', '__httpwww_trustedcomputinggroup_orgXMLSCHEMACore_Integrity_v1_0_1_SignerInfoType_httpwww_trustedcomputinggroup_orgXMLSCHEMACore_Integrity_v1_0_1SigningComponent', False, pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 99, 3), )

    
    SigningComponent = property(__SigningComponent.value, __SigningComponent.set, None, None)

    
    # Element {http://www.w3.org/2000/09/xmldsig#}Signature uses Python identifier Signature
    __Signature = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ds, u'Signature'), 'Signature', '__httpwww_trustedcomputinggroup_orgXMLSCHEMACore_Integrity_v1_0_1_SignerInfoType_httpwww_w3_org200009xmldsigSignature', False, pyxb.utils.utility.Location(u'http://www.w3.org/TR/2002/REC-xmldsig-core-20020212/xmldsig-core-schema.xsd', 43, 0), )

    
    Signature = property(__Signature.value, __Signature.set, None, None)

    
    # Attribute DateTime uses Python identifier DateTime
    __DateTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'DateTime'), 'DateTime', '__httpwww_trustedcomputinggroup_orgXMLSCHEMACore_Integrity_v1_0_1_SignerInfoType_DateTime', pyxb.binding.datatypes.dateTime)
    __DateTime._DeclarationLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 101, 2)
    __DateTime._UseLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 101, 2)
    
    DateTime = property(__DateTime.value, __DateTime.set, None, None)

    
    # Attribute Nonce uses Python identifier Nonce
    __Nonce = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Nonce'), 'Nonce', '__httpwww_trustedcomputinggroup_orgXMLSCHEMACore_Integrity_v1_0_1_SignerInfoType_Nonce', pyxb.binding.datatypes.base64Binary)
    __Nonce._DeclarationLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 102, 2)
    __Nonce._UseLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 102, 2)
    
    Nonce = property(__Nonce.value, __Nonce.set, None, None)

    _ElementMap.update({
        __SigningComponent.name() : __SigningComponent,
        __Signature.name() : __Signature
    })
    _AttributeMap.update({
        __DateTime.name() : __DateTime,
        __Nonce.name() : __Nonce
    })
Namespace.addCategoryObject('typeBinding', u'SignerInfoType', SignerInfoType)


# Complex type {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}ValueType with content type ELEMENT_ONLY
class ValueType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}ValueType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ValueType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 111, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Id uses Python identifier Id
    __Id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Id'), 'Id', '__httpwww_trustedcomputinggroup_orgXMLSCHEMACore_Integrity_v1_0_1_ValueType_Id', pyxb.binding.datatypes.ID)
    __Id._DeclarationLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 115, 2)
    __Id._UseLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 115, 2)
    
    Id = property(__Id.value, __Id.set, None, None)

    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Id.name() : __Id
    })
Namespace.addCategoryObject('typeBinding', u'ValueType', ValueType)


# Complex type {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}VendorIdType with content type ELEMENT_ONLY
class VendorIdType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}VendorIdType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'VendorIdType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 117, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}TcgVendorId uses Python identifier TcgVendorId
    __TcgVendorId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'TcgVendorId'), 'TcgVendorId', '__httpwww_trustedcomputinggroup_orgXMLSCHEMACore_Integrity_v1_0_1_VendorIdType_httpwww_trustedcomputinggroup_orgXMLSCHEMACore_Integrity_v1_0_1TcgVendorId', True, pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 119, 3), )

    
    TcgVendorId = property(__TcgVendorId.value, __TcgVendorId.set, None, None)

    
    # Element {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}SmiVendorId uses Python identifier SmiVendorId
    __SmiVendorId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'SmiVendorId'), 'SmiVendorId', '__httpwww_trustedcomputinggroup_orgXMLSCHEMACore_Integrity_v1_0_1_VendorIdType_httpwww_trustedcomputinggroup_orgXMLSCHEMACore_Integrity_v1_0_1SmiVendorId', True, pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 126, 3), )

    
    SmiVendorId = property(__SmiVendorId.value, __SmiVendorId.set, None, None)

    
    # Element {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}VendorGUID uses Python identifier VendorGUID
    __VendorGUID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'VendorGUID'), 'VendorGUID', '__httpwww_trustedcomputinggroup_orgXMLSCHEMACore_Integrity_v1_0_1_VendorIdType_httpwww_trustedcomputinggroup_orgXMLSCHEMACore_Integrity_v1_0_1VendorGUID', True, pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 127, 3), )

    
    VendorGUID = property(__VendorGUID.value, __VendorGUID.set, None, None)

    
    # Attribute Name uses Python identifier Name
    __Name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Name'), 'Name', '__httpwww_trustedcomputinggroup_orgXMLSCHEMACore_Integrity_v1_0_1_VendorIdType_Name', pyxb.binding.datatypes.normalizedString)
    __Name._DeclarationLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 129, 2)
    __Name._UseLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 129, 2)
    
    Name = property(__Name.value, __Name.set, None, None)

    _ElementMap.update({
        __TcgVendorId.name() : __TcgVendorId,
        __SmiVendorId.name() : __SmiVendorId,
        __VendorGUID.name() : __VendorGUID
    })
    _AttributeMap.update({
        __Name.name() : __Name
    })
Namespace.addCategoryObject('typeBinding', u'VendorIdType', VendorIdType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (ComponentIDType):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 33, 4)
    _ElementMap = ComponentIDType._ElementMap.copy()
    _AttributeMap = ComponentIDType._AttributeMap.copy()
    # Base type is ComponentIDType
    
    # Element VendorID ({http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}VendorID) inherited from {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}ComponentIDType
    
    # Attribute Id inherited from {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}ComponentIDType
    
    # Attribute SimpleName inherited from {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}ComponentIDType
    
    # Attribute ModelName inherited from {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}ComponentIDType
    
    # Attribute ModelNumber inherited from {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}ComponentIDType
    
    # Attribute ModelSerialNumber inherited from {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}ComponentIDType
    
    # Attribute ModelSystemClass inherited from {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}ComponentIDType
    
    # Attribute VersionMajor inherited from {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}ComponentIDType
    
    # Attribute VersionMinor inherited from {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}ComponentIDType
    
    # Attribute VersionBuild inherited from {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}ComponentIDType
    
    # Attribute VersionString inherited from {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}ComponentIDType
    
    # Attribute MfgDate inherited from {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}ComponentIDType
    
    # Attribute PatchLevel inherited from {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}ComponentIDType
    
    # Attribute DiscretePatches inherited from {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}ComponentIDType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })



# Complex type {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}DigestMethodType with content type MIXED
class DigestMethodType (_ImportedBinding__ds.DigestMethodType):
    """Complex type {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}DigestMethodType with content type MIXED"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'DigestMethodType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 48, 1)
    _ElementMap = _ImportedBinding__ds.DigestMethodType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__ds.DigestMethodType._AttributeMap.copy()
    # Base type is _ImportedBinding__ds.DigestMethodType
    
    # Attribute Id uses Python identifier Id
    __Id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Id'), 'Id', '__httpwww_trustedcomputinggroup_orgXMLSCHEMACore_Integrity_v1_0_1_DigestMethodType_Id', pyxb.binding.datatypes.ID, required=True)
    __Id._DeclarationLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 51, 4)
    __Id._UseLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 51, 4)
    
    Id = property(__Id.value, __Id.set, None, None)

    
    # Attribute Algorithm inherited from {http://www.w3.org/2000/09/xmldsig#}DigestMethodType
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Id.name() : __Id
    })
Namespace.addCategoryObject('typeBinding', u'DigestMethodType', DigestMethodType)


# Complex type {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}DigestValueType with content type SIMPLE
class DigestValueType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}DigestValueType with content type SIMPLE"""
    _TypeDefinition = _ImportedBinding__ds.DigestValueType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'DigestValueType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 55, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is _ImportedBinding__ds.DigestValueType
    
    # Attribute Id uses Python identifier Id
    __Id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Id'), 'Id', '__httpwww_trustedcomputinggroup_orgXMLSCHEMACore_Integrity_v1_0_1_DigestValueType_Id', pyxb.binding.datatypes.ID, required=True)
    __Id._DeclarationLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 58, 4)
    __Id._UseLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 58, 4)
    
    Id = property(__Id.value, __Id.set, None, None)

    
    # Attribute AlgRef uses Python identifier AlgRef
    __AlgRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'AlgRef'), 'AlgRef', '__httpwww_trustedcomputinggroup_orgXMLSCHEMACore_Integrity_v1_0_1_DigestValueType_AlgRef', pyxb.binding.datatypes.IDREF, required=True)
    __AlgRef._DeclarationLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 59, 4)
    __AlgRef._UseLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 59, 4)
    
    AlgRef = property(__AlgRef.value, __AlgRef.set, None, None)

    
    # Attribute TransformRefs uses Python identifier TransformRefs
    __TransformRefs = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'TransformRefs'), 'TransformRefs', '__httpwww_trustedcomputinggroup_orgXMLSCHEMACore_Integrity_v1_0_1_DigestValueType_TransformRefs', pyxb.binding.datatypes.IDREFS)
    __TransformRefs._DeclarationLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 60, 4)
    __TransformRefs._UseLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 60, 4)
    
    TransformRefs = property(__TransformRefs.value, __TransformRefs.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Id.name() : __Id,
        __AlgRef.name() : __AlgRef,
        __TransformRefs.name() : __TransformRefs
    })
Namespace.addCategoryObject('typeBinding', u'DigestValueType', DigestValueType)


# Complex type {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}TransformMethodType with content type MIXED
class TransformMethodType (_ImportedBinding__ds.TransformType):
    """Complex type {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}TransformMethodType with content type MIXED"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TransformMethodType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 104, 1)
    _ElementMap = _ImportedBinding__ds.TransformType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__ds.TransformType._AttributeMap.copy()
    # Base type is _ImportedBinding__ds.TransformType
    
    # Element XPath ({http://www.w3.org/2000/09/xmldsig#}XPath) inherited from {http://www.w3.org/2000/09/xmldsig#}TransformType
    
    # Attribute Id uses Python identifier Id
    __Id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Id'), 'Id', '__httpwww_trustedcomputinggroup_orgXMLSCHEMACore_Integrity_v1_0_1_TransformMethodType_Id', pyxb.binding.datatypes.ID, required=True)
    __Id._DeclarationLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 107, 4)
    __Id._UseLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 107, 4)
    
    Id = property(__Id.value, __Id.set, None, None)

    
    # Attribute Algorithm inherited from {http://www.w3.org/2000/09/xmldsig#}TransformType
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Id.name() : __Id
    })
Namespace.addCategoryObject('typeBinding', u'TransformMethodType', TransformMethodType)


# Complex type {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}HashType with content type SIMPLE
class HashType (DigestValueType):
    """Complex type {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}HashType with content type SIMPLE"""
    _TypeDefinition = _ImportedBinding__ds.DigestValueType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'HashType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 70, 1)
    _ElementMap = DigestValueType._ElementMap.copy()
    _AttributeMap = DigestValueType._AttributeMap.copy()
    # Base type is DigestValueType
    
    # Attribute Id inherited from {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}DigestValueType
    
    # Attribute AlgRef inherited from {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}DigestValueType
    
    # Attribute TransformRefs inherited from {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}DigestValueType
    
    # Attribute ExtendOrder uses Python identifier ExtendOrder
    __ExtendOrder = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ExtendOrder'), 'ExtendOrder', '__httpwww_trustedcomputinggroup_orgXMLSCHEMACore_Integrity_v1_0_1_HashType_ExtendOrder', pyxb.binding.datatypes.IDREFS)
    __ExtendOrder._DeclarationLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 73, 4)
    __ExtendOrder._UseLocation = pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 73, 4)
    
    ExtendOrder = property(__ExtendOrder.value, __ExtendOrder.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __ExtendOrder.name() : __ExtendOrder
    })
Namespace.addCategoryObject('typeBinding', u'HashType', HashType)




def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#')), pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 8, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AssertionType._Automaton = _BuildAutomaton()




ComponentIDType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'VendorID'), VendorIdType, scope=ComponentIDType, location=pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 14, 3)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ComponentIDType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'VendorID')), pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 14, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ComponentIDType._Automaton = _BuildAutomaton_()




ComponentRefType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ComponentID'), CTD_ANON, scope=ComponentRefType, location=pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 32, 3)))

ComponentRefType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ComponentIDREF'), pyxb.binding.datatypes.IDREF, scope=ComponentRefType, location=pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 39, 3)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ComponentRefType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ComponentID')), pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 32, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ComponentRefType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ComponentIDREF')), pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 39, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ComponentRefType._Automaton = _BuildAutomaton_2()




HashedURIType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'UriHash'), DigestValueType, scope=HashedURIType, location=pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 66, 3)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 65, 2))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(HashedURIType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'UriHash')), pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 66, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
HashedURIType._Automaton = _BuildAutomaton_3()




IntegrityManifestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ComponentID'), ComponentIDType, scope=IntegrityManifestType, location=pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 79, 3)))

IntegrityManifestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SignerInfo'), SignerInfoType, scope=IntegrityManifestType, location=pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 80, 3)))

IntegrityManifestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ConfidenceValue'), ConfidenceValueType, scope=IntegrityManifestType, location=pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 81, 3)))

IntegrityManifestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Collector'), ComponentRefType, scope=IntegrityManifestType, location=pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 82, 3)))

IntegrityManifestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TransformMethod'), TransformMethodType, scope=IntegrityManifestType, location=pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 83, 3)))

IntegrityManifestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DigestMethod'), DigestMethodType, scope=IntegrityManifestType, location=pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 84, 3)))

IntegrityManifestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Values'), ValueType, scope=IntegrityManifestType, location=pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 85, 3)))

IntegrityManifestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AssertionInfo'), AssertionType, scope=IntegrityManifestType, location=pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 86, 3)))

IntegrityManifestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PlatformClass'), PlatformClassType, scope=IntegrityManifestType, location=pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 87, 3)))

IntegrityManifestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SubComponents'), ComponentRefType, scope=IntegrityManifestType, location=pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 88, 3)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 80, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 81, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 82, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 83, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 84, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 85, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 86, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 87, 3))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 88, 3))
    counters.add(cc_8)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(IntegrityManifestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ComponentID')), pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 79, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(IntegrityManifestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SignerInfo')), pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 80, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(IntegrityManifestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ConfidenceValue')), pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 81, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(IntegrityManifestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Collector')), pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 82, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(IntegrityManifestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TransformMethod')), pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 83, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(IntegrityManifestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DigestMethod')), pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 84, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(IntegrityManifestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Values')), pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 85, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(IntegrityManifestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AssertionInfo')), pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 86, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(IntegrityManifestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PlatformClass')), pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 87, 3))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(IntegrityManifestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SubComponents')), pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 88, 3))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, True) ]))
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
IntegrityManifestType._Automaton = _BuildAutomaton_4()




SignerInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SigningComponent'), ComponentRefType, scope=SignerInfoType, location=pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 99, 3)))

SignerInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ds, u'Signature'), _ImportedBinding__ds.SignatureType, scope=SignerInfoType, location=pyxb.utils.utility.Location(u'http://www.w3.org/TR/2002/REC-xmldsig-core-20020212/xmldsig-core-schema.xsd', 43, 0)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 99, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SignerInfoType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ds, u'Signature')), pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 98, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SignerInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SigningComponent')), pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 99, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SignerInfoType._Automaton = _BuildAutomaton_5()




def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#')), pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 113, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ValueType._Automaton = _BuildAutomaton_6()




VendorIdType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TcgVendorId'), STD_ANON, scope=VendorIdType, location=pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 119, 3)))

VendorIdType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SmiVendorId'), pyxb.binding.datatypes.integer, scope=VendorIdType, location=pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 126, 3)))

VendorIdType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'VendorGUID'), pyxb.binding.datatypes.NMTOKEN, scope=VendorIdType, location=pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 127, 3)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(VendorIdType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TcgVendorId')), pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 119, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(VendorIdType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SmiVendorId')), pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 126, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(VendorIdType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'VendorGUID')), pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 127, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
VendorIdType._Automaton = _BuildAutomaton_7()




def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'VendorID')), pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 14, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton_8()




def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'http://www.w3.org/TR/2002/REC-xmldsig-core-20020212/xmldsig-core-schema.xsd', 130, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://www.w3.org/2000/09/xmldsig#')), pyxb.utils.utility.Location(u'http://www.w3.org/TR/2002/REC-xmldsig-core-20020212/xmldsig-core-schema.xsd', 130, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
DigestMethodType._Automaton = _BuildAutomaton_9()




def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'http://www.w3.org/TR/2002/REC-xmldsig-core-20020212/xmldsig-core-schema.xsd', 117, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://www.w3.org/2000/09/xmldsig#')), pyxb.utils.utility.Location(u'http://www.w3.org/TR/2002/REC-xmldsig-core-20020212/xmldsig-core-schema.xsd', 118, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TransformMethodType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ds, u'XPath')), pyxb.utils.utility.Location(u'http://www.w3.org/TR/2002/REC-xmldsig-core-20020212/xmldsig-core-schema.xsd', 120, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
TransformMethodType._Automaton = _BuildAutomaton_10()

