# Example data for fao_soils

This folder contains example data for testing and demonstrating the FAO soils
datamodel, sorted in subfolders:

- `valid` for data conforming to the datamodel. Used to verify the datamodel.
- `invalid` for data not conforming to the datamodel. Used to verify the validation.
- `problem` for data which are not yet handled correctly in the current schema version,
   again separated into valid/invalid.

The filenames of all example data must conform to the scheme
`ClassName-###.yaml` where `ClassName` is the name of a class from the schema.
The classname is derived by splitting at the first `-` and taking the part
before the `-`.
