

# Slot: timestamp


_"The timestamp of the measurement."_





URI: [http://purl.org/dc/terms/date](http://purl.org/dc/terms/date)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DeviceMetaData](DeviceMetaData.md) | "The Device Metadata |  no  |
| [ServiceInfo](ServiceInfo.md) | "The Service Info |  no  |







## Properties

* Range: [Datetime](Datetime.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/opensourcelab/device_metadata_model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | http://purl.org/dc/terms/date |
| native | oso:timestamp |




## LinkML Source

<details>
```yaml
name: timestamp
description: '"The timestamp of the measurement."'
from_schema: https://w3id.org/opensourcelab/device_metadata_model
rank: 1000
slot_uri: http://purl.org/dc/terms/date
alias: timestamp
domain_of:
- DeviceMetaData
- ServiceInfo
range: datetime
required: true

```
</details>