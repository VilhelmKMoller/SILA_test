

# Slot: device_class


_"The Class / Type of the device. E.g. Gas Chromatograph, NMR. Thermometer, UV-spectrometer, MALDI-TOF-MS, HPLC, etc."_





URI: [oso:measurement/deviceClass](http://w3id.org/oso/measurement/deviceClass)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DeviceMetaData](DeviceMetaData.md) | "The Device Metadata |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/opensourcelab/device_metadata_model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oso:measurement/deviceClass |
| native | oso:device_class |




## LinkML Source

<details>
```yaml
name: device_class
description: '"The Class / Type of the device. E.g. Gas Chromatograph, NMR. Thermometer,
  UV-spectrometer, MALDI-TOF-MS, HPLC, etc."'
from_schema: https://w3id.org/opensourcelab/device_metadata_model
rank: 1000
slot_uri: oso:measurement/deviceClass
alias: device_class
domain_of:
- DeviceMetaData
range: string
required: false

```
</details>