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


class LimitedUser(object):
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
        'bio': 'str',
        'current_avatar_image_url': 'str',
        'current_avatar_thumbnail_image_url': 'str',
        'developer_type': 'DeveloperType',
        'display_name': 'str',
        'fallback_avatar': 'str',
        'id': 'str',
        'is_friend': 'bool',
        'last_platform': 'str',
        'profile_pic_override': 'str',
        'status': 'UserStatus',
        'status_description': 'str',
        'tags': 'list[str]',
        'user_icon': 'str',
        'username': 'str',
        'location': 'str',
        'friend_key': 'str'
    }

    attribute_map = {
        'bio': 'bio',
        'current_avatar_image_url': 'currentAvatarImageUrl',
        'current_avatar_thumbnail_image_url': 'currentAvatarThumbnailImageUrl',
        'developer_type': 'developerType',
        'display_name': 'displayName',
        'fallback_avatar': 'fallbackAvatar',
        'id': 'id',
        'is_friend': 'isFriend',
        'last_platform': 'last_platform',
        'profile_pic_override': 'profilePicOverride',
        'status': 'status',
        'status_description': 'statusDescription',
        'tags': 'tags',
        'user_icon': 'userIcon',
        'username': 'username',
        'location': 'location',
        'friend_key': 'friendKey'
    }

    def __init__(self, bio=None, current_avatar_image_url=None, current_avatar_thumbnail_image_url=None, developer_type=None, display_name=None, fallback_avatar=None, id=None, is_friend=None, last_platform=None, profile_pic_override=None, status=None, status_description=None, tags=None, user_icon=None, username=None, location=None, friend_key=None, local_vars_configuration=None):  # noqa: E501
        """LimitedUser - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._bio = None
        self._current_avatar_image_url = None
        self._current_avatar_thumbnail_image_url = None
        self._developer_type = None
        self._display_name = None
        self._fallback_avatar = None
        self._id = None
        self._is_friend = None
        self._last_platform = None
        self._profile_pic_override = None
        self._status = None
        self._status_description = None
        self._tags = None
        self._user_icon = None
        self._username = None
        self._location = None
        self._friend_key = None
        self.discriminator = None

        if bio is not None:
            self.bio = bio
        if current_avatar_image_url is not None:
            self.current_avatar_image_url = current_avatar_image_url
        if current_avatar_thumbnail_image_url is not None:
            self.current_avatar_thumbnail_image_url = current_avatar_thumbnail_image_url
        self.developer_type = developer_type
        self.display_name = display_name
        if fallback_avatar is not None:
            self.fallback_avatar = fallback_avatar
        self.id = id
        self.is_friend = is_friend
        self.last_platform = last_platform
        if profile_pic_override is not None:
            self.profile_pic_override = profile_pic_override
        self.status = status
        self.status_description = status_description
        self.tags = tags
        if user_icon is not None:
            self.user_icon = user_icon
        if username is not None:
            self.username = username
        if location is not None:
            self.location = location
        if friend_key is not None:
            self.friend_key = friend_key

    @property
    def bio(self):
        """Gets the bio of this LimitedUser.  # noqa: E501


        :return: The bio of this LimitedUser.  # noqa: E501
        :rtype: str
        """
        return self._bio

    @bio.setter
    def bio(self, bio):
        """Sets the bio of this LimitedUser.


        :param bio: The bio of this LimitedUser.  # noqa: E501
        :type bio: str
        """

        self._bio = bio

    @property
    def current_avatar_image_url(self):
        """Gets the current_avatar_image_url of this LimitedUser.  # noqa: E501

        When profilePicOverride is not empty, use it instead.  # noqa: E501

        :return: The current_avatar_image_url of this LimitedUser.  # noqa: E501
        :rtype: str
        """
        return self._current_avatar_image_url

    @current_avatar_image_url.setter
    def current_avatar_image_url(self, current_avatar_image_url):
        """Sets the current_avatar_image_url of this LimitedUser.

        When profilePicOverride is not empty, use it instead.  # noqa: E501

        :param current_avatar_image_url: The current_avatar_image_url of this LimitedUser.  # noqa: E501
        :type current_avatar_image_url: str
        """

        self._current_avatar_image_url = current_avatar_image_url

    @property
    def current_avatar_thumbnail_image_url(self):
        """Gets the current_avatar_thumbnail_image_url of this LimitedUser.  # noqa: E501

        When profilePicOverride is not empty, use it instead.  # noqa: E501

        :return: The current_avatar_thumbnail_image_url of this LimitedUser.  # noqa: E501
        :rtype: str
        """
        return self._current_avatar_thumbnail_image_url

    @current_avatar_thumbnail_image_url.setter
    def current_avatar_thumbnail_image_url(self, current_avatar_thumbnail_image_url):
        """Sets the current_avatar_thumbnail_image_url of this LimitedUser.

        When profilePicOverride is not empty, use it instead.  # noqa: E501

        :param current_avatar_thumbnail_image_url: The current_avatar_thumbnail_image_url of this LimitedUser.  # noqa: E501
        :type current_avatar_thumbnail_image_url: str
        """

        self._current_avatar_thumbnail_image_url = current_avatar_thumbnail_image_url

    @property
    def developer_type(self):
        """Gets the developer_type of this LimitedUser.  # noqa: E501


        :return: The developer_type of this LimitedUser.  # noqa: E501
        :rtype: DeveloperType
        """
        return self._developer_type

    @developer_type.setter
    def developer_type(self, developer_type):
        """Sets the developer_type of this LimitedUser.


        :param developer_type: The developer_type of this LimitedUser.  # noqa: E501
        :type developer_type: DeveloperType
        """
        if self.local_vars_configuration.client_side_validation and developer_type is None:  # noqa: E501
            raise ValueError("Invalid value for `developer_type`, must not be `None`")  # noqa: E501

        self._developer_type = developer_type

    @property
    def display_name(self):
        """Gets the display_name of this LimitedUser.  # noqa: E501


        :return: The display_name of this LimitedUser.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this LimitedUser.


        :param display_name: The display_name of this LimitedUser.  # noqa: E501
        :type display_name: str
        """
        if self.local_vars_configuration.client_side_validation and display_name is None:  # noqa: E501
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name

    @property
    def fallback_avatar(self):
        """Gets the fallback_avatar of this LimitedUser.  # noqa: E501


        :return: The fallback_avatar of this LimitedUser.  # noqa: E501
        :rtype: str
        """
        return self._fallback_avatar

    @fallback_avatar.setter
    def fallback_avatar(self, fallback_avatar):
        """Sets the fallback_avatar of this LimitedUser.


        :param fallback_avatar: The fallback_avatar of this LimitedUser.  # noqa: E501
        :type fallback_avatar: str
        """

        self._fallback_avatar = fallback_avatar

    @property
    def id(self):
        """Gets the id of this LimitedUser.  # noqa: E501

        A users unique ID, usually in the form of `usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469`. Legacy players can have old IDs in the form of `8JoV9XEdpo`. The ID can never be changed.  # noqa: E501

        :return: The id of this LimitedUser.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LimitedUser.

        A users unique ID, usually in the form of `usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469`. Legacy players can have old IDs in the form of `8JoV9XEdpo`. The ID can never be changed.  # noqa: E501

        :param id: The id of this LimitedUser.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def is_friend(self):
        """Gets the is_friend of this LimitedUser.  # noqa: E501


        :return: The is_friend of this LimitedUser.  # noqa: E501
        :rtype: bool
        """
        return self._is_friend

    @is_friend.setter
    def is_friend(self, is_friend):
        """Sets the is_friend of this LimitedUser.


        :param is_friend: The is_friend of this LimitedUser.  # noqa: E501
        :type is_friend: bool
        """
        if self.local_vars_configuration.client_side_validation and is_friend is None:  # noqa: E501
            raise ValueError("Invalid value for `is_friend`, must not be `None`")  # noqa: E501

        self._is_friend = is_friend

    @property
    def last_platform(self):
        """Gets the last_platform of this LimitedUser.  # noqa: E501

        This can be `standalonewindows` or `android`, but can also pretty much be any random Unity verison such as `2019.2.4-801-Release` or `2019.2.2-772-Release` or even `unknownplatform`.  # noqa: E501

        :return: The last_platform of this LimitedUser.  # noqa: E501
        :rtype: str
        """
        return self._last_platform

    @last_platform.setter
    def last_platform(self, last_platform):
        """Sets the last_platform of this LimitedUser.

        This can be `standalonewindows` or `android`, but can also pretty much be any random Unity verison such as `2019.2.4-801-Release` or `2019.2.2-772-Release` or even `unknownplatform`.  # noqa: E501

        :param last_platform: The last_platform of this LimitedUser.  # noqa: E501
        :type last_platform: str
        """
        if self.local_vars_configuration.client_side_validation and last_platform is None:  # noqa: E501
            raise ValueError("Invalid value for `last_platform`, must not be `None`")  # noqa: E501

        self._last_platform = last_platform

    @property
    def profile_pic_override(self):
        """Gets the profile_pic_override of this LimitedUser.  # noqa: E501


        :return: The profile_pic_override of this LimitedUser.  # noqa: E501
        :rtype: str
        """
        return self._profile_pic_override

    @profile_pic_override.setter
    def profile_pic_override(self, profile_pic_override):
        """Sets the profile_pic_override of this LimitedUser.


        :param profile_pic_override: The profile_pic_override of this LimitedUser.  # noqa: E501
        :type profile_pic_override: str
        """

        self._profile_pic_override = profile_pic_override

    @property
    def status(self):
        """Gets the status of this LimitedUser.  # noqa: E501


        :return: The status of this LimitedUser.  # noqa: E501
        :rtype: UserStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this LimitedUser.


        :param status: The status of this LimitedUser.  # noqa: E501
        :type status: UserStatus
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def status_description(self):
        """Gets the status_description of this LimitedUser.  # noqa: E501


        :return: The status_description of this LimitedUser.  # noqa: E501
        :rtype: str
        """
        return self._status_description

    @status_description.setter
    def status_description(self, status_description):
        """Sets the status_description of this LimitedUser.


        :param status_description: The status_description of this LimitedUser.  # noqa: E501
        :type status_description: str
        """
        if self.local_vars_configuration.client_side_validation and status_description is None:  # noqa: E501
            raise ValueError("Invalid value for `status_description`, must not be `None`")  # noqa: E501

        self._status_description = status_description

    @property
    def tags(self):
        """Gets the tags of this LimitedUser.  # noqa: E501

        <- Always empty.  # noqa: E501

        :return: The tags of this LimitedUser.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this LimitedUser.

        <- Always empty.  # noqa: E501

        :param tags: The tags of this LimitedUser.  # noqa: E501
        :type tags: list[str]
        """
        if self.local_vars_configuration.client_side_validation and tags is None:  # noqa: E501
            raise ValueError("Invalid value for `tags`, must not be `None`")  # noqa: E501

        self._tags = tags

    @property
    def user_icon(self):
        """Gets the user_icon of this LimitedUser.  # noqa: E501


        :return: The user_icon of this LimitedUser.  # noqa: E501
        :rtype: str
        """
        return self._user_icon

    @user_icon.setter
    def user_icon(self, user_icon):
        """Sets the user_icon of this LimitedUser.


        :param user_icon: The user_icon of this LimitedUser.  # noqa: E501
        :type user_icon: str
        """

        self._user_icon = user_icon

    @property
    def username(self):
        """Gets the username of this LimitedUser.  # noqa: E501

        -| **DEPRECATED:** VRChat API no longer return usernames of other users. [See issue by Tupper for more information](https://github.com/pypy-vrc/VRCX/issues/429).  # noqa: E501

        :return: The username of this LimitedUser.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this LimitedUser.

        -| **DEPRECATED:** VRChat API no longer return usernames of other users. [See issue by Tupper for more information](https://github.com/pypy-vrc/VRCX/issues/429).  # noqa: E501

        :param username: The username of this LimitedUser.  # noqa: E501
        :type username: str
        """

        self._username = username

    @property
    def location(self):
        """Gets the location of this LimitedUser.  # noqa: E501


        :return: The location of this LimitedUser.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this LimitedUser.


        :param location: The location of this LimitedUser.  # noqa: E501
        :type location: str
        """

        self._location = location

    @property
    def friend_key(self):
        """Gets the friend_key of this LimitedUser.  # noqa: E501


        :return: The friend_key of this LimitedUser.  # noqa: E501
        :rtype: str
        """
        return self._friend_key

    @friend_key.setter
    def friend_key(self, friend_key):
        """Sets the friend_key of this LimitedUser.


        :param friend_key: The friend_key of this LimitedUser.  # noqa: E501
        :type friend_key: str
        """

        self._friend_key = friend_key

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
        if not isinstance(other, LimitedUser):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LimitedUser):
            return True

        return self.to_dict() != other.to_dict()
