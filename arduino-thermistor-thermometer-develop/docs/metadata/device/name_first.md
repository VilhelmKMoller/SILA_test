

# Slot: name_first


_"The first name of the user."_





URI: [oso:entity/firstName](http://w3id.org/oso/entity/firstName)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | "The User class represents a user of the SciDatS system |  no  |







## Properties

* Range: [String](String.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/opensourcelab/device_metadata_model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oso:entity/firstName |
| native | oso:name_first |




## LinkML Source

<details>
```yaml
name: name_first
description: '"The first name of the user."'
from_schema: https://w3id.org/opensourcelab/device_metadata_model
rank: 1000
slot_uri: oso:entity/firstName
alias: name_first
domain_of:
- Person
range: string
required: true

```
</details>