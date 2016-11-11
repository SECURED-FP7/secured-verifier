# ./ir_parser.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:b39877680082d092fd228d85f4b956f1670508b9
# Generated 2014-02-06 17:58:58.706504 by PyXB version 1.2.3
# Namespace http://www.trustedcomputinggroup.org/XML/SCHEMA/Integrity_Report_v1_0#

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
Namespace = pyxb.namespace.NamespaceForURI(u'http://www.trustedcomputinggroup.org/XML/SCHEMA/Integrity_Report_v1_0#', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_core = _ImportedBinding__core.Namespace
_Namespace_core.configureCategories(['typeBinding', 'elementBinding'])

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


# Complex type {http://www.trustedcomputinggroup.org/XML/SCHEMA/Integrity_Report_v1_0#}CapVersionInfoType with content type EMPTY
class CapVersionInfoType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.trustedcomputinggroup.org/XML/SCHEMA/Integrity_Report_v1_0#}CapVersionInfoType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CapVersionInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 9, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Tag uses Python identifier Tag
    __Tag = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Tag'), 'Tag', '__httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0_CapVersionInfoType_Tag', pyxb.binding.datatypes.unsignedShort, required=True)
    __Tag._DeclarationLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 10, 2)
    __Tag._UseLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 10, 2)
    
    Tag = property(__Tag.value, __Tag.set, None, None)

    
    # Attribute VersionMajor uses Python identifier VersionMajor
    __VersionMajor = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'VersionMajor'), 'VersionMajor', '__httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0_CapVersionInfoType_VersionMajor', pyxb.binding.datatypes.unsignedByte, required=True)
    __VersionMajor._DeclarationLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 11, 2)
    __VersionMajor._UseLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 11, 2)
    
    VersionMajor = property(__VersionMajor.value, __VersionMajor.set, None, None)

    
    # Attribute VersionMinor uses Python identifier VersionMinor
    __VersionMinor = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'VersionMinor'), 'VersionMinor', '__httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0_CapVersionInfoType_VersionMinor', pyxb.binding.datatypes.unsignedByte, required=True)
    __VersionMinor._DeclarationLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 12, 2)
    __VersionMinor._UseLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 12, 2)
    
    VersionMinor = property(__VersionMinor.value, __VersionMinor.set, None, None)

    
    # Attribute VersionRevMajor uses Python identifier VersionRevMajor
    __VersionRevMajor = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'VersionRevMajor'), 'VersionRevMajor', '__httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0_CapVersionInfoType_VersionRevMajor', pyxb.binding.datatypes.unsignedByte, required=True)
    __VersionRevMajor._DeclarationLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 13, 2)
    __VersionRevMajor._UseLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 13, 2)
    
    VersionRevMajor = property(__VersionRevMajor.value, __VersionRevMajor.set, None, None)

    
    # Attribute VersionRevMinor uses Python identifier VersionRevMinor
    __VersionRevMinor = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'VersionRevMinor'), 'VersionRevMinor', '__httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0_CapVersionInfoType_VersionRevMinor', pyxb.binding.datatypes.unsignedByte, required=True)
    __VersionRevMinor._DeclarationLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 14, 2)
    __VersionRevMinor._UseLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 14, 2)
    
    VersionRevMinor = property(__VersionRevMinor.value, __VersionRevMinor.set, None, None)

    
    # Attribute SpecLevel uses Python identifier SpecLevel
    __SpecLevel = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'SpecLevel'), 'SpecLevel', '__httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0_CapVersionInfoType_SpecLevel', pyxb.binding.datatypes.unsignedShort, required=True)
    __SpecLevel._DeclarationLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 15, 2)
    __SpecLevel._UseLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 15, 2)
    
    SpecLevel = property(__SpecLevel.value, __SpecLevel.set, None, None)

    
    # Attribute ErrataRev uses Python identifier ErrataRev
    __ErrataRev = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ErrataRev'), 'ErrataRev', '__httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0_CapVersionInfoType_ErrataRev', pyxb.binding.datatypes.unsignedByte, required=True)
    __ErrataRev._DeclarationLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 16, 2)
    __ErrataRev._UseLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 16, 2)
    
    ErrataRev = property(__ErrataRev.value, __ErrataRev.set, None, None)

    
    # Attribute TpmVendorID uses Python identifier TpmVendorID
    __TpmVendorID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'TpmVendorID'), 'TpmVendorID', '__httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0_CapVersionInfoType_TpmVendorID', pyxb.binding.datatypes.normalizedString, required=True)
    __TpmVendorID._DeclarationLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 17, 2)
    __TpmVendorID._UseLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 17, 2)
    
    TpmVendorID = property(__TpmVendorID.value, __TpmVendorID.set, None, None)

    
    # Attribute VendorSpecificSize uses Python identifier VendorSpecificSize
    __VendorSpecificSize = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'VendorSpecificSize'), 'VendorSpecificSize', '__httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0_CapVersionInfoType_VendorSpecificSize', pyxb.binding.datatypes.unsignedShort, required=True)
    __VendorSpecificSize._DeclarationLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 18, 2)
    __VendorSpecificSize._UseLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 18, 2)
    
    VendorSpecificSize = property(__VendorSpecificSize.value, __VendorSpecificSize.set, None, None)

    
    # Attribute VendorSpecific uses Python identifier VendorSpecific
    __VendorSpecific = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'VendorSpecific'), 'VendorSpecific', '__httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0_CapVersionInfoType_VendorSpecific', pyxb.binding.datatypes.base64Binary)
    __VendorSpecific._DeclarationLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 19, 2)
    __VendorSpecific._UseLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 19, 2)
    
    VendorSpecific = property(__VendorSpecific.value, __VendorSpecific.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Tag.name() : __Tag,
        __VersionMajor.name() : __VersionMajor,
        __VersionMinor.name() : __VersionMinor,
        __VersionRevMajor.name() : __VersionRevMajor,
        __VersionRevMinor.name() : __VersionRevMinor,
        __SpecLevel.name() : __SpecLevel,
        __ErrataRev.name() : __ErrataRev,
        __TpmVendorID.name() : __TpmVendorID,
        __VendorSpecificSize.name() : __VendorSpecificSize,
        __VendorSpecific.name() : __VendorSpecific
    })
Namespace.addCategoryObject('typeBinding', u'CapVersionInfoType', CapVersionInfoType)


