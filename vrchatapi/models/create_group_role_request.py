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


class CreateGroupRoleRequest(object):
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
        'description': 'str',
        'is_self_assignable': 'bool',
        'permissions': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'is_self_assignable': 'isSelfAssignable',
        'permissions': 'permissions'
    }

    def __init__(self, id=None, name=None, description=None, is_self_assignable=False, permissions=None, local_vars_configuration=None):  # noqa: E501
        """CreateGroupRoleRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._description = None
        self._is_self_assignable = None
        self._permissions = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if is_self_assignable is not None:
            self.is_self_assignable = is_self_assignable
        if permissions is not None:
            self.permissions = permissions

    @property
    def id(self):
        """Gets the id of this CreateGroupRoleRequest.  # noqa: E501


        :return: The id of this CreateGroupRoleRequest.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateGroupRoleRequest.


        :param id: The id of this CreateGroupRoleRequest.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this CreateGroupRoleRequest.  # noqa: E501


        :return: The name of this CreateGroupRoleRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateGroupRoleRequest.


        :param name: The name of this CreateGroupRoleRequest.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateGroupRoleRequest.  # noqa: E501


        :return: The description of this CreateGroupRoleRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateGroupRoleRequest.


        :param description: The description of this CreateGroupRoleRequest.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def is_self_assignable(self):
        """Gets the is_self_assignable of this CreateGroupRoleRequest.  # noqa: E501


        :return: The is_self_assignable of this CreateGroupRoleRequest.  # noqa: E501
        :rtype: bool
        """
        return self._is_self_assignable

    @is_self_assignable.setter
    def is_self_assignable(self, is_self_assignable):
        """Sets the is_self_assignable of this CreateGroupRoleRequest.


        :param is_self_assignable: The is_self_assignable of this CreateGroupRoleRequest.  # noqa: E501
        :type is_self_assignable: bool
        """

        self._is_self_assignable = is_self_assignable

    @property
    def permissions(self):
        """Gets the permissions of this CreateGroupRoleRequest.  # noqa: E501


        :return: The permissions of this CreateGroupRoleRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this CreateGroupRoleRequest.


        :param permissions: The permissions of this CreateGroupRoleRequest.  # noqa: E501
        :type permissions: list[str]
        """

        self._permissions = permissions

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
        if not isinstance(other, CreateGroupRoleRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateGroupRoleRequest):
            return True

        return self.to_dict() != other.to_dict()
