# coding: utf-8

"""
    VRChat API Documentation


    The version of the OpenAPI document: 1.18.7
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


class RespondGroupJoinRequest(object):
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
        'action': 'GroupJoinRequestAction',
        'block': 'bool'
    }

    attribute_map = {
        'action': 'action',
        'block': 'block'
    }

    def __init__(self, action=None, block=None, local_vars_configuration=None):  # noqa: E501
        """RespondGroupJoinRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._action = None
        self._block = None
        self.discriminator = None

        self.action = action
        if block is not None:
            self.block = block

    @property
    def action(self):
        """Gets the action of this RespondGroupJoinRequest.  # noqa: E501


        :return: The action of this RespondGroupJoinRequest.  # noqa: E501
        :rtype: GroupJoinRequestAction
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this RespondGroupJoinRequest.


        :param action: The action of this RespondGroupJoinRequest.  # noqa: E501
        :type action: GroupJoinRequestAction
        """
        if self.local_vars_configuration.client_side_validation and action is None:  # noqa: E501
            raise ValueError("Invalid value for `action`, must not be `None`")  # noqa: E501

        self._action = action

    @property
    def block(self):
        """Gets the block of this RespondGroupJoinRequest.  # noqa: E501

        Whether to block the user from requesting again  # noqa: E501

        :return: The block of this RespondGroupJoinRequest.  # noqa: E501
        :rtype: bool
        """
        return self._block

    @block.setter
    def block(self, block):
        """Sets the block of this RespondGroupJoinRequest.

        Whether to block the user from requesting again  # noqa: E501

        :param block: The block of this RespondGroupJoinRequest.  # noqa: E501
        :type block: bool
        """

        self._block = block

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
        if not isinstance(other, RespondGroupJoinRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RespondGroupJoinRequest):
            return True

        return self.to_dict() != other.to_dict()