# Complex type {http://www.trustedcomputinggroup.org/XML/SCHEMA/Integrity_Report_v1_0#}QuoteType with content type ELEMENT_ONLY
class QuoteType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.trustedcomputinggroup.org/XML/SCHEMA/Integrity_Report_v1_0#}QuoteType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'QuoteType')
    _XSDLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 21, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.trustedcomputinggroup.org/XML/SCHEMA/Integrity_Report_v1_0#}PcrComposite uses Python identifier PcrComposite
    __PcrComposite = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'PcrComposite'), 'PcrComposite', '__httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0_QuoteType_httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0PcrComposite', False, pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 23, 3), )

    
    PcrComposite = property(__PcrComposite.value, __PcrComposite.set, None, None)

    
    # Element {http://www.trustedcomputinggroup.org/XML/SCHEMA/Integrity_Report_v1_0#}QuoteInfo uses Python identifier QuoteInfo
    __QuoteInfo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'QuoteInfo'), 'QuoteInfo', '__httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0_QuoteType_httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0QuoteInfo', False, pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 24, 3), )

    
    QuoteInfo = property(__QuoteInfo.value, __QuoteInfo.set, None, None)

    
    # Element {http://www.trustedcomputinggroup.org/XML/SCHEMA/Integrity_Report_v1_0#}TpmInfo uses Python identifier TpmInfo
    __TpmInfo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'TpmInfo'), 'TpmInfo', '__httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0_QuoteType_httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0TpmInfo', False, pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 25, 3), )

    
    TpmInfo = property(__TpmInfo.value, __TpmInfo.set, None, None)

    _ElementMap.update({
        __PcrComposite.name() : __PcrComposite,
        __QuoteInfo.name() : __QuoteInfo,
        __TpmInfo.name() : __TpmInfo
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'QuoteType', QuoteType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 26, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.trustedcomputinggroup.org/XML/SCHEMA/Integrity_Report_v1_0#}CapVersionInfo uses Python identifier CapVersionInfo
    __CapVersionInfo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'CapVersionInfo'), 'CapVersionInfo', '__httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0_CTD_ANON_httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0CapVersionInfo', False, pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 28, 6), )

    
    CapVersionInfo = property(__CapVersionInfo.value, __CapVersionInfo.set, None, None)

    
    # Element {http://www.trustedcomputinggroup.org/XML/SCHEMA/Integrity_Report_v1_0#}TpmManufacturer uses Python identifier TpmManufacturer
    __TpmManufacturer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'TpmManufacturer'), 'TpmManufacturer', '__httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0_CTD_ANON_httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0TpmManufacturer', False, pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 29, 6), )

    
    TpmManufacturer = property(__TpmManufacturer.value, __TpmManufacturer.set, None, None)

    _ElementMap.update({
        __CapVersionInfo.name() : __CapVersionInfo,
        __TpmManufacturer.name() : __TpmManufacturer
    })
    _AttributeMap.update({
        
    })



# Complex type {http://www.trustedcomputinggroup.org/XML/SCHEMA/Integrity_Report_v1_0#}Quote2Type with content type ELEMENT_ONLY
class Quote2Type (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.trustedcomputinggroup.org/XML/SCHEMA/Integrity_Report_v1_0#}Quote2Type with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Quote2Type')
    _XSDLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 44, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.trustedcomputinggroup.org/XML/SCHEMA/Integrity_Report_v1_0#}QuoteInfo2 uses Python identifier QuoteInfo2
    __QuoteInfo2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'QuoteInfo2'), 'QuoteInfo2', '__httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0_Quote2Type_httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0QuoteInfo2', False, pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 46, 3), )

    
    QuoteInfo2 = property(__QuoteInfo2.value, __QuoteInfo2.set, None, None)

    
    # Element {http://www.trustedcomputinggroup.org/XML/SCHEMA/Integrity_Report_v1_0#}CapVersionInfo uses Python identifier CapVersionInfo
    __CapVersionInfo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'CapVersionInfo'), 'CapVersionInfo', '__httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0_Quote2Type_httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0CapVersionInfo', False, pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 47, 3), )

    
    CapVersionInfo = property(__CapVersionInfo.value, __CapVersionInfo.set, None, None)

    _ElementMap.update({
        __QuoteInfo2.name() : __QuoteInfo2,
        __CapVersionInfo.name() : __CapVersionInfo
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'Quote2Type', Quote2Type)


# Complex type {http://www.trustedcomputinggroup.org/XML/SCHEMA/Integrity_Report_v1_0#}QuoteInfo2Type with content type ELEMENT_ONLY
class QuoteInfo2Type (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.trustedcomputinggroup.org/XML/SCHEMA/Integrity_Report_v1_0#}QuoteInfo2Type with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'QuoteInfo2Type')
    _XSDLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 50, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.trustedcomputinggroup.org/XML/SCHEMA/Integrity_Report_v1_0#}PcrInfoShort uses Python identifier PcrInfoShort
    __PcrInfoShort = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'PcrInfoShort'), 'PcrInfoShort', '__httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0_QuoteInfo2Type_httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0PcrInfoShort', False, pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 52, 3), )

    
    PcrInfoShort = property(__PcrInfoShort.value, __PcrInfoShort.set, None, None)

    
    # Attribute Tag uses Python identifier Tag
    __Tag = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Tag'), 'Tag', '__httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0_QuoteInfo2Type_Tag', pyxb.binding.datatypes.unsignedShort, required=True)
    __Tag._DeclarationLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 54, 2)
    __Tag._UseLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 54, 2)
    
    Tag = property(__Tag.value, __Tag.set, None, None)

    
    # Attribute Fixed uses Python identifier Fixed
    __Fixed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Fixed'), 'Fixed', '__httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0_QuoteInfo2Type_Fixed', pyxb.binding.datatypes.normalizedString, required=True)
    __Fixed._DeclarationLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 55, 2)
    __Fixed._UseLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 55, 2)
    
    Fixed = property(__Fixed.value, __Fixed.set, None, None)

    
    # Attribute ExternalData uses Python identifier ExternalData
    __ExternalData = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ExternalData'), 'ExternalData', '__httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0_QuoteInfo2Type_ExternalData', pyxb.binding.datatypes.base64Binary, required=True)
    __ExternalData._DeclarationLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 56, 2)
    __ExternalData._UseLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 56, 2)
    
    ExternalData = property(__ExternalData.value, __ExternalData.set, None, None)

    _ElementMap.update({
        __PcrInfoShort.name() : __PcrInfoShort
    })
    _AttributeMap.update({
        __Tag.name() : __Tag,
        __Fixed.name() : __Fixed,
        __ExternalData.name() : __ExternalData
    })
