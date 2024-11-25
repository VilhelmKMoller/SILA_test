

# Slot: service_date


_"The date of the next service."_





URI: [oso:device/deviceServiceDate](http://w3id.org/oso/device/deviceServiceDate)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DeviceMetaData](DeviceMetaData.md) | "The Device Metadata |  no  |
| [ServiceInfo](ServiceInfo.md) | "The Service Info |  no  |







## Properties

* Range: [Datetime](Datetime.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/opensourcelab/device_metadata_model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oso:device/deviceServiceDate |
| native | oso:service_date |




## LinkML Source

<details>
```yaml
name: service_date
description: '"The date of the next service."'
from_schema: https://w3id.org/opensourcelab/device_metadata_model
rank: 1000
slot_uri: oso:device/deviceServiceDate
alias: service_date
domain_of:
- DeviceMetaData
- ServiceInfo
range: datetime
required: false

```
</details>