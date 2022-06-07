# coding: utf-8

"""
    EO Data Store API

    EO Data Store Manager indexing all data hosted on a set of storages  # noqa: E501

    OpenAPI spec version: draft-3
    Contact: christophe.noel@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Group(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'group_id': 'str',
        'dataset_type': 'str',
        'path': 'str',
        'metadata_type': 'str',
        'group_properties': 'list[str]'
    }

    attribute_map = {
        'group_id': 'groupId',
        'dataset_type': 'dataset-type',
        'path': 'path',
        'metadata_type': 'metadata-type',
        'group_properties': 'group-properties'
    }

    def __init__(self, group_id=None, dataset_type=None, path=None, metadata_type=None, group_properties=None):  # noqa: E501
        """Group - a model defined in Swagger"""  # noqa: E501
        self._group_id = None
        self._dataset_type = None
        self._path = None
        self._metadata_type = None
        self._group_properties = None
        self.discriminator = None
        self.group_id = group_id
        self.dataset_type = dataset_type
        if path is not None:
            self.path = path
        if metadata_type is not None:
            self.metadata_type = metadata_type
        if group_properties is not None:
            self.group_properties = group_properties

    @property
    def group_id(self):
        """Gets the group_id of this Group.  # noqa: E501

        Group identifier used for grouping a set of datasets.  Note the groupId is unique regardless the dataset type (product, datafolder)  # noqa: E501

        :return: The group_id of this Group.  # noqa: E501
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this Group.

        Group identifier used for grouping a set of datasets.  Note the groupId is unique regardless the dataset type (product, datafolder)  # noqa: E501

        :param group_id: The group_id of this Group.  # noqa: E501
        :type: str
        """
        if group_id is None:
            raise ValueError("Invalid value for `group_id`, must not be `None`")  # noqa: E501

        self._group_id = group_id

    @property
    def dataset_type(self):
        """Gets the dataset_type of this Group.  # noqa: E501

        Product or Datafolder dataset (mission specific enumeration)  # noqa: E501

        :return: The dataset_type of this Group.  # noqa: E501
        :rtype: str
        """
        return self._dataset_type

    @dataset_type.setter
    def dataset_type(self, dataset_type):
        """Sets the dataset_type of this Group.

        Product or Datafolder dataset (mission specific enumeration)  # noqa: E501

        :param dataset_type: The dataset_type of this Group.  # noqa: E501
        :type: str
        """
        if dataset_type is None:
            raise ValueError("Invalid value for `dataset_type`, must not be `None`")  # noqa: E501
        allowed_values = ["product", "dataset"]  # noqa: E501
        if dataset_type not in allowed_values:
            raise ValueError(
                "Invalid value for `dataset_type` ({0}), must be one of {1}"  # noqa: E501
                .format(dataset_type, allowed_values)
            )

        self._dataset_type = dataset_type

    @property
    def path(self):
        """Gets the path of this Group.  # noqa: E501

        Optional physical root path of the group on the data storage.   If provided, the submitted datasets files are verified against this path.  # noqa: E501

        :return: The path of this Group.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this Group.

        Optional physical root path of the group on the data storage.   If provided, the submitted datasets files are verified against this path.  # noqa: E501

        :param path: The path of this Group.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def metadata_type(self):
        """Gets the metadata_type of this Group.  # noqa: E501

        Metadata format:  either a standard, or a general encoding (such as \"JSON\") which holds the set of metadata properties.    In the case of the ALTIUS mission, the metadata format for products SHALL be 'OGC 10-157r4' (Earth Observation Metadata profile of Observations & Measurement (XML). The set of metadata properties is defined in the ALTIUS Product  Format Definition document.  The metadata format for  datafolders (generic datasets) SHOULD be JSON which holds a set of JSON properties defined as a string.  # noqa: E501

        :return: The metadata_type of this Group.  # noqa: E501
        :rtype: str
        """
        return self._metadata_type

    @metadata_type.setter
    def metadata_type(self, metadata_type):
        """Sets the metadata_type of this Group.

        Metadata format:  either a standard, or a general encoding (such as \"JSON\") which holds the set of metadata properties.    In the case of the ALTIUS mission, the metadata format for products SHALL be 'OGC 10-157r4' (Earth Observation Metadata profile of Observations & Measurement (XML). The set of metadata properties is defined in the ALTIUS Product  Format Definition document.  The metadata format for  datafolders (generic datasets) SHOULD be JSON which holds a set of JSON properties defined as a string.  # noqa: E501

        :param metadata_type: The metadata_type of this Group.  # noqa: E501
        :type: str
        """

        self._metadata_type = metadata_type

    @property
    def group_properties(self):
        """Gets the group_properties of this Group.  # noqa: E501

        Name of the group (searchable) specific properties (up to three).  # noqa: E501

        :return: The group_properties of this Group.  # noqa: E501
        :rtype: list[str]
        """
        return self._group_properties

    @group_properties.setter
    def group_properties(self, group_properties):
        """Sets the group_properties of this Group.

        Name of the group (searchable) specific properties (up to three).  # noqa: E501

        :param group_properties: The group_properties of this Group.  # noqa: E501
        :type: list[str]
        """

        self._group_properties = group_properties

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Group, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Group):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other