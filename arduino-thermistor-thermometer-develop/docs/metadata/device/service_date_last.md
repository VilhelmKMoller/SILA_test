

# Slot: service_date_last


_"The date of the last service."_





URI: [oso:device/deviceServiceDateLast](http://w3id.org/oso/device/deviceServiceDateLast)



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
| self | oso:device/deviceServiceDateLast |
| native | oso:service_date_last |




## LinkML Source

<details>
```yaml
name: service_date_last
description: '"The date of the last service."'
from_schema: https://w3id.org/opensourcelab/device_metadata_model
rank: 1000
slot_uri: oso:device/deviceServiceDateLast
alias: service_date_last
domain_of:
- DeviceMetaData
- ServiceInfo
range: datetime
required: false

```
</details>