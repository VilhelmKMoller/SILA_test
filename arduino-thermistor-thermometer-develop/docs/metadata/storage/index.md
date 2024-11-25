# Storage-Metadata-Model

LinkML Storage Metadata Model.

URI: https://w3id.org/opensourcelab/storage_metadata_model

Name: Storage-Metadata-Model



## Classes

| Class | Description |
| --- | --- |
| [Cover](Cover.md) | "The Cover or door of a device." |
| [LabwareMover](LabwareMover.md) | "The Labware Mover / internal transport system." |
| [LabwarePosition](LabwarePosition.md) | "The Labware Position / location / Nest in a Rack." |
| [LabwareTransfer](LabwareTransfer.md) | "The Labware Transfer Station." |
| [Rack](Rack.md) | "The Rack / Stack - a vertically and/or horizontally arrangement of labware positions." |
| [StorageMetaData](StorageMetaData.md) | "The Storage Metadata." |



## Slots

| Slot | Description |
| --- | --- |
| [configuration](configuration.md) | "Extra / additional configuration of the hardware, in JSON-LD format |
| [covers](covers.md) | "The covers / doors |
| [description](description.md) | "A description of the calculation / measurement |
| [id](id.md) | "The identifier of the resource |
| [iri](iri.md) | "The International Resource Identifier (IRI) of the entity |
| [is_open](is_open.md) | "True if the cover / door is open |
| [is_shaker](is_shaker.md) | "True if the rack is a shaker |
| [is_shaking](is_shaking.md) | "True if the rack is shaking |
| [labware_id](labware_id.md) | "A unique identifier of the labware |
| [labware_max_capacity](labware_max_capacity.md) | labware capacity, max |
| [labware_max_height](labware_max_height.md) | max |
| [labware_min_capacity](labware_min_capacity.md) | labware capacity, min |
| [labware_movers](labware_movers.md) | "The labware movers |
| [labware_positions](labware_positions.md) | "The labware positions / locations / nests in the rack |
| [labware_transfers](labware_transfers.md) | "The labware transfer stations |
| [max_shaking_frequency](max_shaking_frequency.md) | "The maximum shaking frequency |
| [min_shaking_frequency](min_shaking_frequency.md) | "The minimum shaking frequency |
| [name](name.md) | "The name of an entity or object |
| [num_cols](num_cols.md) | "The number of columns in the rack |
| [num_covers](num_covers.md) | "The number of covers / doors in the storage unit |
| [num_labware_movers](num_labware_movers.md) | "The number of labware movers in the storage unit |
| [num_labware_transfers](num_labware_transfers.md) | "The number of transfer stations in the storage unit |
| [num_layers](num_layers.md) | "The number of layers in the rack |
| [num_racks](num_racks.md) | "The number of racks / stacks in the storage unit |
| [num_rows](num_rows.md) | "The number of rows in the rack |
| [occupied](occupied.md) | "True if the position is occupied |
| [orientation](orientation.md) | "The orientation of the labware in a position, e |
| [racks](racks.md) | "The racks in the storage unit |
| [shaking_required](shaking_required.md) | "True if shaking is required |
| [storage_gas](storage_gas.md) | "The storage gas |
| [storage_humidity](storage_humidity.md) | "The storage humidity |
| [storage_light](storage_light.md) | "The storage light |
| [storage_temperature](storage_temperature.md) | "The storage temperature |
| [target_shaking_frequency](target_shaking_frequency.md) | "The target shaking frequency |
| [timestamp](timestamp.md) | "The timestamp of the measurement |
| [url](url.md) | "A Uniform Resource Locator (URL) of, e |


## Enumerations

| Enumeration | Description |
| --- | --- |


## Types

| Type | Description |
| --- | --- |
| [Boolean](Boolean.md) | A binary (true or false) value |
| [Curie](Curie.md) | a compact URI |
| [Date](Date.md) | a date (year, month and day) in an idealized calendar |
| [DateOrDatetime](DateOrDatetime.md) | Either a date or a datetime |
| [Datetime](Datetime.md) | The combination of a date and time |
| [Decimal](Decimal.md) | A real number with arbitrary precision that conforms to the xsd:decimal speci... |
| [Double](Double.md) | A real number that conforms to the xsd:double specification |
| [Float](Float.md) | A real number that conforms to the xsd:float specification |
| [Integer](Integer.md) | An integer |
| [Jsonpath](Jsonpath.md) | A string encoding a JSON Path |
| [Jsonpointer](Jsonpointer.md) | A string encoding a JSON Pointer |
| [NaN](NaN.md) | Not-A-Number (NaN) is a numeric data type value representing an undefined or ... |
| [Ncname](Ncname.md) | Prefix part of CURIE |
| [Nodeidentifier](Nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model |
| [Objectidentifier](Objectidentifier.md) | A URI or CURIE that represents an object in the model |
| [Sparqlpath](Sparqlpath.md) | A string encoding a SPARQL Property Path |
| [String](String.md) | A character string |
| [Time](Time.md) | A time object represents a (local) time of day, independent of any particular... |
| [Uri](Uri.md) | a complete URI |
| [Uriorcurie](Uriorcurie.md) | a URI or a CURIE |


## Subsets

| Subset | Description |
| --- | --- |
