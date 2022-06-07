# datastore.DatasetsApi

All URIs are relative to *https://virtserver.swaggerhub.com/Spacebel.be/datastoreManager/draft-3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dataset**](DatasetsApi.md#create_dataset) | **POST** /groups/{groupId}/datasets | Register a Dataset
[**delete_dataset**](DatasetsApi.md#delete_dataset) | **DELETE** /groups/{groupId}/datasets/{resourceId} | Delete dataset
[**get_dataset_by_id**](DatasetsApi.md#get_dataset_by_id) | **GET** /groups/{groupId}/datasets/{resourceId} | Find dataset by id
[**search_datasets**](DatasetsApi.md#search_datasets) | **GET** /groups/{groupId}/datasets | Search for datasets
[**update_dataset**](DatasetsApi.md#update_dataset) | **PUT** /groups/{groupId}/datasets/{resourceId} | Update a Dataset

# **create_dataset**
> Dataset create_dataset(body, group_id)

Register a Dataset

Create a new dataset (including a new version) 

### Example
```python
from __future__ import print_function
import time
import datastore
from datastore.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = datastore.DatasetsApi()
body = datastore.DatasetDescription() # DatasetDescription | Resource Change Report
group_id = 'group_id_example' # str | name of the Group

try:
    # Register a Dataset
    api_response = api_instance.create_dataset(body, group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasetsApi->create_dataset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DatasetDescription**](DatasetDescription.md)| Resource Change Report | 
 **group_id** | **str**| name of the Group | 

### Return type

[**Dataset**](Dataset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dataset**
> delete_dataset(group_id, resource_id)

Delete dataset

Delete a dataset

### Example
```python
from __future__ import print_function
import time
import datastore
from datastore.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = datastore.DatasetsApi()
group_id = 'group_id_example' # str | name of the group
resource_id = 'resource_id_example' # str | identifier of the rsource

try:
    # Delete dataset
    api_instance.delete_dataset(group_id, resource_id)
except ApiException as e:
    print("Exception when calling DatasetsApi->delete_dataset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| name of the group | 
 **resource_id** | **str**| identifier of the rsource | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dataset_by_id**
> Dataset get_dataset_by_id(group_id, resource_id)

Find dataset by id

Returns a single dataset

### Example
```python
from __future__ import print_function
import time
import datastore
from datastore.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = datastore.DatasetsApi()
group_id = 'group_id_example' # str | name of the group
resource_id = 'resource_id_example' # str | identifier of the rsource

try:
    # Find dataset by id
    api_response = api_instance.get_dataset_by_id(group_id, resource_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasetsApi->get_dataset_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| name of the group | 
 **resource_id** | **str**| identifier of the rsource | 

### Return type

[**Dataset**](Dataset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_datasets**
> list[Dataset] search_datasets(group_id, name=name, acquisition_time=acquisition_time, data_time=data_time, bbox=bbox, orbit_number=orbit_number, orbit_direction=orbit_direction, processor_name=processor_name, processor_version=processor_version, processing_level=processing_level, processing_mode=processing_mode, limit=limit, offset=offset, sort_by=sort_by, sort_order=sort_order, max_versions=max_versions, record_time=record_time, resource_time_scope=resource_time_scope, group_properties=group_properties, dissemination=dissemination, hidden=hidden)

Search for datasets

Search for datasets matching the query

### Example
```python
from __future__ import print_function
import time
import datastore
from datastore.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = datastore.DatasetsApi()
group_id = 'group_id_example' # str | name of the group
name = 'name_example' # str | resource name (optional)
acquisition_time = 'acquisition_time_example' # str | Either a date-time or an interval, open or closed. Date and time expressions adhere to RFC 3339. Open intervals are expressed using double-dots.    Examples:    A date-time: \"2018-02-12T23:20:50Z\"  A closed interval: \"2018-02-12T00:00:00Z/2018-03-18T12:31:12Z\"  Open intervals: \"2018-02-12T00:00:00Z/..\" or \"../2018-03-18T12:31:12Z\"    Only products  that have a acquisition time that intersects the value of datetime are selected.     (optional)
data_time = 'data_time_example' # str | Either a date-time or an interval, open or closed. Date and time expressions adhere to RFC 3339. Open intervals are expressed using double-dots.    Examples:    A date-time: \"2018-02-12T23:20:50Z\"  A closed interval: \"2018-02-12T00:00:00Z/2018-03-18T12:31:12Z\"  Open intervals: \"2018-02-12T00:00:00Z/..\" or \"../2018-03-18T12:31:12Z\"    Only generic dataset  that have a data time that intersects the value of datetime are selected.     (optional)
bbox = [3.4] # list[float] | Only resources that have a geometry that intersects the bounding box are selected. The bounding box is provided as four numbers in WGS 84 longitude,latitude    Lower left corner, coordinate axis 1  Lower left corner, coordinate axis 2  Upper right corner, coordinate axis 1  Upper right corner, coordinate axis 2   (optional)
orbit_number = 56 # int | Filter on orbit number (optional)
orbit_direction = 'orbit_direction_example' # str | Filter on orbit direction (optional)
processor_name = 'processor_name_example' # str | Name of the processor (optional)
processor_version = 'processor_version_example' # str | Version of the processor (optional)
processing_level = 'processing_level_example' # str |  (optional)
processing_mode = 'processing_mode_example' # str | Used for L2 only (NRT, CP, tbd) (optional)
limit = 1000 # int | Limit the number of returned item (optional) (default to 1000)
offset = 0 # int | offset for the returned items (optional) (default to 0)
sort_by = 'sort_by_example' # str | sprt by creation update or access time (optional)
sort_order = 'sort_order_example' # str | ascending or descending (optional)
max_versions = 1 # int | return the last n versions of each resource (optional) (default to 1)
record_time = 'record_time_example' # str | Either a close or open interval. Date and time expressions adhere to RFC 3339. Open intervals are expressed using double-dots. Only resources that were updated (or created) during the interval are selected.The avaialbility-scope may amend the behaviour of this operation (optional)
resource_time_scope = 'resource_time_scope_example' # str | Amend the resource-time scope for filtering the items based  on the access time, update time, or creation time. (optional)
group_properties = {'key': 'group_properties_example'} # dict(str, str) | group specific properties queryables (optional)
dissemination = true # bool | flag for enabling dissemination (optional)
hidden = false # bool | include the default excluded (hidden) records if set to true (optional) (default to false)

try:
    # Search for datasets
    api_response = api_instance.search_datasets(group_id, name=name, acquisition_time=acquisition_time, data_time=data_time, bbox=bbox, orbit_number=orbit_number, orbit_direction=orbit_direction, processor_name=processor_name, processor_version=processor_version, processing_level=processing_level, processing_mode=processing_mode, limit=limit, offset=offset, sort_by=sort_by, sort_order=sort_order, max_versions=max_versions, record_time=record_time, resource_time_scope=resource_time_scope, group_properties=group_properties, dissemination=dissemination, hidden=hidden)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasetsApi->search_datasets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| name of the group | 
 **name** | **str**| resource name | [optional] 
 **acquisition_time** | **str**| Either a date-time or an interval, open or closed. Date and time expressions adhere to RFC 3339. Open intervals are expressed using double-dots.    Examples:    A date-time: \&quot;2018-02-12T23:20:50Z\&quot;  A closed interval: \&quot;2018-02-12T00:00:00Z/2018-03-18T12:31:12Z\&quot;  Open intervals: \&quot;2018-02-12T00:00:00Z/..\&quot; or \&quot;../2018-03-18T12:31:12Z\&quot;    Only products  that have a acquisition time that intersects the value of datetime are selected.     | [optional] 
 **data_time** | **str**| Either a date-time or an interval, open or closed. Date and time expressions adhere to RFC 3339. Open intervals are expressed using double-dots.    Examples:    A date-time: \&quot;2018-02-12T23:20:50Z\&quot;  A closed interval: \&quot;2018-02-12T00:00:00Z/2018-03-18T12:31:12Z\&quot;  Open intervals: \&quot;2018-02-12T00:00:00Z/..\&quot; or \&quot;../2018-03-18T12:31:12Z\&quot;    Only generic dataset  that have a data time that intersects the value of datetime are selected.     | [optional] 
 **bbox** | [**list[float]**](float.md)| Only resources that have a geometry that intersects the bounding box are selected. The bounding box is provided as four numbers in WGS 84 longitude,latitude    Lower left corner, coordinate axis 1  Lower left corner, coordinate axis 2  Upper right corner, coordinate axis 1  Upper right corner, coordinate axis 2   | [optional] 
 **orbit_number** | **int**| Filter on orbit number | [optional] 
 **orbit_direction** | **str**| Filter on orbit direction | [optional] 
 **processor_name** | **str**| Name of the processor | [optional] 
 **processor_version** | **str**| Version of the processor | [optional] 
 **processing_level** | **str**|  | [optional] 
 **processing_mode** | **str**| Used for L2 only (NRT, CP, tbd) | [optional] 
 **limit** | **int**| Limit the number of returned item | [optional] [default to 1000]
 **offset** | **int**| offset for the returned items | [optional] [default to 0]
 **sort_by** | **str**| sprt by creation update or access time | [optional] 
 **sort_order** | **str**| ascending or descending | [optional] 
 **max_versions** | **int**| return the last n versions of each resource | [optional] [default to 1]
 **record_time** | **str**| Either a close or open interval. Date and time expressions adhere to RFC 3339. Open intervals are expressed using double-dots. Only resources that were updated (or created) during the interval are selected.The avaialbility-scope may amend the behaviour of this operation | [optional] 
 **resource_time_scope** | **str**| Amend the resource-time scope for filtering the items based  on the access time, update time, or creation time. | [optional] 
 **group_properties** | [**dict(str, str)**](str.md)| group specific properties queryables | [optional] 
 **dissemination** | **bool**| flag for enabling dissemination | [optional] 
 **hidden** | **bool**| include the default excluded (hidden) records if set to true | [optional] [default to false]

### Return type

[**list[Dataset]**](Dataset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dataset**
> update_dataset(body, group_id, resource_id)

Update a Dataset

Update properties a group  

### Example
```python
from __future__ import print_function
import time
import datastore
from datastore.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = datastore.DatasetsApi()
body = datastore.DatasetDescription() # DatasetDescription | Resource Change Report
group_id = 'group_id_example' # str | name of the Group
resource_id = 'resource_id_example' # str | identifier of the rsource

try:
    # Update a Dataset
    api_instance.update_dataset(body, group_id, resource_id)
except ApiException as e:
    print("Exception when calling DatasetsApi->update_dataset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DatasetDescription**](DatasetDescription.md)| Resource Change Report | 
 **group_id** | **str**| name of the Group | 
 **resource_id** | **str**| identifier of the rsource | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