Namespace.addCategoryObject('typeBinding', u'QuoteInfo2Type', QuoteInfo2Type)


# Complex type {http://www.trustedcomputinggroup.org/XML/SCHEMA/Integrity_Report_v1_0#}PcrSelectionType with content type EMPTY
class PcrSelectionType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.trustedcomputinggroup.org/XML/SCHEMA/Integrity_Report_v1_0#}PcrSelectionType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'PcrSelectionType')
    _XSDLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 58, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute SizeOfSelect uses Python identifier SizeOfSelect
    __SizeOfSelect = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'SizeOfSelect'), 'SizeOfSelect', '__httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0_PcrSelectionType_SizeOfSelect', pyxb.binding.datatypes.unsignedShort, required=True)
    __SizeOfSelect._DeclarationLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 59, 2)
    __SizeOfSelect._UseLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 59, 2)
    
    SizeOfSelect = property(__SizeOfSelect.value, __SizeOfSelect.set, None, None)

    
    # Attribute PcrSelect uses Python identifier PcrSelect
    __PcrSelect = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'PcrSelect'), 'PcrSelect', '__httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0_PcrSelectionType_PcrSelect', pyxb.binding.datatypes.base64Binary, required=True)
    __PcrSelect._DeclarationLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 60, 2)
    __PcrSelect._UseLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 60, 2)
    
    PcrSelect = property(__PcrSelect.value, __PcrSelect.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __SizeOfSelect.name() : __SizeOfSelect,
        __PcrSelect.name() : __PcrSelect
    })
Namespace.addCategoryObject('typeBinding', u'PcrSelectionType', PcrSelectionType)


