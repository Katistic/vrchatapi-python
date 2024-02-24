# coding: utf-8

"""
    VRChat API Documentation


    The version of the OpenAPI document: 1.16.6
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


class UpdateUserRequest(object):
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
        'email': 'str',
        'birthday': 'date',
        'accepted_tos_version': 'float',
        'tags': 'list[str]',
        'status': 'UserStatus',
        'status_description': 'str',
        'bio': 'str',
        'bio_links': 'list[str]',
        'user_icon': 'str'
    }

    attribute_map = {
        'email': 'email',
        'birthday': 'birthday',
        'accepted_tos_version': 'acceptedTOSVersion',
        'tags': 'tags',
        'status': 'status',
        'status_description': 'statusDescription',
        'bio': 'bio',
        'bio_links': 'bioLinks',
        'user_icon': 'userIcon'
    }

    def __init__(self, email=None, birthday=None, accepted_tos_version=None, tags=None, status=None, status_description=None, bio=None, bio_links=None, user_icon=None, local_vars_configuration=None):  # noqa: E501
        """UpdateUserRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._email = None
        self._birthday = None
        self._accepted_tos_version = None
        self._tags = None
        self._status = None
        self._status_description = None
        self._bio = None
        self._bio_links = None
        self._user_icon = None
        self.discriminator = None

        if email is not None:
            self.email = email
        if birthday is not None:
            self.birthday = birthday
        if accepted_tos_version is not None:
            self.accepted_tos_version = accepted_tos_version
        if tags is not None:
            self.tags = tags
        if status is not None:
            self.status = status
        if status_description is not None:
            self.status_description = status_description
        if bio is not None:
            self.bio = bio
        if bio_links is not None:
            self.bio_links = bio_links
        if user_icon is not None:
            self.user_icon = user_icon

    @property
    def email(self):
        """Gets the email of this UpdateUserRequest.  # noqa: E501


        :return: The email of this UpdateUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UpdateUserRequest.


        :param email: The email of this UpdateUserRequest.  # noqa: E501
        :type email: str
        """

        self._email = email

    @property
    def birthday(self):
        """Gets the birthday of this UpdateUserRequest.  # noqa: E501


        :return: The birthday of this UpdateUserRequest.  # noqa: E501
        :rtype: date
        """
        return self._birthday

    @birthday.setter
    def birthday(self, birthday):
        """Sets the birthday of this UpdateUserRequest.


        :param birthday: The birthday of this UpdateUserRequest.  # noqa: E501
        :type birthday: date
        """

        self._birthday = birthday

    @property
    def accepted_tos_version(self):
        """Gets the accepted_tos_version of this UpdateUserRequest.  # noqa: E501


        :return: The accepted_tos_version of this UpdateUserRequest.  # noqa: E501
        :rtype: float
        """
        return self._accepted_tos_version

    @accepted_tos_version.setter
    def accepted_tos_version(self, accepted_tos_version):
        """Sets the accepted_tos_version of this UpdateUserRequest.


        :param accepted_tos_version: The accepted_tos_version of this UpdateUserRequest.  # noqa: E501
        :type accepted_tos_version: float
        """

        self._accepted_tos_version = accepted_tos_version

    @property
    def tags(self):
        """Gets the tags of this UpdateUserRequest.  # noqa: E501

           # noqa: E501

        :return: The tags of this UpdateUserRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this UpdateUserRequest.

           # noqa: E501

        :param tags: The tags of this UpdateUserRequest.  # noqa: E501
        :type tags: list[str]
        """

        self._tags = tags

    @property
    def status(self):
        """Gets the status of this UpdateUserRequest.  # noqa: E501


        :return: The status of this UpdateUserRequest.  # noqa: E501
        :rtype: UserStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UpdateUserRequest.


        :param status: The status of this UpdateUserRequest.  # noqa: E501
        :type status: UserStatus
        """

        self._status = status

    @property
    def status_description(self):
        """Gets the status_description of this UpdateUserRequest.  # noqa: E501


        :return: The status_description of this UpdateUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._status_description

    @status_description.setter
    def status_description(self, status_description):
        """Sets the status_description of this UpdateUserRequest.


        :param status_description: The status_description of this UpdateUserRequest.  # noqa: E501
        :type status_description: str
        """

        self._status_description = status_description

    @property
    def bio(self):
        """Gets the bio of this UpdateUserRequest.  # noqa: E501


        :return: The bio of this UpdateUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._bio

    @bio.setter
    def bio(self, bio):
        """Sets the bio of this UpdateUserRequest.


        :param bio: The bio of this UpdateUserRequest.  # noqa: E501
        :type bio: str
        """
        if (self.local_vars_configuration.client_side_validation and
                bio is not None and len(bio) < 0):
            raise ValueError("Invalid value for `bio`, length must be greater than or equal to `0`")  # noqa: E501

        self._bio = bio

    @property
    def bio_links(self):
        """Gets the bio_links of this UpdateUserRequest.  # noqa: E501


        :return: The bio_links of this UpdateUserRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._bio_links

    @bio_links.setter
    def bio_links(self, bio_links):
        """Sets the bio_links of this UpdateUserRequest.


        :param bio_links: The bio_links of this UpdateUserRequest.  # noqa: E501
        :type bio_links: list[str]
        """

        self._bio_links = bio_links

    @property
    def user_icon(self):
        """Gets the user_icon of this UpdateUserRequest.  # noqa: E501

        MUST be a valid VRChat /file/ url.  # noqa: E501

        :return: The user_icon of this UpdateUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._user_icon

    @user_icon.setter
    def user_icon(self, user_icon):
        """Sets the user_icon of this UpdateUserRequest.

        MUST be a valid VRChat /file/ url.  # noqa: E501

        :param user_icon: The user_icon of this UpdateUserRequest.  # noqa: E501
        :type user_icon: str
        """
        if (self.local_vars_configuration.client_side_validation and
                user_icon is not None and len(user_icon) < 0):
            raise ValueError("Invalid value for `user_icon`, length must be greater than or equal to `0`")  # noqa: E501

        self._user_icon = user_icon

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
        if not isinstance(other, UpdateUserRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateUserRequest):
            return True

        return self.to_dict() != other.to_dict()
