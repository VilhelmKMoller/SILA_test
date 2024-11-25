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
     'description': 'LinkML Storage Metadata Model.',
     'id': 'https://w3id.org/opensourcelab/storage_metadata_model',
     'imports': ['linkml:types'],
     'license': 'https://creativecommons.org/publicdomain/zero/1.0/',
     'name': 'Storage-Metadata-Model',
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
     'source_file': 'storage_metadata_model.yaml',
     'types': {'NaN': {'base': 'float',
                       'description': 'Not-A-Number (NaN) is a numeric data type '
                                      'value representing an undefined or '
                                      'un-representable value.',
                       'exact_mappings': ['schema:NaN', 'python:np.nan'],
                       'from_schema': 'https://w3id.org/opensourcelab/storage_metadata_model',
                       'name': 'NaN',
                       'notes': ['If you are authoring schemas in LinkML YAML, the '
                                 'type is referenced with the lower case '
                                 '"integer".'],
                       'repr': 'np.nan',
                       'uri': 'xsd:float'}}} )


class StorageMetaData(ConfiguredBaseModel):
    """
    \"The Storage Metadata.\"
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'oso:device/storageMetaData',
         'from_schema': 'https://w3id.org/opensourcelab/storage_metadata_model'})

    id: str = Field(..., description="""\"The identifier of the resource.\"""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['StorageMetaData',
                       'LabwarePosition',
                       'LabwareTransfer',
                       'Cover',
                       'LabwareMover',
                       'Rack'],
         'slot_uri': 'http://purl.org/dc/terms/identifier'} })
    timestamp: datetime  = Field(..., description="""\"The timestamp of the measurement.\"""", json_schema_extra = { "linkml_meta": {'alias': 'timestamp',
         'domain_of': ['StorageMetaData',
                       'LabwarePosition',
                       'LabwareTransfer',
                       'Cover',
                       'LabwareMover',
                       'Rack'],
         'slot_uri': 'http://purl.org/dc/terms/date'} })
    description: Optional[str] = Field(None, description="""\"A description of the calculation / measurement.\"""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['StorageMetaData',
                       'LabwarePosition',
                       'LabwareTransfer',
                       'LabwareMover',
                       'Rack'],
         'slot_uri': 'http://purl.org/dc/terms/description'} })
    iri: Optional[str] = Field(None, description="""\"The International Resource Identifier (IRI) of the entity.\"""", json_schema_extra = { "linkml_meta": {'alias': 'iri', 'domain_of': ['StorageMetaData'], 'slot_uri': 'oso:entity/IRI'} })
    labware_min_capacity: Optional[int] = Field(None, description="""labware capacity, min. number of labware, some centrifuges need at least 2 labware, e.g. for balancing""", json_schema_extra = { "linkml_meta": {'alias': 'labware_min_capacity',
         'domain_of': ['StorageMetaData', 'Rack'],
         'slot_uri': 'oso:device/labware_min_capacity'} })
    labware_max_capacity: Optional[int] = Field(None, description="""labware capacity, max. number of labware""", json_schema_extra = { "linkml_meta": {'alias': 'labware_max_capacity',
         'domain_of': ['StorageMetaData', 'Rack'],
         'slot_uri': 'oso:device/labware_max_capacity'} })
    labware_max_height: Optional[float] = Field(None, description="""max. labware height in m""", json_schema_extra = { "linkml_meta": {'alias': 'labware_max_height',
         'domain_of': ['StorageMetaData', 'LabwarePosition', 'Rack'],
         'slot_uri': 'oso:device/labware_max_height'} })
    storage_temperature: Optional[float] = Field(None, description="""\"The storage temperature.\"""", json_schema_extra = { "linkml_meta": {'alias': 'storage_temperature',
         'domain_of': ['StorageMetaData'],
         'slot_uri': 'oso:device/storageTemperature',
         'unit': {'has_quantity_kind': 'OM:Temperature', 'ucum_code': 'K'}} })
    storage_humidity: Optional[float] = Field(None, description="""\"The storage humidity.\"""", json_schema_extra = { "linkml_meta": {'alias': 'storage_humidity',
         'domain_of': ['StorageMetaData'],
         'slot_uri': 'oso:device/storageHumidity',
         'unit': {'has_quantity_kind': 'OM:RelativeHumidity'}} })
    storage_light: Optional[float] = Field(None, description="""\"The storage light.\"""", json_schema_extra = { "linkml_meta": {'alias': 'storage_light',
         'domain_of': ['StorageMetaData'],
         'slot_uri': 'oso:device/storageLight',
         'unit': {'has_quantity_kind': 'OM:LuminousIntensity', 'ucum_code': 'lx'}} })
    storage_gas: Optional[str] = Field(None, description="""\"The storage gas.\"""", json_schema_extra = { "linkml_meta": {'alias': 'storage_gas',
         'domain_of': ['StorageMetaData'],
         'slot_uri': 'oso:device/storageGas'} })
    num_racks: Optional[int] = Field(None, description="""\"The number of racks / stacks in the storage unit.\"""", json_schema_extra = { "linkml_meta": {'alias': 'num_racks',
         'domain_of': ['StorageMetaData'],
         'slot_uri': 'oso:device/numRacks'} })
    racks: Optional[List[str]] = Field(None, description="""\"The racks in the storage unit.\"""", json_schema_extra = { "linkml_meta": {'alias': 'racks',
         'domain_of': ['StorageMetaData'],
         'slot_uri': 'oso:device/racks'} })
    num_labware_movers: Optional[int] = Field(None, description="""\"The number of labware movers in the storage unit.\"""", json_schema_extra = { "linkml_meta": {'alias': 'num_labware_movers',
         'domain_of': ['StorageMetaData'],
         'slot_uri': 'oso:device/numLabwareMovers'} })
    labware_movers: Optional[List[str]] = Field(None, description="""\"The labware movers.\"""", json_schema_extra = { "linkml_meta": {'alias': 'labware_movers',
         'domain_of': ['StorageMetaData'],
         'slot_uri': 'oso:device/labwareMovers'} })
    num_labware_transfers: Optional[int] = Field(None, description="""\"The number of transfer stations in the storage unit.\"""", json_schema_extra = { "linkml_meta": {'alias': 'num_labware_transfers',
         'domain_of': ['StorageMetaData'],
         'slot_uri': 'oso:device/numTransferStations'} })
    labware_transfers: Optional[List[str]] = Field(None, description="""\"The labware transfer stations.\"""", json_schema_extra = { "linkml_meta": {'alias': 'labware_transfers',
         'domain_of': ['StorageMetaData'],
         'slot_uri': 'oso:device/labwareTransfers'} })
    num_covers: Optional[int] = Field(None, description="""\"The number of covers / doors in the storage unit.\"""", json_schema_extra = { "linkml_meta": {'alias': 'num_covers',
         'domain_of': ['StorageMetaData'],
         'slot_uri': 'oso:device/numCovers'} })
    covers: Optional[List[str]] = Field(None, description="""\"The covers / doors.\"""", json_schema_extra = { "linkml_meta": {'alias': 'covers',
         'domain_of': ['StorageMetaData'],
         'slot_uri': 'oso:device/covers'} })
    configuration: Optional[str] = Field(None, description="""\"Extra / additional configuration of the hardware, in JSON-LD format.\"""", json_schema_extra = { "linkml_meta": {'alias': 'configuration',
         'domain_of': ['StorageMetaData',
                       'LabwarePosition',
                       'LabwareTransfer',
                       'Cover',
                       'LabwareMover',
                       'Rack'],
         'slot_uri': 'oso:device/configuration'} })


