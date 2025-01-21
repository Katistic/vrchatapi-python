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


class GroupPermissions(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    group_all = "*"
    group_announcement_manage = "group-announcement-manage"
    group_audit_view = "group-audit-view"
    group_bans_manage = "group-bans-manage"
    group_data_manage = "group-data-manage"
    group_default_role_manage = "group-default-role-manage"
    group_galleries_manage = "group-galleries-manage"
    group_instance_age_gated_create = "group-instance-age-gated-create"
    group_instance_join = "group-instance-join"
    group_instance_manage = "group-instance-manage"
    group_instance_moderate = "group-instance-moderate"
    group_instance_open_create = "group-instance-open-create"
    group_instance_plus_create = "group-instance-plus-create"
    group_instance_plus_portal = "group-instance-plus-portal"
    group_instance_plus_portal_unlocked = "group-instance-plus-portal-unlocked"
    group_instance_public_create = "group-instance-public-create"
    group_instance_queue_priority = "group-instance-queue-priority"
    group_instance_restricted_create = "group-instance-restricted-create"
    group_invites_manage = "group-invites-manage"
    group_members_manage = "group-members-manage"
    group_members_remove = "group-members-remove"
    group_members_viewall = "group-members-viewall"
    group_roles_assign = "group-roles-assign"
    group_roles_manage = "group-roles-manage"

    allowable_values = [group_all, group_announcement_manage, group_audit_view, group_bans_manage, group_data_manage, group_default_role_manage, group_galleries_manage, group_instance_age_gated_create, group_instance_join, group_instance_manage, group_instance_moderate, group_instance_open_create, group_instance_plus_create, group_instance_plus_portal, group_instance_plus_portal_unlocked, group_instance_public_create, group_instance_queue_priority, group_instance_restricted_create, group_invites_manage, group_members_manage, group_members_remove, group_members_viewall, group_roles_assign, group_roles_manage]  # noqa: E501

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
    }

    attribute_map = {
    }

    def __init__(self, local_vars_configuration=None):  # noqa: E501
        """GroupPermissions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration
        self.discriminator = None

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
        if not isinstance(other, GroupPermissions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GroupPermissions):
            return True

        return self.to_dict() != other.to_dict()
