# coding: utf-8

"""
    VRChat API Documentation


    The version of the OpenAPI document: 1.18.5
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


class InfoPush(object):
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
        'is_enabled': 'bool',
        'release_status': 'ReleaseStatus',
        'priority': 'int',
        'tags': 'list[str]',
        'data': 'InfoPushData',
        'hash': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'start_date': 'datetime',
        'end_date': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'is_enabled': 'isEnabled',
        'release_status': 'releaseStatus',
        'priority': 'priority',
        'tags': 'tags',
        'data': 'data',
        'hash': 'hash',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'start_date': 'startDate',
        'end_date': 'endDate'
    }

    def __init__(self, id=None, is_enabled=True, release_status=None, priority=None, tags=None, data=None, hash=None, created_at=None, updated_at=None, start_date=None, end_date=None, local_vars_configuration=None):  # noqa: E501
        """InfoPush - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._is_enabled = None
        self._release_status = None
        self._priority = None
        self._tags = None
        self._data = None
        self._hash = None
        self._created_at = None
        self._updated_at = None
        self._start_date = None
        self._end_date = None
        self.discriminator = None

        self.id = id
        self.is_enabled = is_enabled
        self.release_status = release_status
        self.priority = priority
        self.tags = tags
        self.data = data
        self.hash = hash
        self.created_at = created_at
        self.updated_at = updated_at
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date

    @property
    def id(self):
        """Gets the id of this InfoPush.  # noqa: E501


        :return: The id of this InfoPush.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InfoPush.


        :param id: The id of this InfoPush.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                id is not None and len(id) < 1):
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `1`")  # noqa: E501

        self._id = id

    @property
    def is_enabled(self):
        """Gets the is_enabled of this InfoPush.  # noqa: E501


        :return: The is_enabled of this InfoPush.  # noqa: E501
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """Sets the is_enabled of this InfoPush.


        :param is_enabled: The is_enabled of this InfoPush.  # noqa: E501
        :type is_enabled: bool
        """
        if self.local_vars_configuration.client_side_validation and is_enabled is None:  # noqa: E501
            raise ValueError("Invalid value for `is_enabled`, must not be `None`")  # noqa: E501

        self._is_enabled = is_enabled

    @property
    def release_status(self):
        """Gets the release_status of this InfoPush.  # noqa: E501


        :return: The release_status of this InfoPush.  # noqa: E501
        :rtype: ReleaseStatus
        """
        return self._release_status

    @release_status.setter
    def release_status(self, release_status):
        """Sets the release_status of this InfoPush.


        :param release_status: The release_status of this InfoPush.  # noqa: E501
        :type release_status: ReleaseStatus
        """
        if self.local_vars_configuration.client_side_validation and release_status is None:  # noqa: E501
            raise ValueError("Invalid value for `release_status`, must not be `None`")  # noqa: E501

        self._release_status = release_status

    @property
    def priority(self):
        """Gets the priority of this InfoPush.  # noqa: E501


        :return: The priority of this InfoPush.  # noqa: E501
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this InfoPush.


        :param priority: The priority of this InfoPush.  # noqa: E501
        :type priority: int
        """
        if self.local_vars_configuration.client_side_validation and priority is None:  # noqa: E501
            raise ValueError("Invalid value for `priority`, must not be `None`")  # noqa: E501

        self._priority = priority

    @property
    def tags(self):
        """Gets the tags of this InfoPush.  # noqa: E501

           # noqa: E501

        :return: The tags of this InfoPush.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this InfoPush.

           # noqa: E501

        :param tags: The tags of this InfoPush.  # noqa: E501
        :type tags: list[str]
        """
        if self.local_vars_configuration.client_side_validation and tags is None:  # noqa: E501
            raise ValueError("Invalid value for `tags`, must not be `None`")  # noqa: E501

        self._tags = tags

    @property
    def data(self):
        """Gets the data of this InfoPush.  # noqa: E501


        :return: The data of this InfoPush.  # noqa: E501
        :rtype: InfoPushData
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this InfoPush.


        :param data: The data of this InfoPush.  # noqa: E501
        :type data: InfoPushData
        """
        if self.local_vars_configuration.client_side_validation and data is None:  # noqa: E501
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

    @property
    def hash(self):
        """Gets the hash of this InfoPush.  # noqa: E501

        Unknown usage, MD5  # noqa: E501

        :return: The hash of this InfoPush.  # noqa: E501
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this InfoPush.

        Unknown usage, MD5  # noqa: E501

        :param hash: The hash of this InfoPush.  # noqa: E501
        :type hash: str
        """
        if self.local_vars_configuration.client_side_validation and hash is None:  # noqa: E501
            raise ValueError("Invalid value for `hash`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                hash is not None and len(hash) < 1):
            raise ValueError("Invalid value for `hash`, length must be greater than or equal to `1`")  # noqa: E501

        self._hash = hash

    @property
    def created_at(self):
        """Gets the created_at of this InfoPush.  # noqa: E501


        :return: The created_at of this InfoPush.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this InfoPush.


        :param created_at: The created_at of this InfoPush.  # noqa: E501
        :type created_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this InfoPush.  # noqa: E501


        :return: The updated_at of this InfoPush.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this InfoPush.


        :param updated_at: The updated_at of this InfoPush.  # noqa: E501
        :type updated_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and updated_at is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

    @property
    def start_date(self):
        """Gets the start_date of this InfoPush.  # noqa: E501

          # noqa: E501

        :return: The start_date of this InfoPush.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this InfoPush.

          # noqa: E501

        :param start_date: The start_date of this InfoPush.  # noqa: E501
        :type start_date: datetime
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this InfoPush.  # noqa: E501


        :return: The end_date of this InfoPush.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this InfoPush.


        :param end_date: The end_date of this InfoPush.  # noqa: E501
        :type end_date: datetime
        """

        self._end_date = end_date

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
        if not isinstance(other, InfoPush):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InfoPush):
            return True

        return self.to_dict() != other.to_dict()
