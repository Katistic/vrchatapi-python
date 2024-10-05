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


class InstancePlatforms(object):
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
        'android': 'int',
        'ios': 'int',
        'standalonewindows': 'int'
    }

    attribute_map = {
        'android': 'android',
        'ios': 'ios',
        'standalonewindows': 'standalonewindows'
    }

    def __init__(self, android=None, ios=None, standalonewindows=None, local_vars_configuration=None):  # noqa: E501
        """InstancePlatforms - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._android = None
        self._ios = None
        self._standalonewindows = None
        self.discriminator = None

        self.android = android
        if ios is not None:
            self.ios = ios
        self.standalonewindows = standalonewindows

    @property
    def android(self):
        """Gets the android of this InstancePlatforms.  # noqa: E501


        :return: The android of this InstancePlatforms.  # noqa: E501
        :rtype: int
        """
        return self._android

    @android.setter
    def android(self, android):
        """Sets the android of this InstancePlatforms.


        :param android: The android of this InstancePlatforms.  # noqa: E501
        :type android: int
        """
        if self.local_vars_configuration.client_side_validation and android is None:  # noqa: E501
            raise ValueError("Invalid value for `android`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                android is not None and android < 0):  # noqa: E501
            raise ValueError("Invalid value for `android`, must be a value greater than or equal to `0`")  # noqa: E501

        self._android = android

    @property
    def ios(self):
        """Gets the ios of this InstancePlatforms.  # noqa: E501


        :return: The ios of this InstancePlatforms.  # noqa: E501
        :rtype: int
        """
        return self._ios

    @ios.setter
    def ios(self, ios):
        """Sets the ios of this InstancePlatforms.


        :param ios: The ios of this InstancePlatforms.  # noqa: E501
        :type ios: int
        """
        if (self.local_vars_configuration.client_side_validation and
                ios is not None and ios < 0):  # noqa: E501
            raise ValueError("Invalid value for `ios`, must be a value greater than or equal to `0`")  # noqa: E501

        self._ios = ios

    @property
    def standalonewindows(self):
        """Gets the standalonewindows of this InstancePlatforms.  # noqa: E501


        :return: The standalonewindows of this InstancePlatforms.  # noqa: E501
        :rtype: int
        """
        return self._standalonewindows

    @standalonewindows.setter
    def standalonewindows(self, standalonewindows):
        """Sets the standalonewindows of this InstancePlatforms.


        :param standalonewindows: The standalonewindows of this InstancePlatforms.  # noqa: E501
        :type standalonewindows: int
        """
        if self.local_vars_configuration.client_side_validation and standalonewindows is None:  # noqa: E501
            raise ValueError("Invalid value for `standalonewindows`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                standalonewindows is not None and standalonewindows < 0):  # noqa: E501
            raise ValueError("Invalid value for `standalonewindows`, must be a value greater than or equal to `0`")  # noqa: E501

        self._standalonewindows = standalonewindows

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
        if not isinstance(other, InstancePlatforms):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InstancePlatforms):
            return True

        return self.to_dict() != other.to_dict()
