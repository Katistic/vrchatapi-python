# coding: utf-8

"""
    VRChat API Documentation


    The version of the OpenAPI document: 1.18.5
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


class PlatformBuildInfo(object):
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
        'min_build_number': 'int',
        'redirection_address': 'str'
    }

    attribute_map = {
        'min_build_number': 'minBuildNumber',
        'redirection_address': 'redirectionAddress'
    }

    def __init__(self, min_build_number=None, redirection_address=None, local_vars_configuration=None):  # noqa: E501
        """PlatformBuildInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._min_build_number = None
        self._redirection_address = None
        self.discriminator = None

        self.min_build_number = min_build_number
        self.redirection_address = redirection_address

    @property
    def min_build_number(self):
        """Gets the min_build_number of this PlatformBuildInfo.  # noqa: E501

        Minimum build number required for the platform  # noqa: E501

        :return: The min_build_number of this PlatformBuildInfo.  # noqa: E501
        :rtype: int
        """
        return self._min_build_number

    @min_build_number.setter
    def min_build_number(self, min_build_number):
        """Sets the min_build_number of this PlatformBuildInfo.

        Minimum build number required for the platform  # noqa: E501

        :param min_build_number: The min_build_number of this PlatformBuildInfo.  # noqa: E501
        :type min_build_number: int
        """
        if self.local_vars_configuration.client_side_validation and min_build_number is None:  # noqa: E501
            raise ValueError("Invalid value for `min_build_number`, must not be `None`")  # noqa: E501

        self._min_build_number = min_build_number

    @property
    def redirection_address(self):
        """Gets the redirection_address of this PlatformBuildInfo.  # noqa: E501

        Redirection URL for updating the app  # noqa: E501

        :return: The redirection_address of this PlatformBuildInfo.  # noqa: E501
        :rtype: str
        """
        return self._redirection_address

    @redirection_address.setter
    def redirection_address(self, redirection_address):
        """Sets the redirection_address of this PlatformBuildInfo.

        Redirection URL for updating the app  # noqa: E501

        :param redirection_address: The redirection_address of this PlatformBuildInfo.  # noqa: E501
        :type redirection_address: str
        """
        if self.local_vars_configuration.client_side_validation and redirection_address is None:  # noqa: E501
            raise ValueError("Invalid value for `redirection_address`, must not be `None`")  # noqa: E501

        self._redirection_address = redirection_address

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
        if not isinstance(other, PlatformBuildInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PlatformBuildInfo):
            return True

        return self.to_dict() != other.to_dict()
