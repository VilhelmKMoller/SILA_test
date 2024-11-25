

# Slot: service_date_next


_"The date of the next service."_





URI: [oso:device/deviceServiceDateNext](http://w3id.org/oso/device/deviceServiceDateNext)



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
| self | oso:device/deviceServiceDateNext |
| native | oso:service_date_next |




## LinkML Source

<details>
```yaml
name: service_date_next
description: '"The date of the next service."'
from_schema: https://w3id.org/opensourcelab/device_metadata_model
rank: 1000
slot_uri: oso:device/deviceServiceDateNext
alias: service_date_next
domain_of:
- DeviceMetaData
- ServiceInfo
range: datetime
required: false

```
</details>