# Complex type {http://www.trustedcomputinggroup.org/XML/SCHEMA/Integrity_Report_v1_0#}PcrCompositeType with content type ELEMENT_ONLY
class PcrCompositeType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.trustedcomputinggroup.org/XML/SCHEMA/Integrity_Report_v1_0#}PcrCompositeType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'PcrCompositeType')
    _XSDLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 62, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.trustedcomputinggroup.org/XML/SCHEMA/Integrity_Report_v1_0#}PcrSelection uses Python identifier PcrSelection
    __PcrSelection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'PcrSelection'), 'PcrSelection', '__httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0_PcrCompositeType_httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0PcrSelection', False, pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 64, 3), )

    
    PcrSelection = property(__PcrSelection.value, __PcrSelection.set, None, None)

    
    # Element {http://www.trustedcomputinggroup.org/XML/SCHEMA/Integrity_Report_v1_0#}ValueSize uses Python identifier ValueSize
    __ValueSize = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ValueSize'), 'ValueSize', '__httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0_PcrCompositeType_httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0ValueSize', False, pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 65, 3), )

    
    ValueSize = property(__ValueSize.value, __ValueSize.set, None, None)

    
    # Element {http://www.trustedcomputinggroup.org/XML/SCHEMA/Integrity_Report_v1_0#}PcrValue uses Python identifier PcrValue
    __PcrValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'PcrValue'), 'PcrValue', '__httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0_PcrCompositeType_httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0PcrValue', True, pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 66, 3), )

    
    PcrValue = property(__PcrValue.value, __PcrValue.set, None, None)

    _ElementMap.update({
        __PcrSelection.name() : __PcrSelection,
        __ValueSize.name() : __ValueSize,
        __PcrValue.name() : __PcrValue
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'PcrCompositeType', PcrCompositeType)


# Complex type {http://www.trustedcomputinggroup.org/XML/SCHEMA/Integrity_Report_v1_0#}PcrInfoShortType with content type ELEMENT_ONLY
class PcrInfoShortType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.trustedcomputinggroup.org/XML/SCHEMA/Integrity_Report_v1_0#}PcrInfoShortType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'PcrInfoShortType')
    _XSDLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 78, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.trustedcomputinggroup.org/XML/SCHEMA/Integrity_Report_v1_0#}PcrSelection uses Python identifier PcrSelection
    __PcrSelection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'PcrSelection'), 'PcrSelection', '__httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0_PcrInfoShortType_httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0PcrSelection', False, pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 80, 3), )

    
    PcrSelection = property(__PcrSelection.value, __PcrSelection.set, None, None)

    
    # Element {http://www.trustedcomputinggroup.org/XML/SCHEMA/Integrity_Report_v1_0#}LocalityAtRelease uses Python identifier LocalityAtRelease
    __LocalityAtRelease = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'LocalityAtRelease'), 'LocalityAtRelease', '__httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0_PcrInfoShortType_httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0LocalityAtRelease', False, pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 81, 3), )

    
    LocalityAtRelease = property(__LocalityAtRelease.value, __LocalityAtRelease.set, None, None)

    
    # Element {http://www.trustedcomputinggroup.org/XML/SCHEMA/Integrity_Report_v1_0#}CompositeHash uses Python identifier CompositeHash
    __CompositeHash = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'CompositeHash'), 'CompositeHash', '__httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0_PcrInfoShortType_httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0CompositeHash', False, pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 82, 3), )

    
    CompositeHash = property(__CompositeHash.value, __CompositeHash.set, None, None)

    
    # Element {http://www.trustedcomputinggroup.org/XML/SCHEMA/Integrity_Report_v1_0#}PcrComposite uses Python identifier PcrComposite
    __PcrComposite = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'PcrComposite'), 'PcrComposite', '__httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0_PcrInfoShortType_httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0PcrComposite', False, pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 83, 3), )

    
    PcrComposite = property(__PcrComposite.value, __PcrComposite.set, None, None)

    _ElementMap.update({
        __PcrSelection.name() : __PcrSelection,
        __LocalityAtRelease.name() : __LocalityAtRelease,
        __CompositeHash.name() : __CompositeHash,
        __PcrComposite.name() : __PcrComposite
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'PcrInfoShortType', PcrInfoShortType)


# Complex type {http://www.trustedcomputinggroup.org/XML/SCHEMA/Integrity_Report_v1_0#}QuoteSignatureType with content type ELEMENT_ONLY
class QuoteSignatureType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.trustedcomputinggroup.org/XML/SCHEMA/Integrity_Report_v1_0#}QuoteSignatureType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'QuoteSignatureType')
    _XSDLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 86, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.trustedcomputinggroup.org/XML/SCHEMA/Integrity_Report_v1_0#}CanonicalizationMethod uses Python identifier CanonicalizationMethod
    __CanonicalizationMethod = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'CanonicalizationMethod'), 'CanonicalizationMethod', '__httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0_QuoteSignatureType_httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0CanonicalizationMethod', False, pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 88, 3), )

    
    CanonicalizationMethod = property(__CanonicalizationMethod.value, __CanonicalizationMethod.set, None, None)

    
    # Element {http://www.trustedcomputinggroup.org/XML/SCHEMA/Integrity_Report_v1_0#}SignatureMethod uses Python identifier SignatureMethod
    __SignatureMethod = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'SignatureMethod'), 'SignatureMethod', '__httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0_QuoteSignatureType_httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0SignatureMethod', False, pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 89, 3), )

    
    SignatureMethod = property(__SignatureMethod.value, __SignatureMethod.set, None, None)

    
    # Element {http://www.trustedcomputinggroup.org/XML/SCHEMA/Integrity_Report_v1_0#}SignatureValue uses Python identifier SignatureValue
    __SignatureValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'SignatureValue'), 'SignatureValue', '__httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0_QuoteSignatureType_httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0SignatureValue', False, pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 90, 3), )

    
    SignatureValue = property(__SignatureValue.value, __SignatureValue.set, None, None)

    
    # Element {http://www.trustedcomputinggroup.org/XML/SCHEMA/Integrity_Report_v1_0#}KeyInfo uses Python identifier KeyInfo
    __KeyInfo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'KeyInfo'), 'KeyInfo', '__httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0_QuoteSignatureType_httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0KeyInfo', False, pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 91, 3), )

    
    KeyInfo = property(__KeyInfo.value, __KeyInfo.set, None, None)

    
    # Element {http://www.trustedcomputinggroup.org/XML/SCHEMA/Integrity_Report_v1_0#}ObjectType uses Python identifier ObjectType
    __ObjectType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ObjectType'), 'ObjectType', '__httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0_QuoteSignatureType_httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0ObjectType', False, pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 92, 3), )

    
    ObjectType = property(__ObjectType.value, __ObjectType.set, None, None)

    _ElementMap.update({
        __CanonicalizationMethod.name() : __CanonicalizationMethod,
        __SignatureMethod.name() : __SignatureMethod,
        __SignatureValue.name() : __SignatureValue,
        __KeyInfo.name() : __KeyInfo,
        __ObjectType.name() : __ObjectType
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'QuoteSignatureType', QuoteSignatureType)


# Complex type {http://www.trustedcomputinggroup.org/XML/SCHEMA/Integrity_Report_v1_0#}QuoteDataType with content type ELEMENT_ONLY
class QuoteDataType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.trustedcomputinggroup.org/XML/SCHEMA/Integrity_Report_v1_0#}QuoteDataType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'QuoteDataType')
    _XSDLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 95, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.trustedcomputinggroup.org/XML/SCHEMA/Integrity_Report_v1_0#}Quote uses Python identifier Quote
    __Quote = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Quote'), 'Quote', '__httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0_QuoteDataType_httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0Quote', False, pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 98, 4), )

    
    Quote = property(__Quote.value, __Quote.set, None, None)

    
    # Element {http://www.trustedcomputinggroup.org/XML/SCHEMA/Integrity_Report_v1_0#}Quote2 uses Python identifier Quote2
    __Quote2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Quote2'), 'Quote2', '__httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0_QuoteDataType_httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0Quote2', False, pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 99, 4), )

    
    Quote2 = property(__Quote2.value, __Quote2.set, None, None)

    
    # Element {http://www.trustedcomputinggroup.org/XML/SCHEMA/Integrity_Report_v1_0#}TpmSignature uses Python identifier TpmSignature
    __TpmSignature = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'TpmSignature'), 'TpmSignature', '__httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0_QuoteDataType_httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0TpmSignature', False, pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 101, 3), )

    
    TpmSignature = property(__TpmSignature.value, __TpmSignature.set, None, None)

    
    # Attribute ID uses Python identifier ID
    __ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ID'), 'ID', '__httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0_QuoteDataType_ID', pyxb.binding.datatypes.ID, required=True)
    __ID._DeclarationLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 103, 2)
    __ID._UseLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 103, 2)
    
    ID = property(__ID.value, __ID.set, None, None)

    _ElementMap.update({
        __Quote.name() : __Quote,
        __Quote2.name() : __Quote2,
        __TpmSignature.name() : __TpmSignature
    })
    _AttributeMap.update({
        __ID.name() : __ID
    })
Namespace.addCategoryObject('typeBinding', u'QuoteDataType', QuoteDataType)


