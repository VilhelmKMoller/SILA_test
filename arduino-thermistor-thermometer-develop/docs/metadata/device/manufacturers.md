

# Slot: manufacturers


_"Manufacturer of the device."_





URI: [oso:device/Manufacturer](http://w3id.org/oso/device/Manufacturer)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DeviceMetaData](DeviceMetaData.md) | "The Device Metadata |  no  |







## Properties

* Range: [Company](Company.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/opensourcelab/device_metadata_model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oso:device/Manufacturer |
| native | oso:manufacturers |




## LinkML Source

<details>
```yaml
name: manufacturers
description: '"Manufacturer of the device."'
from_schema: https://w3id.org/opensourcelab/device_metadata_model
rank: 1000
slot_uri: oso:device/Manufacturer
alias: manufacturers
domain_of:
- DeviceMetaData
range: Company
required: false
multivalued: true

```
</details>