

# Class: DeviceType


_"The Device Type."_





URI: [oso:device/DeviceType](http://w3id.org/oso/device/DeviceType)






```mermaid
 classDiagram
    class DeviceType
    click DeviceType href "../DeviceType"
      DeviceType : id
        
      DeviceType : iri
        
      DeviceType : name
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [String](String.md) | "The identifier of the resource | direct |
| [name](name.md) | 1 <br/> [String](String.md) | "The name of an entity or object | direct |
| [iri](iri.md) | 0..1 <br/> [String](String.md) | "The International Resource Identifier (IRI) of the entity | direct |









## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/opensourcelab/device_metadata_model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oso:device/DeviceType |
| native | oso:DeviceType |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DeviceType
description: '"The Device Type."'
from_schema: https://w3id.org/opensourcelab/device_metadata_model
slots:
- id
- name
- iri
class_uri: oso:device/DeviceType

```
</details>

### Induced

<details>
```yaml
name: DeviceType
description: '"The Device Type."'
from_schema: https://w3id.org/opensourcelab/device_metadata_model
attributes:
  id:
    name: id
    description: '"The identifier of the resource."'
    from_schema: https://w3id.org/opensourcelab/device_metadata_model
    rank: 1000
    slot_uri: http://purl.org/dc/terms/identifier
    identifier: true
    alias: id
    owner: DeviceType
    domain_of:
    - Company
    - DeviceType
    - DeviceMetaData
    - ServiceInfo
    range: string
    required: true
  name:
    name: name
    description: '"The name of an entity or object."'
    from_schema: https://w3id.org/opensourcelab/device_metadata_model
    rank: 1000
    slot_uri: oso:entity/Name
    alias: name
    owner: DeviceType
    domain_of:
    - Company
    - DeviceType
    range: string
    required: true
  iri:
    name: iri
    description: '"The International Resource Identifier (IRI) of the entity."'
    from_schema: https://w3id.org/opensourcelab/device_metadata_model
    rank: 1000
    slot_uri: oso:entity/IRI
    alias: iri
    owner: DeviceType
    domain_of:
    - DeviceType
    - DeviceMetaData
    range: string
    required: false
class_uri: oso:device/DeviceType

```
</details>