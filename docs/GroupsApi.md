# datastore.GroupsApi

All URIs are relative to *https://virtserver.swaggerhub.com/Spacebel.be/datastoreManager/draft-3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_group**](GroupsApi.md#add_group) | **POST** /groups | Add a group (dataset group or file group)
[**delete_group**](GroupsApi.md#delete_group) | **DELETE** /groups/{groupId} | Delete Group by name
[**get_group_by_id**](GroupsApi.md#get_group_by_id) | **GET** /groups | List Groups
[**update_group**](GroupsApi.md#update_group) | **PUT** /groups/{groupId} | Update a Group

# **add_group**
> Group add_group(body)

Add a group (dataset group or file group)

Add a group for a group of resources of the same type (dataset, file, ...). 

### Example
```python
from __future__ import print_function
import time
import datastore
from datastore.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = datastore.GroupsApi()
body = datastore.Group() # Group | group properties

try:
    # Add a group (dataset group or file group)
    api_response = api_instance.add_group(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->add_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Group**](Group.md)| group properties | 

### Return type

[**Group**](Group.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group**
> delete_group(group_id)

Delete Group by name

Remove a Group which prevent registering new resource (not removing existing resources)

### Example
```python
from __future__ import print_function
import time
import datastore
from datastore.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = datastore.GroupsApi()
group_id = 'group_id_example' # str | name of the Group

try:
    # Delete Group by name
    api_instance.delete_group(group_id)
except ApiException as e:
    print("Exception when calling GroupsApi->delete_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| name of the Group | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_by_id**
> list[Group] get_group_by_id()

List Groups

Returns a single group

### Example
```python
from __future__ import print_function
import time
import datastore
from datastore.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = datastore.GroupsApi()

try:
    # List Groups
    api_response = api_instance.get_group_by_id()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->get_group_by_id: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Group]**](Group.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group**
> update_group(body, group_id)

Update a Group

Update properties a group  

### Example
```python
from __future__ import print_function
import time
import datastore
from datastore.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = datastore.GroupsApi()
body = datastore.Group() # Group | Group properties
group_id = 'group_id_example' # str | name of the Group

try:
    # Update a Group
    api_instance.update_group(body, group_id)
except ApiException as e:
    print("Exception when calling GroupsApi->update_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Group**](Group.md)| Group properties | 
 **group_id** | **str**| name of the Group | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

