

# Slot: service_provider


_"The service provider, e.g. a company."_





URI: [oso:device/deviceServiceProvider](http://w3id.org/oso/device/deviceServiceProvider)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DeviceMetaData](DeviceMetaData.md) | "The Device Metadata |  no  |
| [ServiceInfo](ServiceInfo.md) | "The Service Info |  no  |







## Properties

* Range: [Company](Company.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/opensourcelab/device_metadata_model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oso:device/deviceServiceProvider |
| native | oso:service_provider |




## LinkML Source

<details>
```yaml
name: service_provider
description: '"The service provider, e.g. a company."'
from_schema: https://w3id.org/opensourcelab/device_metadata_model
rank: 1000
slot_uri: oso:device/deviceServiceProvider
alias: service_provider
domain_of:
- DeviceMetaData
- ServiceInfo
range: Company
required: false

```
</details>