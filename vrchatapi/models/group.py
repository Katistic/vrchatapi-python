# coding: utf-8

"""
    VRChat API Documentation


    The version of the OpenAPI document: 1.13.0
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


class Group(object):
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
        'name': 'str',
        'short_code': 'str',
        'discriminator': 'str',
        'description': 'str',
        'icon_url': 'str',
        'banner_url': 'str',
        'privacy': 'GroupPrivacy',
        'owner_id': 'str',
        'rules': 'str',
        'links': 'list[str]',
        'languages': 'list[str]',
        'icon_id': 'str',
        'banner_id': 'str',
        'member_count': 'int',
        'member_count_synced_at': 'datetime',
        'is_verified': 'bool',
        'join_state': 'GroupJoinState',
        'tags': 'list[str]',
        'galleries': 'list[GroupGallery]',
        'created_at': 'datetime',
        'online_member_count': 'int',
        'membership_status': 'GroupMemberStatus',
        'my_member': 'GroupMyMember',
        'roles': 'list[GroupRole]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'short_code': 'shortCode',
        'discriminator': 'discriminator',
        'description': 'description',
        'icon_url': 'iconUrl',
        'banner_url': 'bannerUrl',
        'privacy': 'privacy',
        'owner_id': 'ownerId',
        'rules': 'rules',
        'links': 'links',
        'languages': 'languages',
        'icon_id': 'iconId',
        'banner_id': 'bannerId',
        'member_count': 'memberCount',
        'member_count_synced_at': 'memberCountSyncedAt',
        'is_verified': 'isVerified',
        'join_state': 'joinState',
        'tags': 'tags',
        'galleries': 'galleries',
        'created_at': 'createdAt',
        'online_member_count': 'onlineMemberCount',
        'membership_status': 'membershipStatus',
        'my_member': 'myMember',
        'roles': 'roles'
    }

    def __init__(self, id=None, name=None, short_code=None, discriminator=None, description=None, icon_url=None, banner_url=None, privacy=None, owner_id=None, rules=None, links=None, languages=None, icon_id=None, banner_id=None, member_count=None, member_count_synced_at=None, is_verified=False, join_state=None, tags=None, galleries=None, created_at=None, online_member_count=None, membership_status=None, my_member=None, roles=None, local_vars_configuration=None):  # noqa: E501
        """Group - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._short_code = None
        self._discriminator = None
        self._description = None
        self._icon_url = None
        self._banner_url = None
        self._privacy = None
        self._owner_id = None
        self._rules = None
        self._links = None
        self._languages = None
        self._icon_id = None
        self._banner_id = None
        self._member_count = None
        self._member_count_synced_at = None
        self._is_verified = None
        self._join_state = None
        self._tags = None
        self._galleries = None
        self._created_at = None
        self._online_member_count = None
        self._membership_status = None
        self._my_member = None
        self._roles = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if short_code is not None:
            self.short_code = short_code
        if discriminator is not None:
            self.discriminator = discriminator
        if description is not None:
            self.description = description
        self.icon_url = icon_url
        self.banner_url = banner_url
        if privacy is not None:
            self.privacy = privacy
        if owner_id is not None:
            self.owner_id = owner_id
        self.rules = rules
        if links is not None:
            self.links = links
        if languages is not None:
            self.languages = languages
        self.icon_id = icon_id
        self.banner_id = banner_id
        if member_count is not None:
            self.member_count = member_count
        if member_count_synced_at is not None:
            self.member_count_synced_at = member_count_synced_at
        if is_verified is not None:
            self.is_verified = is_verified
        if join_state is not None:
            self.join_state = join_state
        if tags is not None:
            self.tags = tags
        if galleries is not None:
            self.galleries = galleries
        if created_at is not None:
            self.created_at = created_at
        if online_member_count is not None:
            self.online_member_count = online_member_count
        if membership_status is not None:
            self.membership_status = membership_status
        if my_member is not None:
            self.my_member = my_member
        self.roles = roles

    @property
    def id(self):
        """Gets the id of this Group.  # noqa: E501


        :return: The id of this Group.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Group.


        :param id: The id of this Group.  # noqa: E501
        :type id: str
        """
        if (self.local_vars_configuration.client_side_validation and
                id is not None and not re.search(r'grp_[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}', id)):  # noqa: E501
            raise ValueError(r"Invalid value for `id`, must be a follow pattern or equal to `/grp_[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}/`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this Group.  # noqa: E501


        :return: The name of this Group.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Group.


        :param name: The name of this Group.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def short_code(self):
        """Gets the short_code of this Group.  # noqa: E501


        :return: The short_code of this Group.  # noqa: E501
        :rtype: str
        """
        return self._short_code

    @short_code.setter
    def short_code(self, short_code):
        """Sets the short_code of this Group.


        :param short_code: The short_code of this Group.  # noqa: E501
        :type short_code: str
        """
        if (self.local_vars_configuration.client_side_validation and
                short_code is not None and not re.search(r'^[A-Z0-9]{3,6}$', short_code)):  # noqa: E501
            raise ValueError(r"Invalid value for `short_code`, must be a follow pattern or equal to `/^[A-Z0-9]{3,6}$/`")  # noqa: E501

        self._short_code = short_code

    @property
    def discriminator(self):
        """Gets the discriminator of this Group.  # noqa: E501


        :return: The discriminator of this Group.  # noqa: E501
        :rtype: str
        """
        return self._discriminator

    @discriminator.setter
    def discriminator(self, discriminator):
        """Sets the discriminator of this Group.


        :param discriminator: The discriminator of this Group.  # noqa: E501
        :type discriminator: str
        """
        if (self.local_vars_configuration.client_side_validation and
                discriminator is not None and not re.search(r'^[0-9]{4}$', discriminator)):  # noqa: E501
            raise ValueError(r"Invalid value for `discriminator`, must be a follow pattern or equal to `/^[0-9]{4}$/`")  # noqa: E501

        self._discriminator = discriminator

    @property
    def description(self):
        """Gets the description of this Group.  # noqa: E501


        :return: The description of this Group.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Group.


        :param description: The description of this Group.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def icon_url(self):
        """Gets the icon_url of this Group.  # noqa: E501


        :return: The icon_url of this Group.  # noqa: E501
        :rtype: str
        """
        return self._icon_url

    @icon_url.setter
    def icon_url(self, icon_url):
        """Sets the icon_url of this Group.


        :param icon_url: The icon_url of this Group.  # noqa: E501
        :type icon_url: str
        """

        self._icon_url = icon_url

    @property
    def banner_url(self):
        """Gets the banner_url of this Group.  # noqa: E501


        :return: The banner_url of this Group.  # noqa: E501
        :rtype: str
        """
        return self._banner_url

    @banner_url.setter
    def banner_url(self, banner_url):
        """Sets the banner_url of this Group.


        :param banner_url: The banner_url of this Group.  # noqa: E501
        :type banner_url: str
        """

        self._banner_url = banner_url

    @property
    def privacy(self):
        """Gets the privacy of this Group.  # noqa: E501


        :return: The privacy of this Group.  # noqa: E501
        :rtype: GroupPrivacy
        """
        return self._privacy

    @privacy.setter
    def privacy(self, privacy):
        """Sets the privacy of this Group.


        :param privacy: The privacy of this Group.  # noqa: E501
        :type privacy: GroupPrivacy
        """

        self._privacy = privacy

    @property
    def owner_id(self):
        """Gets the owner_id of this Group.  # noqa: E501

        A users unique ID, usually in the form of `usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469`. Legacy players can have old IDs in the form of `8JoV9XEdpo`. The ID can never be changed.  # noqa: E501

        :return: The owner_id of this Group.  # noqa: E501
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this Group.

        A users unique ID, usually in the form of `usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469`. Legacy players can have old IDs in the form of `8JoV9XEdpo`. The ID can never be changed.  # noqa: E501

        :param owner_id: The owner_id of this Group.  # noqa: E501
        :type owner_id: str
        """

        self._owner_id = owner_id

    @property
    def rules(self):
        """Gets the rules of this Group.  # noqa: E501


        :return: The rules of this Group.  # noqa: E501
        :rtype: str
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this Group.


        :param rules: The rules of this Group.  # noqa: E501
        :type rules: str
        """

        self._rules = rules

    @property
    def links(self):
        """Gets the links of this Group.  # noqa: E501


        :return: The links of this Group.  # noqa: E501
        :rtype: list[str]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Group.


        :param links: The links of this Group.  # noqa: E501
        :type links: list[str]
        """

        self._links = links

    @property
    def languages(self):
        """Gets the languages of this Group.  # noqa: E501


        :return: The languages of this Group.  # noqa: E501
        :rtype: list[str]
        """
        return self._languages

    @languages.setter
    def languages(self, languages):
        """Sets the languages of this Group.


        :param languages: The languages of this Group.  # noqa: E501
        :type languages: list[str]
        """

        self._languages = languages

    @property
    def icon_id(self):
        """Gets the icon_id of this Group.  # noqa: E501


        :return: The icon_id of this Group.  # noqa: E501
        :rtype: str
        """
        return self._icon_id

    @icon_id.setter
    def icon_id(self, icon_id):
        """Sets the icon_id of this Group.


        :param icon_id: The icon_id of this Group.  # noqa: E501
        :type icon_id: str
        """

        self._icon_id = icon_id

    @property
    def banner_id(self):
        """Gets the banner_id of this Group.  # noqa: E501


        :return: The banner_id of this Group.  # noqa: E501
        :rtype: str
        """
        return self._banner_id

    @banner_id.setter
    def banner_id(self, banner_id):
        """Sets the banner_id of this Group.


        :param banner_id: The banner_id of this Group.  # noqa: E501
        :type banner_id: str
        """

        self._banner_id = banner_id

    @property
    def member_count(self):
        """Gets the member_count of this Group.  # noqa: E501


        :return: The member_count of this Group.  # noqa: E501
        :rtype: int
        """
        return self._member_count

    @member_count.setter
    def member_count(self, member_count):
        """Sets the member_count of this Group.


        :param member_count: The member_count of this Group.  # noqa: E501
        :type member_count: int
        """

        self._member_count = member_count

    @property
    def member_count_synced_at(self):
        """Gets the member_count_synced_at of this Group.  # noqa: E501


        :return: The member_count_synced_at of this Group.  # noqa: E501
        :rtype: datetime
        """
        return self._member_count_synced_at

    @member_count_synced_at.setter
    def member_count_synced_at(self, member_count_synced_at):
        """Sets the member_count_synced_at of this Group.


        :param member_count_synced_at: The member_count_synced_at of this Group.  # noqa: E501
        :type member_count_synced_at: datetime
        """

        self._member_count_synced_at = member_count_synced_at

    @property
    def is_verified(self):
        """Gets the is_verified of this Group.  # noqa: E501


        :return: The is_verified of this Group.  # noqa: E501
        :rtype: bool
        """
        return self._is_verified

    @is_verified.setter
    def is_verified(self, is_verified):
        """Sets the is_verified of this Group.


        :param is_verified: The is_verified of this Group.  # noqa: E501
        :type is_verified: bool
        """

        self._is_verified = is_verified

    @property
    def join_state(self):
        """Gets the join_state of this Group.  # noqa: E501


        :return: The join_state of this Group.  # noqa: E501
        :rtype: GroupJoinState
        """
        return self._join_state

    @join_state.setter
    def join_state(self, join_state):
        """Sets the join_state of this Group.


        :param join_state: The join_state of this Group.  # noqa: E501
        :type join_state: GroupJoinState
        """

        self._join_state = join_state

    @property
    def tags(self):
        """Gets the tags of this Group.  # noqa: E501

           # noqa: E501

        :return: The tags of this Group.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Group.

           # noqa: E501

        :param tags: The tags of this Group.  # noqa: E501
        :type tags: list[str]
        """

        self._tags = tags

    @property
    def galleries(self):
        """Gets the galleries of this Group.  # noqa: E501

           # noqa: E501

        :return: The galleries of this Group.  # noqa: E501
        :rtype: list[GroupGallery]
        """
        return self._galleries

    @galleries.setter
    def galleries(self, galleries):
        """Sets the galleries of this Group.

           # noqa: E501

        :param galleries: The galleries of this Group.  # noqa: E501
        :type galleries: list[GroupGallery]
        """

        self._galleries = galleries

    @property
    def created_at(self):
        """Gets the created_at of this Group.  # noqa: E501


        :return: The created_at of this Group.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Group.


        :param created_at: The created_at of this Group.  # noqa: E501
        :type created_at: datetime
        """

        self._created_at = created_at

    @property
    def online_member_count(self):
        """Gets the online_member_count of this Group.  # noqa: E501


        :return: The online_member_count of this Group.  # noqa: E501
        :rtype: int
        """
        return self._online_member_count

    @online_member_count.setter
    def online_member_count(self, online_member_count):
        """Sets the online_member_count of this Group.


        :param online_member_count: The online_member_count of this Group.  # noqa: E501
        :type online_member_count: int
        """

        self._online_member_count = online_member_count

    @property
    def membership_status(self):
        """Gets the membership_status of this Group.  # noqa: E501


        :return: The membership_status of this Group.  # noqa: E501
        :rtype: GroupMemberStatus
        """
        return self._membership_status

    @membership_status.setter
    def membership_status(self, membership_status):
        """Sets the membership_status of this Group.


        :param membership_status: The membership_status of this Group.  # noqa: E501
        :type membership_status: GroupMemberStatus
        """

        self._membership_status = membership_status

    @property
    def my_member(self):
        """Gets the my_member of this Group.  # noqa: E501


        :return: The my_member of this Group.  # noqa: E501
        :rtype: GroupMyMember
        """
        return self._my_member

    @my_member.setter
    def my_member(self, my_member):
        """Sets the my_member of this Group.


        :param my_member: The my_member of this Group.  # noqa: E501
        :type my_member: GroupMyMember
        """

        self._my_member = my_member

    @property
    def roles(self):
        """Gets the roles of this Group.  # noqa: E501

        Only returned if ?includeRoles=true is specified.  # noqa: E501

        :return: The roles of this Group.  # noqa: E501
        :rtype: list[GroupRole]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this Group.

        Only returned if ?includeRoles=true is specified.  # noqa: E501

        :param roles: The roles of this Group.  # noqa: E501
        :type roles: list[GroupRole]
        """

        self._roles = roles

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
        if not isinstance(other, Group):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Group):
            return True

        return self.to_dict() != other.to_dict()