class LabwarePosition(ConfiguredBaseModel):
    """
    \"The Labware Position / location / Nest in a Rack.\"
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'oso:device/Position',
         'from_schema': 'https://w3id.org/opensourcelab/storage_metadata_model'})

    id: str = Field(..., description="""\"The identifier of the resource.\"""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['StorageMetaData',
                       'LabwarePosition',
                       'LabwareTransfer',
                       'Cover',
                       'LabwareMover',
                       'Rack'],
         'slot_uri': 'http://purl.org/dc/terms/identifier'} })
    timestamp: datetime  = Field(..., description="""\"The timestamp of the measurement.\"""", json_schema_extra = { "linkml_meta": {'alias': 'timestamp',
         'domain_of': ['StorageMetaData',
                       'LabwarePosition',
                       'LabwareTransfer',
                       'Cover',
                       'LabwareMover',
                       'Rack'],
         'slot_uri': 'http://purl.org/dc/terms/date'} })
    name: str = Field(..., description="""\"The name of an entity or object.\"""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['LabwarePosition', 'LabwareTransfer', 'Cover'],
         'slot_uri': 'oso:entity/Name'} })
    description: Optional[str] = Field(None, description="""\"A description of the calculation / measurement.\"""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['StorageMetaData',
                       'LabwarePosition',
                       'LabwareTransfer',
                       'LabwareMover',
                       'Rack'],
         'slot_uri': 'http://purl.org/dc/terms/description'} })
    labware_id: Optional[str] = Field(None, description="""\"A unique identifier of the labware.\"""", json_schema_extra = { "linkml_meta": {'alias': 'labware_id',
         'domain_of': ['LabwarePosition', 'LabwareTransfer', 'LabwareMover'],
         'slot_uri': 'oso:device/labwareID'} })
    labware_max_height: Optional[float] = Field(None, description="""max. labware height in m""", json_schema_extra = { "linkml_meta": {'alias': 'labware_max_height',
         'domain_of': ['StorageMetaData', 'LabwarePosition', 'Rack'],
         'slot_uri': 'oso:device/labware_max_height'} })
    orientation: Optional[str] = Field(None, description="""\"The orientation of the labware in a position, e.g. landscape / portrait.\"""", json_schema_extra = { "linkml_meta": {'alias': 'orientation',
         'domain_of': ['LabwarePosition'],
         'slot_uri': 'oso:device/orientation'} })
    occupied: Optional[bool] = Field(None, description="""\"True if the position is occupied.\"""", json_schema_extra = { "linkml_meta": {'alias': 'occupied',
         'domain_of': ['LabwarePosition', 'LabwareTransfer', 'LabwareMover'],
         'slot_uri': 'oso:device/occupied'} })
    configuration: Optional[str] = Field(None, description="""\"Extra / additional configuration of the hardware, in JSON-LD format.\"""", json_schema_extra = { "linkml_meta": {'alias': 'configuration',
         'domain_of': ['StorageMetaData',
                       'LabwarePosition',
                       'LabwareTransfer',
                       'Cover',
                       'LabwareMover',
                       'Rack'],
         'slot_uri': 'oso:device/configuration'} })


