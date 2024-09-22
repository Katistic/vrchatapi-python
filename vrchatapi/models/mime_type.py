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


class MIMEType(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    IMAGE_JPEG = "image/jpeg"
    IMAGE_JPG = "image/jpg"
    IMAGE_PNG = "image/png"
    IMAGE_WEBP = "image/webp"
    IMAGE_GIF = "image/gif"
    IMAGE_BMP = "image/bmp"
    IMAGE_SVG_XML = "image/svg＋xml"
    IMAGE_TIFF = "image/tiff"
    APPLICATION_X_AVATAR = "application/x-avatar"
    APPLICATION_X_WORLD = "application/x-world"
    APPLICATION_GZIP = "application/gzip"
    APPLICATION_X_RSYNC_SIGNATURE = "application/x-rsync-signature"
    APPLICATION_X_RSYNC_DELTA = "application/x-rsync-delta"
    APPLICATION_OCTET_STREAM = "application/octet-stream"

    allowable_values = [IMAGE_JPEG, IMAGE_JPG, IMAGE_PNG, IMAGE_WEBP, IMAGE_GIF, IMAGE_BMP, IMAGE_SVG_XML, IMAGE_TIFF, APPLICATION_X_AVATAR, APPLICATION_X_WORLD, APPLICATION_GZIP, APPLICATION_X_RSYNC_SIGNATURE, APPLICATION_X_RSYNC_DELTA, APPLICATION_OCTET_STREAM]  # noqa: E501

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
        """MIMEType - a model defined in OpenAPI"""  # noqa: E501
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
        if not isinstance(other, MIMEType):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MIMEType):
            return True

        return self.to_dict() != other.to_dict()
