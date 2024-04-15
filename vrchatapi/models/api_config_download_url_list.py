# coding: utf-8

"""
    VRChat API Documentation


    The version of the OpenAPI document: 1.17.0
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


class APIConfigDownloadURLList(object):
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
        'sdk2': 'str',
        'sdk3_avatars': 'str',
        'sdk3_worlds': 'str',
        'vcc': 'str',
        'bootstrap': 'str'
    }

    attribute_map = {
        'sdk2': 'sdk2',
        'sdk3_avatars': 'sdk3-avatars',
        'sdk3_worlds': 'sdk3-worlds',
        'vcc': 'vcc',
        'bootstrap': 'bootstrap'
    }

    def __init__(self, sdk2=None, sdk3_avatars=None, sdk3_worlds=None, vcc=None, bootstrap=None, local_vars_configuration=None):  # noqa: E501
        """APIConfigDownloadURLList - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._sdk2 = None
        self._sdk3_avatars = None
        self._sdk3_worlds = None
        self._vcc = None
        self._bootstrap = None
        self.discriminator = None

        self.sdk2 = sdk2
        self.sdk3_avatars = sdk3_avatars
        self.sdk3_worlds = sdk3_worlds
        self.vcc = vcc
        self.bootstrap = bootstrap

    @property
    def sdk2(self):
        """Gets the sdk2 of this APIConfigDownloadURLList.  # noqa: E501

        Download link for legacy SDK2  # noqa: E501

        :return: The sdk2 of this APIConfigDownloadURLList.  # noqa: E501
        :rtype: str
        """
        return self._sdk2

    @sdk2.setter
    def sdk2(self, sdk2):
        """Sets the sdk2 of this APIConfigDownloadURLList.

        Download link for legacy SDK2  # noqa: E501

        :param sdk2: The sdk2 of this APIConfigDownloadURLList.  # noqa: E501
        :type sdk2: str
        """
        if self.local_vars_configuration.client_side_validation and sdk2 is None:  # noqa: E501
            raise ValueError("Invalid value for `sdk2`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                sdk2 is not None and len(sdk2) < 1):
            raise ValueError("Invalid value for `sdk2`, length must be greater than or equal to `1`")  # noqa: E501

        self._sdk2 = sdk2

    @property
    def sdk3_avatars(self):
        """Gets the sdk3_avatars of this APIConfigDownloadURLList.  # noqa: E501

        Download link for SDK3 for Avatars  # noqa: E501

        :return: The sdk3_avatars of this APIConfigDownloadURLList.  # noqa: E501
        :rtype: str
        """
        return self._sdk3_avatars

    @sdk3_avatars.setter
    def sdk3_avatars(self, sdk3_avatars):
        """Sets the sdk3_avatars of this APIConfigDownloadURLList.

        Download link for SDK3 for Avatars  # noqa: E501

        :param sdk3_avatars: The sdk3_avatars of this APIConfigDownloadURLList.  # noqa: E501
        :type sdk3_avatars: str
        """
        if self.local_vars_configuration.client_side_validation and sdk3_avatars is None:  # noqa: E501
            raise ValueError("Invalid value for `sdk3_avatars`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                sdk3_avatars is not None and len(sdk3_avatars) < 1):
            raise ValueError("Invalid value for `sdk3_avatars`, length must be greater than or equal to `1`")  # noqa: E501

        self._sdk3_avatars = sdk3_avatars

    @property
    def sdk3_worlds(self):
        """Gets the sdk3_worlds of this APIConfigDownloadURLList.  # noqa: E501

        Download link for SDK3 for Worlds  # noqa: E501

        :return: The sdk3_worlds of this APIConfigDownloadURLList.  # noqa: E501
        :rtype: str
        """
        return self._sdk3_worlds

    @sdk3_worlds.setter
    def sdk3_worlds(self, sdk3_worlds):
        """Sets the sdk3_worlds of this APIConfigDownloadURLList.

        Download link for SDK3 for Worlds  # noqa: E501

        :param sdk3_worlds: The sdk3_worlds of this APIConfigDownloadURLList.  # noqa: E501
        :type sdk3_worlds: str
        """
        if self.local_vars_configuration.client_side_validation and sdk3_worlds is None:  # noqa: E501
            raise ValueError("Invalid value for `sdk3_worlds`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                sdk3_worlds is not None and len(sdk3_worlds) < 1):
            raise ValueError("Invalid value for `sdk3_worlds`, length must be greater than or equal to `1`")  # noqa: E501

        self._sdk3_worlds = sdk3_worlds

    @property
    def vcc(self):
        """Gets the vcc of this APIConfigDownloadURLList.  # noqa: E501

        Download link for the Creator Companion  # noqa: E501

        :return: The vcc of this APIConfigDownloadURLList.  # noqa: E501
        :rtype: str
        """
        return self._vcc

    @vcc.setter
    def vcc(self, vcc):
        """Sets the vcc of this APIConfigDownloadURLList.

        Download link for the Creator Companion  # noqa: E501

        :param vcc: The vcc of this APIConfigDownloadURLList.  # noqa: E501
        :type vcc: str
        """
        if self.local_vars_configuration.client_side_validation and vcc is None:  # noqa: E501
            raise ValueError("Invalid value for `vcc`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                vcc is not None and len(vcc) < 1):
            raise ValueError("Invalid value for `vcc`, length must be greater than or equal to `1`")  # noqa: E501

        self._vcc = vcc

    @property
    def bootstrap(self):
        """Gets the bootstrap of this APIConfigDownloadURLList.  # noqa: E501

        Download link for ???  # noqa: E501

        :return: The bootstrap of this APIConfigDownloadURLList.  # noqa: E501
        :rtype: str
        """
        return self._bootstrap

    @bootstrap.setter
    def bootstrap(self, bootstrap):
        """Sets the bootstrap of this APIConfigDownloadURLList.

        Download link for ???  # noqa: E501

        :param bootstrap: The bootstrap of this APIConfigDownloadURLList.  # noqa: E501
        :type bootstrap: str
        """
        if self.local_vars_configuration.client_side_validation and bootstrap is None:  # noqa: E501
            raise ValueError("Invalid value for `bootstrap`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                bootstrap is not None and len(bootstrap) < 1):
            raise ValueError("Invalid value for `bootstrap`, length must be greater than or equal to `1`")  # noqa: E501

        self._bootstrap = bootstrap

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
        if not isinstance(other, APIConfigDownloadURLList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, APIConfigDownloadURLList):
            return True

        return self.to_dict() != other.to_dict()
