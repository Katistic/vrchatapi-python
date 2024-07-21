# coding: utf-8

"""
    VRChat API Documentation


    The version of the OpenAPI document: 1.18.0
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


class LimitedWorld(object):
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
        'author_id': 'str',
        'author_name': 'str',
        'capacity': 'int',
        'recommended_capacity': 'int',
        'created_at': 'datetime',
        'favorites': 'int',
        'visits': 'int',
        'heat': 'int',
        'id': 'str',
        'image_url': 'str',
        'labs_publication_date': 'str',
        'name': 'str',
        'occupants': 'int',
        'organization': 'str',
        'popularity': 'int',
        'preview_youtube_id': 'str',
        'publication_date': 'str',
        'release_status': 'ReleaseStatus',
        'tags': 'list[str]',
        'thumbnail_image_url': 'str',
        'unity_packages': 'list[LimitedUnityPackage]',
        'updated_at': 'datetime',
        'udon_products': 'list[str]'
    }

    attribute_map = {
        'author_id': 'authorId',
        'author_name': 'authorName',
        'capacity': 'capacity',
        'recommended_capacity': 'recommendedCapacity',
        'created_at': 'created_at',
        'favorites': 'favorites',
        'visits': 'visits',
        'heat': 'heat',
        'id': 'id',
        'image_url': 'imageUrl',
        'labs_publication_date': 'labsPublicationDate',
        'name': 'name',
        'occupants': 'occupants',
        'organization': 'organization',
        'popularity': 'popularity',
        'preview_youtube_id': 'previewYoutubeId',
        'publication_date': 'publicationDate',
        'release_status': 'releaseStatus',
        'tags': 'tags',
        'thumbnail_image_url': 'thumbnailImageUrl',
        'unity_packages': 'unityPackages',
        'updated_at': 'updated_at',
        'udon_products': 'udonProducts'
    }

    def __init__(self, author_id=None, author_name=None, capacity=None, recommended_capacity=None, created_at=None, favorites=0, visits=0, heat=0, id=None, image_url=None, labs_publication_date=None, name=None, occupants=0, organization='vrchat', popularity=0, preview_youtube_id=None, publication_date=None, release_status=None, tags=None, thumbnail_image_url=None, unity_packages=None, updated_at=None, udon_products=None, local_vars_configuration=None):  # noqa: E501
        """LimitedWorld - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._author_id = None
        self._author_name = None
        self._capacity = None
        self._recommended_capacity = None
        self._created_at = None
        self._favorites = None
        self._visits = None
        self._heat = None
        self._id = None
        self._image_url = None
        self._labs_publication_date = None
        self._name = None
        self._occupants = None
        self._organization = None
        self._popularity = None
        self._preview_youtube_id = None
        self._publication_date = None
        self._release_status = None
        self._tags = None
        self._thumbnail_image_url = None
        self._unity_packages = None
        self._updated_at = None
        self._udon_products = None
        self.discriminator = None

        self.author_id = author_id
        self.author_name = author_name
        self.capacity = capacity
        if recommended_capacity is not None:
            self.recommended_capacity = recommended_capacity
        self.created_at = created_at
        self.favorites = favorites
        if visits is not None:
            self.visits = visits
        self.heat = heat
        self.id = id
        self.image_url = image_url
        self.labs_publication_date = labs_publication_date
        self.name = name
        self.occupants = occupants
        self.organization = organization
        self.popularity = popularity
        self.preview_youtube_id = preview_youtube_id
        self.publication_date = publication_date
        self.release_status = release_status
        self.tags = tags
        self.thumbnail_image_url = thumbnail_image_url
        self.unity_packages = unity_packages
        self.updated_at = updated_at
        if udon_products is not None:
            self.udon_products = udon_products

    @property
    def author_id(self):
        """Gets the author_id of this LimitedWorld.  # noqa: E501

        A users unique ID, usually in the form of `usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469`. Legacy players can have old IDs in the form of `8JoV9XEdpo`. The ID can never be changed.  # noqa: E501

        :return: The author_id of this LimitedWorld.  # noqa: E501
        :rtype: str
        """
        return self._author_id

    @author_id.setter
    def author_id(self, author_id):
        """Sets the author_id of this LimitedWorld.

        A users unique ID, usually in the form of `usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469`. Legacy players can have old IDs in the form of `8JoV9XEdpo`. The ID can never be changed.  # noqa: E501

        :param author_id: The author_id of this LimitedWorld.  # noqa: E501
        :type author_id: str
        """
        if self.local_vars_configuration.client_side_validation and author_id is None:  # noqa: E501
            raise ValueError("Invalid value for `author_id`, must not be `None`")  # noqa: E501

        self._author_id = author_id

    @property
    def author_name(self):
        """Gets the author_name of this LimitedWorld.  # noqa: E501


        :return: The author_name of this LimitedWorld.  # noqa: E501
        :rtype: str
        """
        return self._author_name

    @author_name.setter
    def author_name(self, author_name):
        """Sets the author_name of this LimitedWorld.


        :param author_name: The author_name of this LimitedWorld.  # noqa: E501
        :type author_name: str
        """
        if self.local_vars_configuration.client_side_validation and author_name is None:  # noqa: E501
            raise ValueError("Invalid value for `author_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                author_name is not None and len(author_name) < 1):
            raise ValueError("Invalid value for `author_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._author_name = author_name

    @property
    def capacity(self):
        """Gets the capacity of this LimitedWorld.  # noqa: E501


        :return: The capacity of this LimitedWorld.  # noqa: E501
        :rtype: int
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """Sets the capacity of this LimitedWorld.


        :param capacity: The capacity of this LimitedWorld.  # noqa: E501
        :type capacity: int
        """
        if self.local_vars_configuration.client_side_validation and capacity is None:  # noqa: E501
            raise ValueError("Invalid value for `capacity`, must not be `None`")  # noqa: E501

        self._capacity = capacity

    @property
    def recommended_capacity(self):
        """Gets the recommended_capacity of this LimitedWorld.  # noqa: E501


        :return: The recommended_capacity of this LimitedWorld.  # noqa: E501
        :rtype: int
        """
        return self._recommended_capacity

    @recommended_capacity.setter
    def recommended_capacity(self, recommended_capacity):
        """Sets the recommended_capacity of this LimitedWorld.


        :param recommended_capacity: The recommended_capacity of this LimitedWorld.  # noqa: E501
        :type recommended_capacity: int
        """

        self._recommended_capacity = recommended_capacity

    @property
    def created_at(self):
        """Gets the created_at of this LimitedWorld.  # noqa: E501


        :return: The created_at of this LimitedWorld.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this LimitedWorld.


        :param created_at: The created_at of this LimitedWorld.  # noqa: E501
        :type created_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def favorites(self):
        """Gets the favorites of this LimitedWorld.  # noqa: E501


        :return: The favorites of this LimitedWorld.  # noqa: E501
        :rtype: int
        """
        return self._favorites

    @favorites.setter
    def favorites(self, favorites):
        """Sets the favorites of this LimitedWorld.


        :param favorites: The favorites of this LimitedWorld.  # noqa: E501
        :type favorites: int
        """
        if self.local_vars_configuration.client_side_validation and favorites is None:  # noqa: E501
            raise ValueError("Invalid value for `favorites`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                favorites is not None and favorites < 0):  # noqa: E501
            raise ValueError("Invalid value for `favorites`, must be a value greater than or equal to `0`")  # noqa: E501

        self._favorites = favorites

    @property
    def visits(self):
        """Gets the visits of this LimitedWorld.  # noqa: E501


        :return: The visits of this LimitedWorld.  # noqa: E501
        :rtype: int
        """
        return self._visits

    @visits.setter
    def visits(self, visits):
        """Sets the visits of this LimitedWorld.


        :param visits: The visits of this LimitedWorld.  # noqa: E501
        :type visits: int
        """
        if (self.local_vars_configuration.client_side_validation and
                visits is not None and visits < 0):  # noqa: E501
            raise ValueError("Invalid value for `visits`, must be a value greater than or equal to `0`")  # noqa: E501

        self._visits = visits

    @property
    def heat(self):
        """Gets the heat of this LimitedWorld.  # noqa: E501


        :return: The heat of this LimitedWorld.  # noqa: E501
        :rtype: int
        """
        return self._heat

    @heat.setter
    def heat(self, heat):
        """Sets the heat of this LimitedWorld.


        :param heat: The heat of this LimitedWorld.  # noqa: E501
        :type heat: int
        """
        if self.local_vars_configuration.client_side_validation and heat is None:  # noqa: E501
            raise ValueError("Invalid value for `heat`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                heat is not None and heat < 0):  # noqa: E501
            raise ValueError("Invalid value for `heat`, must be a value greater than or equal to `0`")  # noqa: E501

        self._heat = heat

    @property
    def id(self):
        """Gets the id of this LimitedWorld.  # noqa: E501

        WorldID be \"offline\" on User profiles if you are not friends with that user.  # noqa: E501

        :return: The id of this LimitedWorld.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LimitedWorld.

        WorldID be \"offline\" on User profiles if you are not friends with that user.  # noqa: E501

        :param id: The id of this LimitedWorld.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def image_url(self):
        """Gets the image_url of this LimitedWorld.  # noqa: E501


        :return: The image_url of this LimitedWorld.  # noqa: E501
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """Sets the image_url of this LimitedWorld.


        :param image_url: The image_url of this LimitedWorld.  # noqa: E501
        :type image_url: str
        """
        if self.local_vars_configuration.client_side_validation and image_url is None:  # noqa: E501
            raise ValueError("Invalid value for `image_url`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                image_url is not None and len(image_url) < 1):
            raise ValueError("Invalid value for `image_url`, length must be greater than or equal to `1`")  # noqa: E501

        self._image_url = image_url

    @property
    def labs_publication_date(self):
        """Gets the labs_publication_date of this LimitedWorld.  # noqa: E501


        :return: The labs_publication_date of this LimitedWorld.  # noqa: E501
        :rtype: str
        """
        return self._labs_publication_date

    @labs_publication_date.setter
    def labs_publication_date(self, labs_publication_date):
        """Sets the labs_publication_date of this LimitedWorld.


        :param labs_publication_date: The labs_publication_date of this LimitedWorld.  # noqa: E501
        :type labs_publication_date: str
        """
        if self.local_vars_configuration.client_side_validation and labs_publication_date is None:  # noqa: E501
            raise ValueError("Invalid value for `labs_publication_date`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                labs_publication_date is not None and len(labs_publication_date) < 1):
            raise ValueError("Invalid value for `labs_publication_date`, length must be greater than or equal to `1`")  # noqa: E501

        self._labs_publication_date = labs_publication_date

    @property
    def name(self):
        """Gets the name of this LimitedWorld.  # noqa: E501


        :return: The name of this LimitedWorld.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LimitedWorld.


        :param name: The name of this LimitedWorld.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def occupants(self):
        """Gets the occupants of this LimitedWorld.  # noqa: E501


        :return: The occupants of this LimitedWorld.  # noqa: E501
        :rtype: int
        """
        return self._occupants

    @occupants.setter
    def occupants(self, occupants):
        """Sets the occupants of this LimitedWorld.


        :param occupants: The occupants of this LimitedWorld.  # noqa: E501
        :type occupants: int
        """
        if self.local_vars_configuration.client_side_validation and occupants is None:  # noqa: E501
            raise ValueError("Invalid value for `occupants`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                occupants is not None and occupants < 0):  # noqa: E501
            raise ValueError("Invalid value for `occupants`, must be a value greater than or equal to `0`")  # noqa: E501

        self._occupants = occupants

    @property
    def organization(self):
        """Gets the organization of this LimitedWorld.  # noqa: E501


        :return: The organization of this LimitedWorld.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this LimitedWorld.


        :param organization: The organization of this LimitedWorld.  # noqa: E501
        :type organization: str
        """
        if self.local_vars_configuration.client_side_validation and organization is None:  # noqa: E501
            raise ValueError("Invalid value for `organization`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                organization is not None and len(organization) < 1):
            raise ValueError("Invalid value for `organization`, length must be greater than or equal to `1`")  # noqa: E501

        self._organization = organization

    @property
    def popularity(self):
        """Gets the popularity of this LimitedWorld.  # noqa: E501


        :return: The popularity of this LimitedWorld.  # noqa: E501
        :rtype: int
        """
        return self._popularity

    @popularity.setter
    def popularity(self, popularity):
        """Sets the popularity of this LimitedWorld.


        :param popularity: The popularity of this LimitedWorld.  # noqa: E501
        :type popularity: int
        """
        if self.local_vars_configuration.client_side_validation and popularity is None:  # noqa: E501
            raise ValueError("Invalid value for `popularity`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                popularity is not None and popularity < 0):  # noqa: E501
            raise ValueError("Invalid value for `popularity`, must be a value greater than or equal to `0`")  # noqa: E501

        self._popularity = popularity

    @property
    def preview_youtube_id(self):
        """Gets the preview_youtube_id of this LimitedWorld.  # noqa: E501


        :return: The preview_youtube_id of this LimitedWorld.  # noqa: E501
        :rtype: str
        """
        return self._preview_youtube_id

    @preview_youtube_id.setter
    def preview_youtube_id(self, preview_youtube_id):
        """Sets the preview_youtube_id of this LimitedWorld.


        :param preview_youtube_id: The preview_youtube_id of this LimitedWorld.  # noqa: E501
        :type preview_youtube_id: str
        """

        self._preview_youtube_id = preview_youtube_id

    @property
    def publication_date(self):
        """Gets the publication_date of this LimitedWorld.  # noqa: E501


        :return: The publication_date of this LimitedWorld.  # noqa: E501
        :rtype: str
        """
        return self._publication_date

    @publication_date.setter
    def publication_date(self, publication_date):
        """Sets the publication_date of this LimitedWorld.


        :param publication_date: The publication_date of this LimitedWorld.  # noqa: E501
        :type publication_date: str
        """
        if self.local_vars_configuration.client_side_validation and publication_date is None:  # noqa: E501
            raise ValueError("Invalid value for `publication_date`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                publication_date is not None and len(publication_date) < 1):
            raise ValueError("Invalid value for `publication_date`, length must be greater than or equal to `1`")  # noqa: E501

        self._publication_date = publication_date

    @property
    def release_status(self):
        """Gets the release_status of this LimitedWorld.  # noqa: E501


        :return: The release_status of this LimitedWorld.  # noqa: E501
        :rtype: ReleaseStatus
        """
        return self._release_status

    @release_status.setter
    def release_status(self, release_status):
        """Sets the release_status of this LimitedWorld.


        :param release_status: The release_status of this LimitedWorld.  # noqa: E501
        :type release_status: ReleaseStatus
        """
        if self.local_vars_configuration.client_side_validation and release_status is None:  # noqa: E501
            raise ValueError("Invalid value for `release_status`, must not be `None`")  # noqa: E501

        self._release_status = release_status

    @property
    def tags(self):
        """Gets the tags of this LimitedWorld.  # noqa: E501

           # noqa: E501

        :return: The tags of this LimitedWorld.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this LimitedWorld.

           # noqa: E501

        :param tags: The tags of this LimitedWorld.  # noqa: E501
        :type tags: list[str]
        """
        if self.local_vars_configuration.client_side_validation and tags is None:  # noqa: E501
            raise ValueError("Invalid value for `tags`, must not be `None`")  # noqa: E501

        self._tags = tags

    @property
    def thumbnail_image_url(self):
        """Gets the thumbnail_image_url of this LimitedWorld.  # noqa: E501


        :return: The thumbnail_image_url of this LimitedWorld.  # noqa: E501
        :rtype: str
        """
        return self._thumbnail_image_url

    @thumbnail_image_url.setter
    def thumbnail_image_url(self, thumbnail_image_url):
        """Sets the thumbnail_image_url of this LimitedWorld.


        :param thumbnail_image_url: The thumbnail_image_url of this LimitedWorld.  # noqa: E501
        :type thumbnail_image_url: str
        """
        if self.local_vars_configuration.client_side_validation and thumbnail_image_url is None:  # noqa: E501
            raise ValueError("Invalid value for `thumbnail_image_url`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                thumbnail_image_url is not None and len(thumbnail_image_url) < 1):
            raise ValueError("Invalid value for `thumbnail_image_url`, length must be greater than or equal to `1`")  # noqa: E501

        self._thumbnail_image_url = thumbnail_image_url

    @property
    def unity_packages(self):
        """Gets the unity_packages of this LimitedWorld.  # noqa: E501

           # noqa: E501

        :return: The unity_packages of this LimitedWorld.  # noqa: E501
        :rtype: list[LimitedUnityPackage]
        """
        return self._unity_packages

    @unity_packages.setter
    def unity_packages(self, unity_packages):
        """Sets the unity_packages of this LimitedWorld.

           # noqa: E501

        :param unity_packages: The unity_packages of this LimitedWorld.  # noqa: E501
        :type unity_packages: list[LimitedUnityPackage]
        """
        if self.local_vars_configuration.client_side_validation and unity_packages is None:  # noqa: E501
            raise ValueError("Invalid value for `unity_packages`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                unity_packages is not None and len(unity_packages) < 1):
            raise ValueError("Invalid value for `unity_packages`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._unity_packages = unity_packages

    @property
    def updated_at(self):
        """Gets the updated_at of this LimitedWorld.  # noqa: E501


        :return: The updated_at of this LimitedWorld.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this LimitedWorld.


        :param updated_at: The updated_at of this LimitedWorld.  # noqa: E501
        :type updated_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and updated_at is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

    @property
    def udon_products(self):
        """Gets the udon_products of this LimitedWorld.  # noqa: E501


        :return: The udon_products of this LimitedWorld.  # noqa: E501
        :rtype: list[str]
        """
        return self._udon_products

    @udon_products.setter
    def udon_products(self, udon_products):
        """Sets the udon_products of this LimitedWorld.


        :param udon_products: The udon_products of this LimitedWorld.  # noqa: E501
        :type udon_products: list[str]
        """

        self._udon_products = udon_products

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
        if not isinstance(other, LimitedWorld):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LimitedWorld):
            return True

        return self.to_dict() != other.to_dict()
