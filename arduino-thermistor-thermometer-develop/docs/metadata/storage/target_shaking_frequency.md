

# Slot: target_shaking_frequency


_"The target shaking frequency."_





URI: [oso:device/targetShakingFrequency](http://w3id.org/oso/device/targetShakingFrequency)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Rack](Rack.md) | "The Rack / Stack - a vertically and/or horizontally arrangement of labware p... |  no  |







## Properties

* Range: [Float](Float.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/opensourcelab/storage_metadata_model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oso:device/targetShakingFrequency |
| native | oso:target_shaking_frequency |




## LinkML Source

<details>
```yaml
name: target_shaking_frequency
description: '"The target shaking frequency."'
from_schema: https://w3id.org/opensourcelab/storage_metadata_model
rank: 1000
slot_uri: oso:device/targetShakingFrequency
alias: target_shaking_frequency
domain_of:
- Rack
range: float
required: false
unit:
  ucum_code: Hz
  has_quantity_kind: OM:Frequency

```
</details>