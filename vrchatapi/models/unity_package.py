# coding: utf-8

"""
    VRChat API Documentation


    The version of the OpenAPI document: 1.18.8
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


class UnityPackage(object):
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
        'asset_url': 'str',
        'asset_url_object': 'object',
        'asset_version': 'int',
        'created_at': 'datetime',
        'impostorizer_version': 'str',
        'performance_rating': 'PerformanceRatings',
        'platform': 'str',
        'plugin_url': 'str',
        'plugin_url_object': 'object',
        'unity_sort_number': 'int',
        'unity_version': 'str',
        'world_signature': 'str',
        'impostor_url': 'str',
        'scan_status': 'str',
        'variant': 'str'
    }

    attribute_map = {
        'id': 'id',
        'asset_url': 'assetUrl',
        'asset_url_object': 'assetUrlObject',
        'asset_version': 'assetVersion',
        'created_at': 'created_at',
        'impostorizer_version': 'impostorizerVersion',
        'performance_rating': 'performanceRating',
        'platform': 'platform',
        'plugin_url': 'pluginUrl',
        'plugin_url_object': 'pluginUrlObject',
        'unity_sort_number': 'unitySortNumber',
        'unity_version': 'unityVersion',
        'world_signature': 'worldSignature',
        'impostor_url': 'impostorUrl',
        'scan_status': 'scanStatus',
        'variant': 'variant'
    }

    def __init__(self, id=None, asset_url=None, asset_url_object=None, asset_version=None, created_at=None, impostorizer_version=None, performance_rating=None, platform=None, plugin_url=None, plugin_url_object=None, unity_sort_number=None, unity_version='5.3.4p1', world_signature=None, impostor_url=None, scan_status=None, variant=None, local_vars_configuration=None):  # noqa: E501
        """UnityPackage - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._asset_url = None
        self._asset_url_object = None
        self._asset_version = None
        self._created_at = None
        self._impostorizer_version = None
        self._performance_rating = None
        self._platform = None
        self._plugin_url = None
        self._plugin_url_object = None
        self._unity_sort_number = None
        self._unity_version = None
        self._world_signature = None
        self._impostor_url = None
        self._scan_status = None
        self._variant = None
        self.discriminator = None

        self.id = id
        self.asset_url = asset_url
        if asset_url_object is not None:
            self.asset_url_object = asset_url_object
        self.asset_version = asset_version
        if created_at is not None:
            self.created_at = created_at
        if impostorizer_version is not None:
            self.impostorizer_version = impostorizer_version
        if performance_rating is not None:
            self.performance_rating = performance_rating
        self.platform = platform
        if plugin_url is not None:
            self.plugin_url = plugin_url
        if plugin_url_object is not None:
            self.plugin_url_object = plugin_url_object
        if unity_sort_number is not None:
            self.unity_sort_number = unity_sort_number
        self.unity_version = unity_version
        self.world_signature = world_signature
        self.impostor_url = impostor_url
        if scan_status is not None:
            self.scan_status = scan_status
        if variant is not None:
            self.variant = variant

    @property
    def id(self):
        """Gets the id of this UnityPackage.  # noqa: E501


        :return: The id of this UnityPackage.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UnityPackage.


        :param id: The id of this UnityPackage.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def asset_url(self):
        """Gets the asset_url of this UnityPackage.  # noqa: E501


        :return: The asset_url of this UnityPackage.  # noqa: E501
        :rtype: str
        """
        return self._asset_url

    @asset_url.setter
    def asset_url(self, asset_url):
        """Sets the asset_url of this UnityPackage.


        :param asset_url: The asset_url of this UnityPackage.  # noqa: E501
        :type asset_url: str
        """

        self._asset_url = asset_url

    @property
    def asset_url_object(self):
        """Gets the asset_url_object of this UnityPackage.  # noqa: E501


        :return: The asset_url_object of this UnityPackage.  # noqa: E501
        :rtype: object
        """
        return self._asset_url_object

    @asset_url_object.setter
    def asset_url_object(self, asset_url_object):
        """Sets the asset_url_object of this UnityPackage.


        :param asset_url_object: The asset_url_object of this UnityPackage.  # noqa: E501
        :type asset_url_object: object
        """

        self._asset_url_object = asset_url_object

    @property
    def asset_version(self):
        """Gets the asset_version of this UnityPackage.  # noqa: E501


        :return: The asset_version of this UnityPackage.  # noqa: E501
        :rtype: int
        """
        return self._asset_version

    @asset_version.setter
    def asset_version(self, asset_version):
        """Sets the asset_version of this UnityPackage.


        :param asset_version: The asset_version of this UnityPackage.  # noqa: E501
        :type asset_version: int
        """
        if self.local_vars_configuration.client_side_validation and asset_version is None:  # noqa: E501
            raise ValueError("Invalid value for `asset_version`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                asset_version is not None and asset_version < 0):  # noqa: E501
            raise ValueError("Invalid value for `asset_version`, must be a value greater than or equal to `0`")  # noqa: E501

        self._asset_version = asset_version

    @property
    def created_at(self):
        """Gets the created_at of this UnityPackage.  # noqa: E501


        :return: The created_at of this UnityPackage.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this UnityPackage.


        :param created_at: The created_at of this UnityPackage.  # noqa: E501
        :type created_at: datetime
        """

        self._created_at = created_at

    @property
    def impostorizer_version(self):
        """Gets the impostorizer_version of this UnityPackage.  # noqa: E501


        :return: The impostorizer_version of this UnityPackage.  # noqa: E501
        :rtype: str
        """
        return self._impostorizer_version

    @impostorizer_version.setter
    def impostorizer_version(self, impostorizer_version):
        """Sets the impostorizer_version of this UnityPackage.


        :param impostorizer_version: The impostorizer_version of this UnityPackage.  # noqa: E501
        :type impostorizer_version: str
        """

        self._impostorizer_version = impostorizer_version

    @property
    def performance_rating(self):
        """Gets the performance_rating of this UnityPackage.  # noqa: E501


        :return: The performance_rating of this UnityPackage.  # noqa: E501
        :rtype: PerformanceRatings
        """
        return self._performance_rating

    @performance_rating.setter
    def performance_rating(self, performance_rating):
        """Sets the performance_rating of this UnityPackage.


        :param performance_rating: The performance_rating of this UnityPackage.  # noqa: E501
        :type performance_rating: PerformanceRatings
        """

        self._performance_rating = performance_rating

    @property
    def platform(self):
        """Gets the platform of this UnityPackage.  # noqa: E501

        This can be `standalonewindows` or `android`, but can also pretty much be any random Unity verison such as `2019.2.4-801-Release` or `2019.2.2-772-Release` or even `unknownplatform`.  # noqa: E501

        :return: The platform of this UnityPackage.  # noqa: E501
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this UnityPackage.

        This can be `standalonewindows` or `android`, but can also pretty much be any random Unity verison such as `2019.2.4-801-Release` or `2019.2.2-772-Release` or even `unknownplatform`.  # noqa: E501

        :param platform: The platform of this UnityPackage.  # noqa: E501
        :type platform: str
        """
        if self.local_vars_configuration.client_side_validation and platform is None:  # noqa: E501
            raise ValueError("Invalid value for `platform`, must not be `None`")  # noqa: E501

        self._platform = platform

    @property
    def plugin_url(self):
        """Gets the plugin_url of this UnityPackage.  # noqa: E501


        :return: The plugin_url of this UnityPackage.  # noqa: E501
        :rtype: str
        """
        return self._plugin_url

    @plugin_url.setter
    def plugin_url(self, plugin_url):
        """Sets the plugin_url of this UnityPackage.


        :param plugin_url: The plugin_url of this UnityPackage.  # noqa: E501
        :type plugin_url: str
        """

        self._plugin_url = plugin_url

    @property
    def plugin_url_object(self):
        """Gets the plugin_url_object of this UnityPackage.  # noqa: E501


        :return: The plugin_url_object of this UnityPackage.  # noqa: E501
        :rtype: object
        """
        return self._plugin_url_object

    @plugin_url_object.setter
    def plugin_url_object(self, plugin_url_object):
        """Sets the plugin_url_object of this UnityPackage.


        :param plugin_url_object: The plugin_url_object of this UnityPackage.  # noqa: E501
        :type plugin_url_object: object
        """

        self._plugin_url_object = plugin_url_object

    @property
    def unity_sort_number(self):
        """Gets the unity_sort_number of this UnityPackage.  # noqa: E501


        :return: The unity_sort_number of this UnityPackage.  # noqa: E501
        :rtype: int
        """
        return self._unity_sort_number

    @unity_sort_number.setter
    def unity_sort_number(self, unity_sort_number):
        """Sets the unity_sort_number of this UnityPackage.


        :param unity_sort_number: The unity_sort_number of this UnityPackage.  # noqa: E501
        :type unity_sort_number: int
        """
        if (self.local_vars_configuration.client_side_validation and
                unity_sort_number is not None and unity_sort_number < 0):  # noqa: E501
            raise ValueError("Invalid value for `unity_sort_number`, must be a value greater than or equal to `0`")  # noqa: E501

        self._unity_sort_number = unity_sort_number

    @property
    def unity_version(self):
        """Gets the unity_version of this UnityPackage.  # noqa: E501


        :return: The unity_version of this UnityPackage.  # noqa: E501
        :rtype: str
        """
        return self._unity_version

    @unity_version.setter
    def unity_version(self, unity_version):
        """Sets the unity_version of this UnityPackage.


        :param unity_version: The unity_version of this UnityPackage.  # noqa: E501
        :type unity_version: str
        """
        if self.local_vars_configuration.client_side_validation and unity_version is None:  # noqa: E501
            raise ValueError("Invalid value for `unity_version`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                unity_version is not None and len(unity_version) < 1):
            raise ValueError("Invalid value for `unity_version`, length must be greater than or equal to `1`")  # noqa: E501

        self._unity_version = unity_version

    @property
    def world_signature(self):
        """Gets the world_signature of this UnityPackage.  # noqa: E501


        :return: The world_signature of this UnityPackage.  # noqa: E501
        :rtype: str
        """
        return self._world_signature

    @world_signature.setter
    def world_signature(self, world_signature):
        """Sets the world_signature of this UnityPackage.


        :param world_signature: The world_signature of this UnityPackage.  # noqa: E501
        :type world_signature: str
        """

        self._world_signature = world_signature

    @property
    def impostor_url(self):
        """Gets the impostor_url of this UnityPackage.  # noqa: E501


        :return: The impostor_url of this UnityPackage.  # noqa: E501
        :rtype: str
        """
        return self._impostor_url

    @impostor_url.setter
    def impostor_url(self, impostor_url):
        """Sets the impostor_url of this UnityPackage.


        :param impostor_url: The impostor_url of this UnityPackage.  # noqa: E501
        :type impostor_url: str
        """

        self._impostor_url = impostor_url

    @property
    def scan_status(self):
        """Gets the scan_status of this UnityPackage.  # noqa: E501


        :return: The scan_status of this UnityPackage.  # noqa: E501
        :rtype: str
        """
        return self._scan_status

    @scan_status.setter
    def scan_status(self, scan_status):
        """Sets the scan_status of this UnityPackage.


        :param scan_status: The scan_status of this UnityPackage.  # noqa: E501
        :type scan_status: str
        """

        self._scan_status = scan_status

    @property
    def variant(self):
        """Gets the variant of this UnityPackage.  # noqa: E501


        :return: The variant of this UnityPackage.  # noqa: E501
        :rtype: str
        """
        return self._variant

    @variant.setter
    def variant(self, variant):
        """Sets the variant of this UnityPackage.


        :param variant: The variant of this UnityPackage.  # noqa: E501
        :type variant: str
        """

        self._variant = variant

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
        if not isinstance(other, UnityPackage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UnityPackage):
            return True

        return self.to_dict() != other.to_dict()
