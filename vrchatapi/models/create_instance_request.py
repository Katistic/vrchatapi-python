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


class CreateInstanceRequest(object):
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
        'world_id': 'str',
        'type': 'InstanceType',
        'region': 'InstanceRegion',
        'owner_id': 'str',
        'role_ids': 'list[str]',
        'group_access_type': 'GroupAccessType',
        'queue_enabled': 'bool',
        'closed_at': 'datetime',
        'can_request_invite': 'bool',
        'hard_close': 'bool',
        'invite_only': 'bool'
    }

    attribute_map = {
        'world_id': 'worldId',
        'type': 'type',
        'region': 'region',
        'owner_id': 'ownerId',
        'role_ids': 'roleIds',
        'group_access_type': 'groupAccessType',
        'queue_enabled': 'queueEnabled',
        'closed_at': 'closedAt',
        'can_request_invite': 'canRequestInvite',
        'hard_close': 'hardClose',
        'invite_only': 'inviteOnly'
    }

    def __init__(self, world_id=None, type=None, region=None, owner_id=None, role_ids=None, group_access_type=None, queue_enabled=False, closed_at=None, can_request_invite=False, hard_close=False, invite_only=False, local_vars_configuration=None):  # noqa: E501
        """CreateInstanceRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._world_id = None
        self._type = None
        self._region = None
        self._owner_id = None
        self._role_ids = None
        self._group_access_type = None
        self._queue_enabled = None
        self._closed_at = None
        self._can_request_invite = None
        self._hard_close = None
        self._invite_only = None
        self.discriminator = None

        self.world_id = world_id
        self.type = type
        self.region = region
        self.owner_id = owner_id
        if role_ids is not None:
            self.role_ids = role_ids
        if group_access_type is not None:
            self.group_access_type = group_access_type
        if queue_enabled is not None:
            self.queue_enabled = queue_enabled
        if closed_at is not None:
            self.closed_at = closed_at
        if can_request_invite is not None:
            self.can_request_invite = can_request_invite
        if hard_close is not None:
            self.hard_close = hard_close
        if invite_only is not None:
            self.invite_only = invite_only

    @property
    def world_id(self):
        """Gets the world_id of this CreateInstanceRequest.  # noqa: E501

        WorldID be \"offline\" on User profiles if you are not friends with that user.  # noqa: E501

        :return: The world_id of this CreateInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._world_id

    @world_id.setter
    def world_id(self, world_id):
        """Sets the world_id of this CreateInstanceRequest.

        WorldID be \"offline\" on User profiles if you are not friends with that user.  # noqa: E501

        :param world_id: The world_id of this CreateInstanceRequest.  # noqa: E501
        :type world_id: str
        """
        if self.local_vars_configuration.client_side_validation and world_id is None:  # noqa: E501
            raise ValueError("Invalid value for `world_id`, must not be `None`")  # noqa: E501

        self._world_id = world_id

    @property
    def type(self):
        """Gets the type of this CreateInstanceRequest.  # noqa: E501


        :return: The type of this CreateInstanceRequest.  # noqa: E501
        :rtype: InstanceType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateInstanceRequest.


        :param type: The type of this CreateInstanceRequest.  # noqa: E501
        :type type: InstanceType
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def region(self):
        """Gets the region of this CreateInstanceRequest.  # noqa: E501


        :return: The region of this CreateInstanceRequest.  # noqa: E501
        :rtype: InstanceRegion
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this CreateInstanceRequest.


        :param region: The region of this CreateInstanceRequest.  # noqa: E501
        :type region: InstanceRegion
        """
        if self.local_vars_configuration.client_side_validation and region is None:  # noqa: E501
            raise ValueError("Invalid value for `region`, must not be `None`")  # noqa: E501

        self._region = region

    @property
    def owner_id(self):
        """Gets the owner_id of this CreateInstanceRequest.  # noqa: E501

        A groupId if the instance type is \"group\", null if instance type is public, or a userId otherwise  # noqa: E501

        :return: The owner_id of this CreateInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this CreateInstanceRequest.

        A groupId if the instance type is \"group\", null if instance type is public, or a userId otherwise  # noqa: E501

        :param owner_id: The owner_id of this CreateInstanceRequest.  # noqa: E501
        :type owner_id: str
        """

        self._owner_id = owner_id

    @property
    def role_ids(self):
        """Gets the role_ids of this CreateInstanceRequest.  # noqa: E501

        Group roleIds that are allowed to join if the type is \"group\" and groupAccessType is \"member\"  # noqa: E501

        :return: The role_ids of this CreateInstanceRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._role_ids

    @role_ids.setter
    def role_ids(self, role_ids):
        """Sets the role_ids of this CreateInstanceRequest.

        Group roleIds that are allowed to join if the type is \"group\" and groupAccessType is \"member\"  # noqa: E501

        :param role_ids: The role_ids of this CreateInstanceRequest.  # noqa: E501
        :type role_ids: list[str]
        """

        self._role_ids = role_ids

    @property
    def group_access_type(self):
        """Gets the group_access_type of this CreateInstanceRequest.  # noqa: E501


        :return: The group_access_type of this CreateInstanceRequest.  # noqa: E501
        :rtype: GroupAccessType
        """
        return self._group_access_type

    @group_access_type.setter
    def group_access_type(self, group_access_type):
        """Sets the group_access_type of this CreateInstanceRequest.


        :param group_access_type: The group_access_type of this CreateInstanceRequest.  # noqa: E501
        :type group_access_type: GroupAccessType
        """

        self._group_access_type = group_access_type

    @property
    def queue_enabled(self):
        """Gets the queue_enabled of this CreateInstanceRequest.  # noqa: E501


        :return: The queue_enabled of this CreateInstanceRequest.  # noqa: E501
        :rtype: bool
        """
        return self._queue_enabled

    @queue_enabled.setter
    def queue_enabled(self, queue_enabled):
        """Sets the queue_enabled of this CreateInstanceRequest.


        :param queue_enabled: The queue_enabled of this CreateInstanceRequest.  # noqa: E501
        :type queue_enabled: bool
        """

        self._queue_enabled = queue_enabled

    @property
    def closed_at(self):
        """Gets the closed_at of this CreateInstanceRequest.  # noqa: E501

        The time after which users won't be allowed to join the instance. This doesn't work for public instances.  # noqa: E501

        :return: The closed_at of this CreateInstanceRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._closed_at

    @closed_at.setter
    def closed_at(self, closed_at):
        """Sets the closed_at of this CreateInstanceRequest.

        The time after which users won't be allowed to join the instance. This doesn't work for public instances.  # noqa: E501

        :param closed_at: The closed_at of this CreateInstanceRequest.  # noqa: E501
        :type closed_at: datetime
        """

        self._closed_at = closed_at

    @property
    def can_request_invite(self):
        """Gets the can_request_invite of this CreateInstanceRequest.  # noqa: E501

        Only applies to invite type instances to make them invite+  # noqa: E501

        :return: The can_request_invite of this CreateInstanceRequest.  # noqa: E501
        :rtype: bool
        """
        return self._can_request_invite

    @can_request_invite.setter
    def can_request_invite(self, can_request_invite):
        """Sets the can_request_invite of this CreateInstanceRequest.

        Only applies to invite type instances to make them invite+  # noqa: E501

        :param can_request_invite: The can_request_invite of this CreateInstanceRequest.  # noqa: E501
        :type can_request_invite: bool
        """

        self._can_request_invite = can_request_invite

    @property
    def hard_close(self):
        """Gets the hard_close of this CreateInstanceRequest.  # noqa: E501

        Currently unused, but will eventually be a flag to set if the closing of the instance should kick people.  # noqa: E501

        :return: The hard_close of this CreateInstanceRequest.  # noqa: E501
        :rtype: bool
        """
        return self._hard_close

    @hard_close.setter
    def hard_close(self, hard_close):
        """Sets the hard_close of this CreateInstanceRequest.

        Currently unused, but will eventually be a flag to set if the closing of the instance should kick people.  # noqa: E501

        :param hard_close: The hard_close of this CreateInstanceRequest.  # noqa: E501
        :type hard_close: bool
        """

        self._hard_close = hard_close

    @property
    def invite_only(self):
        """Gets the invite_only of this CreateInstanceRequest.  # noqa: E501


        :return: The invite_only of this CreateInstanceRequest.  # noqa: E501
        :rtype: bool
        """
        return self._invite_only

    @invite_only.setter
    def invite_only(self, invite_only):
        """Sets the invite_only of this CreateInstanceRequest.


        :param invite_only: The invite_only of this CreateInstanceRequest.  # noqa: E501
        :type invite_only: bool
        """

        self._invite_only = invite_only

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
        if not isinstance(other, CreateInstanceRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateInstanceRequest):
            return True

        return self.to_dict() != other.to_dict()
