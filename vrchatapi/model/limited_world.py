"""
    VRChat API Documentation


    The version of the OpenAPI document: 1.6.10
    Contact: me@ruby.js.org
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from vrchatapi.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)
from ..model_utils import OpenApiModel
from vrchatapi.exceptions import ApiAttributeError


def lazy_import():
    from vrchatapi.model.limited_unity_package import LimitedUnityPackage
    from vrchatapi.model.release_status import ReleaseStatus
    from vrchatapi.model.tag import Tag
    from vrchatapi.model.world_id import WorldID
    globals()['LimitedUnityPackage'] = LimitedUnityPackage
    globals()['ReleaseStatus'] = ReleaseStatus
    globals()['Tag'] = Tag
    globals()['WorldID'] = WorldID


class LimitedWorld(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
        ('author_name',): {
            'min_length': 1,
        },
        ('capacity',): {
            'inclusive_maximum': 40,
            'inclusive_minimum': 0,
        },
        ('favorites',): {
            'inclusive_minimum': 0,
        },
        ('heat',): {
            'inclusive_minimum': 0,
        },
        ('image_url',): {
            'min_length': 1,
        },
        ('labs_publication_date',): {
            'min_length': 1,
        },
        ('name',): {
            'min_length': 1,
        },
        ('occupants',): {
            'inclusive_minimum': 0,
        },
        ('organization',): {
            'min_length': 1,
        },
        ('popularity',): {
            'inclusive_minimum': 0,
        },
        ('publication_date',): {
            'min_length': 1,
        },
        ('thumbnail_image_url',): {
            'min_length': 1,
        },
        ('unity_packages',): {
            'min_items': 1,
        },
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'author_id': (str,),  # noqa: E501
            'author_name': (str,),  # noqa: E501
            'capacity': (int,),  # noqa: E501
            'created_at': (datetime,),  # noqa: E501
            'favorites': (int,),  # noqa: E501
            'heat': (int,),  # noqa: E501
            'id': (WorldID,),  # noqa: E501
            'image_url': (str,),  # noqa: E501
            'labs_publication_date': (str,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'occupants': (int,),  # noqa: E501
            'organization': (str,),  # noqa: E501
            'popularity': (int,),  # noqa: E501
            'publication_date': (str,),  # noqa: E501
            'release_status': (ReleaseStatus,),  # noqa: E501
            'tags': ([Tag],),  # noqa: E501
            'thumbnail_image_url': (str,),  # noqa: E501
            'unity_packages': ([LimitedUnityPackage],),  # noqa: E501
            'updated_at': (datetime,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'author_id': 'authorId',  # noqa: E501
        'author_name': 'authorName',  # noqa: E501
        'capacity': 'capacity',  # noqa: E501
        'created_at': 'created_at',  # noqa: E501
        'favorites': 'favorites',  # noqa: E501
        'heat': 'heat',  # noqa: E501
        'id': 'id',  # noqa: E501
        'image_url': 'imageUrl',  # noqa: E501
        'labs_publication_date': 'labsPublicationDate',  # noqa: E501
        'name': 'name',  # noqa: E501
        'occupants': 'occupants',  # noqa: E501
        'organization': 'organization',  # noqa: E501
        'popularity': 'popularity',  # noqa: E501
        'publication_date': 'publicationDate',  # noqa: E501
        'release_status': 'releaseStatus',  # noqa: E501
        'tags': 'tags',  # noqa: E501
        'thumbnail_image_url': 'thumbnailImageUrl',  # noqa: E501
        'unity_packages': 'unityPackages',  # noqa: E501
        'updated_at': 'updated_at',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, author_id, author_name, capacity, created_at, id, image_url, labs_publication_date, name, publication_date, release_status, tags, thumbnail_image_url, unity_packages, updated_at, *args, **kwargs):  # noqa: E501
        """LimitedWorld - a model defined in OpenAPI

        Args:
            author_id (str): A users unique ID, usually in the form of `usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469`. Legacy players can have old IDs in the form of `8JoV9XEdpo`. The ID can never be changed.
            author_name (str):
            capacity (int):
            created_at (datetime):
            id (WorldID):
            image_url (str):
            labs_publication_date (str):
            name (str):
            publication_date (str):
            release_status (ReleaseStatus):
            tags ([Tag]):
            thumbnail_image_url (str):
            unity_packages ([LimitedUnityPackage]):
            updated_at (datetime):

        Keyword Args:
            favorites (int): defaults to 0  # noqa: E501
            heat (int): defaults to 0  # noqa: E501
            occupants (int): defaults to 0  # noqa: E501
            organization (str): defaults to "vrchat"  # noqa: E501
            popularity (int): defaults to 0  # noqa: E501
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
        """

        favorites = kwargs.get('favorites', 0)
        heat = kwargs.get('heat', 0)
        occupants = kwargs.get('occupants', 0)
        organization = kwargs.get('organization', "vrchat")
        popularity = kwargs.get('popularity', 0)
        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.author_id = author_id
        self.author_name = author_name
        self.capacity = capacity
        self.created_at = created_at
        self.favorites = favorites
        self.heat = heat
        self.id = id
        self.image_url = image_url
        self.labs_publication_date = labs_publication_date
        self.name = name
        self.occupants = occupants
        self.organization = organization
        self.popularity = popularity
        self.publication_date = publication_date
        self.release_status = release_status
        self.tags = tags
        self.thumbnail_image_url = thumbnail_image_url
        self.unity_packages = unity_packages
        self.updated_at = updated_at
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, author_id, author_name, capacity, created_at, id, image_url, labs_publication_date, name, publication_date, release_status, tags, thumbnail_image_url, unity_packages, updated_at, *args, **kwargs):  # noqa: E501
        """LimitedWorld - a model defined in OpenAPI

        Args:
            author_id (str): A users unique ID, usually in the form of `usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469`. Legacy players can have old IDs in the form of `8JoV9XEdpo`. The ID can never be changed.
            author_name (str):
            capacity (int):
            created_at (datetime):
            id (WorldID):
            image_url (str):
            labs_publication_date (str):
            name (str):
            publication_date (str):
            release_status (ReleaseStatus):
            tags ([Tag]):
            thumbnail_image_url (str):
            unity_packages ([LimitedUnityPackage]):
            updated_at (datetime):

        Keyword Args:
            favorites (int): defaults to 0  # noqa: E501
            heat (int): defaults to 0  # noqa: E501
            occupants (int): defaults to 0  # noqa: E501
            organization (str): defaults to "vrchat"  # noqa: E501
            popularity (int): defaults to 0  # noqa: E501
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
        """

        favorites = kwargs.get('favorites', 0)
        heat = kwargs.get('heat', 0)
        occupants = kwargs.get('occupants', 0)
        organization = kwargs.get('organization', "vrchat")
        popularity = kwargs.get('popularity', 0)
        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.author_id = author_id
        self.author_name = author_name
        self.capacity = capacity
        self.created_at = created_at
        self.favorites = favorites
        self.heat = heat
        self.id = id
        self.image_url = image_url
        self.labs_publication_date = labs_publication_date
        self.name = name
        self.occupants = occupants
        self.organization = organization
        self.popularity = popularity
        self.publication_date = publication_date
        self.release_status = release_status
        self.tags = tags
        self.thumbnail_image_url = thumbnail_image_url
        self.unity_packages = unity_packages
        self.updated_at = updated_at
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
