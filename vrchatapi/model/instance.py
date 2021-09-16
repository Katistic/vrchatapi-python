"""
    VRChat API Documentation


    The version of the OpenAPI document: 1.3.1
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
    from vrchatapi.model.instance_id import InstanceID
    from vrchatapi.model.instance_platforms import InstancePlatforms
    from vrchatapi.model.tag import Tag
    from vrchatapi.model.world_id import WorldID
    globals()['InstanceID'] = InstanceID
    globals()['InstancePlatforms'] = InstancePlatforms
    globals()['Tag'] = Tag
    globals()['WorldID'] = WorldID


class Instance(ModelNormal):
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
        ('capacity',): {
            'inclusive_maximum': 40,
            'inclusive_minimum': 0,
        },
        ('client_number',): {
            'min_length': 1,
        },
        ('instance_id',): {
            'min_length': 1,
        },
        ('location',): {
            'min_length': 1,
        },
        ('n_users',): {
            'inclusive_minimum': 0,
        },
        ('name',): {
            'min_length': 1,
        },
        ('photon_region',): {
            'min_length': 1,
        },
        ('region',): {
            'min_length': 1,
        },
        ('short_name',): {
            'min_length': 1,
        },
        ('type',): {
            'min_length': 1,
        },
        ('nonce',): {
            'min_length': 1,
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
            'active': (bool,),  # noqa: E501
            'can_request_invite': (bool,),  # noqa: E501
            'capacity': (float,),  # noqa: E501
            'client_number': (str,),  # noqa: E501
            'full': (bool,),  # noqa: E501
            'id': (InstanceID,),  # noqa: E501
            'instance_id': (str,),  # noqa: E501
            'location': (str,),  # noqa: E501
            'n_users': (float,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'owner_id': (str,),  # noqa: E501
            'permanent': (bool,),  # noqa: E501
            'photon_region': (str,),  # noqa: E501
            'platforms': (InstancePlatforms,),  # noqa: E501
            'region': (str,),  # noqa: E501
            'short_name': (str,),  # noqa: E501
            'tags': ([Tag],),  # noqa: E501
            'type': (str,),  # noqa: E501
            'world_id': (WorldID,),  # noqa: E501
            'nonce': (str,),  # noqa: E501
            'users': ([{str: (bool, date, datetime, dict, float, int, list, str, none_type)}],),  # noqa: E501
            'world': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'active': 'active',  # noqa: E501
        'can_request_invite': 'canRequestInvite',  # noqa: E501
        'capacity': 'capacity',  # noqa: E501
        'client_number': 'clientNumber',  # noqa: E501
        'full': 'full',  # noqa: E501
        'id': 'id',  # noqa: E501
        'instance_id': 'instanceId',  # noqa: E501
        'location': 'location',  # noqa: E501
        'n_users': 'n_users',  # noqa: E501
        'name': 'name',  # noqa: E501
        'owner_id': 'ownerId',  # noqa: E501
        'permanent': 'permanent',  # noqa: E501
        'photon_region': 'photonRegion',  # noqa: E501
        'platforms': 'platforms',  # noqa: E501
        'region': 'region',  # noqa: E501
        'short_name': 'shortName',  # noqa: E501
        'tags': 'tags',  # noqa: E501
        'type': 'type',  # noqa: E501
        'world_id': 'worldId',  # noqa: E501
        'nonce': 'nonce',  # noqa: E501
        'users': 'users',  # noqa: E501
        'world': 'world',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, capacity, client_number, id, instance_id, location, n_users, name, owner_id, photon_region, platforms, region, short_name, tags, type, world_id, *args, **kwargs):  # noqa: E501
        """Instance - a model defined in OpenAPI

        Args:
            capacity (float):
            client_number (str):
            id (InstanceID):
            instance_id (str):
            location (str):
            n_users (float):
            name (str):
            owner_id (str):
            photon_region (str):
            platforms (InstancePlatforms):
            region (str):
            short_name (str):
            tags ([Tag]):
            type (str):
            world_id (WorldID):

        Keyword Args:
            active (bool): defaults to True  # noqa: E501
            can_request_invite (bool): defaults to True  # noqa: E501
            full (bool): defaults to False  # noqa: E501
            permanent (bool): defaults to False  # noqa: E501
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
            nonce (str): [optional]  # noqa: E501
            users ([{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]): Always empty on non-existing instances, and non-present on existing instances.. [optional]  # noqa: E501
            world ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Only present on non-existing instances, and only contains a very small subject of World object. Use World API instead.. [optional]  # noqa: E501
        """

        active = kwargs.get('active', True)
        can_request_invite = kwargs.get('can_request_invite', True)
        full = kwargs.get('full', False)
        permanent = kwargs.get('permanent', False)
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

        self.active = active
        self.can_request_invite = can_request_invite
        self.capacity = capacity
        self.client_number = client_number
        self.full = full
        self.id = id
        self.instance_id = instance_id
        self.location = location
        self.n_users = n_users
        self.name = name
        self.owner_id = owner_id
        self.permanent = permanent
        self.photon_region = photon_region
        self.platforms = platforms
        self.region = region
        self.short_name = short_name
        self.tags = tags
        self.type = type
        self.world_id = world_id
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
    def __init__(self, capacity, client_number, id, instance_id, location, n_users, name, owner_id, photon_region, platforms, region, short_name, tags, type, world_id, *args, **kwargs):  # noqa: E501
        """Instance - a model defined in OpenAPI

        Args:
            capacity (float):
            client_number (str):
            id (InstanceID):
            instance_id (str):
            location (str):
            n_users (float):
            name (str):
            owner_id (str):
            photon_region (str):
            platforms (InstancePlatforms):
            region (str):
            short_name (str):
            tags ([Tag]):
            type (str):
            world_id (WorldID):

        Keyword Args:
            active (bool): defaults to True  # noqa: E501
            can_request_invite (bool): defaults to True  # noqa: E501
            full (bool): defaults to False  # noqa: E501
            permanent (bool): defaults to False  # noqa: E501
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
            nonce (str): [optional]  # noqa: E501
            users ([{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]): Always empty on non-existing instances, and non-present on existing instances.. [optional]  # noqa: E501
            world ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Only present on non-existing instances, and only contains a very small subject of World object. Use World API instead.. [optional]  # noqa: E501
        """

        active = kwargs.get('active', True)
        can_request_invite = kwargs.get('can_request_invite', True)
        full = kwargs.get('full', False)
        permanent = kwargs.get('permanent', False)
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

        self.active = active
        self.can_request_invite = can_request_invite
        self.capacity = capacity
        self.client_number = client_number
        self.full = full
        self.id = id
        self.instance_id = instance_id
        self.location = location
        self.n_users = n_users
        self.name = name
        self.owner_id = owner_id
        self.permanent = permanent
        self.photon_region = photon_region
        self.platforms = platforms
        self.region = region
        self.short_name = short_name
        self.tags = tags
        self.type = type
        self.world_id = world_id
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
