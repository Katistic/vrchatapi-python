# coding: utf-8

"""
    VRChat API Documentation


    The version of the OpenAPI document: 1.16.4
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


class UpdateAvatarRequest(object):
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
        'asset_url': 'str',
        'id': 'str',
        'name': 'str',
        'description': 'str',
        'tags': 'list[str]',
        'image_url': 'str',
        'release_status': 'ReleaseStatus',
        'version': 'float',
        'unity_package_url': 'str'
    }

    attribute_map = {
        'asset_url': 'assetUrl',
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'tags': 'tags',
        'image_url': 'imageUrl',
        'release_status': 'releaseStatus',
        'version': 'version',
        'unity_package_url': 'unityPackageUrl'
    }

    def __init__(self, asset_url=None, id=None, name=None, description=None, tags=None, image_url=None, release_status=None, version=1, unity_package_url=None, local_vars_configuration=None):  # noqa: E501
        """UpdateAvatarRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._asset_url = None
        self._id = None
        self._name = None
        self._description = None
        self._tags = None
        self._image_url = None
        self._release_status = None
        self._version = None
        self._unity_package_url = None
        self.discriminator = None

        if asset_url is not None:
            self.asset_url = asset_url
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if tags is not None:
            self.tags = tags
        if image_url is not None:
            self.image_url = image_url
        if release_status is not None:
            self.release_status = release_status
        if version is not None:
            self.version = version
        if unity_package_url is not None:
            self.unity_package_url = unity_package_url

    @property
    def asset_url(self):
        """Gets the asset_url of this UpdateAvatarRequest.  # noqa: E501


        :return: The asset_url of this UpdateAvatarRequest.  # noqa: E501
        :rtype: str
        """
        return self._asset_url

    @asset_url.setter
    def asset_url(self, asset_url):
        """Sets the asset_url of this UpdateAvatarRequest.


        :param asset_url: The asset_url of this UpdateAvatarRequest.  # noqa: E501
        :type asset_url: str
        """

        self._asset_url = asset_url

    @property
    def id(self):
        """Gets the id of this UpdateAvatarRequest.  # noqa: E501


        :return: The id of this UpdateAvatarRequest.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdateAvatarRequest.


        :param id: The id of this UpdateAvatarRequest.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this UpdateAvatarRequest.  # noqa: E501


        :return: The name of this UpdateAvatarRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateAvatarRequest.


        :param name: The name of this UpdateAvatarRequest.  # noqa: E501
        :type name: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this UpdateAvatarRequest.  # noqa: E501


        :return: The description of this UpdateAvatarRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateAvatarRequest.


        :param description: The description of this UpdateAvatarRequest.  # noqa: E501
        :type description: str
        """
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) < 1):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `1`")  # noqa: E501

        self._description = description

    @property
    def tags(self):
        """Gets the tags of this UpdateAvatarRequest.  # noqa: E501

           # noqa: E501

        :return: The tags of this UpdateAvatarRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this UpdateAvatarRequest.

           # noqa: E501

        :param tags: The tags of this UpdateAvatarRequest.  # noqa: E501
        :type tags: list[str]
        """

        self._tags = tags

    @property
    def image_url(self):
        """Gets the image_url of this UpdateAvatarRequest.  # noqa: E501


        :return: The image_url of this UpdateAvatarRequest.  # noqa: E501
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """Sets the image_url of this UpdateAvatarRequest.


        :param image_url: The image_url of this UpdateAvatarRequest.  # noqa: E501
        :type image_url: str
        """
        if (self.local_vars_configuration.client_side_validation and
                image_url is not None and len(image_url) < 1):
            raise ValueError("Invalid value for `image_url`, length must be greater than or equal to `1`")  # noqa: E501

        self._image_url = image_url

    @property
    def release_status(self):
        """Gets the release_status of this UpdateAvatarRequest.  # noqa: E501


        :return: The release_status of this UpdateAvatarRequest.  # noqa: E501
        :rtype: ReleaseStatus
        """
        return self._release_status

    @release_status.setter
    def release_status(self, release_status):
        """Sets the release_status of this UpdateAvatarRequest.


        :param release_status: The release_status of this UpdateAvatarRequest.  # noqa: E501
        :type release_status: ReleaseStatus
        """

        self._release_status = release_status

    @property
    def version(self):
        """Gets the version of this UpdateAvatarRequest.  # noqa: E501


        :return: The version of this UpdateAvatarRequest.  # noqa: E501
        :rtype: float
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this UpdateAvatarRequest.


        :param version: The version of this UpdateAvatarRequest.  # noqa: E501
        :type version: float
        """
        if (self.local_vars_configuration.client_side_validation and
                version is not None and version < 0):  # noqa: E501
            raise ValueError("Invalid value for `version`, must be a value greater than or equal to `0`")  # noqa: E501

        self._version = version

    @property
    def unity_package_url(self):
        """Gets the unity_package_url of this UpdateAvatarRequest.  # noqa: E501


        :return: The unity_package_url of this UpdateAvatarRequest.  # noqa: E501
        :rtype: str
        """
        return self._unity_package_url

    @unity_package_url.setter
    def unity_package_url(self, unity_package_url):
        """Sets the unity_package_url of this UpdateAvatarRequest.


        :param unity_package_url: The unity_package_url of this UpdateAvatarRequest.  # noqa: E501
        :type unity_package_url: str
        """

        self._unity_package_url = unity_package_url

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
        if not isinstance(other, UpdateAvatarRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateAvatarRequest):
            return True

        return self.to_dict() != other.to_dict()
