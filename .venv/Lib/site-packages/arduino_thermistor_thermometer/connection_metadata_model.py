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
     'description': 'LinkML Connection Metadata Model.',
     'id': 'https://w3id.org/opensourcelab/connection_metadata_model',
     'imports': ['linkml:types'],
     'license': 'https://creativecommons.org/publicdomain/zero/1.0/',
     'name': 'Connection-Metadata-Model',
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
     'source_file': 'connection_metadata_model.yaml',
     'types': {'NaN': {'base': 'float',
                       'description': 'Not-A-Number (NaN) is a numeric data type '
                                      'value representing an undefined or '
                                      'un-representable value.',
                       'exact_mappings': ['schema:NaN', 'python:np.nan'],
                       'from_schema': 'https://w3id.org/opensourcelab/connection_metadata_model',
                       'name': 'NaN',
                       'notes': ['If you are authoring schemas in LinkML YAML, the '
                                 'type is referenced with the lower case '
                                 '"integer".'],
                       'repr': 'np.nan',
                       'uri': 'xsd:float'}}} )


class ConnectionMetaData(ConfiguredBaseModel):
    """
    \"The Connection Metadata.\"
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'oso:device/connectionMetaData',
         'from_schema': 'https://w3id.org/opensourcelab/connection_metadata_model'})

    id: str = Field(..., description="""\"The identifier of the resource.\"""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['ConnectionMetaData', 'Connection'],
         'slot_uri': 'http://purl.org/dc/terms/identifier'} })
    timestamp: datetime  = Field(..., description="""\"The timestamp of the measurement.\"""", json_schema_extra = { "linkml_meta": {'alias': 'timestamp',
         'domain_of': ['ConnectionMetaData', 'Connection'],
         'slot_uri': 'http://purl.org/dc/terms/date'} })
    description: Optional[str] = Field(None, description="""\"A description of the calculation / measurement.\"""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['ConnectionMetaData', 'Connection'],
         'slot_uri': 'http://purl.org/dc/terms/description'} })
    iri: Optional[str] = Field(None, description="""\"The International Resource Identifier (IRI) of the entity.\"""", json_schema_extra = { "linkml_meta": {'alias': 'iri',
         'domain_of': ['ConnectionMetaData'],
         'slot_uri': 'oso:entity/IRI'} })
    connection: Optional[Connection] = Field(None, description="""\"The connection descriptor, e.g., a set of connection parameters, like IP, port, bus, etc.\"""", json_schema_extra = { "linkml_meta": {'alias': 'connection',
         'domain_of': ['ConnectionMetaData'],
         'slot_uri': 'oso:device/connection'} })
    configuration: Optional[str] = Field(None, description="""\"Extra / additional configuration of the hardware, in JSON-LD format.\"""", json_schema_extra = { "linkml_meta": {'alias': 'configuration',
         'domain_of': ['ConnectionMetaData'],
         'slot_uri': 'oso:device/configuration'} })


class Connection(ConfiguredBaseModel):
    """
    \"The Connection Descriptor.\"
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'oso:device/Connection',
         'from_schema': 'https://w3id.org/opensourcelab/connection_metadata_model'})

    id: str = Field(..., description="""\"The identifier of the resource.\"""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['ConnectionMetaData', 'Connection'],
         'slot_uri': 'http://purl.org/dc/terms/identifier'} })
    timestamp: datetime  = Field(..., description="""\"The timestamp of the measurement.\"""", json_schema_extra = { "linkml_meta": {'alias': 'timestamp',
         'domain_of': ['ConnectionMetaData', 'Connection'],
         'slot_uri': 'http://purl.org/dc/terms/date'} })
    description: Optional[str] = Field(None, description="""\"A description of the calculation / measurement.\"""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['ConnectionMetaData', 'Connection'],
         'slot_uri': 'http://purl.org/dc/terms/description'} })
    connection_type: Optional[str] = Field(None, description="""\"The type of connection, e.g., Ethernet, USB, etc.\"""", json_schema_extra = { "linkml_meta": {'alias': 'connection_type',
         'domain_of': ['Connection'],
         'slot_uri': 'oso:device/connectionType'} })
    connection_address: Optional[str] = Field(None, description="""\"The address of the connection.\"""", json_schema_extra = { "linkml_meta": {'alias': 'connection_address',
         'domain_of': ['Connection'],
         'slot_uri': 'oso:device/connectionAddress'} })
    port: Optional[str] = Field(None, description="""\"The port of the connection. (e.g., 80, 8080, etc.)\"""", json_schema_extra = { "linkml_meta": {'alias': 'port', 'domain_of': ['Connection'], 'slot_uri': 'oso:device/port'} })
    socket: Optional[str] = Field(None, description="""\"The socket of the connection.\"""", json_schema_extra = { "linkml_meta": {'alias': 'socket',
         'domain_of': ['Connection'],
         'slot_uri': 'oso:device/socket'} })
    bus: Optional[str] = Field(None, description="""\"The bus identifier of the connection.\"""", json_schema_extra = { "linkml_meta": {'alias': 'bus', 'domain_of': ['Connection'], 'slot_uri': 'oso:device/bus'} })
    serial_port: Optional[str] = Field(None, description="""\"The serial port of the connection.\"""", json_schema_extra = { "linkml_meta": {'alias': 'serial_port',
         'domain_of': ['Connection'],
         'slot_uri': 'oso:device/serialPort'} })
    baud_rate: Optional[str] = Field(None, description="""\"The baud rate of the connection.\"""", json_schema_extra = { "linkml_meta": {'alias': 'baud_rate',
         'domain_of': ['Connection'],
         'slot_uri': 'oso:device/baudRate'} })
    data_bits: Optional[str] = Field(None, description="""\"The data bits of the connection.\"""", json_schema_extra = { "linkml_meta": {'alias': 'data_bits',
         'domain_of': ['Connection'],
         'slot_uri': 'oso:device/dataBits'} })
    stop_bits: Optional[str] = Field(None, description="""\"The stop bits of the connection.\"""", json_schema_extra = { "linkml_meta": {'alias': 'stop_bits',
         'domain_of': ['Connection'],
         'slot_uri': 'oso:device/stopBits'} })
    parity: Optional[str] = Field(None, description="""\"The parity of the connection.\"""", json_schema_extra = { "linkml_meta": {'alias': 'parity',
         'domain_of': ['Connection'],
         'slot_uri': 'oso:device/parity'} })
    flow_control: Optional[str] = Field(None, description="""\"The flow control of the connection.\"""", json_schema_extra = { "linkml_meta": {'alias': 'flow_control',
         'domain_of': ['Connection'],
         'slot_uri': 'oso:device/flowControl'} })
    parameters: Optional[str] = Field(None, description="""\"Generic additional parameters - in JSON-LD.\"""", json_schema_extra = { "linkml_meta": {'alias': 'parameters',
         'domain_of': ['Connection'],
         'slot_uri': 'oso:device/parameters'} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
ConnectionMetaData.model_rebuild()
Connection.model_rebuild()

