

# Slot: service_type


_"The type of service, e.g., calibration, maintenance, repair."_





URI: [oso:device/deviceServiceType](http://w3id.org/oso/device/deviceServiceType)



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
| self | oso:device/deviceServiceType |
| native | oso:service_type |




## LinkML Source

<details>
```yaml
name: service_type
description: '"The type of service, e.g., calibration, maintenance, repair."'
from_schema: https://w3id.org/opensourcelab/device_metadata_model
rank: 1000
slot_uri: oso:device/deviceServiceType
alias: service_type
domain_of:
- DeviceMetaData
- ServiceInfo
range: string
required: false

```
</details>