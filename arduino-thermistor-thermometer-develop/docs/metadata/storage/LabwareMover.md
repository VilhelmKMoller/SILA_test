

# Class: LabwareMover


_"The Labware Mover / internal transport system."_





URI: [oso:device/LabwareMover](http://w3id.org/oso/device/LabwareMover)






```mermaid
 classDiagram
    class LabwareMover
    click LabwareMover href "../LabwareMover"
      LabwareMover : configuration
        
      LabwareMover : description
        
      LabwareMover : id
        
      LabwareMover : labware_id
        
      LabwareMover : occupied
        
      LabwareMover : timestamp
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [String](String.md) | "The identifier of the resource | direct |
| [timestamp](timestamp.md) | 1 <br/> [Datetime](Datetime.md) | "The timestamp of the measurement | direct |
| [description](description.md) | 0..1 <br/> [String](String.md) | "A description of the calculation / measurement | direct |
| [labware_id](labware_id.md) | 0..1 <br/> [String](String.md) | "A unique identifier of the labware | direct |
| [occupied](occupied.md) | 0..1 <br/> [Boolean](Boolean.md) | "True if the position is occupied | direct |
| [configuration](configuration.md) | 0..1 <br/> [String](String.md) | "Extra / additional configuration of the hardware, in JSON-LD format | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [StorageMetaData](StorageMetaData.md) | [labware_movers](labware_movers.md) | range | [LabwareMover](LabwareMover.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/opensourcelab/storage_metadata_model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oso:device/LabwareMover |
| native | oso:LabwareMover |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: LabwareMover
description: '"The Labware Mover / internal transport system."'
from_schema: https://w3id.org/opensourcelab/storage_metadata_model
slots:
- id
- timestamp
- description
- labware_id
- occupied
- configuration
class_uri: oso:device/LabwareMover

```
</details>

### Induced

<details>
```yaml
name: LabwareMover
description: '"The Labware Mover / internal transport system."'
from_schema: https://w3id.org/opensourcelab/storage_metadata_model
attributes:
  id:
    name: id
    description: '"The identifier of the resource."'
    from_schema: https://w3id.org/opensourcelab/storage_metadata_model
    rank: 1000
    slot_uri: http://purl.org/dc/terms/identifier
    identifier: true
    alias: id
    owner: LabwareMover
    domain_of:
    - StorageMetaData
    - LabwarePosition
    - LabwareTransfer
    - Cover
    - LabwareMover
    - Rack
    range: string
    required: true
  timestamp:
    name: timestamp
    description: '"The timestamp of the measurement."'
    from_schema: https://w3id.org/opensourcelab/storage_metadata_model
    rank: 1000
    slot_uri: http://purl.org/dc/terms/date
    alias: timestamp
    owner: LabwareMover
    domain_of:
    - StorageMetaData
    - LabwarePosition
    - LabwareTransfer
    - Cover
    - LabwareMover
    - Rack
    range: datetime
    required: true
  description:
    name: description
    description: '"A description of the calculation / measurement."'
    from_schema: https://w3id.org/opensourcelab/storage_metadata_model
    rank: 1000
    slot_uri: http://purl.org/dc/terms/description
    alias: description
    owner: LabwareMover
    domain_of:
    - StorageMetaData
    - LabwarePosition
    - LabwareTransfer
    - LabwareMover
    - Rack
    range: string
    required: false
  labware_id:
    name: labware_id
    description: '"A unique identifier of the labware."'
    from_schema: https://w3id.org/opensourcelab/storage_metadata_model
    rank: 1000
    slot_uri: oso:device/labwareID
    alias: labware_id
    owner: LabwareMover
    domain_of:
    - LabwarePosition
    - LabwareTransfer
    - LabwareMover
    range: string
    required: false
  occupied:
    name: occupied
    description: '"True if the position is occupied."'
    from_schema: https://w3id.org/opensourcelab/storage_metadata_model
    rank: 1000
    slot_uri: oso:device/occupied
    alias: occupied
    owner: LabwareMover
    domain_of:
    - LabwarePosition
    - LabwareTransfer
    - LabwareMover
    range: boolean
    required: false
  configuration:
    name: configuration
    description: '"Extra / additional configuration of the hardware, in JSON-LD format."'
    from_schema: https://w3id.org/opensourcelab/storage_metadata_model
    rank: 1000
    slot_uri: oso:device/configuration
    alias: configuration
    owner: LabwareMover
    domain_of:
    - StorageMetaData
    - LabwarePosition
    - LabwareTransfer
    - Cover
    - LabwareMover
    - Rack
    range: string
    required: false
class_uri: oso:device/LabwareMover

```
</details>