# Complex type {http://www.trustedcomputinggroup.org/XML/SCHEMA/Integrity_Report_v1_0#}ReportType with content type ELEMENT_ONLY
class ReportType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.trustedcomputinggroup.org/XML/SCHEMA/Integrity_Report_v1_0#}ReportType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ReportType')
    _XSDLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 141, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.trustedcomputinggroup.org/XML/SCHEMA/Integrity_Report_v1_0#}SignerInfo uses Python identifier SignerInfo
    __SignerInfo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'SignerInfo'), 'SignerInfo', '__httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0_ReportType_httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0SignerInfo', False, pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 143, 3), )

    
    SignerInfo = property(__SignerInfo.value, __SignerInfo.set, None, None)

    
    # Element {http://www.trustedcomputinggroup.org/XML/SCHEMA/Integrity_Report_v1_0#}ConfidenceValue uses Python identifier ConfidenceValue
    __ConfidenceValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ConfidenceValue'), 'ConfidenceValue', '__httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0_ReportType_httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0ConfidenceValue', False, pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 144, 3), )

    
    ConfidenceValue = property(__ConfidenceValue.value, __ConfidenceValue.set, None, None)

    
    # Element {http://www.trustedcomputinggroup.org/XML/SCHEMA/Integrity_Report_v1_0#}QuoteData uses Python identifier QuoteData
    __QuoteData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'QuoteData'), 'QuoteData', '__httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0_ReportType_httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0QuoteData', True, pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 145, 3), )

    
    QuoteData = property(__QuoteData.value, __QuoteData.set, None, None)

    
    # Element {http://www.trustedcomputinggroup.org/XML/SCHEMA/Integrity_Report_v1_0#}SnapshotCollection uses Python identifier SnapshotCollection
    __SnapshotCollection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'SnapshotCollection'), 'SnapshotCollection', '__httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0_ReportType_httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0SnapshotCollection', True, pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 146, 3), )

    
    SnapshotCollection = property(__SnapshotCollection.value, __SnapshotCollection.set, None, None)

    
    # Attribute ID uses Python identifier ID
    __ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ID'), 'ID', '__httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0_ReportType_ID', pyxb.binding.datatypes.ID, required=True)
    __ID._DeclarationLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 148, 2)
    __ID._UseLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 148, 2)
    
    ID = property(__ID.value, __ID.set, None, None)

    
    # Attribute UUID uses Python identifier UUID
    __UUID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'UUID'), 'UUID', '__httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0_ReportType_UUID', pyxb.binding.datatypes.NMTOKEN, required=True)
    __UUID._DeclarationLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 149, 2)
    __UUID._UseLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 149, 2)
    
    UUID = property(__UUID.value, __UUID.set, None, None)

    
    # Attribute SyncSnapshotRefs uses Python identifier SyncSnapshotRefs
    __SyncSnapshotRefs = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'SyncSnapshotRefs'), 'SyncSnapshotRefs', '__httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0_ReportType_SyncSnapshotRefs', pyxb.binding.datatypes.IDREFS)
    __SyncSnapshotRefs._DeclarationLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 150, 2)
    __SyncSnapshotRefs._UseLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 150, 2)
    
    SyncSnapshotRefs = property(__SyncSnapshotRefs.value, __SyncSnapshotRefs.set, None, None)

    
    # Attribute TransitiveTrustPath uses Python identifier TransitiveTrustPath
    __TransitiveTrustPath = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'TransitiveTrustPath'), 'TransitiveTrustPath', '__httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0_ReportType_TransitiveTrustPath', pyxb.binding.datatypes.IDREFS)
    __TransitiveTrustPath._DeclarationLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 151, 2)
    __TransitiveTrustPath._UseLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 151, 2)
    
    TransitiveTrustPath = property(__TransitiveTrustPath.value, __TransitiveTrustPath.set, None, None)

    _ElementMap.update({
        __SignerInfo.name() : __SignerInfo,
        __ConfidenceValue.name() : __ConfidenceValue,
        __QuoteData.name() : __QuoteData,
        __SnapshotCollection.name() : __SnapshotCollection
    })
    _AttributeMap.update({
        __ID.name() : __ID,
        __UUID.name() : __UUID,
        __SyncSnapshotRefs.name() : __SyncSnapshotRefs,
        __TransitiveTrustPath.name() : __TransitiveTrustPath
    })
Namespace.addCategoryObject('typeBinding', u'ReportType', ReportType)


# Complex type {http://www.trustedcomputinggroup.org/XML/SCHEMA/Integrity_Report_v1_0#}QuoteInfoType with content type EMPTY
class QuoteInfoType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.trustedcomputinggroup.org/XML/SCHEMA/Integrity_Report_v1_0#}QuoteInfoType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'QuoteInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 35, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute VersionMajor uses Python identifier VersionMajor
    __VersionMajor = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'VersionMajor'), 'VersionMajor', '__httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0_QuoteInfoType_VersionMajor', pyxb.binding.datatypes.unsignedByte, required=True)
    __VersionMajor._DeclarationLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 36, 2)
    __VersionMajor._UseLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 36, 2)
    
    VersionMajor = property(__VersionMajor.value, __VersionMajor.set, None, None)

    
    # Attribute VersionMinor uses Python identifier VersionMinor
    __VersionMinor = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'VersionMinor'), 'VersionMinor', '__httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0_QuoteInfoType_VersionMinor', pyxb.binding.datatypes.unsignedByte, required=True)
    __VersionMinor._DeclarationLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 37, 2)
    __VersionMinor._UseLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 37, 2)
    
    VersionMinor = property(__VersionMinor.value, __VersionMinor.set, None, None)

    
    # Attribute VersionRevMajor uses Python identifier VersionRevMajor
    __VersionRevMajor = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'VersionRevMajor'), 'VersionRevMajor', '__httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0_QuoteInfoType_VersionRevMajor', pyxb.binding.datatypes.unsignedByte, required=True)
    __VersionRevMajor._DeclarationLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 38, 2)
    __VersionRevMajor._UseLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 38, 2)
    
    VersionRevMajor = property(__VersionRevMajor.value, __VersionRevMajor.set, None, None)

    
    # Attribute VersionRevMinor uses Python identifier VersionRevMinor
    __VersionRevMinor = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'VersionRevMinor'), 'VersionRevMinor', '__httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0_QuoteInfoType_VersionRevMinor', pyxb.binding.datatypes.unsignedByte, required=True)
    __VersionRevMinor._DeclarationLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 39, 2)
    __VersionRevMinor._UseLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 39, 2)
    
    VersionRevMinor = property(__VersionRevMinor.value, __VersionRevMinor.set, None, None)

    
    # Attribute Fixed uses Python identifier Fixed
    __Fixed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Fixed'), 'Fixed', '__httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0_QuoteInfoType_Fixed', pyxb.binding.datatypes.normalizedString, required=True)
    __Fixed._DeclarationLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 40, 2)
    __Fixed._UseLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 40, 2)
    
    Fixed = property(__Fixed.value, __Fixed.set, None, None)

    
    # Attribute DigestValue uses Python identifier DigestValue
    __DigestValue = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'DigestValue'), 'DigestValue', '__httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0_QuoteInfoType_DigestValue', _ImportedBinding__ds.DigestValueType, required=True)
    __DigestValue._DeclarationLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 41, 2)
    __DigestValue._UseLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 41, 2)
    
    DigestValue = property(__DigestValue.value, __DigestValue.set, None, None)

    
    # Attribute ExternalData uses Python identifier ExternalData
    __ExternalData = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ExternalData'), 'ExternalData', '__httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0_QuoteInfoType_ExternalData', pyxb.binding.datatypes.base64Binary, required=True)
    __ExternalData._DeclarationLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 42, 2)
    __ExternalData._UseLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 42, 2)
    
    ExternalData = property(__ExternalData.value, __ExternalData.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __VersionMajor.name() : __VersionMajor,
        __VersionMinor.name() : __VersionMinor,
        __VersionRevMajor.name() : __VersionRevMajor,
        __VersionRevMinor.name() : __VersionRevMinor,
        __Fixed.name() : __Fixed,
        __DigestValue.name() : __DigestValue,
        __ExternalData.name() : __ExternalData
    })
