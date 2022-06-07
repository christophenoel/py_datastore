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

class DatasetDescription(object):
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
        'version': 'str',
        'folder_path': 'str',
        'data_path': 'str',
        'metadata_path': 'str',
        'name': 'str',
        'dissemination': 'bool',
        'hidden': 'bool'
    }

    attribute_map = {
        'version': 'version',
        'folder_path': 'folder-path',
        'data_path': 'data-path',
        'metadata_path': 'metadata-path',
        'name': 'name',
        'dissemination': 'dissemination',
        'hidden': 'hidden'
    }

    def __init__(self, version=None, folder_path=None, data_path=None, metadata_path='./metadata', name=None, dissemination=False, hidden=None):  # noqa: E501
        """DatasetDescription - a model defined in Swagger"""  # noqa: E501
        self._version = None
        self._folder_path = None
        self._data_path = None
        self._metadata_path = None
        self._name = None
        self._dissemination = None
        self._hidden = None
        self.discriminator = None
        if version is not None:
            self.version = version
        if folder_path is not None:
            self.folder_path = folder_path
        if data_path is not None:
            self.data_path = data_path
        if metadata_path is not None:
            self.metadata_path = metadata_path
        if name is not None:
            self.name = name
        if dissemination is not None:
            self.dissemination = dissemination
        if hidden is not None:
            self.hidden = hidden

    @property
    def version(self):
        """Gets the version of this DatasetDescription.  # noqa: E501

        Optional explicit version of this dataset (by default, an internal versioning strategy is used)  # noqa: E501

        :return: The version of this DatasetDescription.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this DatasetDescription.

        Optional explicit version of this dataset (by default, an internal versioning strategy is used)  # noqa: E501

        :param version: The version of this DatasetDescription.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def folder_path(self):
        """Gets the folder_path of this DatasetDescription.  # noqa: E501

        Absolute path of the physical folder (containing the data, metadata and other dataset files).  NOTE the leaf directory is the folder unique name  # noqa: E501

        :return: The folder_path of this DatasetDescription.  # noqa: E501
        :rtype: str
        """
        return self._folder_path

    @folder_path.setter
    def folder_path(self, folder_path):
        """Sets the folder_path of this DatasetDescription.

        Absolute path of the physical folder (containing the data, metadata and other dataset files).  NOTE the leaf directory is the folder unique name  # noqa: E501

        :param folder_path: The folder_path of this DatasetDescription.  # noqa: E501
        :type: str
        """

        self._folder_path = folder_path

    @property
    def data_path(self):
        """Gets the data_path of this DatasetDescription.  # noqa: E501

        RELATIVE path of the data file in the dataset folder (if the data was created or updated)  # noqa: E501

        :return: The data_path of this DatasetDescription.  # noqa: E501
        :rtype: str
        """
        return self._data_path

    @data_path.setter
    def data_path(self, data_path):
        """Sets the data_path of this DatasetDescription.

        RELATIVE path of the data file in the dataset folder (if the data was created or updated)  # noqa: E501

        :param data_path: The data_path of this DatasetDescription.  # noqa: E501
        :type: str
        """

        self._data_path = data_path

    @property
    def metadata_path(self):
        """Gets the metadata_path of this DatasetDescription.  # noqa: E501

        RELATIVE path of the metadata directory in the dataset folder (if some metadata were created or updated)  # noqa: E501

        :return: The metadata_path of this DatasetDescription.  # noqa: E501
        :rtype: str
        """
        return self._metadata_path

    @metadata_path.setter
    def metadata_path(self, metadata_path):
        """Sets the metadata_path of this DatasetDescription.

        RELATIVE path of the metadata directory in the dataset folder (if some metadata were created or updated)  # noqa: E501

        :param metadata_path: The metadata_path of this DatasetDescription.  # noqa: E501
        :type: str
        """

        self._metadata_path = metadata_path

    @property
    def name(self):
        """Gets the name of this DatasetDescription.  # noqa: E501

        If provided, overrides the dataset identifier which is set by default to the folder path leaf directory.   In ALTIUS mission, this parameter shall not be used for products.   # noqa: E501

        :return: The name of this DatasetDescription.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DatasetDescription.

        If provided, overrides the dataset identifier which is set by default to the folder path leaf directory.   In ALTIUS mission, this parameter shall not be used for products.   # noqa: E501

        :param name: The name of this DatasetDescription.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def dissemination(self):
        """Gets the dissemination of this DatasetDescription.  # noqa: E501

        Flag authorising publication of the product  # noqa: E501

        :return: The dissemination of this DatasetDescription.  # noqa: E501
        :rtype: bool
        """
        return self._dissemination

    @dissemination.setter
    def dissemination(self, dissemination):
        """Sets the dissemination of this DatasetDescription.

        Flag authorising publication of the product  # noqa: E501

        :param dissemination: The dissemination of this DatasetDescription.  # noqa: E501
        :type: bool
        """

        self._dissemination = dissemination

    @property
    def hidden(self):
        """Gets the hidden of this DatasetDescription.  # noqa: E501

        Flag implying this record will be hidden by default in the search results.  # noqa: E501

        :return: The hidden of this DatasetDescription.  # noqa: E501
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """Sets the hidden of this DatasetDescription.

        Flag implying this record will be hidden by default in the search results.  # noqa: E501

        :param hidden: The hidden of this DatasetDescription.  # noqa: E501
        :type: bool
        """

        self._hidden = hidden

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
        if issubclass(DatasetDescription, dict):
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
        if not isinstance(other, DatasetDescription):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other