

# Slot: max_shaking_frequency


_"The maximum shaking frequency."_





URI: [oso:device/maxShakingFrequency](http://w3id.org/oso/device/maxShakingFrequency)



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
| self | oso:device/maxShakingFrequency |
| native | oso:max_shaking_frequency |




## LinkML Source

<details>
```yaml
name: max_shaking_frequency
description: '"The maximum shaking frequency."'
from_schema: https://w3id.org/opensourcelab/storage_metadata_model
rank: 1000
slot_uri: oso:device/maxShakingFrequency
alias: max_shaking_frequency
domain_of:
- Rack
range: float
required: false
unit:
  ucum_code: Hz
  has_quantity_kind: OM:Frequency

```
</details>