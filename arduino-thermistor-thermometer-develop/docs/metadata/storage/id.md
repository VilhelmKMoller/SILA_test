

# Slot: id


_"The identifier of the resource."_





URI: [http://purl.org/dc/terms/identifier](http://purl.org/dc/terms/identifier)



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

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/opensourcelab/storage_metadata_model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | http://purl.org/dc/terms/identifier |
| native | oso:id |




## LinkML Source

<details>
```yaml
name: id
description: '"The identifier of the resource."'
from_schema: https://w3id.org/opensourcelab/storage_metadata_model
rank: 1000
slot_uri: http://purl.org/dc/terms/identifier
identifier: true
alias: id
domain_of:
- StorageMetaData
- LabwarePosition
- LabwareTransfer
- Cover
- LabwareMover
- Rack
range: string
required: true

```
</details>