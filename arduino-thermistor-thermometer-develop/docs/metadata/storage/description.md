

# Slot: description


_"A description of the calculation / measurement."_





URI: [http://purl.org/dc/terms/description](http://purl.org/dc/terms/description)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [LabwareTransfer](LabwareTransfer.md) | "The Labware Transfer Station |  no  |
| [LabwareMover](LabwareMover.md) | "The Labware Mover / internal transport system |  no  |
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
| self | http://purl.org/dc/terms/description |
| native | oso:description |




## LinkML Source

<details>
```yaml
name: description
description: '"A description of the calculation / measurement."'
from_schema: https://w3id.org/opensourcelab/storage_metadata_model
rank: 1000
slot_uri: http://purl.org/dc/terms/description
alias: description
domain_of:
- StorageMetaData
- LabwarePosition
- LabwareTransfer
- LabwareMover
- Rack
range: string
required: false

```
</details>