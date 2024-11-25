

# Slot: firmware_version


_"The version of the firmware of the device."_





URI: [oso:device/deviceFirmwareVersion](http://w3id.org/oso/device/deviceFirmwareVersion)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DeviceMetaData](DeviceMetaData.md) | "The Device Metadata |  no  |







## Properties

* Range: [String](String.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/opensourcelab/device_metadata_model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oso:device/deviceFirmwareVersion |
| native | oso:firmware_version |




## LinkML Source

<details>
```yaml
name: firmware_version
description: '"The version of the firmware of the device."'
from_schema: https://w3id.org/opensourcelab/device_metadata_model
rank: 1000
slot_uri: oso:device/deviceFirmwareVersion
alias: firmware_version
domain_of:
- DeviceMetaData
range: string
required: true

```
</details>