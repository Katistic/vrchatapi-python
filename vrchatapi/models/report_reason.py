# coding: utf-8

"""
    VRChat API Documentation


    The version of the OpenAPI document: 1.18.8
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


class ReportReason(object):
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
        'text': 'str',
        'tooltip': 'str'
    }

    attribute_map = {
        'text': 'text',
        'tooltip': 'tooltip'
    }

    def __init__(self, text=None, tooltip=None, local_vars_configuration=None):  # noqa: E501
        """ReportReason - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._text = None
        self._tooltip = None
        self.discriminator = None

        self.text = text
        self.tooltip = tooltip

    @property
    def text(self):
        """Gets the text of this ReportReason.  # noqa: E501

        The label or name of the report reason  # noqa: E501

        :return: The text of this ReportReason.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this ReportReason.

        The label or name of the report reason  # noqa: E501

        :param text: The text of this ReportReason.  # noqa: E501
        :type text: str
        """
        if self.local_vars_configuration.client_side_validation and text is None:  # noqa: E501
            raise ValueError("Invalid value for `text`, must not be `None`")  # noqa: E501

        self._text = text

    @property
    def tooltip(self):
        """Gets the tooltip of this ReportReason.  # noqa: E501

        A brief explanation of what this reason entails  # noqa: E501

        :return: The tooltip of this ReportReason.  # noqa: E501
        :rtype: str
        """
        return self._tooltip

    @tooltip.setter
    def tooltip(self, tooltip):
        """Sets the tooltip of this ReportReason.

        A brief explanation of what this reason entails  # noqa: E501

        :param tooltip: The tooltip of this ReportReason.  # noqa: E501
        :type tooltip: str
        """
        if self.local_vars_configuration.client_side_validation and tooltip is None:  # noqa: E501
            raise ValueError("Invalid value for `tooltip`, must not be `None`")  # noqa: E501

        self._tooltip = tooltip

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
        if not isinstance(other, ReportReason):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReportReason):
            return True

        return self.to_dict() != other.to_dict()
