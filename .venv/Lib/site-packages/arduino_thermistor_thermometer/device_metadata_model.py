from __future__ import annotations 

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal 
from enum import Enum 
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    field_validator
)


metamodel_version = "None"
version = "0.0.1"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )
    pass




class LinkMLMeta(RootModel):
    root: Dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'oso',
     'description': 'LinkML Device Metadata Model.',
     'id': 'https://w3id.org/opensourcelab/device_metadata_model',
     'imports': ['linkml:types'],
     'license': 'https://creativecommons.org/publicdomain/zero/1.0/',
     'name': 'Device-Metadata-Model',
     'prefixes': {'OM': {'prefix_prefix': 'OM',
                         'prefix_reference': 'http://www.ontology-of-units-of-measure.org/resource/om-2/'},
                  'UO': {'prefix_prefix': 'UO',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/UO_'},
                  'dcat': {'prefix_prefix': 'dcat',
                           'prefix_reference': 'http://www.w3.org/ns/dcat#'},
                  'dcatap': {'prefix_prefix': 'dcatap',
                             'prefix_reference': 'http://data.europa.eu/m8g/'},
                  'dcmi': {'prefix_prefix': 'dcmi',
                           'prefix_reference': 'http://purl.org/dc/dcmitype/'},
                  'dct': {'prefix_prefix': 'dct',
                          'prefix_reference': 'http://purl.org/dc/terms/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'oso': {'prefix_prefix': 'oso',
                          'prefix_reference': 'http://w3id.org/oso/'},
                  'qudt': {'prefix_prefix': 'qudt',
                           'prefix_reference': 'http://qudt.org/schema/qudt/'},
                  'sh': {'prefix_prefix': 'sh',
                         'prefix_reference': 'https://w3id.org/shacl/'}},
     'source_file': 'device_metadata_model.yaml',
     'types': {'NaN': {'base': 'float',
                       'description': 'Not-A-Number (NaN) is a numeric data type '
                                      'value representing an undefined or '
                                      'un-representable value.',
                       'exact_mappings': ['schema:NaN', 'python:np.nan'],
                       'from_schema': 'https://w3id.org/opensourcelab/device_metadata_model',
                       'name': 'NaN',
                       'notes': ['If you are authoring schemas in LinkML YAML, the '
                                 'type is referenced with the lower case '
                                 '"integer".'],
                       'repr': 'np.nan',
                       'uri': 'xsd:float'}}} )


class Person(ConfiguredBaseModel):
    """
    \"The User class represents a user of the SciDatS system.\"
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'oso:entity',
         'from_schema': 'https://w3id.org/opensourcelab/device_metadata_model'})

    name_last: str = Field(..., description="""\"The last name of the user.\"""", json_schema_extra = { "linkml_meta": {'alias': 'name_last',
         'domain_of': ['Person'],
         'slot_uri': 'oso:entity/lastName'} })
    name_first: str = Field(..., description="""\"The first name of the user.\"""", json_schema_extra = { "linkml_meta": {'alias': 'name_first',
         'domain_of': ['Person'],
         'slot_uri': 'oso:entity/firstName'} })
    email: Optional[str] = Field(None, description="""\"The email address of an entity, person or company.\"""", json_schema_extra = { "linkml_meta": {'alias': 'email',
         'domain_of': ['Person', 'Company'],
         'slot_uri': 'oso:entity/email'} })
    phone_numbers: Optional[List[str]] = Field(None, description="""\"A list of phone numbers.\"""", json_schema_extra = { "linkml_meta": {'alias': 'phone_numbers',
         'domain_of': ['Person', 'Company'],
         'slot_uri': 'oso:entity/phoneNumber'} })
    orcid: str = Field(..., description="""\"The Open Researcher and Contributor ID [ORCID](https://orcid.org/) of a researcher.\"""", json_schema_extra = { "linkml_meta": {'alias': 'orcid', 'domain_of': ['Person'], 'slot_uri': 'oso:entity/ORCID'} })


