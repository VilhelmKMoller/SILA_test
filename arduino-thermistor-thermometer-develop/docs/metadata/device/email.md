

# Slot: email


_"The email address of an entity, person or company."_





URI: [oso:entity/email](http://w3id.org/oso/entity/email)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | "The User class represents a user of the SciDatS system |  no  |
| [Company](Company.md) | "A class representing a Company, e |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/opensourcelab/device_metadata_model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oso:entity/email |
| native | oso:email |




## LinkML Source

<details>
```yaml
name: email
description: '"The email address of an entity, person or company."'
from_schema: https://w3id.org/opensourcelab/device_metadata_model
rank: 1000
slot_uri: oso:entity/email
alias: email
domain_of:
- Person
- Company
range: string
required: false

```
</details>