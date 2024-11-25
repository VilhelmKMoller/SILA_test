

# Slot: configuration


_"Extra / additional configuration of the hardware, in JSON-LD format."_





URI: [oso:device/configuration](http://w3id.org/oso/device/configuration)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [LabwareTransfer](LabwareTransfer.md) | "The Labware Transfer Station |  no  |
| [LabwareMover](LabwareMover.md) | "The Labware Mover / internal transport system |  no  |
| [Cover](Cover.md) | "The Cover or door of a device |  no  |
| [Rack](Rack.md) | "The Rack / Stack - a vertically and/or horizontally arrangement of labware p... |  no  |
| [LabwarePosition](LabwarePosition.md) | "The Labware Position / location / Nest in a Rack |  no  |
| [StorageMetaData](StorageMetaData.md) | "The Storage Metadata |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/opensourcelab/storage_metadata_model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oso:device/configuration |
| native | oso:configuration |




## LinkML Source

<details>
```yaml
name: configuration
description: '"Extra / additional configuration of the hardware, in JSON-LD format."'
from_schema: https://w3id.org/opensourcelab/storage_metadata_model
rank: 1000
slot_uri: oso:device/configuration
alias: configuration
domain_of:
- StorageMetaData
- LabwarePosition
- LabwareTransfer
- Cover
- LabwareMover
- Rack
range: string
required: false

```
</details>