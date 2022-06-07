# Group

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** | Group identifier used for grouping a set of datasets.  Note the groupId is unique regardless the dataset type (product, datafolder) | 
**dataset_type** | **str** | Product or Datafolder dataset (mission specific enumeration) | 
**path** | **str** | Optional physical root path of the group on the data storage.   If provided, the submitted datasets files are verified against this path. | [optional] 
**metadata_type** | **str** | Metadata format:  either a standard, or a general encoding (such as \&quot;JSON\&quot;) which holds the set of metadata properties.    In the case of the ALTIUS mission, the metadata format for products SHALL be &#x27;OGC 10-157r4&#x27; (Earth Observation Metadata profile of Observations &amp; Measurement (XML). The set of metadata properties is defined in the ALTIUS Product  Format Definition document.  The metadata format for  datafolders (generic datasets) SHOULD be JSON which holds a set of JSON properties defined as a string. | [optional] 
**group_properties** | **list[str]** | Name of the group (searchable) specific properties (up to three). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

