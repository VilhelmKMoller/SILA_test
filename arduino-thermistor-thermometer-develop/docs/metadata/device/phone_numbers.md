

# Slot: phone_numbers


_"A list of phone numbers."_





URI: [oso:entity/phoneNumber](http://w3id.org/oso/entity/phoneNumber)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | "The User class represents a user of the SciDatS system |  no  |
| [Company](Company.md) | "A class representing a Company, e |  no  |







## Properties

* Range: [String](String.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/opensourcelab/device_metadata_model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oso:entity/phoneNumber |
| native | oso:phone_numbers |




## LinkML Source

<details>
```yaml
name: phone_numbers
description: '"A list of phone numbers."'
from_schema: https://w3id.org/opensourcelab/device_metadata_model
rank: 1000
slot_uri: oso:entity/phoneNumber
alias: phone_numbers
domain_of:
- Person
- Company
range: string
required: false
multivalued: true

```
</details>