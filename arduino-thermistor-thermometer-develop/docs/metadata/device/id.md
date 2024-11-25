

# Slot: id


_"The identifier of the resource."_





URI: [http://purl.org/dc/terms/identifier](http://purl.org/dc/terms/identifier)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DeviceMetaData](DeviceMetaData.md) | "The Device Metadata |  no  |
| [Company](Company.md) | "A class representing a Company, e |  no  |
| [ServiceInfo](ServiceInfo.md) | "The Service Info |  no  |
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
| self | http://purl.org/dc/terms/identifier |
| native | oso:id |




## LinkML Source

<details>
```yaml
name: id
description: '"The identifier of the resource."'
from_schema: https://w3id.org/opensourcelab/device_metadata_model
rank: 1000
slot_uri: http://purl.org/dc/terms/identifier
identifier: true
alias: id
domain_of:
- Company
- DeviceClass
- DeviceMetaData
- ServiceInfo
range: string
required: true

```
</details>