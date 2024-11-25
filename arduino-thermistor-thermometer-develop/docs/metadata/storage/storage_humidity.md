

# Slot: storage_humidity


_"The storage humidity."_





URI: [oso:device/storageHumidity](http://w3id.org/oso/device/storageHumidity)



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
| self | oso:device/storageHumidity |
| native | oso:storage_humidity |




## LinkML Source

<details>
```yaml
name: storage_humidity
description: '"The storage humidity."'
from_schema: https://w3id.org/opensourcelab/storage_metadata_model
rank: 1000
slot_uri: oso:device/storageHumidity
alias: storage_humidity
domain_of:
- StorageMetaData
range: float
required: false
unit:
  has_quantity_kind: OM:RelativeHumidity

```
</details>