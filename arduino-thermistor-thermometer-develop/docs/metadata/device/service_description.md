

# Slot: service_description


_"A description of the service."_





URI: [oso:device/deviceServiceDescription](http://w3id.org/oso/device/deviceServiceDescription)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DeviceMetaData](DeviceMetaData.md) | "The Device Metadata |  no  |
| [ServiceInfo](ServiceInfo.md) | "The Service Info |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/opensourcelab/device_metadata_model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oso:device/deviceServiceDescription |
| native | oso:service_description |




## LinkML Source

<details>
```yaml
name: service_description
description: '"A description of the service."'
from_schema: https://w3id.org/opensourcelab/device_metadata_model
rank: 1000
slot_uri: oso:device/deviceServiceDescription
alias: service_description
domain_of:
- DeviceMetaData
- ServiceInfo
range: string
required: false

```
</details>