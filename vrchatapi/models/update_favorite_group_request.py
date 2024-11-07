# coding: utf-8

"""
    VRChat API Documentation


    The version of the OpenAPI document: 1.18.7
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


class UpdateFavoriteGroupRequest(object):
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
        'display_name': 'str',
        'visibility': 'FavoriteGroupVisibility',
        'tags': 'list[str]'
    }

    attribute_map = {
        'display_name': 'displayName',
        'visibility': 'visibility',
        'tags': 'tags'
    }

    def __init__(self, display_name=None, visibility=None, tags=None, local_vars_configuration=None):  # noqa: E501
        """UpdateFavoriteGroupRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._display_name = None
        self._visibility = None
        self._tags = None
        self.discriminator = None

        if display_name is not None:
            self.display_name = display_name
        if visibility is not None:
            self.visibility = visibility
        if tags is not None:
            self.tags = tags

    @property
    def display_name(self):
        """Gets the display_name of this UpdateFavoriteGroupRequest.  # noqa: E501


        :return: The display_name of this UpdateFavoriteGroupRequest.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this UpdateFavoriteGroupRequest.


        :param display_name: The display_name of this UpdateFavoriteGroupRequest.  # noqa: E501
        :type display_name: str
        """

        self._display_name = display_name

    @property
    def visibility(self):
        """Gets the visibility of this UpdateFavoriteGroupRequest.  # noqa: E501


        :return: The visibility of this UpdateFavoriteGroupRequest.  # noqa: E501
        :rtype: FavoriteGroupVisibility
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        """Sets the visibility of this UpdateFavoriteGroupRequest.


        :param visibility: The visibility of this UpdateFavoriteGroupRequest.  # noqa: E501
        :type visibility: FavoriteGroupVisibility
        """

        self._visibility = visibility

    @property
    def tags(self):
        """Gets the tags of this UpdateFavoriteGroupRequest.  # noqa: E501

        Tags on FavoriteGroups are believed to do nothing.  # noqa: E501

        :return: The tags of this UpdateFavoriteGroupRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this UpdateFavoriteGroupRequest.

        Tags on FavoriteGroups are believed to do nothing.  # noqa: E501

        :param tags: The tags of this UpdateFavoriteGroupRequest.  # noqa: E501
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
        if not isinstance(other, UpdateFavoriteGroupRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateFavoriteGroupRequest):
            return True

        return self.to_dict() != other.to_dict()
