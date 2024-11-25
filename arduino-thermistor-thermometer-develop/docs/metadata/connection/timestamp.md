

# Slot: timestamp


_"The timestamp of the measurement."_





URI: [http://purl.org/dc/terms/date](http://purl.org/dc/terms/date)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Connection](Connection.md) | "The Connection Descriptor |  no  |
| [ConnectionMetaData](ConnectionMetaData.md) | "The Connection Metadata |  no  |







## Properties

* Range: [Datetime](Datetime.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/opensourcelab/connection_metadata_model




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
from_schema: https://w3id.org/opensourcelab/connection_metadata_model
rank: 1000
slot_uri: http://purl.org/dc/terms/date
alias: timestamp
domain_of:
- ConnectionMetaData
- Connection
range: datetime
required: true

```
</details>