

# Slot: occupied


_"True if the position is occupied."_





URI: [oso:device/occupied](http://w3id.org/oso/device/occupied)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [LabwareTransfer](LabwareTransfer.md) | "The Labware Transfer Station |  no  |
| [LabwareMover](LabwareMover.md) | "The Labware Mover / internal transport system |  no  |
| [LabwarePosition](LabwarePosition.md) | "The Labware Position / location / Nest in a Rack |  no  |







## Properties

* Range: [Boolean](Boolean.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/opensourcelab/storage_metadata_model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oso:device/occupied |
| native | oso:occupied |




## LinkML Source

<details>
```yaml
name: occupied
description: '"True if the position is occupied."'
from_schema: https://w3id.org/opensourcelab/storage_metadata_model
rank: 1000
slot_uri: oso:device/occupied
alias: occupied
domain_of:
- LabwarePosition
- LabwareTransfer
- LabwareMover
range: boolean
required: false

```
</details>