Namespace.addCategoryObject('typeBinding', u'QuoteInfoType', QuoteInfoType)


# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = _ImportedBinding__ds.DigestValueType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 67, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is _ImportedBinding__ds.DigestValueType
    
    # Attribute SnapshotRef uses Python identifier SnapshotRef
    __SnapshotRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'SnapshotRef'), 'SnapshotRef', '__httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0_CTD_ANON__SnapshotRef', pyxb.binding.datatypes.IDREF)
    __SnapshotRef._DeclarationLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 70, 7)
    __SnapshotRef._UseLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 70, 7)
    
    SnapshotRef = property(__SnapshotRef.value, __SnapshotRef.set, None, None)

    
    # Attribute PcrNumber uses Python identifier PcrNumber
    __PcrNumber = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'PcrNumber'), 'PcrNumber', '__httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0_CTD_ANON__PcrNumber', pyxb.binding.datatypes.unsignedLong, required=True)
    __PcrNumber._DeclarationLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 71, 7)
    __PcrNumber._UseLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 71, 7)
    
    PcrNumber = property(__PcrNumber.value, __PcrNumber.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __SnapshotRef.name() : __SnapshotRef,
        __PcrNumber.name() : __PcrNumber
    })



# Complex type {http://www.trustedcomputinggroup.org/XML/SCHEMA/Integrity_Report_v1_0#}SnapshotType with content type ELEMENT_ONLY
class SnapshotType (_ImportedBinding__core.IntegrityManifestType):
    """Complex type {http://www.trustedcomputinggroup.org/XML/SCHEMA/Integrity_Report_v1_0#}SnapshotType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SnapshotType')
    _XSDLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 129, 1)
    _ElementMap = _ImportedBinding__core.IntegrityManifestType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__core.IntegrityManifestType._AttributeMap.copy()
    # Base type is _ImportedBinding__core.IntegrityManifestType
    
    # Element ComponentID ({http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}ComponentID) inherited from {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}IntegrityManifestType
    
    # Element SignerInfo ({http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}SignerInfo) inherited from {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}IntegrityManifestType
    
    # Element ConfidenceValue ({http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}ConfidenceValue) inherited from {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}IntegrityManifestType
    
    # Element Collector ({http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}Collector) inherited from {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}IntegrityManifestType
    
    # Element TransformMethod ({http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}TransformMethod) inherited from {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}IntegrityManifestType
    
    # Element DigestMethod ({http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}DigestMethod) inherited from {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}IntegrityManifestType
    
    # Element Values ({http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}Values) inherited from {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}IntegrityManifestType
    
    # Element AssertionInfo ({http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}AssertionInfo) inherited from {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}IntegrityManifestType
    
    # Element PlatformClass ({http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}PlatformClass) inherited from {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}IntegrityManifestType
    
    # Element SubComponents ({http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}SubComponents) inherited from {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}IntegrityManifestType
    
    # Element {http://www.trustedcomputinggroup.org/XML/SCHEMA/Integrity_Report_v1_0#}CompositeHash uses Python identifier CompositeHash
    __CompositeHash = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'CompositeHash'), 'CompositeHash', '__httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0_SnapshotType_httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0CompositeHash', True, pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 133, 5), )

    
    CompositeHash = property(__CompositeHash.value, __CompositeHash.set, None, None)

    
    # Element {http://www.trustedcomputinggroup.org/XML/SCHEMA/Integrity_Report_v1_0#}PcrHash uses Python identifier PcrHash
    __PcrHash = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'PcrHash'), 'PcrHash', '__httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0_SnapshotType_httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0PcrHash', True, pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 134, 5), )

    
    PcrHash = property(__PcrHash.value, __PcrHash.set, None, None)

    
    # Attribute Id inherited from {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}IntegrityManifestType
    
    # Attribute RevLevel inherited from {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}IntegrityManifestType
    
    # Attribute UUID uses Python identifier UUID
    __UUID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'UUID'), 'UUID', '__httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0_SnapshotType_UUID', pyxb.binding.datatypes.NMTOKEN, required=True)
    __UUID._DeclarationLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 136, 4)
    __UUID._UseLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 136, 4)
    
    UUID = property(__UUID.value, __UUID.set, None, None)

    _ElementMap.update({
        __CompositeHash.name() : __CompositeHash,
        __PcrHash.name() : __PcrHash
    })
    _AttributeMap.update({
        __UUID.name() : __UUID
    })
Namespace.addCategoryObject('typeBinding', u'SnapshotType', SnapshotType)


# Complex type {http://www.trustedcomputinggroup.org/XML/SCHEMA/Integrity_Report_v1_0#}CompositeHashType with content type SIMPLE
class CompositeHashType (_ImportedBinding__core.HashType):
    """Complex type {http://www.trustedcomputinggroup.org/XML/SCHEMA/Integrity_Report_v1_0#}CompositeHashType with content type SIMPLE"""
    _TypeDefinition = _ImportedBinding__ds.DigestValueType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CompositeHashType')
    _XSDLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 105, 1)
    _ElementMap = _ImportedBinding__core.HashType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__core.HashType._AttributeMap.copy()
    # Base type is _ImportedBinding__core.HashType
    
    # Attribute Id inherited from {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}DigestValueType
    
    # Attribute AlgRef inherited from {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}DigestValueType
    
    # Attribute TransformRefs inherited from {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}DigestValueType
    
    # Attribute ExtendOrder inherited from {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}HashType
    
    # Attribute Name uses Python identifier Name
    __Name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Name'), 'Name', '__httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0_CompositeHashType_Name', pyxb.binding.datatypes.normalizedString)
    __Name._DeclarationLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 108, 4)
    __Name._UseLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 108, 4)
    
    Name = property(__Name.value, __Name.set, None, None)

    
    # Attribute Number uses Python identifier Number
    __Number = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Number'), 'Number', '__httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0_CompositeHashType_Number', pyxb.binding.datatypes.integer)
    __Number._DeclarationLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 109, 4)
    __Number._UseLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 109, 4)
    
    Number = property(__Number.value, __Number.set, None, None)

    
    # Attribute StartHash uses Python identifier StartHash
    __StartHash = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'StartHash'), 'StartHash', '__httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0_CompositeHashType_StartHash', _ImportedBinding__ds.DigestValueType)
    __StartHash._DeclarationLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 110, 4)
    __StartHash._UseLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 110, 4)
    
    StartHash = property(__StartHash.value, __StartHash.set, None, None)

    
    # Attribute SyncRef uses Python identifier SyncRef
    __SyncRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'SyncRef'), 'SyncRef', '__httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0_CompositeHashType_SyncRef', pyxb.binding.datatypes.IDREF)
    __SyncRef._DeclarationLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 111, 4)
    __SyncRef._UseLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 111, 4)
    
    SyncRef = property(__SyncRef.value, __SyncRef.set, None, None)

    
    # Attribute Timestamp uses Python identifier Timestamp
    __Timestamp = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Timestamp'), 'Timestamp', '__httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0_CompositeHashType_Timestamp', pyxb.binding.datatypes.dateTime)
    __Timestamp._DeclarationLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 112, 4)
    __Timestamp._UseLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 112, 4)
    
    Timestamp = property(__Timestamp.value, __Timestamp.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Name.name() : __Name,
        __Number.name() : __Number,
        __StartHash.name() : __StartHash,
        __SyncRef.name() : __SyncRef,
        __Timestamp.name() : __Timestamp
    })
