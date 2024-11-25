

# Slot: name


_"The name of an entity or object."_





URI: [oso:entity/Name](http://w3id.org/oso/entity/Name)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Cover](Cover.md) | "The Cover or door of a device |  no  |
| [LabwareTransfer](LabwareTransfer.md) | "The Labware Transfer Station |  no  |
| [LabwarePosition](LabwarePosition.md) | "The Labware Position / location / Nest in a Rack |  no  |







## Properties

* Range: [String](String.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/opensourcelab/storage_metadata_model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oso:entity/Name |
| native | oso:name |




## LinkML Source

<details>
```yaml
name: name
description: '"The name of an entity or object."'
from_schema: https://w3id.org/opensourcelab/storage_metadata_model
rank: 1000
slot_uri: oso:entity/Name
alias: name
domain_of:
- LabwarePosition
- LabwareTransfer
- Cover
range: string
required: true

```
</details>