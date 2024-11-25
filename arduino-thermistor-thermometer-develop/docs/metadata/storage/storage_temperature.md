

# Slot: storage_temperature


_"The storage temperature."_





URI: [oso:device/storageTemperature](http://w3id.org/oso/device/storageTemperature)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StorageMetaData](StorageMetaData.md) | "The Storage Metadata |  no  |







## Properties

* Range: [Float](Float.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/opensourcelab/storage_metadata_model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oso:device/storageTemperature |
| native | oso:storage_temperature |




## LinkML Source

<details>
```yaml
name: storage_temperature
description: '"The storage temperature."'
from_schema: https://w3id.org/opensourcelab/storage_metadata_model
rank: 1000
slot_uri: oso:device/storageTemperature
alias: storage_temperature
domain_of:
- StorageMetaData
range: float
required: false
unit:
  ucum_code: K
  has_quantity_kind: OM:Temperature

```
</details>