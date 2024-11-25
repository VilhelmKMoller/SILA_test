

# Slot: service_report


_"An URL to the service report."_





URI: [oso:device/deviceServiceReport](http://w3id.org/oso/device/deviceServiceReport)



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
| self | oso:device/deviceServiceReport |
| native | oso:service_report |




## LinkML Source

<details>
```yaml
name: service_report
description: '"An URL to the service report."'
from_schema: https://w3id.org/opensourcelab/device_metadata_model
rank: 1000
slot_uri: oso:device/deviceServiceReport
alias: service_report
domain_of:
- DeviceMetaData
- ServiceInfo
range: string
required: false

```
</details>