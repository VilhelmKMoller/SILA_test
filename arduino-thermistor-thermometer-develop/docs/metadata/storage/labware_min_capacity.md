

# Slot: labware_min_capacity


_labware capacity, min. number of labware, some centrifuges need at least 2 labware, e.g. for balancing_





URI: [oso:device/labware_min_capacity](http://w3id.org/oso/device/labware_min_capacity)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Rack](Rack.md) | "The Rack / Stack - a vertically and/or horizontally arrangement of labware p... |  no  |
| [StorageMetaData](StorageMetaData.md) | "The Storage Metadata |  no  |







## Properties

* Range: [Integer](Integer.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/opensourcelab/storage_metadata_model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oso:device/labware_min_capacity |
| native | oso:labware_min_capacity |




## LinkML Source

<details>
```yaml
name: labware_min_capacity
description: labware capacity, min. number of labware, some centrifuges need at least
  2 labware, e.g. for balancing
from_schema: https://w3id.org/opensourcelab/storage_metadata_model
rank: 1000
slot_uri: oso:device/labware_min_capacity
alias: labware_min_capacity
domain_of:
- StorageMetaData
- Rack
range: integer
required: false

```
</details>