class Company(ConfiguredBaseModel):
    """
    \"A class representing a Company, e.g., Manufacturer, Service provider.\"
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'oso:entity/Company',
         'from_schema': 'https://w3id.org/opensourcelab/device_metadata_model'})

    id: str = Field(..., description="""\"The identifier of the resource.\"""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['Company', 'DeviceClass', 'DeviceMetaData', 'ServiceInfo'],
         'slot_uri': 'http://purl.org/dc/terms/identifier'} })
    name: str = Field(..., description="""\"The name of an entity or object.\"""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Company', 'DeviceClass', 'ServiceInfo'],
         'slot_uri': 'oso:entity/Name'} })
    url: Optional[str] = Field(None, description="""\"A Uniform Resource Locator (URL) of, e.g., an entity, person or company.\"""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Company'], 'slot_uri': 'oso:entity/url'} })
    email: Optional[str] = Field(None, description="""\"The email address of an entity, person or company.\"""", json_schema_extra = { "linkml_meta": {'alias': 'email',
         'domain_of': ['Person', 'Company'],
         'slot_uri': 'oso:entity/email'} })
    phone_numbers: Optional[List[str]] = Field(None, description="""\"A list of phone numbers.\"""", json_schema_extra = { "linkml_meta": {'alias': 'phone_numbers',
         'domain_of': ['Person', 'Company'],
         'slot_uri': 'oso:entity/phoneNumber'} })
    manufacturer_id: Optional[str] = Field(None, description="""\"Unique ID of a manufacturer (MID).\"""", json_schema_extra = { "linkml_meta": {'alias': 'manufacturer_id',
         'domain_of': ['Company'],
         'slot_uri': 'oso:device/ManufacturerID'} })


class DeviceClass(ConfiguredBaseModel):
    """
    \"The Device Class / Type.\"
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'oso:device/DeviceClass',
         'from_schema': 'https://w3id.org/opensourcelab/device_metadata_model'})

    id: str = Field(..., description="""\"The identifier of the resource.\"""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['Company', 'DeviceClass', 'DeviceMetaData', 'ServiceInfo'],
         'slot_uri': 'http://purl.org/dc/terms/identifier'} })
    name: str = Field(..., description="""\"The name of an entity or object.\"""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Company', 'DeviceClass', 'ServiceInfo'],
         'slot_uri': 'oso:entity/Name'} })
    iri: Optional[str] = Field(None, description="""\"The International Resource Identifier (IRI) of the entity.\"""", json_schema_extra = { "linkml_meta": {'alias': 'iri',
         'domain_of': ['DeviceClass', 'DeviceMetaData'],
         'slot_uri': 'oso:entity/IRI'} })


