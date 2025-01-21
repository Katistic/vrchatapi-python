# coding: utf-8

"""
    VRChat API Documentation


    The version of the OpenAPI document: 1.19.0
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


class APIConfigConstantsLANGUAGE(object):
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
        'spoken_language_options': 'dict(str, str)'
    }

    attribute_map = {
        'spoken_language_options': 'SPOKEN_LANGUAGE_OPTIONS'
    }

    def __init__(self, spoken_language_options=None, local_vars_configuration=None):  # noqa: E501
        """APIConfigConstantsLANGUAGE - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._spoken_language_options = None
        self.discriminator = None

        if spoken_language_options is not None:
            self.spoken_language_options = spoken_language_options

    @property
    def spoken_language_options(self):
        """Gets the spoken_language_options of this APIConfigConstantsLANGUAGE.  # noqa: E501

        Supported spoken language options  # noqa: E501

        :return: The spoken_language_options of this APIConfigConstantsLANGUAGE.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._spoken_language_options

    @spoken_language_options.setter
    def spoken_language_options(self, spoken_language_options):
        """Sets the spoken_language_options of this APIConfigConstantsLANGUAGE.

        Supported spoken language options  # noqa: E501

        :param spoken_language_options: The spoken_language_options of this APIConfigConstantsLANGUAGE.  # noqa: E501
        :type spoken_language_options: dict(str, str)
        """

        self._spoken_language_options = spoken_language_options

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
        if not isinstance(other, APIConfigConstantsLANGUAGE):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, APIConfigConstantsLANGUAGE):
            return True

        return self.to_dict() != other.to_dict()
