

# Slot: connection


_"The connection descriptor, e.g., a set of connection parameters, like IP, port, bus, etc."_





URI: [oso:device/connection](http://w3id.org/oso/device/connection)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ConnectionMetaData](ConnectionMetaData.md) | "The Connection Metadata |  no  |







## Properties

* Range: [Connection](Connection.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/opensourcelab/connection_metadata_model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oso:device/connection |
| native | oso:connection |




## LinkML Source

<details>
```yaml
name: connection
description: '"The connection descriptor, e.g., a set of connection parameters, like
  IP, port, bus, etc."'
from_schema: https://w3id.org/opensourcelab/connection_metadata_model
rank: 1000
slot_uri: oso:device/connection
alias: connection
domain_of:
- ConnectionMetaData
range: Connection
required: false

```
</details>