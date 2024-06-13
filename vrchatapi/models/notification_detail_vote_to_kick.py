# coding: utf-8

"""
    VRChat API Documentation


    The version of the OpenAPI document: 1.17.6
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


class NotificationDetailVoteToKick(object):
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
        'initiator_user_id': 'str',
        'user_to_kick_id': 'str'
    }

    attribute_map = {
        'initiator_user_id': 'initiatorUserId',
        'user_to_kick_id': 'userToKickId'
    }

    def __init__(self, initiator_user_id=None, user_to_kick_id=None, local_vars_configuration=None):  # noqa: E501
        """NotificationDetailVoteToKick - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._initiator_user_id = None
        self._user_to_kick_id = None
        self.discriminator = None

        self.initiator_user_id = initiator_user_id
        self.user_to_kick_id = user_to_kick_id

    @property
    def initiator_user_id(self):
        """Gets the initiator_user_id of this NotificationDetailVoteToKick.  # noqa: E501

        A users unique ID, usually in the form of `usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469`. Legacy players can have old IDs in the form of `8JoV9XEdpo`. The ID can never be changed.  # noqa: E501

        :return: The initiator_user_id of this NotificationDetailVoteToKick.  # noqa: E501
        :rtype: str
        """
        return self._initiator_user_id

    @initiator_user_id.setter
    def initiator_user_id(self, initiator_user_id):
        """Sets the initiator_user_id of this NotificationDetailVoteToKick.

        A users unique ID, usually in the form of `usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469`. Legacy players can have old IDs in the form of `8JoV9XEdpo`. The ID can never be changed.  # noqa: E501

        :param initiator_user_id: The initiator_user_id of this NotificationDetailVoteToKick.  # noqa: E501
        :type initiator_user_id: str
        """
        if self.local_vars_configuration.client_side_validation and initiator_user_id is None:  # noqa: E501
            raise ValueError("Invalid value for `initiator_user_id`, must not be `None`")  # noqa: E501

        self._initiator_user_id = initiator_user_id

    @property
    def user_to_kick_id(self):
        """Gets the user_to_kick_id of this NotificationDetailVoteToKick.  # noqa: E501

        A users unique ID, usually in the form of `usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469`. Legacy players can have old IDs in the form of `8JoV9XEdpo`. The ID can never be changed.  # noqa: E501

        :return: The user_to_kick_id of this NotificationDetailVoteToKick.  # noqa: E501
        :rtype: str
        """
        return self._user_to_kick_id

    @user_to_kick_id.setter
    def user_to_kick_id(self, user_to_kick_id):
        """Sets the user_to_kick_id of this NotificationDetailVoteToKick.

        A users unique ID, usually in the form of `usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469`. Legacy players can have old IDs in the form of `8JoV9XEdpo`. The ID can never be changed.  # noqa: E501

        :param user_to_kick_id: The user_to_kick_id of this NotificationDetailVoteToKick.  # noqa: E501
        :type user_to_kick_id: str
        """
        if self.local_vars_configuration.client_side_validation and user_to_kick_id is None:  # noqa: E501
            raise ValueError("Invalid value for `user_to_kick_id`, must not be `None`")  # noqa: E501

        self._user_to_kick_id = user_to_kick_id

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
        if not isinstance(other, NotificationDetailVoteToKick):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NotificationDetailVoteToKick):
            return True

        return self.to_dict() != other.to_dict()
