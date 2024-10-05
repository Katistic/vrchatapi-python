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


class LimitedUnityPackage(object):
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
        'platform': 'str',
        'unity_version': 'str'
    }

    attribute_map = {
        'platform': 'platform',
        'unity_version': 'unityVersion'
    }

    def __init__(self, platform=None, unity_version=None, local_vars_configuration=None):  # noqa: E501
        """LimitedUnityPackage - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._platform = None
        self._unity_version = None
        self.discriminator = None

        self.platform = platform
        self.unity_version = unity_version

    @property
    def platform(self):
        """Gets the platform of this LimitedUnityPackage.  # noqa: E501

        This can be `standalonewindows` or `android`, but can also pretty much be any random Unity verison such as `2019.2.4-801-Release` or `2019.2.2-772-Release` or even `unknownplatform`.  # noqa: E501

        :return: The platform of this LimitedUnityPackage.  # noqa: E501
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this LimitedUnityPackage.

        This can be `standalonewindows` or `android`, but can also pretty much be any random Unity verison such as `2019.2.4-801-Release` or `2019.2.2-772-Release` or even `unknownplatform`.  # noqa: E501

        :param platform: The platform of this LimitedUnityPackage.  # noqa: E501
        :type platform: str
        """
        if self.local_vars_configuration.client_side_validation and platform is None:  # noqa: E501
            raise ValueError("Invalid value for `platform`, must not be `None`")  # noqa: E501

        self._platform = platform

    @property
    def unity_version(self):
        """Gets the unity_version of this LimitedUnityPackage.  # noqa: E501


        :return: The unity_version of this LimitedUnityPackage.  # noqa: E501
        :rtype: str
        """
        return self._unity_version

    @unity_version.setter
    def unity_version(self, unity_version):
        """Sets the unity_version of this LimitedUnityPackage.


        :param unity_version: The unity_version of this LimitedUnityPackage.  # noqa: E501
        :type unity_version: str
        """
        if self.local_vars_configuration.client_side_validation and unity_version is None:  # noqa: E501
            raise ValueError("Invalid value for `unity_version`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                unity_version is not None and len(unity_version) < 1):
            raise ValueError("Invalid value for `unity_version`, length must be greater than or equal to `1`")  # noqa: E501

        self._unity_version = unity_version

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
        if not isinstance(other, LimitedUnityPackage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LimitedUnityPackage):
            return True

        return self.to_dict() != other.to_dict()
