

# Slot: port


_"The port of the connection. (e.g., 80, 8080, etc.)"_





URI: [oso:device/port](http://w3id.org/oso/device/port)



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
| self | oso:device/port |
| native | oso:port |




## LinkML Source

<details>
```yaml
name: port
description: '"The port of the connection. (e.g., 80, 8080, etc.)"'
from_schema: https://w3id.org/opensourcelab/connection_metadata_model
rank: 1000
slot_uri: oso:device/port
alias: port
domain_of:
- Connection
range: string
required: false

```
</details>