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

class GenericDataProperties(object):
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
        'data_time': 'str',
        'description': 'str'
    }

    attribute_map = {
        'data_time': 'data-time',
        'description': 'description'
    }

    def __init__(self, data_time=None, description=None):  # noqa: E501
        """GenericDataProperties - a model defined in Swagger"""  # noqa: E501
        self._data_time = None
        self._description = None
        self.discriminator = None
        if data_time is not None:
            self.data_time = data_time
        if description is not None:
            self.description = description

    @property
    def data_time(self):
        """Gets the data_time of this GenericDataProperties.  # noqa: E501

        Provide the time or period associated to this datafolder  # noqa: E501

        :return: The data_time of this GenericDataProperties.  # noqa: E501
        :rtype: str
        """
        return self._data_time

    @data_time.setter
    def data_time(self, data_time):
        """Sets the data_time of this GenericDataProperties.

        Provide the time or period associated to this datafolder  # noqa: E501

        :param data_time: The data_time of this GenericDataProperties.  # noqa: E501
        :type: str
        """

        self._data_time = data_time

    @property
    def description(self):
        """Gets the description of this GenericDataProperties.  # noqa: E501

        optional description of the dataset  # noqa: E501

        :return: The description of this GenericDataProperties.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GenericDataProperties.

        optional description of the dataset  # noqa: E501

        :param description: The description of this GenericDataProperties.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if issubclass(GenericDataProperties, dict):
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
        if not isinstance(other, GenericDataProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
