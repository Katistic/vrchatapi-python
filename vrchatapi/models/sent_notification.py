# coding: utf-8

"""
    VRChat API Documentation


    The version of the OpenAPI document: 1.16.8
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


class SentNotification(object):
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
        'created_at': 'datetime',
        'details': 'str',
        'id': 'str',
        'message': 'str',
        'reciever_user_id': 'str',
        'sender_user_id': 'str',
        'sender_username': 'str',
        'type': 'NotificationType'
    }

    attribute_map = {
        'created_at': 'created_at',
        'details': 'details',
        'id': 'id',
        'message': 'message',
        'reciever_user_id': 'recieverUserId',
        'sender_user_id': 'senderUserId',
        'sender_username': 'senderUsername',
        'type': 'type'
    }

    def __init__(self, created_at=None, details='{}', id=None, message=None, reciever_user_id=None, sender_user_id=None, sender_username=None, type=None, local_vars_configuration=None):  # noqa: E501
        """SentNotification - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._created_at = None
        self._details = None
        self._id = None
        self._message = None
        self._reciever_user_id = None
        self._sender_user_id = None
        self._sender_username = None
        self._type = None
        self.discriminator = None

        self.created_at = created_at
        self.details = details
        self.id = id
        self.message = message
        self.reciever_user_id = reciever_user_id
        self.sender_user_id = sender_user_id
        if sender_username is not None:
            self.sender_username = sender_username
        self.type = type

    @property
    def created_at(self):
        """Gets the created_at of this SentNotification.  # noqa: E501


        :return: The created_at of this SentNotification.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this SentNotification.


        :param created_at: The created_at of this SentNotification.  # noqa: E501
        :type created_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def details(self):
        """Gets the details of this SentNotification.  # noqa: E501

        **NOTICE:** This is not a JSON object, this is a json **encoded** object, meaning you have to json-de-encode to get the NotificationDetail object depending on the NotificationType.  # noqa: E501

        :return: The details of this SentNotification.  # noqa: E501
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this SentNotification.

        **NOTICE:** This is not a JSON object, this is a json **encoded** object, meaning you have to json-de-encode to get the NotificationDetail object depending on the NotificationType.  # noqa: E501

        :param details: The details of this SentNotification.  # noqa: E501
        :type details: str
        """
        if self.local_vars_configuration.client_side_validation and details is None:  # noqa: E501
            raise ValueError("Invalid value for `details`, must not be `None`")  # noqa: E501

        self._details = details

    @property
    def id(self):
        """Gets the id of this SentNotification.  # noqa: E501


        :return: The id of this SentNotification.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SentNotification.


        :param id: The id of this SentNotification.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                id is not None and len(id) < 1):
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `1`")  # noqa: E501

        self._id = id

    @property
    def message(self):
        """Gets the message of this SentNotification.  # noqa: E501

          # noqa: E501

        :return: The message of this SentNotification.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this SentNotification.

          # noqa: E501

        :param message: The message of this SentNotification.  # noqa: E501
        :type message: str
        """
        if self.local_vars_configuration.client_side_validation and message is None:  # noqa: E501
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def reciever_user_id(self):
        """Gets the reciever_user_id of this SentNotification.  # noqa: E501

        A users unique ID, usually in the form of `usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469`. Legacy players can have old IDs in the form of `8JoV9XEdpo`. The ID can never be changed.  # noqa: E501

        :return: The reciever_user_id of this SentNotification.  # noqa: E501
        :rtype: str
        """
        return self._reciever_user_id

    @reciever_user_id.setter
    def reciever_user_id(self, reciever_user_id):
        """Sets the reciever_user_id of this SentNotification.

        A users unique ID, usually in the form of `usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469`. Legacy players can have old IDs in the form of `8JoV9XEdpo`. The ID can never be changed.  # noqa: E501

        :param reciever_user_id: The reciever_user_id of this SentNotification.  # noqa: E501
        :type reciever_user_id: str
        """
        if self.local_vars_configuration.client_side_validation and reciever_user_id is None:  # noqa: E501
            raise ValueError("Invalid value for `reciever_user_id`, must not be `None`")  # noqa: E501

        self._reciever_user_id = reciever_user_id

    @property
    def sender_user_id(self):
        """Gets the sender_user_id of this SentNotification.  # noqa: E501

        A users unique ID, usually in the form of `usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469`. Legacy players can have old IDs in the form of `8JoV9XEdpo`. The ID can never be changed.  # noqa: E501

        :return: The sender_user_id of this SentNotification.  # noqa: E501
        :rtype: str
        """
        return self._sender_user_id

    @sender_user_id.setter
    def sender_user_id(self, sender_user_id):
        """Sets the sender_user_id of this SentNotification.

        A users unique ID, usually in the form of `usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469`. Legacy players can have old IDs in the form of `8JoV9XEdpo`. The ID can never be changed.  # noqa: E501

        :param sender_user_id: The sender_user_id of this SentNotification.  # noqa: E501
        :type sender_user_id: str
        """
        if self.local_vars_configuration.client_side_validation and sender_user_id is None:  # noqa: E501
            raise ValueError("Invalid value for `sender_user_id`, must not be `None`")  # noqa: E501

        self._sender_user_id = sender_user_id

    @property
    def sender_username(self):
        """Gets the sender_username of this SentNotification.  # noqa: E501

        -| **DEPRECATED:** VRChat API no longer return usernames of other users. [See issue by Tupper for more information](https://github.com/pypy-vrc/VRCX/issues/429).  # noqa: E501

        :return: The sender_username of this SentNotification.  # noqa: E501
        :rtype: str
        """
        return self._sender_username

    @sender_username.setter
    def sender_username(self, sender_username):
        """Sets the sender_username of this SentNotification.

        -| **DEPRECATED:** VRChat API no longer return usernames of other users. [See issue by Tupper for more information](https://github.com/pypy-vrc/VRCX/issues/429).  # noqa: E501

        :param sender_username: The sender_username of this SentNotification.  # noqa: E501
        :type sender_username: str
        """
        if (self.local_vars_configuration.client_side_validation and
                sender_username is not None and len(sender_username) < 1):
            raise ValueError("Invalid value for `sender_username`, length must be greater than or equal to `1`")  # noqa: E501

        self._sender_username = sender_username

    @property
    def type(self):
        """Gets the type of this SentNotification.  # noqa: E501


        :return: The type of this SentNotification.  # noqa: E501
        :rtype: NotificationType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SentNotification.


        :param type: The type of this SentNotification.  # noqa: E501
        :type type: NotificationType
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

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
        if not isinstance(other, SentNotification):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SentNotification):
            return True

        return self.to_dict() != other.to_dict()
