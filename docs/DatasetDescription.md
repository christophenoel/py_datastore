# DatasetDescription

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | Optional explicit version of this dataset (by default, an internal versioning strategy is used) | [optional] 
**folder_path** | **str** | Absolute path of the physical folder (containing the data, metadata and other dataset files).  NOTE the leaf directory is the folder unique name | [optional] 
**data_path** | **str** | RELATIVE path of the data file in the dataset folder (if the data was created or updated) | [optional] 
**metadata_path** | **str** | RELATIVE path of the metadata directory in the dataset folder (if some metadata were created or updated) | [optional] [default to './metadata']
**name** | **str** | If provided, overrides the dataset identifier which is set by default to the folder path leaf directory.   In ALTIUS mission, this parameter shall not be used for products.  | [optional] 
**dissemination** | **bool** | Flag authorising publication of the product | [optional] [default to False]
**hidden** | **bool** | Flag implying this record will be hidden by default in the search results. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