class DeviceMetaData(ConfiguredBaseModel):
    """
    \"The Device Metadata.\"
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'oso:device/DeviceMetaData',
         'from_schema': 'https://w3id.org/opensourcelab/device_metadata_model'})

    id: str = Field(..., description="""\"The identifier of the resource.\"""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['Company', 'DeviceClass', 'DeviceMetaData', 'ServiceInfo'],
         'slot_uri': 'http://purl.org/dc/terms/identifier'} })
    timestamp: datetime  = Field(..., description="""\"The timestamp of the measurement.\"""", json_schema_extra = { "linkml_meta": {'alias': 'timestamp',
         'domain_of': ['DeviceMetaData', 'ServiceInfo'],
         'slot_uri': 'http://purl.org/dc/terms/date'} })
    description: Optional[str] = Field(None, description="""\"A description of the calculation / measurement.\"""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['DeviceMetaData'],
         'slot_uri': 'http://purl.org/dc/terms/description'} })
    iri: Optional[str] = Field(None, description="""\"The International Resource Identifier (IRI) of the entity.\"""", json_schema_extra = { "linkml_meta": {'alias': 'iri',
         'domain_of': ['DeviceClass', 'DeviceMetaData'],
         'slot_uri': 'oso:entity/IRI'} })
    manufacturers: Optional[List[Company]] = Field(None, description="""\"Manufacturer of the device.\"""", json_schema_extra = { "linkml_meta": {'alias': 'manufacturers',
         'domain_of': ['DeviceMetaData'],
         'slot_uri': 'oso:device/Manufacturer'} })
    device_class: Optional[DeviceClass] = Field(None, description="""\"The Class / Type of the device. E.g. Gas Chromatograph, NMR. Thermometer, UV-spectrometer, MALDI-TOF-MS, HPLC, etc.\"""", json_schema_extra = { "linkml_meta": {'alias': 'device_class',
         'domain_of': ['DeviceMetaData'],
         'slot_uri': 'oso:measurement/deviceClass'} })
    device_name: Optional[str] = Field(None, description="""\"The full name of the device.\"""", json_schema_extra = { "linkml_meta": {'alias': 'device_name',
         'domain_of': ['DeviceMetaData'],
         'slot_uri': 'oso:measurement/deviceName'} })
    model_name: Optional[str] = Field(None, description="""\"The model name of the device.\"""", json_schema_extra = { "linkml_meta": {'alias': 'model_name',
         'domain_of': ['DeviceMetaData'],
         'slot_uri': 'oso:measurement/deviceModel'} })
    device_version: Optional[str] = Field(None, description="""\"The version of the device.\"""", json_schema_extra = { "linkml_meta": {'alias': 'device_version',
         'domain_of': ['DeviceMetaData'],
         'slot_uri': 'oso:/device/version'} })
    device_serial_number: Optional[str] = Field(None, description="""\"The serial number of the device.\"""", json_schema_extra = { "linkml_meta": {'alias': 'device_serial_number',
         'domain_of': ['DeviceMetaData'],
         'slot_uri': 'oso:device/serialNumber'} })
    part_number: Optional[str] = Field(None, description="""\"The part number.\"""", json_schema_extra = { "linkml_meta": {'alias': 'part_number',
         'domain_of': ['DeviceMetaData'],
         'slot_uri': 'oso:device/partNumber'} })
    device_pid: Optional[str] = Field(None, description="""\"The persistent and unique identifier (PID) of the device.\"""", json_schema_extra = { "linkml_meta": {'alias': 'device_pid',
         'domain_of': ['DeviceMetaData'],
         'slot_uri': 'oso:/device/PID'} })
    pac_id: Optional[str] = Field(None, description="""\"The Publicly Addressable Content IDentifier (PAC-ID) is a unique identifier (s. https://github.com/ApiniLabs/PAC-ID) .\"""", json_schema_extra = { "linkml_meta": {'alias': 'pac_id',
         'domain_of': ['DeviceMetaData'],
         'slot_uri': 'oso:device/pacID'} })
    firmware_version: str = Field(..., description="""\"The version of the firmware of the device.\"""", json_schema_extra = { "linkml_meta": {'alias': 'firmware_version',
         'domain_of': ['DeviceMetaData'],
         'slot_uri': 'oso:device/deviceFirmwareVersion'} })
    device_manual_url: Optional[str] = Field(None, description="""\"An URL to the manual of the device.\"""", json_schema_extra = { "linkml_meta": {'alias': 'device_manual_url',
         'domain_of': ['DeviceMetaData'],
         'slot_uri': 'oso:device/deviceManual'} })
    device_quick_start_guide_url: Optional[str] = Field(None, description="""\"An URL to the quick start guide of the device.\"""", json_schema_extra = { "linkml_meta": {'alias': 'device_quick_start_guide_url',
         'domain_of': ['DeviceMetaData'],
         'slot_uri': 'oso:device/deviceQuickStartGuide'} })
    device_service_manual_url: Optional[str] = Field(None, description="""\"An URL to the service manual of the device.\"""", json_schema_extra = { "linkml_meta": {'alias': 'device_service_manual_url',
         'domain_of': ['DeviceMetaData'],
         'slot_uri': 'oso:device/deviceServiceManual'} })
    registration_number: Optional[str] = Field(None, description="""\"The registration number of the device, e.g. inventory number.\"""", json_schema_extra = { "linkml_meta": {'alias': 'registration_number',
         'domain_of': ['DeviceMetaData'],
         'slot_uri': 'oso:device/deviceRegistrationNumber'} })
    registration_barcode: Optional[str] = Field(None, description="""\"The registration barcode of the device.\"""", json_schema_extra = { "linkml_meta": {'alias': 'registration_barcode',
         'domain_of': ['DeviceMetaData'],
         'slot_uri': 'oso:device/deviceRegistrationBarcode'} })
    purchase_date: Optional[datetime ] = Field(None, description="""\"The date of purchase of the device.\"""", json_schema_extra = { "linkml_meta": {'alias': 'purchase_date',
         'domain_of': ['DeviceMetaData'],
         'slot_uri': 'oso:device/devicePurchaseDate'} })
    end_of_warranty_date: Optional[datetime ] = Field(None, description="""\"The end of warranty date of the device.\"""", json_schema_extra = { "linkml_meta": {'alias': 'end_of_warranty_date',
         'domain_of': ['DeviceMetaData'],
         'slot_uri': 'oso:device/deviceEndOfWarrantyDate'} })
    service_date_last: Optional[datetime ] = Field(None, description="""\"The date of the last service.\"""", json_schema_extra = { "linkml_meta": {'alias': 'service_date_last',
         'domain_of': ['DeviceMetaData', 'ServiceInfo'],
         'slot_uri': 'oso:device/deviceServiceDateLast'} })
    service_date_next: Optional[datetime ] = Field(None, description="""\"The date of the next service.\"""", json_schema_extra = { "linkml_meta": {'alias': 'service_date_next',
         'domain_of': ['DeviceMetaData', 'ServiceInfo'],
         'slot_uri': 'oso:device/deviceServiceDateNext'} })
    service_type: Optional[str] = Field(None, description="""\"The type of service, e.g., calibration, maintenance, repair.\"""", json_schema_extra = { "linkml_meta": {'alias': 'service_type',
         'domain_of': ['DeviceMetaData', 'ServiceInfo'],
         'slot_uri': 'oso:device/deviceServiceType'} })
    service_description: Optional[str] = Field(None, description="""\"A description of the service.\"""", json_schema_extra = { "linkml_meta": {'alias': 'service_description',
         'domain_of': ['DeviceMetaData', 'ServiceInfo'],
         'slot_uri': 'oso:device/deviceServiceDescription'} })
    service_report: Optional[str] = Field(None, description="""\"An URL to the service report.\"""", json_schema_extra = { "linkml_meta": {'alias': 'service_report',
         'domain_of': ['DeviceMetaData', 'ServiceInfo'],
         'slot_uri': 'oso:device/deviceServiceReport'} })
    service_provider: Optional[Company] = Field(None, description="""\"The service provider, e.g. a company.\"""", json_schema_extra = { "linkml_meta": {'alias': 'service_provider',
         'domain_of': ['DeviceMetaData', 'ServiceInfo'],
         'slot_uri': 'oso:device/deviceServiceProvider'} })
    service_engineer: Optional[Person] = Field(None, description="""\"The service engineer.\"""", json_schema_extra = { "linkml_meta": {'alias': 'service_engineer',
         'domain_of': ['DeviceMetaData', 'ServiceInfo'],
         'slot_uri': 'oso:device/deviceServiceEngineer'} })


