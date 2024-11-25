

# Slot: labware_id


_"A unique identifier of the labware."_





URI: [oso:device/labwareID](http://w3id.org/oso/device/labwareID)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [LabwareTransfer](LabwareTransfer.md) | "The Labware Transfer Station |  no  |
| [LabwareMover](LabwareMover.md) | "The Labware Mover / internal transport system |  no  |
| [LabwarePosition](LabwarePosition.md) | "The Labware Position / location / Nest in a Rack |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/opensourcelab/storage_metadata_model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oso:device/labwareID |
| native | oso:labware_id |




## LinkML Source

<details>
```yaml
name: labware_id
description: '"A unique identifier of the labware."'
from_schema: https://w3id.org/opensourcelab/storage_metadata_model
rank: 1000
slot_uri: oso:device/labwareID
alias: labware_id
domain_of:
- LabwarePosition
- LabwareTransfer
- LabwareMover
range: string
required: false

```
</details>