class LabwareTransfer(ConfiguredBaseModel):
    """
    \"The Labware Transfer Station.\"
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'oso:device/LabwareTransfer',
         'from_schema': 'https://w3id.org/opensourcelab/storage_metadata_model'})

    id: str = Field(..., description="""\"The identifier of the resource.\"""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['StorageMetaData',
                       'LabwarePosition',
                       'LabwareTransfer',
                       'Cover',
                       'LabwareMover',
                       'Rack'],
         'slot_uri': 'http://purl.org/dc/terms/identifier'} })
    timestamp: datetime  = Field(..., description="""\"The timestamp of the measurement.\"""", json_schema_extra = { "linkml_meta": {'alias': 'timestamp',
         'domain_of': ['StorageMetaData',
                       'LabwarePosition',
                       'LabwareTransfer',
                       'Cover',
                       'LabwareMover',
                       'Rack'],
         'slot_uri': 'http://purl.org/dc/terms/date'} })
    name: str = Field(..., description="""\"The name of an entity or object.\"""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['LabwarePosition', 'LabwareTransfer', 'Cover'],
         'slot_uri': 'oso:entity/Name'} })
    description: Optional[str] = Field(None, description="""\"A description of the calculation / measurement.\"""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['StorageMetaData',
                       'LabwarePosition',
                       'LabwareTransfer',
                       'LabwareMover',
                       'Rack'],
         'slot_uri': 'http://purl.org/dc/terms/description'} })
    labware_id: Optional[str] = Field(None, description="""\"A unique identifier of the labware.\"""", json_schema_extra = { "linkml_meta": {'alias': 'labware_id',
         'domain_of': ['LabwarePosition', 'LabwareTransfer', 'LabwareMover'],
         'slot_uri': 'oso:device/labwareID'} })
    occupied: Optional[bool] = Field(None, description="""\"True if the position is occupied.\"""", json_schema_extra = { "linkml_meta": {'alias': 'occupied',
         'domain_of': ['LabwarePosition', 'LabwareTransfer', 'LabwareMover'],
         'slot_uri': 'oso:device/occupied'} })
    configuration: Optional[str] = Field(None, description="""\"Extra / additional configuration of the hardware, in JSON-LD format.\"""", json_schema_extra = { "linkml_meta": {'alias': 'configuration',
         'domain_of': ['StorageMetaData',
                       'LabwarePosition',
                       'LabwareTransfer',
                       'Cover',
                       'LabwareMover',
                       'Rack'],
         'slot_uri': 'oso:device/configuration'} })


