

# Slot: name


_"The name of an entity or object."_





URI: [oso:entity/Name](http://w3id.org/oso/entity/Name)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ServiceInfo](ServiceInfo.md) | "The Service Info |  no  |
| [Company](Company.md) | "A class representing a Company, e |  no  |
| [DeviceClass](DeviceClass.md) | "The Device Class / Type |  no  |







## Properties

* Range: [String](String.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/opensourcelab/device_metadata_model




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
from_schema: https://w3id.org/opensourcelab/device_metadata_model
rank: 1000
slot_uri: oso:entity/Name
alias: name
domain_of:
- Company
- DeviceClass
- ServiceInfo
range: string
required: true

```
</details>