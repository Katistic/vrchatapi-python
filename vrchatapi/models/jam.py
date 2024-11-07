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


class Jam(object):
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
        'description': 'str',
        'id': 'str',
        'is_visible': 'bool',
        'more_info': 'str',
        'state': 'str',
        'state_change_dates': 'JamStateChangeDates',
        'submission_content_gate_date': 'datetime',
        'submission_content_gated': 'bool',
        'title': 'str',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'description': 'description',
        'id': 'id',
        'is_visible': 'isVisible',
        'more_info': 'moreInfo',
        'state': 'state',
        'state_change_dates': 'stateChangeDates',
        'submission_content_gate_date': 'submissionContentGateDate',
        'submission_content_gated': 'submissionContentGated',
        'title': 'title',
        'updated_at': 'updated_at'
    }

    def __init__(self, description=None, id=None, is_visible=None, more_info=None, state=None, state_change_dates=None, submission_content_gate_date=None, submission_content_gated=None, title=None, updated_at=None, local_vars_configuration=None):  # noqa: E501
        """Jam - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._description = None
        self._id = None
        self._is_visible = None
        self._more_info = None
        self._state = None
        self._state_change_dates = None
        self._submission_content_gate_date = None
        self._submission_content_gated = None
        self._title = None
        self._updated_at = None
        self.discriminator = None

        self.description = description
        self.id = id
        self.is_visible = is_visible
        self.more_info = more_info
        self.state = state
        self.state_change_dates = state_change_dates
        self.submission_content_gate_date = submission_content_gate_date
        self.submission_content_gated = submission_content_gated
        self.title = title
        self.updated_at = updated_at

    @property
    def description(self):
        """Gets the description of this Jam.  # noqa: E501


        :return: The description of this Jam.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Jam.


        :param description: The description of this Jam.  # noqa: E501
        :type description: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) < 1):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `1`")  # noqa: E501

        self._description = description

    @property
    def id(self):
        """Gets the id of this Jam.  # noqa: E501


        :return: The id of this Jam.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Jam.


        :param id: The id of this Jam.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                id is not None and len(id) < 1):
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `1`")  # noqa: E501

        self._id = id

    @property
    def is_visible(self):
        """Gets the is_visible of this Jam.  # noqa: E501


        :return: The is_visible of this Jam.  # noqa: E501
        :rtype: bool
        """
        return self._is_visible

    @is_visible.setter
    def is_visible(self, is_visible):
        """Sets the is_visible of this Jam.


        :param is_visible: The is_visible of this Jam.  # noqa: E501
        :type is_visible: bool
        """
        if self.local_vars_configuration.client_side_validation and is_visible is None:  # noqa: E501
            raise ValueError("Invalid value for `is_visible`, must not be `None`")  # noqa: E501

        self._is_visible = is_visible

    @property
    def more_info(self):
        """Gets the more_info of this Jam.  # noqa: E501


        :return: The more_info of this Jam.  # noqa: E501
        :rtype: str
        """
        return self._more_info

    @more_info.setter
    def more_info(self, more_info):
        """Sets the more_info of this Jam.


        :param more_info: The more_info of this Jam.  # noqa: E501
        :type more_info: str
        """
        if self.local_vars_configuration.client_side_validation and more_info is None:  # noqa: E501
            raise ValueError("Invalid value for `more_info`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                more_info is not None and len(more_info) < 1):
            raise ValueError("Invalid value for `more_info`, length must be greater than or equal to `1`")  # noqa: E501

        self._more_info = more_info

    @property
    def state(self):
        """Gets the state of this Jam.  # noqa: E501

        One of: - submissions_open - closed  # noqa: E501

        :return: The state of this Jam.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Jam.

        One of: - submissions_open - closed  # noqa: E501

        :param state: The state of this Jam.  # noqa: E501
        :type state: str
        """
        if self.local_vars_configuration.client_side_validation and state is None:  # noqa: E501
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                state is not None and len(state) < 1):
            raise ValueError("Invalid value for `state`, length must be greater than or equal to `1`")  # noqa: E501

        self._state = state

    @property
    def state_change_dates(self):
        """Gets the state_change_dates of this Jam.  # noqa: E501


        :return: The state_change_dates of this Jam.  # noqa: E501
        :rtype: JamStateChangeDates
        """
        return self._state_change_dates

    @state_change_dates.setter
    def state_change_dates(self, state_change_dates):
        """Sets the state_change_dates of this Jam.


        :param state_change_dates: The state_change_dates of this Jam.  # noqa: E501
        :type state_change_dates: JamStateChangeDates
        """
        if self.local_vars_configuration.client_side_validation and state_change_dates is None:  # noqa: E501
            raise ValueError("Invalid value for `state_change_dates`, must not be `None`")  # noqa: E501

        self._state_change_dates = state_change_dates

    @property
    def submission_content_gate_date(self):
        """Gets the submission_content_gate_date of this Jam.  # noqa: E501


        :return: The submission_content_gate_date of this Jam.  # noqa: E501
        :rtype: datetime
        """
        return self._submission_content_gate_date

    @submission_content_gate_date.setter
    def submission_content_gate_date(self, submission_content_gate_date):
        """Sets the submission_content_gate_date of this Jam.


        :param submission_content_gate_date: The submission_content_gate_date of this Jam.  # noqa: E501
        :type submission_content_gate_date: datetime
        """

        self._submission_content_gate_date = submission_content_gate_date

    @property
    def submission_content_gated(self):
        """Gets the submission_content_gated of this Jam.  # noqa: E501


        :return: The submission_content_gated of this Jam.  # noqa: E501
        :rtype: bool
        """
        return self._submission_content_gated

    @submission_content_gated.setter
    def submission_content_gated(self, submission_content_gated):
        """Sets the submission_content_gated of this Jam.


        :param submission_content_gated: The submission_content_gated of this Jam.  # noqa: E501
        :type submission_content_gated: bool
        """
        if self.local_vars_configuration.client_side_validation and submission_content_gated is None:  # noqa: E501
            raise ValueError("Invalid value for `submission_content_gated`, must not be `None`")  # noqa: E501

        self._submission_content_gated = submission_content_gated

    @property
    def title(self):
        """Gets the title of this Jam.  # noqa: E501


        :return: The title of this Jam.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Jam.


        :param title: The title of this Jam.  # noqa: E501
        :type title: str
        """
        if self.local_vars_configuration.client_side_validation and title is None:  # noqa: E501
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                title is not None and len(title) < 1):
            raise ValueError("Invalid value for `title`, length must be greater than or equal to `1`")  # noqa: E501

        self._title = title

    @property
    def updated_at(self):
        """Gets the updated_at of this Jam.  # noqa: E501


        :return: The updated_at of this Jam.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Jam.


        :param updated_at: The updated_at of this Jam.  # noqa: E501
        :type updated_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and updated_at is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

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
        if not isinstance(other, Jam):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Jam):
            return True

        return self.to_dict() != other.to_dict()
