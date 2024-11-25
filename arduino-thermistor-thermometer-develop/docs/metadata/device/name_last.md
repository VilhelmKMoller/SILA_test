

# Slot: name_last


_"The last name of the user."_





URI: [oso:entity/lastName](http://w3id.org/oso/entity/lastName)



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
| self | oso:entity/lastName |
| native | oso:name_last |




## LinkML Source

<details>
```yaml
name: name_last
description: '"The last name of the user."'
from_schema: https://w3id.org/opensourcelab/device_metadata_model
rank: 1000
slot_uri: oso:entity/lastName
alias: name_last
domain_of:
- Person
range: string
required: true

```
</details>