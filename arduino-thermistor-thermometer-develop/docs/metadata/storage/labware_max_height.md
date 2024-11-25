

# Slot: labware_max_height


_max. labware height in m_





URI: [oso:device/labware_max_height](http://w3id.org/oso/device/labware_max_height)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Rack](Rack.md) | "The Rack / Stack - a vertically and/or horizontally arrangement of labware p... |  no  |
| [StorageMetaData](StorageMetaData.md) | "The Storage Metadata |  no  |
| [LabwarePosition](LabwarePosition.md) | "The Labware Position / location / Nest in a Rack |  no  |







## Properties

* Range: [Float](Float.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/opensourcelab/storage_metadata_model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oso:device/labware_max_height |
| native | oso:labware_max_height |




## LinkML Source

<details>
```yaml
name: labware_max_height
description: max. labware height in m
from_schema: https://w3id.org/opensourcelab/storage_metadata_model
rank: 1000
slot_uri: oso:device/labware_max_height
alias: labware_max_height
domain_of:
- StorageMetaData
- LabwarePosition
- Rack
range: float
required: false

```
</details>