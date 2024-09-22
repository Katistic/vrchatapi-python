# coding: utf-8

"""
    VRChat API Documentation


    The version of the OpenAPI document: 1.18.4
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


class UpdateGroupMemberRequest(object):
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
        'visibility': 'GroupUserVisibility',
        'is_subscribed_to_announcements': 'bool',
        'manager_notes': 'str'
    }

    attribute_map = {
        'visibility': 'visibility',
        'is_subscribed_to_announcements': 'isSubscribedToAnnouncements',
        'manager_notes': 'managerNotes'
    }

    def __init__(self, visibility=None, is_subscribed_to_announcements=None, manager_notes=None, local_vars_configuration=None):  # noqa: E501
        """UpdateGroupMemberRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._visibility = None
        self._is_subscribed_to_announcements = None
        self._manager_notes = None
        self.discriminator = None

        if visibility is not None:
            self.visibility = visibility
        if is_subscribed_to_announcements is not None:
            self.is_subscribed_to_announcements = is_subscribed_to_announcements
        if manager_notes is not None:
            self.manager_notes = manager_notes

    @property
    def visibility(self):
        """Gets the visibility of this UpdateGroupMemberRequest.  # noqa: E501


        :return: The visibility of this UpdateGroupMemberRequest.  # noqa: E501
        :rtype: GroupUserVisibility
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        """Sets the visibility of this UpdateGroupMemberRequest.


        :param visibility: The visibility of this UpdateGroupMemberRequest.  # noqa: E501
        :type visibility: GroupUserVisibility
        """

        self._visibility = visibility

    @property
    def is_subscribed_to_announcements(self):
        """Gets the is_subscribed_to_announcements of this UpdateGroupMemberRequest.  # noqa: E501


        :return: The is_subscribed_to_announcements of this UpdateGroupMemberRequest.  # noqa: E501
        :rtype: bool
        """
        return self._is_subscribed_to_announcements

    @is_subscribed_to_announcements.setter
    def is_subscribed_to_announcements(self, is_subscribed_to_announcements):
        """Sets the is_subscribed_to_announcements of this UpdateGroupMemberRequest.


        :param is_subscribed_to_announcements: The is_subscribed_to_announcements of this UpdateGroupMemberRequest.  # noqa: E501
        :type is_subscribed_to_announcements: bool
        """

        self._is_subscribed_to_announcements = is_subscribed_to_announcements

    @property
    def manager_notes(self):
        """Gets the manager_notes of this UpdateGroupMemberRequest.  # noqa: E501


        :return: The manager_notes of this UpdateGroupMemberRequest.  # noqa: E501
        :rtype: str
        """
        return self._manager_notes

    @manager_notes.setter
    def manager_notes(self, manager_notes):
        """Sets the manager_notes of this UpdateGroupMemberRequest.


        :param manager_notes: The manager_notes of this UpdateGroupMemberRequest.  # noqa: E501
        :type manager_notes: str
        """

        self._manager_notes = manager_notes

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
        if not isinstance(other, UpdateGroupMemberRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateGroupMemberRequest):
            return True

        return self.to_dict() != other.to_dict()
