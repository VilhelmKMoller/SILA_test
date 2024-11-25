

# Slot: timestamp


_"The timestamp of the measurement."_





URI: [http://purl.org/dc/terms/date](http://purl.org/dc/terms/date)



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

* Range: [Datetime](Datetime.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/opensourcelab/storage_metadata_model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | http://purl.org/dc/terms/date |
| native | oso:timestamp |




## LinkML Source

<details>
```yaml
name: timestamp
description: '"The timestamp of the measurement."'
from_schema: https://w3id.org/opensourcelab/storage_metadata_model
rank: 1000
slot_uri: http://purl.org/dc/terms/date
alias: timestamp
domain_of:
- StorageMetaData
- LabwarePosition
- LabwareTransfer
- Cover
- LabwareMover
- Rack
range: datetime
required: true

```
</details>