class Cover(ConfiguredBaseModel):
    """
    \"The Cover or door of a device.\"
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'oso:device/Cover',
         'from_schema': 'https://w3id.org/opensourcelab/storage_metadata_model'})

    id: str = Field(..., description="""\"The identifier of the resource.\"""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['StorageMetaData',
                       'LabwarePosition',
                       'LabwareTransfer',
                       'Cover',
                       'LabwareMover',
                       'Rack'],
         'slot_uri': 'http://purl.org/dc/terms/identifier'} })
    timestamp: datetime  = Field(..., description="""\"The timestamp of the measurement.\"""", json_schema_extra = { "linkml_meta": {'alias': 'timestamp',
         'domain_of': ['StorageMetaData',
                       'LabwarePosition',
                       'LabwareTransfer',
                       'Cover',
                       'LabwareMover',
                       'Rack'],
         'slot_uri': 'http://purl.org/dc/terms/date'} })
    name: str = Field(..., description="""\"The name of an entity or object.\"""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['LabwarePosition', 'LabwareTransfer', 'Cover'],
         'slot_uri': 'oso:entity/Name'} })
    is_open: Optional[bool] = Field(None, description="""\"True if the cover / door is open.\"""", json_schema_extra = { "linkml_meta": {'alias': 'is_open', 'domain_of': ['Cover'], 'slot_uri': 'oso:device/isOpen'} })
    configuration: Optional[str] = Field(None, description="""\"Extra / additional configuration of the hardware, in JSON-LD format.\"""", json_schema_extra = { "linkml_meta": {'alias': 'configuration',
         'domain_of': ['StorageMetaData',
                       'LabwarePosition',
                       'LabwareTransfer',
                       'Cover',
                       'LabwareMover',
                       'Rack'],
         'slot_uri': 'oso:device/configuration'} })


