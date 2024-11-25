

# Slot: connection_type


_"The type of connection, e.g., Ethernet, USB, etc."_





URI: [oso:device/connectionType](http://w3id.org/oso/device/connectionType)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Connection](Connection.md) | "The Connection Descriptor |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/opensourcelab/connection_metadata_model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oso:device/connectionType |
| native | oso:connection_type |




## LinkML Source

<details>
```yaml
name: connection_type
description: '"The type of connection, e.g., Ethernet, USB, etc."'
from_schema: https://w3id.org/opensourcelab/connection_metadata_model
rank: 1000
slot_uri: oso:device/connectionType
alias: connection_type
domain_of:
- Connection
range: string
required: false

```
</details>