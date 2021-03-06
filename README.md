# datastore-client
EO Data Store Manager indexing all data hosted on a set of storages

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: draft-3
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import datastore 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import datastore
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import datastore
from datastore.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = datastore.DatasetsApi(datastore.ApiClient(configuration))
body = datastore.DatasetDescription() # DatasetDescription | Resource Change Report
group_id = 'group_id_example' # str | name of the Group

try:
    # Register a Dataset
    api_response = api_instance.create_dataset(body, group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasetsApi->create_dataset: %s\n" % e)

# create an instance of the API class
api_instance = datastore.DatasetsApi(datastore.ApiClient(configuration))
group_id = 'group_id_example' # str | name of the group
resource_id = 'resource_id_example' # str | identifier of the rsource

try:
    # Delete dataset
    api_instance.delete_dataset(group_id, resource_id)
except ApiException as e:
    print("Exception when calling DatasetsApi->delete_dataset: %s\n" % e)

# create an instance of the API class
api_instance = datastore.DatasetsApi(datastore.ApiClient(configuration))
group_id = 'group_id_example' # str | name of the group
resource_id = 'resource_id_example' # str | identifier of the rsource

try:
    # Find dataset by id
    api_response = api_instance.get_dataset_by_id(group_id, resource_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasetsApi->get_dataset_by_id: %s\n" % e)

# create an instance of the API class
api_instance = datastore.DatasetsApi(datastore.ApiClient(configuration))
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

# create an instance of the API class
api_instance = datastore.DatasetsApi(datastore.ApiClient(configuration))
body = datastore.DatasetDescription() # DatasetDescription | Resource Change Report
group_id = 'group_id_example' # str | name of the Group
resource_id = 'resource_id_example' # str | identifier of the rsource

try:
    # Update a Dataset
    api_instance.update_dataset(body, group_id, resource_id)
except ApiException as e:
    print("Exception when calling DatasetsApi->update_dataset: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://virtserver.swaggerhub.com/Spacebel.be/datastoreManager/draft-3*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DatasetsApi* | [**create_dataset**](docs/DatasetsApi.md#create_dataset) | **POST** /groups/{groupId}/datasets | Register a Dataset
*DatasetsApi* | [**delete_dataset**](docs/DatasetsApi.md#delete_dataset) | **DELETE** /groups/{groupId}/datasets/{resourceId} | Delete dataset
*DatasetsApi* | [**get_dataset_by_id**](docs/DatasetsApi.md#get_dataset_by_id) | **GET** /groups/{groupId}/datasets/{resourceId} | Find dataset by id
*DatasetsApi* | [**search_datasets**](docs/DatasetsApi.md#search_datasets) | **GET** /groups/{groupId}/datasets | Search for datasets
*DatasetsApi* | [**update_dataset**](docs/DatasetsApi.md#update_dataset) | **PUT** /groups/{groupId}/datasets/{resourceId} | Update a Dataset
*GroupsApi* | [**add_group**](docs/GroupsApi.md#add_group) | **POST** /groups | Add a group (dataset group or file group)
*GroupsApi* | [**delete_group**](docs/GroupsApi.md#delete_group) | **DELETE** /groups/{groupId} | Delete Group by name
*GroupsApi* | [**get_group_by_id**](docs/GroupsApi.md#get_group_by_id) | **GET** /groups | List Groups
*GroupsApi* | [**update_group**](docs/GroupsApi.md#update_group) | **PUT** /groups/{groupId} | Update a Group

## Documentation For Models

 - [Dataset](docs/Dataset.md)
 - [DatasetChange](docs/DatasetChange.md)
 - [DatasetDescription](docs/DatasetDescription.md)
 - [DatasetInfoDetails](docs/DatasetInfoDetails.md)
 - [GenericDataProperties](docs/GenericDataProperties.md)
 - [Group](docs/Group.md)
 - [ProductProperties](docs/ProductProperties.md)

## Documentation For Authorization

 All endpoints do not require authorization.


## Author

christophe.noel@gmail.com
