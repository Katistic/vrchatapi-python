# coding: utf-8

"""
    VRChat API Documentation


    The version of the OpenAPI document: 1.18.6
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


class GroupLimitedMember(object):
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
        'id': 'str',
        'group_id': 'str',
        'user_id': 'str',
        'is_representing': 'bool',
        'role_ids': 'list[str]',
        'm_role_ids': 'list[str]',
        'joined_at': 'datetime',
        'membership_status': 'GroupMemberStatus',
        'visibility': 'str',
        'is_subscribed_to_announcements': 'bool',
        'created_at': 'datetime',
        'banned_at': 'datetime',
        'manager_notes': 'str',
        'last_post_read_at': 'datetime',
        'has_joined_from_purchase': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'group_id': 'groupId',
        'user_id': 'userId',
        'is_representing': 'isRepresenting',
        'role_ids': 'roleIds',
        'm_role_ids': 'mRoleIds',
        'joined_at': 'joinedAt',
        'membership_status': 'membershipStatus',
        'visibility': 'visibility',
        'is_subscribed_to_announcements': 'isSubscribedToAnnouncements',
        'created_at': 'createdAt',
        'banned_at': 'bannedAt',
        'manager_notes': 'managerNotes',
        'last_post_read_at': 'lastPostReadAt',
        'has_joined_from_purchase': 'hasJoinedFromPurchase'
    }

    def __init__(self, id=None, group_id=None, user_id=None, is_representing=False, role_ids=None, m_role_ids=None, joined_at=None, membership_status=None, visibility=None, is_subscribed_to_announcements=False, created_at=None, banned_at=None, manager_notes=None, last_post_read_at=None, has_joined_from_purchase=None, local_vars_configuration=None):  # noqa: E501
        """GroupLimitedMember - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._group_id = None
        self._user_id = None
        self._is_representing = None
        self._role_ids = None
        self._m_role_ids = None
        self._joined_at = None
        self._membership_status = None
        self._visibility = None
        self._is_subscribed_to_announcements = None
        self._created_at = None
        self._banned_at = None
        self._manager_notes = None
        self._last_post_read_at = None
        self._has_joined_from_purchase = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if group_id is not None:
            self.group_id = group_id
        if user_id is not None:
            self.user_id = user_id
        if is_representing is not None:
            self.is_representing = is_representing
        if role_ids is not None:
            self.role_ids = role_ids
        if m_role_ids is not None:
            self.m_role_ids = m_role_ids
        self.joined_at = joined_at
        if membership_status is not None:
            self.membership_status = membership_status
        if visibility is not None:
            self.visibility = visibility
        if is_subscribed_to_announcements is not None:
            self.is_subscribed_to_announcements = is_subscribed_to_announcements
        self.created_at = created_at
        self.banned_at = banned_at
        self.manager_notes = manager_notes
        self.last_post_read_at = last_post_read_at
        if has_joined_from_purchase is not None:
            self.has_joined_from_purchase = has_joined_from_purchase

    @property
    def id(self):
        """Gets the id of this GroupLimitedMember.  # noqa: E501


        :return: The id of this GroupLimitedMember.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GroupLimitedMember.


        :param id: The id of this GroupLimitedMember.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def group_id(self):
        """Gets the group_id of this GroupLimitedMember.  # noqa: E501


        :return: The group_id of this GroupLimitedMember.  # noqa: E501
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this GroupLimitedMember.


        :param group_id: The group_id of this GroupLimitedMember.  # noqa: E501
        :type group_id: str
        """

        self._group_id = group_id

    @property
    def user_id(self):
        """Gets the user_id of this GroupLimitedMember.  # noqa: E501

        A users unique ID, usually in the form of `usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469`. Legacy players can have old IDs in the form of `8JoV9XEdpo`. The ID can never be changed.  # noqa: E501

        :return: The user_id of this GroupLimitedMember.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this GroupLimitedMember.

        A users unique ID, usually in the form of `usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469`. Legacy players can have old IDs in the form of `8JoV9XEdpo`. The ID can never be changed.  # noqa: E501

        :param user_id: The user_id of this GroupLimitedMember.  # noqa: E501
        :type user_id: str
        """

        self._user_id = user_id

    @property
    def is_representing(self):
        """Gets the is_representing of this GroupLimitedMember.  # noqa: E501

        Whether the user is representing the group. This makes the group show up above the name tag in-game.  # noqa: E501

        :return: The is_representing of this GroupLimitedMember.  # noqa: E501
        :rtype: bool
        """
        return self._is_representing

    @is_representing.setter
    def is_representing(self, is_representing):
        """Sets the is_representing of this GroupLimitedMember.

        Whether the user is representing the group. This makes the group show up above the name tag in-game.  # noqa: E501

        :param is_representing: The is_representing of this GroupLimitedMember.  # noqa: E501
        :type is_representing: bool
        """

        self._is_representing = is_representing

    @property
    def role_ids(self):
        """Gets the role_ids of this GroupLimitedMember.  # noqa: E501


        :return: The role_ids of this GroupLimitedMember.  # noqa: E501
        :rtype: list[str]
        """
        return self._role_ids

    @role_ids.setter
    def role_ids(self, role_ids):
        """Sets the role_ids of this GroupLimitedMember.


        :param role_ids: The role_ids of this GroupLimitedMember.  # noqa: E501
        :type role_ids: list[str]
        """

        self._role_ids = role_ids

    @property
    def m_role_ids(self):
        """Gets the m_role_ids of this GroupLimitedMember.  # noqa: E501


        :return: The m_role_ids of this GroupLimitedMember.  # noqa: E501
        :rtype: list[str]
        """
        return self._m_role_ids

    @m_role_ids.setter
    def m_role_ids(self, m_role_ids):
        """Sets the m_role_ids of this GroupLimitedMember.


        :param m_role_ids: The m_role_ids of this GroupLimitedMember.  # noqa: E501
        :type m_role_ids: list[str]
        """

        self._m_role_ids = m_role_ids

    @property
    def joined_at(self):
        """Gets the joined_at of this GroupLimitedMember.  # noqa: E501


        :return: The joined_at of this GroupLimitedMember.  # noqa: E501
        :rtype: datetime
        """
        return self._joined_at

    @joined_at.setter
    def joined_at(self, joined_at):
        """Sets the joined_at of this GroupLimitedMember.


        :param joined_at: The joined_at of this GroupLimitedMember.  # noqa: E501
        :type joined_at: datetime
        """

        self._joined_at = joined_at

    @property
    def membership_status(self):
        """Gets the membership_status of this GroupLimitedMember.  # noqa: E501


        :return: The membership_status of this GroupLimitedMember.  # noqa: E501
        :rtype: GroupMemberStatus
        """
        return self._membership_status

    @membership_status.setter
    def membership_status(self, membership_status):
        """Sets the membership_status of this GroupLimitedMember.


        :param membership_status: The membership_status of this GroupLimitedMember.  # noqa: E501
        :type membership_status: GroupMemberStatus
        """

        self._membership_status = membership_status

    @property
    def visibility(self):
        """Gets the visibility of this GroupLimitedMember.  # noqa: E501


        :return: The visibility of this GroupLimitedMember.  # noqa: E501
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        """Sets the visibility of this GroupLimitedMember.


        :param visibility: The visibility of this GroupLimitedMember.  # noqa: E501
        :type visibility: str
        """

        self._visibility = visibility

    @property
    def is_subscribed_to_announcements(self):
        """Gets the is_subscribed_to_announcements of this GroupLimitedMember.  # noqa: E501


        :return: The is_subscribed_to_announcements of this GroupLimitedMember.  # noqa: E501
        :rtype: bool
        """
        return self._is_subscribed_to_announcements

    @is_subscribed_to_announcements.setter
    def is_subscribed_to_announcements(self, is_subscribed_to_announcements):
        """Sets the is_subscribed_to_announcements of this GroupLimitedMember.


        :param is_subscribed_to_announcements: The is_subscribed_to_announcements of this GroupLimitedMember.  # noqa: E501
        :type is_subscribed_to_announcements: bool
        """

        self._is_subscribed_to_announcements = is_subscribed_to_announcements

    @property
    def created_at(self):
        """Gets the created_at of this GroupLimitedMember.  # noqa: E501

        Only visible via the /groups/:groupId/members endpoint, **not** when fetching a specific user.  # noqa: E501

        :return: The created_at of this GroupLimitedMember.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this GroupLimitedMember.

        Only visible via the /groups/:groupId/members endpoint, **not** when fetching a specific user.  # noqa: E501

        :param created_at: The created_at of this GroupLimitedMember.  # noqa: E501
        :type created_at: datetime
        """

        self._created_at = created_at

    @property
    def banned_at(self):
        """Gets the banned_at of this GroupLimitedMember.  # noqa: E501

        Only visible via the /groups/:groupId/members endpoint, **not** when fetching a specific user.  # noqa: E501

        :return: The banned_at of this GroupLimitedMember.  # noqa: E501
        :rtype: datetime
        """
        return self._banned_at

    @banned_at.setter
    def banned_at(self, banned_at):
        """Sets the banned_at of this GroupLimitedMember.

        Only visible via the /groups/:groupId/members endpoint, **not** when fetching a specific user.  # noqa: E501

        :param banned_at: The banned_at of this GroupLimitedMember.  # noqa: E501
        :type banned_at: datetime
        """

        self._banned_at = banned_at

    @property
    def manager_notes(self):
        """Gets the manager_notes of this GroupLimitedMember.  # noqa: E501

        Only visible via the /groups/:groupId/members endpoint, **not** when fetching a specific user.  # noqa: E501

        :return: The manager_notes of this GroupLimitedMember.  # noqa: E501
        :rtype: str
        """
        return self._manager_notes

    @manager_notes.setter
    def manager_notes(self, manager_notes):
        """Sets the manager_notes of this GroupLimitedMember.

        Only visible via the /groups/:groupId/members endpoint, **not** when fetching a specific user.  # noqa: E501

        :param manager_notes: The manager_notes of this GroupLimitedMember.  # noqa: E501
        :type manager_notes: str
        """

        self._manager_notes = manager_notes

    @property
    def last_post_read_at(self):
        """Gets the last_post_read_at of this GroupLimitedMember.  # noqa: E501


        :return: The last_post_read_at of this GroupLimitedMember.  # noqa: E501
        :rtype: datetime
        """
        return self._last_post_read_at

    @last_post_read_at.setter
    def last_post_read_at(self, last_post_read_at):
        """Sets the last_post_read_at of this GroupLimitedMember.


        :param last_post_read_at: The last_post_read_at of this GroupLimitedMember.  # noqa: E501
        :type last_post_read_at: datetime
        """

        self._last_post_read_at = last_post_read_at

    @property
    def has_joined_from_purchase(self):
        """Gets the has_joined_from_purchase of this GroupLimitedMember.  # noqa: E501


        :return: The has_joined_from_purchase of this GroupLimitedMember.  # noqa: E501
        :rtype: bool
        """
        return self._has_joined_from_purchase

    @has_joined_from_purchase.setter
    def has_joined_from_purchase(self, has_joined_from_purchase):
        """Sets the has_joined_from_purchase of this GroupLimitedMember.


        :param has_joined_from_purchase: The has_joined_from_purchase of this GroupLimitedMember.  # noqa: E501
        :type has_joined_from_purchase: bool
        """

        self._has_joined_from_purchase = has_joined_from_purchase

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
        if not isinstance(other, GroupLimitedMember):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GroupLimitedMember):
            return True

        return self.to_dict() != other.to_dict()
