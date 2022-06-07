# coding: utf-8

"""
    EO Data Store API

    EO Data Store Manager indexing all data hosted on a set of storages  # noqa: E501

    OpenAPI spec version: draft-3
    Contact: christophe.noel@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from datastore.api_client import ApiClient


class DatasetsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_dataset(self, body, group_id, **kwargs):  # noqa: E501
        """Register a Dataset  # noqa: E501

        Create a new dataset (including a new version)   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_dataset(body, group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DatasetDescription body: Resource Change Report (required)
        :param str group_id: name of the Group (required)
        :return: Dataset
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_dataset_with_http_info(body, group_id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_dataset_with_http_info(body, group_id, **kwargs)  # noqa: E501
            return data

    def create_dataset_with_http_info(self, body, group_id, **kwargs):  # noqa: E501
        """Register a Dataset  # noqa: E501

        Create a new dataset (including a new version)   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_dataset_with_http_info(body, group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DatasetDescription body: Resource Change Report (required)
        :param str group_id: name of the Group (required)
        :return: Dataset
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'group_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_dataset" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_dataset`")  # noqa: E501
        # verify the required parameter 'group_id' is set
        if ('group_id' not in params or
                params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `create_dataset`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id' in params:
            path_params['groupId'] = params['group_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/groups/{groupId}/datasets', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Dataset',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_dataset(self, group_id, resource_id, **kwargs):  # noqa: E501
        """Delete dataset  # noqa: E501

        Delete a dataset  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_dataset(group_id, resource_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: name of the group (required)
        :param str resource_id: identifier of the rsource (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_dataset_with_http_info(group_id, resource_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_dataset_with_http_info(group_id, resource_id, **kwargs)  # noqa: E501
            return data

    def delete_dataset_with_http_info(self, group_id, resource_id, **kwargs):  # noqa: E501
        """Delete dataset  # noqa: E501

        Delete a dataset  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_dataset_with_http_info(group_id, resource_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: name of the group (required)
        :param str resource_id: identifier of the rsource (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_id', 'resource_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_dataset" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_id' is set
        if ('group_id' not in params or
                params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `delete_dataset`")  # noqa: E501
        # verify the required parameter 'resource_id' is set
        if ('resource_id' not in params or
                params['resource_id'] is None):
            raise ValueError("Missing the required parameter `resource_id` when calling `delete_dataset`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id' in params:
            path_params['groupId'] = params['group_id']  # noqa: E501
        if 'resource_id' in params:
            path_params['resourceId'] = params['resource_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/groups/{groupId}/datasets/{resourceId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_dataset_by_id(self, group_id, resource_id, **kwargs):  # noqa: E501
        """Find dataset by id  # noqa: E501

        Returns a single dataset  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dataset_by_id(group_id, resource_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: name of the group (required)
        :param str resource_id: identifier of the rsource (required)
        :return: Dataset
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_dataset_by_id_with_http_info(group_id, resource_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_dataset_by_id_with_http_info(group_id, resource_id, **kwargs)  # noqa: E501
            return data

    def get_dataset_by_id_with_http_info(self, group_id, resource_id, **kwargs):  # noqa: E501
        """Find dataset by id  # noqa: E501

        Returns a single dataset  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dataset_by_id_with_http_info(group_id, resource_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: name of the group (required)
        :param str resource_id: identifier of the rsource (required)
        :return: Dataset
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_id', 'resource_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dataset_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_id' is set
        if ('group_id' not in params or
                params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `get_dataset_by_id`")  # noqa: E501
        # verify the required parameter 'resource_id' is set
        if ('resource_id' not in params or
                params['resource_id'] is None):
            raise ValueError("Missing the required parameter `resource_id` when calling `get_dataset_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id' in params:
            path_params['groupId'] = params['group_id']  # noqa: E501
        if 'resource_id' in params:
            path_params['resourceId'] = params['resource_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/groups/{groupId}/datasets/{resourceId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Dataset',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_datasets(self, group_id, **kwargs):  # noqa: E501
        """Search for datasets  # noqa: E501

        Search for datasets matching the query  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_datasets(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: name of the group (required)
        :param str name: resource name
        :param str acquisition_time: Either a date-time or an interval, open or closed. Date and time expressions adhere to RFC 3339. Open intervals are expressed using double-dots.    Examples:    A date-time: \"2018-02-12T23:20:50Z\"  A closed interval: \"2018-02-12T00:00:00Z/2018-03-18T12:31:12Z\"  Open intervals: \"2018-02-12T00:00:00Z/..\" or \"../2018-03-18T12:31:12Z\"    Only products  that have a acquisition time that intersects the value of datetime are selected.    
        :param str data_time: Either a date-time or an interval, open or closed. Date and time expressions adhere to RFC 3339. Open intervals are expressed using double-dots.    Examples:    A date-time: \"2018-02-12T23:20:50Z\"  A closed interval: \"2018-02-12T00:00:00Z/2018-03-18T12:31:12Z\"  Open intervals: \"2018-02-12T00:00:00Z/..\" or \"../2018-03-18T12:31:12Z\"    Only generic dataset  that have a data time that intersects the value of datetime are selected.    
        :param list[float] bbox: Only resources that have a geometry that intersects the bounding box are selected. The bounding box is provided as four numbers in WGS 84 longitude,latitude    Lower left corner, coordinate axis 1  Lower left corner, coordinate axis 2  Upper right corner, coordinate axis 1  Upper right corner, coordinate axis 2  
        :param int orbit_number: Filter on orbit number
        :param str orbit_direction: Filter on orbit direction
        :param str processor_name: Name of the processor
        :param str processor_version: Version of the processor
        :param str processing_level:
        :param str processing_mode: Used for L2 only (NRT, CP, tbd)
        :param int limit: Limit the number of returned item
        :param int offset: offset for the returned items
        :param str sort_by: sprt by creation update or access time
        :param str sort_order: ascending or descending
        :param int max_versions: return the last n versions of each resource
        :param str record_time: Either a close or open interval. Date and time expressions adhere to RFC 3339. Open intervals are expressed using double-dots. Only resources that were updated (or created) during the interval are selected.The avaialbility-scope may amend the behaviour of this operation
        :param str resource_time_scope: Amend the resource-time scope for filtering the items based  on the access time, update time, or creation time.
        :param dict(str, str) group_properties: group specific properties queryables
        :param bool dissemination: flag for enabling dissemination
        :param bool hidden: include the default excluded (hidden) records if set to true
        :return: list[Dataset]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_datasets_with_http_info(group_id, **kwargs)  # noqa: E501
        else:
            (data) = self.search_datasets_with_http_info(group_id, **kwargs)  # noqa: E501
            return data

    def search_datasets_with_http_info(self, group_id, **kwargs):  # noqa: E501
        """Search for datasets  # noqa: E501

        Search for datasets matching the query  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_datasets_with_http_info(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: name of the group (required)
        :param str name: resource name
        :param str acquisition_time: Either a date-time or an interval, open or closed. Date and time expressions adhere to RFC 3339. Open intervals are expressed using double-dots.    Examples:    A date-time: \"2018-02-12T23:20:50Z\"  A closed interval: \"2018-02-12T00:00:00Z/2018-03-18T12:31:12Z\"  Open intervals: \"2018-02-12T00:00:00Z/..\" or \"../2018-03-18T12:31:12Z\"    Only products  that have a acquisition time that intersects the value of datetime are selected.    
        :param str data_time: Either a date-time or an interval, open or closed. Date and time expressions adhere to RFC 3339. Open intervals are expressed using double-dots.    Examples:    A date-time: \"2018-02-12T23:20:50Z\"  A closed interval: \"2018-02-12T00:00:00Z/2018-03-18T12:31:12Z\"  Open intervals: \"2018-02-12T00:00:00Z/..\" or \"../2018-03-18T12:31:12Z\"    Only generic dataset  that have a data time that intersects the value of datetime are selected.    
        :param list[float] bbox: Only resources that have a geometry that intersects the bounding box are selected. The bounding box is provided as four numbers in WGS 84 longitude,latitude    Lower left corner, coordinate axis 1  Lower left corner, coordinate axis 2  Upper right corner, coordinate axis 1  Upper right corner, coordinate axis 2  
        :param int orbit_number: Filter on orbit number
        :param str orbit_direction: Filter on orbit direction
        :param str processor_name: Name of the processor
        :param str processor_version: Version of the processor
        :param str processing_level:
        :param str processing_mode: Used for L2 only (NRT, CP, tbd)
        :param int limit: Limit the number of returned item
        :param int offset: offset for the returned items
        :param str sort_by: sprt by creation update or access time
        :param str sort_order: ascending or descending
        :param int max_versions: return the last n versions of each resource
        :param str record_time: Either a close or open interval. Date and time expressions adhere to RFC 3339. Open intervals are expressed using double-dots. Only resources that were updated (or created) during the interval are selected.The avaialbility-scope may amend the behaviour of this operation
        :param str resource_time_scope: Amend the resource-time scope for filtering the items based  on the access time, update time, or creation time.
        :param dict(str, str) group_properties: group specific properties queryables
        :param bool dissemination: flag for enabling dissemination
        :param bool hidden: include the default excluded (hidden) records if set to true
        :return: list[Dataset]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_id', 'name', 'acquisition_time', 'data_time', 'bbox', 'orbit_number', 'orbit_direction', 'processor_name', 'processor_version', 'processing_level', 'processing_mode', 'limit', 'offset', 'sort_by', 'sort_order', 'max_versions', 'record_time', 'resource_time_scope', 'group_properties', 'dissemination', 'hidden']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_datasets" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_id' is set
        if ('group_id' not in params or
                params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `search_datasets`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id' in params:
            path_params['groupId'] = params['group_id']  # noqa: E501

        query_params = []
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501
        if 'acquisition_time' in params:
            query_params.append(('acquisitionTime', params['acquisition_time']))  # noqa: E501
        if 'data_time' in params:
            query_params.append(('dataTime', params['data_time']))  # noqa: E501
        if 'bbox' in params:
            query_params.append(('bbox', params['bbox']))  # noqa: E501
            collection_formats['bbox'] = 'multi'  # noqa: E501
        if 'orbit_number' in params:
            query_params.append(('orbitNumber', params['orbit_number']))  # noqa: E501
        if 'orbit_direction' in params:
            query_params.append(('orbitDirection', params['orbit_direction']))  # noqa: E501
        if 'processor_name' in params:
            query_params.append(('processorName', params['processor_name']))  # noqa: E501
        if 'processor_version' in params:
            query_params.append(('processorVersion', params['processor_version']))  # noqa: E501
        if 'processing_level' in params:
            query_params.append(('processingLevel', params['processing_level']))  # noqa: E501
        if 'processing_mode' in params:
            query_params.append(('processingMode', params['processing_mode']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'sort_by' in params:
            query_params.append(('sort-by', params['sort_by']))  # noqa: E501
        if 'sort_order' in params:
            query_params.append(('sort-order', params['sort_order']))  # noqa: E501
        if 'max_versions' in params:
            query_params.append(('max-versions', params['max_versions']))  # noqa: E501
        if 'record_time' in params:
            query_params.append(('record-time', params['record_time']))  # noqa: E501
        if 'resource_time_scope' in params:
            query_params.append(('resource-time-scope', params['resource_time_scope']))  # noqa: E501
        if 'group_properties' in params:
            query_params.append(('group-properties', params['group_properties']))  # noqa: E501
        if 'dissemination' in params:
            query_params.append(('dissemination', params['dissemination']))  # noqa: E501
        if 'hidden' in params:
            query_params.append(('hidden', params['hidden']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/groups/{groupId}/datasets', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Dataset]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_dataset(self, body, group_id, resource_id, **kwargs):  # noqa: E501
        """Update a Dataset  # noqa: E501

        Update properties a group    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_dataset(body, group_id, resource_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DatasetDescription body: Resource Change Report (required)
        :param str group_id: name of the Group (required)
        :param str resource_id: identifier of the rsource (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_dataset_with_http_info(body, group_id, resource_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_dataset_with_http_info(body, group_id, resource_id, **kwargs)  # noqa: E501
            return data

    def update_dataset_with_http_info(self, body, group_id, resource_id, **kwargs):  # noqa: E501
        """Update a Dataset  # noqa: E501

        Update properties a group    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_dataset_with_http_info(body, group_id, resource_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DatasetDescription body: Resource Change Report (required)
        :param str group_id: name of the Group (required)
        :param str resource_id: identifier of the rsource (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'group_id', 'resource_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_dataset" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_dataset`")  # noqa: E501
        # verify the required parameter 'group_id' is set
        if ('group_id' not in params or
                params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `update_dataset`")  # noqa: E501
        # verify the required parameter 'resource_id' is set
        if ('resource_id' not in params or
                params['resource_id'] is None):
            raise ValueError("Missing the required parameter `resource_id` when calling `update_dataset`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id' in params:
            path_params['groupId'] = params['group_id']  # noqa: E501
        if 'resource_id' in params:
            path_params['resourceId'] = params['resource_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/groups/{groupId}/datasets/{resourceId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
