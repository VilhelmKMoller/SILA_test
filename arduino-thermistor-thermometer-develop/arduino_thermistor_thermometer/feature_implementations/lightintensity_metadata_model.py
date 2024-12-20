from __future__ import annotations 
from datetime import (
    datetime,
    date
)
from decimal import Decimal 
from enum import Enum 
import re
from typing import (
    Any,
    ClassVar,
    List,
    Literal,
    Dict,
    Optional,
    Union
)
from pydantic.version import VERSION  as PYDANTIC_VERSION 
if int(PYDANTIC_VERSION[0])>=2:
    from pydantic import (
        BaseModel,
        ConfigDict,
        Field,
        RootModel,
        field_validator
    )
else:
    from pydantic import (
        BaseModel,
        Field,
        validator
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


linkml_meta = LinkMLMeta({'default_prefix': 'https://w3id.org/Measurement/core_metadata_model/',
     'description': 'Measurement LinkML Core Metadata Model.',
     'id': 'https://w3id.org/Measurement/core_metadata_model',
     'name': 'Measurement-Core-Metadata-Model'} )


class LightIntensityMetaData(ConfiguredBaseModel):
    """
    \"The LightIntensityMetaData class represents the core metadata model for LightIntensityMetaData.\"
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/Measurement/core_metadata_model'})

    id: str = Field(..., description="""\"The identifier of the resource.\"""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['LightIntensityMetaData'],
         'slot_uri': 'http://purl.org/dc/terms/identifier'} })
    lightintensity: float = Field(..., description="""\"The intensity of light.\"""", json_schema_extra = { "linkml_meta": {'alias': 'lightintensity',
         'domain_of': ['LightIntensityMetaData'],
         'slot_uri': 'oso:measurement/LightIntensity',
         'unit': {'has_quantity_kind': 'OM:LightIntensity', 'ucum_code': 'Ca'}} })
    lightintensity_target: float = Field(..., description="""\"Target intensity of light.\"""", json_schema_extra = { "linkml_meta": {'alias': 'lightintensity_target',
         'domain_of': ['LightIntensityMetaData'],
         'slot_uri': 'oso:measurement/LightIntensityTarget',
         'unit': {'has_quantity_kind': 'OM:LightIntensity', 'ucum_code': 'Ca'}} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
LightIntensityMetaData.model_rebuild()

# lightintensity_JSON-LD_context 

jsonld_context = """
{
   "comments": {
      "description": "Auto generated by LinkML jsonld context generator",
      "generation_date": "2024-05-09T10:57:03",
      "source": "measurement_metadata_model.yaml"
   },
   "@context": {
      "Measurement": "http://w3c.org/Measurement/",
      "OM": "http://www.ontology-of-units-of-measure.org/resource/om-2/",
      "UO": {
         "@id": "http://purl.obolibrary.org/obo/UO_",
         "@prefix": true
      },
      "dcat": "http://www.w3.org/ns/dcat#",
      "dct": "http://purl.org/dc/terms/",
      "linkml": "https://w3id.org/linkml/",
      "oso": "http://w3c.org/oso/",
      "qudt": "http://qudt.org/schema/qudt/",
      "sh": "https://w3id.org/shacl/",
      "@vocab": "http://w3c.org/Measurement/",
      "altitude": {
         "@type": "xsd:float",
         "@id": "oso:environment/altitude"
      },
      "device_manufacturer_name": {
         "@id": "oso:measurement/measurementDeviceManufacturerName"
      },
      "device_model_name": {
         "@id": "oso:measurement/measurementDeviceModel"
      },
      "device_name": {
         "@id": "oso:measurement/measurementDeviceName"
      },
      "device_serial": {
         "@id": "oso:measurement/measurementDeviceSerial"
      },
      "device_type": {
         "@id": "oso:measurement/measurementDeviceType"
      },
      "device_version": {
         "@id": "oso:measurement/measurementDeviceVersion"
      },
      "environment_air_humidity": {
         "@type": "xsd:float",
         "@id": "oso:environment/environmentAirHumidity"
      },
      "environment_air_pressure": {
         "@type": "xsd:float",
         "@id": "oso:environment/environmentAirPressure"
      },
      "environment_temperature": {
         "@type": "xsd:float",
         "@id": "oso:environment/environmentTemperature"
      },
      "geolocation": {
         "@id": "oso:environment/geolocation"
      },
      "id": "@id",
      "meas_procedure_name": {
         "@id": "oso:measurement/measurementProcedure"
      },
      "meas_software": {
         "@id": "oso:measurement/measurementSoftware"
      },
      "meas_software_version": {
         "@id": "oso:measurement/measurementSoftwareVersion"
      },
      "method": {
         "@id": "dct:method"
      },
      "session_name": {
         "@id": "oso:measurement/measurementSession"
      },
      "timestamp": {
         "@type": "xsd:dateTime",
         "@id": "dct:date"
      },
      "users": {
         "@id": "oso:measurement/measurementUsers"
      },
      "MeasurementMetaData": {
         "@id": "MeasurementMetaData"
      }, 
      "lightintensity": {
         "@type": "xsd:float",
         "@id": "oso:measurement/LightIntensity"
      },
      "lightintensity_target": {
         "@type": "xsd:float",
         "@id": "oso:measurement/LightIntensityTarget"
      },
      "LightIntensityMetaData": {
         "@id": "LightIntensityMetaData"
      }
   }
}
"""