# coding: utf-8

"""
    VRChat API Documentation


    The version of the OpenAPI document: 1.18.0
    Contact: vrchatapi.lpv0t@aries.fyi
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from vrchatapi.configuration import Configuration


class CreateFileRequest(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'name': 'str',
        'mime_type': 'MIMEType',
        'extension': 'str',
        'tags': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'mime_type': 'mimeType',
        'extension': 'extension',
        'tags': 'tags'
    }

    def __init__(self, name=None, mime_type=None, extension=None, tags=None, local_vars_configuration=None):  # noqa: E501
        """CreateFileRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._mime_type = None
        self._extension = None
        self._tags = None
        self.discriminator = None

        self.name = name
        self.mime_type = mime_type
        self.extension = extension
        if tags is not None:
            self.tags = tags

    @property
    def name(self):
        """Gets the name of this CreateFileRequest.  # noqa: E501


        :return: The name of this CreateFileRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateFileRequest.


        :param name: The name of this CreateFileRequest.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 0):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `0`")  # noqa: E501

        self._name = name

    @property
    def mime_type(self):
        """Gets the mime_type of this CreateFileRequest.  # noqa: E501


        :return: The mime_type of this CreateFileRequest.  # noqa: E501
        :rtype: MIMEType
        """
        return self._mime_type

    @mime_type.setter
    def mime_type(self, mime_type):
        """Sets the mime_type of this CreateFileRequest.


        :param mime_type: The mime_type of this CreateFileRequest.  # noqa: E501
        :type mime_type: MIMEType
        """
        if self.local_vars_configuration.client_side_validation and mime_type is None:  # noqa: E501
            raise ValueError("Invalid value for `mime_type`, must not be `None`")  # noqa: E501

        self._mime_type = mime_type

    @property
    def extension(self):
        """Gets the extension of this CreateFileRequest.  # noqa: E501


        :return: The extension of this CreateFileRequest.  # noqa: E501
        :rtype: str
        """
        return self._extension

    @extension.setter
    def extension(self, extension):
        """Sets the extension of this CreateFileRequest.


        :param extension: The extension of this CreateFileRequest.  # noqa: E501
        :type extension: str
        """
        if self.local_vars_configuration.client_side_validation and extension is None:  # noqa: E501
            raise ValueError("Invalid value for `extension`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                extension is not None and len(extension) < 1):
            raise ValueError("Invalid value for `extension`, length must be greater than or equal to `1`")  # noqa: E501

        self._extension = extension

    @property
    def tags(self):
        """Gets the tags of this CreateFileRequest.  # noqa: E501

           # noqa: E501

        :return: The tags of this CreateFileRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateFileRequest.

           # noqa: E501

        :param tags: The tags of this CreateFileRequest.  # noqa: E501
        :type tags: list[str]
        """

        self._tags = tags

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateFileRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateFileRequest):
            return True

        return self.to_dict() != other.to_dict()
