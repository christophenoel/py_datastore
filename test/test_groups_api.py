# coding: utf-8

"""
    EO Data Store API

    EO Data Store Manager indexing all data hosted on a set of storages  # noqa: E501

    OpenAPI spec version: draft-3
    Contact: christophe.noel@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import datastore
from datastore.api.groups_api import GroupsApi  # noqa: E501
from datastore.rest import ApiException


class TestGroupsApi(unittest.TestCase):
    """GroupsApi unit test stubs"""

    def setUp(self):
        self.api = GroupsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_group(self):
        """Test case for add_group

        Add a group (dataset group or file group)  # noqa: E501
        """
        pass

    def test_delete_group(self):
        """Test case for delete_group

        Delete Group by name  # noqa: E501
        """
        pass

    def test_get_group_by_id(self):
        """Test case for get_group_by_id

        List Groups  # noqa: E501
        """
        pass

    def test_update_group(self):
        """Test case for update_group

        Update a Group  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