class LabwareMover(ConfiguredBaseModel):
    """
    \"The Labware Mover / internal transport system.\"
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'oso:device/LabwareMover',
         'from_schema': 'https://w3id.org/opensourcelab/storage_metadata_model'})

    id: str = Field(..., description="""\"The identifier of the resource.\"""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['StorageMetaData',
                       'LabwarePosition',
                       'LabwareTransfer',
                       'Cover',
                       'LabwareMover',
                       'Rack'],
         'slot_uri': 'http://purl.org/dc/terms/identifier'} })
    timestamp: datetime  = Field(..., description="""\"The timestamp of the measurement.\"""", json_schema_extra = { "linkml_meta": {'alias': 'timestamp',
         'domain_of': ['StorageMetaData',
                       'LabwarePosition',
                       'LabwareTransfer',
                       'Cover',
                       'LabwareMover',
                       'Rack'],
         'slot_uri': 'http://purl.org/dc/terms/date'} })
    description: Optional[str] = Field(None, description="""\"A description of the calculation / measurement.\"""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['StorageMetaData',
                       'LabwarePosition',
                       'LabwareTransfer',
                       'LabwareMover',
                       'Rack'],
         'slot_uri': 'http://purl.org/dc/terms/description'} })
    labware_id: Optional[str] = Field(None, description="""\"A unique identifier of the labware.\"""", json_schema_extra = { "linkml_meta": {'alias': 'labware_id',
         'domain_of': ['LabwarePosition', 'LabwareTransfer', 'LabwareMover'],
         'slot_uri': 'oso:device/labwareID'} })
    occupied: Optional[bool] = Field(None, description="""\"True if the position is occupied.\"""", json_schema_extra = { "linkml_meta": {'alias': 'occupied',
         'domain_of': ['LabwarePosition', 'LabwareTransfer', 'LabwareMover'],
         'slot_uri': 'oso:device/occupied'} })
    configuration: Optional[str] = Field(None, description="""\"Extra / additional configuration of the hardware, in JSON-LD format.\"""", json_schema_extra = { "linkml_meta": {'alias': 'configuration',
         'domain_of': ['StorageMetaData',
                       'LabwarePosition',
                       'LabwareTransfer',
                       'Cover',
                       'LabwareMover',
                       'Rack'],
         'slot_uri': 'oso:device/configuration'} })