Namespace.addCategoryObject('typeBinding', u'CompositeHashType', CompositeHashType)


# Complex type {http://www.trustedcomputinggroup.org/XML/SCHEMA/Integrity_Report_v1_0#}TpmDigestValueType with content type SIMPLE
class TpmDigestValueType (_ImportedBinding__core.HashType):
    """Complex type {http://www.trustedcomputinggroup.org/XML/SCHEMA/Integrity_Report_v1_0#}TpmDigestValueType with content type SIMPLE"""
    _TypeDefinition = _ImportedBinding__ds.DigestValueType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TpmDigestValueType')
    _XSDLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 116, 1)
    _ElementMap = _ImportedBinding__core.HashType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__core.HashType._AttributeMap.copy()
    # Base type is _ImportedBinding__core.HashType
    
    # Attribute Id inherited from {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}DigestValueType
    
    # Attribute AlgRef inherited from {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}DigestValueType
    
    # Attribute TransformRefs inherited from {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}DigestValueType
    
    # Attribute ExtendOrder inherited from {http://www.trustedcomputinggroup.org/XML/SCHEMA/Core_Integrity_v1_0_1#}HashType
    
    # Attribute Locality uses Python identifier Locality
    __Locality = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Locality'), 'Locality', '__httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0_TpmDigestValueType_Locality', pyxb.binding.datatypes.integer)
    __Locality._DeclarationLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 119, 4)
    __Locality._UseLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 119, 4)
    
    Locality = property(__Locality.value, __Locality.set, None, None)

    
    # Attribute IsResetable uses Python identifier IsResetable
    __IsResetable = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'IsResetable'), 'IsResetable', '__httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0_TpmDigestValueType_IsResetable', pyxb.binding.datatypes.boolean, required=True)
    __IsResetable._DeclarationLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 120, 4)
    __IsResetable._UseLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 120, 4)
    
    IsResetable = property(__IsResetable.value, __IsResetable.set, None, None)

    
    # Attribute Name uses Python identifier Name
    __Name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Name'), 'Name', '__httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0_TpmDigestValueType_Name', pyxb.binding.datatypes.normalizedString)
    __Name._DeclarationLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 121, 4)
    __Name._UseLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 121, 4)
    
    Name = property(__Name.value, __Name.set, None, None)

    
    # Attribute Number uses Python identifier Number
    __Number = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Number'), 'Number', '__httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0_TpmDigestValueType_Number', pyxb.binding.datatypes.integer)
    __Number._DeclarationLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 122, 4)
    __Number._UseLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 122, 4)
    
    Number = property(__Number.value, __Number.set, None, None)

    
    # Attribute StartHash uses Python identifier StartHash
    __StartHash = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'StartHash'), 'StartHash', '__httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0_TpmDigestValueType_StartHash', _ImportedBinding__ds.DigestValueType, required=True)
    __StartHash._DeclarationLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 123, 4)
    __StartHash._UseLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 123, 4)
    
    StartHash = property(__StartHash.value, __StartHash.set, None, None)

    
    # Attribute SyncRef uses Python identifier SyncRef
    __SyncRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'SyncRef'), 'SyncRef', '__httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0_TpmDigestValueType_SyncRef', pyxb.binding.datatypes.IDREF)
    __SyncRef._DeclarationLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 124, 4)
    __SyncRef._UseLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 124, 4)
    
    SyncRef = property(__SyncRef.value, __SyncRef.set, None, None)

    
    # Attribute Timestamp uses Python identifier Timestamp
    __Timestamp = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Timestamp'), 'Timestamp', '__httpwww_trustedcomputinggroup_orgXMLSCHEMAIntegrity_Report_v1_0_TpmDigestValueType_Timestamp', pyxb.binding.datatypes.dateTime)
    __Timestamp._DeclarationLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 125, 4)
    __Timestamp._UseLocation = pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 125, 4)
    
    Timestamp = property(__Timestamp.value, __Timestamp.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Locality.name() : __Locality,
        __IsResetable.name() : __IsResetable,
        __Name.name() : __Name,
        __Number.name() : __Number,
        __StartHash.name() : __StartHash,
        __SyncRef.name() : __SyncRef,
        __Timestamp.name() : __Timestamp
    })
Namespace.addCategoryObject('typeBinding', u'TpmDigestValueType', TpmDigestValueType)


Report = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Report'), ReportType, location=pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 153, 1))
Namespace.addCategoryObject('elementBinding', Report.name().localName(), Report)

Snapshot = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Snapshot'), SnapshotType, location=pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 140, 1))
Namespace.addCategoryObject('elementBinding', Snapshot.name().localName(), Snapshot)



QuoteType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PcrComposite'), PcrCompositeType, scope=QuoteType, location=pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 23, 3)))

QuoteType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'QuoteInfo'), QuoteInfoType, scope=QuoteType, location=pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 24, 3)))

QuoteType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TpmInfo'), CTD_ANON, scope=QuoteType, location=pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 25, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 25, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(QuoteType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PcrComposite')), pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 23, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(QuoteType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'QuoteInfo')), pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 24, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QuoteType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TpmInfo')), pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 25, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
QuoteType._Automaton = _BuildAutomaton()




CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CapVersionInfo'), CapVersionInfoType, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 28, 6)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TpmManufacturer'), pyxb.binding.datatypes.normalizedString, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 29, 6)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CapVersionInfo')), pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 28, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TpmManufacturer')), pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 29, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton_()




Quote2Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'QuoteInfo2'), QuoteInfo2Type, scope=Quote2Type, location=pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 46, 3)))

Quote2Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CapVersionInfo'), CapVersionInfoType, scope=Quote2Type, location=pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 47, 3)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 47, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Quote2Type._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'QuoteInfo2')), pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 46, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Quote2Type._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CapVersionInfo')), pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 47, 3))
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
Quote2Type._Automaton = _BuildAutomaton_2()




QuoteInfo2Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PcrInfoShort'), PcrInfoShortType, scope=QuoteInfo2Type, location=pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 52, 3)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(QuoteInfo2Type._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PcrInfoShort')), pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 52, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
QuoteInfo2Type._Automaton = _BuildAutomaton_3()




PcrCompositeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PcrSelection'), PcrSelectionType, scope=PcrCompositeType, location=pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 64, 3)))

PcrCompositeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ValueSize'), pyxb.binding.datatypes.unsignedLong, scope=PcrCompositeType, location=pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 65, 3)))

PcrCompositeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PcrValue'), CTD_ANON_, scope=PcrCompositeType, location=pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 66, 3)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PcrCompositeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PcrSelection')), pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 64, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PcrCompositeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ValueSize')), pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 65, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PcrCompositeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PcrValue')), pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 66, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
PcrCompositeType._Automaton = _BuildAutomaton_4()




PcrInfoShortType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PcrSelection'), PcrSelectionType, scope=PcrInfoShortType, location=pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 80, 3)))

PcrInfoShortType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'LocalityAtRelease'), pyxb.binding.datatypes.unsignedByte, scope=PcrInfoShortType, location=pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 81, 3)))

PcrInfoShortType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CompositeHash'), _ImportedBinding__ds.DigestValueType, scope=PcrInfoShortType, location=pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 82, 3)))

PcrInfoShortType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PcrComposite'), PcrCompositeType, scope=PcrInfoShortType, location=pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 83, 3)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PcrInfoShortType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PcrSelection')), pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 80, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PcrInfoShortType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'LocalityAtRelease')), pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 81, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PcrInfoShortType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CompositeHash')), pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 82, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PcrInfoShortType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PcrComposite')), pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 83, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
PcrInfoShortType._Automaton = _BuildAutomaton_5()




QuoteSignatureType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CanonicalizationMethod'), _ImportedBinding__ds.CanonicalizationMethodType, scope=QuoteSignatureType, location=pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 88, 3)))

QuoteSignatureType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SignatureMethod'), _ImportedBinding__ds.SignatureMethodType, scope=QuoteSignatureType, location=pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 89, 3)))

QuoteSignatureType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SignatureValue'), _ImportedBinding__ds.SignatureValueType, scope=QuoteSignatureType, location=pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 90, 3)))

QuoteSignatureType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'KeyInfo'), _ImportedBinding__ds.KeyInfoType, scope=QuoteSignatureType, location=pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 91, 3)))

QuoteSignatureType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ObjectType'), _ImportedBinding__ds.ObjectType, scope=QuoteSignatureType, location=pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 92, 3)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 88, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 92, 3))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(QuoteSignatureType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CanonicalizationMethod')), pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 88, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(QuoteSignatureType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SignatureMethod')), pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 89, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(QuoteSignatureType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SignatureValue')), pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 90, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(QuoteSignatureType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'KeyInfo')), pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 91, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(QuoteSignatureType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ObjectType')), pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 92, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
QuoteSignatureType._Automaton = _BuildAutomaton_6()




QuoteDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Quote'), QuoteType, scope=QuoteDataType, location=pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 98, 4)))

QuoteDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Quote2'), Quote2Type, scope=QuoteDataType, location=pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 99, 4)))

QuoteDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TpmSignature'), QuoteSignatureType, scope=QuoteDataType, location=pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 101, 3)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(QuoteDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Quote')), pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 98, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(QuoteDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Quote2')), pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 99, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(QuoteDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TpmSignature')), pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 101, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
QuoteDataType._Automaton = _BuildAutomaton_7()




ReportType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SignerInfo'), _ImportedBinding__core.SignerInfoType, scope=ReportType, location=pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 143, 3)))

ReportType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ConfidenceValue'), _ImportedBinding__core.ConfidenceValueType, scope=ReportType, location=pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 144, 3)))

ReportType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'QuoteData'), QuoteDataType, scope=ReportType, location=pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 145, 3)))

ReportType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SnapshotCollection'), SnapshotType, scope=ReportType, location=pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 146, 3)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 143, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 144, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 145, 3))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ReportType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SignerInfo')), pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 143, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ReportType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ConfidenceValue')), pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 144, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ReportType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'QuoteData')), pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 145, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ReportType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SnapshotCollection')), pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 146, 3))
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
ReportType._Automaton = _BuildAutomaton_8()




SnapshotType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CompositeHash'), CompositeHashType, scope=SnapshotType, location=pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 133, 5)))

SnapshotType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PcrHash'), TpmDigestValueType, scope=SnapshotType, location=pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 134, 5)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
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
    cc_9 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 132, 4))
    counters.add(cc_9)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SnapshotType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, u'ComponentID')), pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 79, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SnapshotType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, u'SignerInfo')), pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 80, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(SnapshotType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, u'ConfidenceValue')), pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 81, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(SnapshotType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, u'Collector')), pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 82, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(SnapshotType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, u'TransformMethod')), pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 83, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(SnapshotType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, u'DigestMethod')), pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 84, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(SnapshotType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, u'Values')), pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 85, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(SnapshotType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, u'AssertionInfo')), pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 86, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(SnapshotType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, u'PlatformClass')), pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 87, 3))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(SnapshotType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, u'SubComponents')), pyxb.utils.utility.Location(u'/home/robyz/sources/pyxb/Core_Integrity_Manifest_v1_0_1.xsd', 88, 3))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(SnapshotType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CompositeHash')), pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 133, 5))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(SnapshotType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PcrHash')), pyxb.utils.utility.Location('/home/robyz/sources/pyxb/Integrity_Report_Manifest_v1_0.xsd', 134, 5))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
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
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
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
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
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
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
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
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
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
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
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
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
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
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, True) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, True) ]))
    st_11._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SnapshotType._Automaton = _BuildAutomaton_9()