class ServiceInfo(ConfiguredBaseModel):
    """
    \"The Service Info.\"
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'oso:device/ServiceInfo',
         'from_schema': 'https://w3id.org/opensourcelab/device_metadata_model'})

    id: str = Field(..., description="""\"The identifier of the resource.\"""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['Company', 'DeviceClass', 'DeviceMetaData', 'ServiceInfo'],
         'slot_uri': 'http://purl.org/dc/terms/identifier'} })
    timestamp: datetime  = Field(..., description="""\"The timestamp of the measurement.\"""", json_schema_extra = { "linkml_meta": {'alias': 'timestamp',
         'domain_of': ['DeviceMetaData', 'ServiceInfo'],
         'slot_uri': 'http://purl.org/dc/terms/date'} })
    name: str = Field(..., description="""\"The name of an entity or object.\"""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Company', 'DeviceClass', 'ServiceInfo'],
         'slot_uri': 'oso:entity/Name'} })
    service_description: Optional[str] = Field(None, description="""\"A description of the service.\"""", json_schema_extra = { "linkml_meta": {'alias': 'service_description',
         'domain_of': ['DeviceMetaData', 'ServiceInfo'],
         'slot_uri': 'oso:device/deviceServiceDescription'} })
    service_type: Optional[str] = Field(None, description="""\"The type of service, e.g., calibration, maintenance, repair.\"""", json_schema_extra = { "linkml_meta": {'alias': 'service_type',
         'domain_of': ['DeviceMetaData', 'ServiceInfo'],
         'slot_uri': 'oso:device/deviceServiceType'} })
    service_date_last: Optional[datetime ] = Field(None, description="""\"The date of the last service.\"""", json_schema_extra = { "linkml_meta": {'alias': 'service_date_last',
         'domain_of': ['DeviceMetaData', 'ServiceInfo'],
         'slot_uri': 'oso:device/deviceServiceDateLast'} })
    service_date_next: Optional[datetime ] = Field(None, description="""\"The date of the next service.\"""", json_schema_extra = { "linkml_meta": {'alias': 'service_date_next',
         'domain_of': ['DeviceMetaData', 'ServiceInfo'],
         'slot_uri': 'oso:device/deviceServiceDateNext'} })
    service_report: Optional[str] = Field(None, description="""\"An URL to the service report.\"""", json_schema_extra = { "linkml_meta": {'alias': 'service_report',
         'domain_of': ['DeviceMetaData', 'ServiceInfo'],
         'slot_uri': 'oso:device/deviceServiceReport'} })
    service_provider: Optional[Company] = Field(None, description="""\"The service provider, e.g. a company.\"""", json_schema_extra = { "linkml_meta": {'alias': 'service_provider',
         'domain_of': ['DeviceMetaData', 'ServiceInfo'],
         'slot_uri': 'oso:device/deviceServiceProvider'} })
    service_engineer: Optional[Person] = Field(None, description="""\"The service engineer.\"""", json_schema_extra = { "linkml_meta": {'alias': 'service_engineer',
         'domain_of': ['DeviceMetaData', 'ServiceInfo'],
         'slot_uri': 'oso:device/deviceServiceEngineer'} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Person.model_rebuild()
Company.model_rebuild()
DeviceClass.model_rebuild()
DeviceMetaData.model_rebuild()
ServiceInfo.model_rebuild()