class Rack(ConfiguredBaseModel):
    """
    \"The Rack / Stack - a vertically and/or horizontally arrangement of labware positions.\"
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'oso:device/Rack',
         'from_schema': 'https://w3id.org/opensourcelab/storage_metadata_model'})

    id: str = Field(..., description="""\"The identifier of the resource.\"""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['StorageMetaData',
                       'LabwarePosition',
                       'LabwareTransfer',
                       'Cover',
                       'LabwareMover',
                       'Rack'],
         'slot_uri': 'http://purl.org/dc/terms/identifier'} })
    timestamp: datetime  = Field(..., description="""\"The timestamp of the measurement.\"""", json_schema_extra = { "linkml_meta": {'alias': 'timestamp',
         'domain_of': ['StorageMetaData',
                       'LabwarePosition',
                       'LabwareTransfer',
                       'Cover',
                       'LabwareMover',
                       'Rack'],
         'slot_uri': 'http://purl.org/dc/terms/date'} })
    description: Optional[str] = Field(None, description="""\"A description of the calculation / measurement.\"""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['StorageMetaData',
                       'LabwarePosition',
                       'LabwareTransfer',
                       'LabwareMover',
                       'Rack'],
         'slot_uri': 'http://purl.org/dc/terms/description'} })
    labware_positions: Optional[str] = Field(None, description="""\"The labware positions / locations / nests in the rack.\"""", json_schema_extra = { "linkml_meta": {'alias': 'labware_positions',
         'domain_of': ['Rack'],
         'slot_uri': 'oso:device/positions'} })
    num_cols: Optional[int] = Field(None, description="""\"The number of columns in the rack.\"""", json_schema_extra = { "linkml_meta": {'alias': 'num_cols', 'domain_of': ['Rack'], 'slot_uri': 'oso:device/numCols'} })
    num_rows: Optional[int] = Field(None, description="""\"The number of rows in the rack.\"""", json_schema_extra = { "linkml_meta": {'alias': 'num_rows', 'domain_of': ['Rack'], 'slot_uri': 'oso:device/numRows'} })
    num_layers: Optional[int] = Field(None, description="""\"The number of layers in the rack.\"""", json_schema_extra = { "linkml_meta": {'alias': 'num_layers',
         'domain_of': ['Rack'],
         'slot_uri': 'oso:device/numLayers'} })
    labware_min_capacity: Optional[int] = Field(None, description="""labware capacity, min. number of labware, some centrifuges need at least 2 labware, e.g. for balancing""", json_schema_extra = { "linkml_meta": {'alias': 'labware_min_capacity',
         'domain_of': ['StorageMetaData', 'Rack'],
         'slot_uri': 'oso:device/labware_min_capacity'} })
    labware_max_capacity: Optional[int] = Field(None, description="""labware capacity, max. number of labware""", json_schema_extra = { "linkml_meta": {'alias': 'labware_max_capacity',
         'domain_of': ['StorageMetaData', 'Rack'],
         'slot_uri': 'oso:device/labware_max_capacity'} })
    labware_max_height: Optional[float] = Field(None, description="""max. labware height in m""", json_schema_extra = { "linkml_meta": {'alias': 'labware_max_height',
         'domain_of': ['StorageMetaData', 'LabwarePosition', 'Rack'],
         'slot_uri': 'oso:device/labware_max_height'} })
    is_shaker: Optional[bool] = Field(None, description="""\"True if the rack is a shaker.\"""", json_schema_extra = { "linkml_meta": {'alias': 'is_shaker', 'domain_of': ['Rack'], 'slot_uri': 'oso:device/isShaker'} })
    min_shaking_frequency: Optional[float] = Field(None, description="""\"The minimum shaking frequency.\"""", json_schema_extra = { "linkml_meta": {'alias': 'min_shaking_frequency',
         'domain_of': ['Rack'],
         'slot_uri': 'oso:device/minShakingFrequency',
         'unit': {'has_quantity_kind': 'OM:Frequency', 'ucum_code': 'Hz'}} })
    max_shaking_frequency: Optional[float] = Field(None, description="""\"The maximum shaking frequency.\"""", json_schema_extra = { "linkml_meta": {'alias': 'max_shaking_frequency',
         'domain_of': ['Rack'],
         'slot_uri': 'oso:device/maxShakingFrequency',
         'unit': {'has_quantity_kind': 'OM:Frequency', 'ucum_code': 'Hz'}} })
    target_shaking_frequency: Optional[float] = Field(None, description="""\"The target shaking frequency.\"""", json_schema_extra = { "linkml_meta": {'alias': 'target_shaking_frequency',
         'domain_of': ['Rack'],
         'slot_uri': 'oso:device/targetShakingFrequency',
         'unit': {'has_quantity_kind': 'OM:Frequency', 'ucum_code': 'Hz'}} })
    is_shaking: Optional[bool] = Field(None, description="""\"True if the rack is shaking.\"""", json_schema_extra = { "linkml_meta": {'alias': 'is_shaking',
         'domain_of': ['Rack'],
         'slot_uri': 'oso:device/isShaking'} })
    shaking_required: Optional[bool] = Field(None, description="""\"True if shaking is required.\"""", json_schema_extra = { "linkml_meta": {'alias': 'shaking_required',
         'domain_of': ['Rack'],
         'slot_uri': 'oso:device/shakingRequired'} })
    configuration: Optional[str] = Field(None, description="""\"Extra / additional configuration of the hardware, in JSON-LD format.\"""", json_schema_extra = { "linkml_meta": {'alias': 'configuration',
         'domain_of': ['StorageMetaData',
                       'LabwarePosition',
                       'LabwareTransfer',
                       'Cover',
                       'LabwareMover',
                       'Rack'],
         'slot_uri': 'oso:device/configuration'} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
StorageMetaData.model_rebuild()
LabwarePosition.model_rebuild()
LabwareTransfer.model_rebuild()
Cover.model_rebuild()
LabwareMover.model_rebuild()
Rack.model_rebuild()

