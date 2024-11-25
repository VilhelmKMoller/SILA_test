

# Slot: storage_light


_"The storage light."_





URI: [oso:device/storageLight](http://w3id.org/oso/device/storageLight)



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
| self | oso:device/storageLight |
| native | oso:storage_light |




## LinkML Source

<details>
```yaml
name: storage_light
description: '"The storage light."'
from_schema: https://w3id.org/opensourcelab/storage_metadata_model
rank: 1000
slot_uri: oso:device/storageLight
alias: storage_light
domain_of:
- StorageMetaData
range: float
required: false
unit:
  ucum_code: lx
  has_quantity_kind: OM:LuminousIntensity

```
</details>