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


class UpdateUserNoteRequest(object):
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
        'target_user_id': 'str',
        'note': 'str'
    }

    attribute_map = {
        'target_user_id': 'targetUserId',
        'note': 'note'
    }

    def __init__(self, target_user_id=None, note=None, local_vars_configuration=None):  # noqa: E501
        """UpdateUserNoteRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._target_user_id = None
        self._note = None
        self.discriminator = None

        self.target_user_id = target_user_id
        self.note = note

    @property
    def target_user_id(self):
        """Gets the target_user_id of this UpdateUserNoteRequest.  # noqa: E501

        A users unique ID, usually in the form of `usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469`. Legacy players can have old IDs in the form of `8JoV9XEdpo`. The ID can never be changed.  # noqa: E501

        :return: The target_user_id of this UpdateUserNoteRequest.  # noqa: E501
        :rtype: str
        """
        return self._target_user_id

    @target_user_id.setter
    def target_user_id(self, target_user_id):
        """Sets the target_user_id of this UpdateUserNoteRequest.

        A users unique ID, usually in the form of `usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469`. Legacy players can have old IDs in the form of `8JoV9XEdpo`. The ID can never be changed.  # noqa: E501

        :param target_user_id: The target_user_id of this UpdateUserNoteRequest.  # noqa: E501
        :type target_user_id: str
        """
        if self.local_vars_configuration.client_side_validation and target_user_id is None:  # noqa: E501
            raise ValueError("Invalid value for `target_user_id`, must not be `None`")  # noqa: E501

        self._target_user_id = target_user_id

    @property
    def note(self):
        """Gets the note of this UpdateUserNoteRequest.  # noqa: E501


        :return: The note of this UpdateUserNoteRequest.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this UpdateUserNoteRequest.


        :param note: The note of this UpdateUserNoteRequest.  # noqa: E501
        :type note: str
        """
        if self.local_vars_configuration.client_side_validation and note is None:  # noqa: E501
            raise ValueError("Invalid value for `note`, must not be `None`")  # noqa: E501

        self._note = note

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
        if not isinstance(other, UpdateUserNoteRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateUserNoteRequest):
            return True

        return self.to_dict() != other.to_dict()
