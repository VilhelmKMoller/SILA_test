import json


metadata_model_context = json.loads( 
"""

{
   "comments": {
      "description": "Auto generated by LinkML jsonld context generator",
      "generation_date": "2024-10-27T19:18:36",
      "source": "device_metadata_model.yaml"
   },
   "@context": {
      "xsd": "http://www.w3.org/2001/XMLSchema#",
      "OM": "http://www.ontology-of-units-of-measure.org/resource/om-2/",
      "UO": {
         "@id": "http://purl.obolibrary.org/obo/UO_",
         "@prefix": true
      },
      "dcat": "http://www.w3.org/ns/dcat#",
      "dcatap": "http://data.europa.eu/m8g/",
      "dcmi": "http://purl.org/dc/dcmitype/",
      "dct": "http://purl.org/dc/terms/",
      "linkml": "https://w3id.org/linkml/",
      "oso": "http://w3id.org/oso/",
      "qudt": "http://qudt.org/schema/qudt/",
      "sh": "https://w3id.org/shacl/",
      "@vocab": "http://w3id.org/oso/",
      "description": {
         "@id": "dct:description"
      },
      "device_class": {
         "@id": "measurement/deviceClass"
      },
      "device_manual_url": {
         "@id": "device/deviceManual"
      },
      "device_name": {
         "@id": "measurement/deviceName"
      },
      "device_pid": {
         "@id": "/device/PID"
      },
      "device_quick_start_guide_url": {
         "@id": "device/deviceQuickStartGuide"
      },
      "device_serial_number": {
         "@id": "device/serialNumber"
      },
      "device_service_manual_url": {
         "@id": "device/deviceServiceManual"
      },
      "device_version": {
         "@id": "/device/version"
      },
      "email": {
         "@id": "entity/email"
      },
      "end_of_warranty_date": {
         "@type": "xsd:dateTime",
         "@id": "device/deviceEndOfWarrantyDate"
      },
      "energy_consumption": {
         "@type": "xsd:float",
         "@id": "device/energy_consumption"
      },
      "firmware_version": {
         "@id": "device/deviceFirmwareVersion"
      },
      "icon": {
         "@id": "device/icon"
      },
      "id": "@id",
      "image": {
         "@id": "device/image"
      },
      "iri": {
         "@id": "entity/IRI"
      },
      "manufacturer_id": {
         "@id": "device/ManufacturerID"
      },
      "manufacturers": {
         "@type": "@id",
         "@id": "device/Manufacturer"
      },
      "model_name": {
         "@id": "measurement/deviceModel"
      },
      "model_no": {
         "@id": "device/model_no"
      },
      "name": {
         "@id": "entity/Name"
      },
      "name_first": {
         "@id": "entity/firstName"
      },
      "name_last": {
         "@id": "entity/lastName"
      },
      "orcid": {
         "@id": "entity/ORCID"
      },
      "pac_id": {
         "@id": "device/pacID"
      },
      "part_number": {
         "@id": "device/partNumber"
      },
      "phone_numbers": {
         "@id": "entity/phoneNumber"
      },
      "product_no": {
         "@id": "device/product_no"
      },
      "product_type": {
         "@id": "device/product_type"
      },
      "purchase_date": {
         "@type": "xsd:dateTime",
         "@id": "device/devicePurchaseDate"
      },
      "registration_barcode": {
         "@id": "device/deviceRegistrationBarcode"
      },
      "registration_number": {
         "@id": "device/deviceRegistrationNumber"
      },
      "resources_external": {
         "@id": "device/resources_external"
      },
      "service_date_last": {
         "@type": "xsd:dateTime",
         "@id": "device/deviceServiceDateLast"
      },
      "service_date_next": {
         "@type": "xsd:dateTime",
         "@id": "device/deviceServiceDateNext"
      },
      "service_description": {
         "@id": "device/deviceServiceDescription"
      },
      "service_engineer": {
         "@type": "@id",
         "@id": "device/deviceServiceEngineer"
      },
      "service_provider": {
         "@type": "@id",
         "@id": "device/deviceServiceProvider"
      },
      "service_report": {
         "@id": "device/deviceServiceReport"
      },
      "service_type": {
         "@id": "device/deviceServiceType"
      },
      "shape": {
         "@id": "device/shape"
      },
      "spec_json": {
         "@id": "device/spec_json"
      },
      "tags": {
         "@id": "device/tag"
      },
      "timestamp": {
         "@type": "xsd:dateTime",
         "@id": "dct:date"
      },
      "type_barcode": {
         "@id": "device/type_barcode"
      },
      "url": {
         "@id": "entity/url"
      },
      "weight": {
         "@type": "xsd:float",
         "@id": "device/weight"
      },
      "Company": {
         "@id": "entity/Company"
      },
      "DeviceClass": {
         "@id": "device/DeviceClass"
      },
      "DeviceMetaData": {
         "@id": "device/DeviceMetaData"
      },
      "Person": {
         "@id": "entity"
      },
      "ServiceInfo": {
         "@id": "device/ServiceInfo"
      }
   }
}





"""
)