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


class JamStateChangeDates(object):
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
        'closed': 'datetime',
        'submissions_closed': 'datetime',
        'submissions_opened': 'datetime',
        'winners_selected': 'datetime'
    }

    attribute_map = {
        'closed': 'closed',
        'submissions_closed': 'submissionsClosed',
        'submissions_opened': 'submissionsOpened',
        'winners_selected': 'winnersSelected'
    }

    def __init__(self, closed=None, submissions_closed=None, submissions_opened=None, winners_selected=None, local_vars_configuration=None):  # noqa: E501
        """JamStateChangeDates - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._closed = None
        self._submissions_closed = None
        self._submissions_opened = None
        self._winners_selected = None
        self.discriminator = None

        self.closed = closed
        self.submissions_closed = submissions_closed
        self.submissions_opened = submissions_opened
        self.winners_selected = winners_selected

    @property
    def closed(self):
        """Gets the closed of this JamStateChangeDates.  # noqa: E501


        :return: The closed of this JamStateChangeDates.  # noqa: E501
        :rtype: datetime
        """
        return self._closed

    @closed.setter
    def closed(self, closed):
        """Sets the closed of this JamStateChangeDates.


        :param closed: The closed of this JamStateChangeDates.  # noqa: E501
        :type closed: datetime
        """

        self._closed = closed

    @property
    def submissions_closed(self):
        """Gets the submissions_closed of this JamStateChangeDates.  # noqa: E501


        :return: The submissions_closed of this JamStateChangeDates.  # noqa: E501
        :rtype: datetime
        """
        return self._submissions_closed

    @submissions_closed.setter
    def submissions_closed(self, submissions_closed):
        """Sets the submissions_closed of this JamStateChangeDates.


        :param submissions_closed: The submissions_closed of this JamStateChangeDates.  # noqa: E501
        :type submissions_closed: datetime
        """

        self._submissions_closed = submissions_closed

    @property
    def submissions_opened(self):
        """Gets the submissions_opened of this JamStateChangeDates.  # noqa: E501


        :return: The submissions_opened of this JamStateChangeDates.  # noqa: E501
        :rtype: datetime
        """
        return self._submissions_opened

    @submissions_opened.setter
    def submissions_opened(self, submissions_opened):
        """Sets the submissions_opened of this JamStateChangeDates.


        :param submissions_opened: The submissions_opened of this JamStateChangeDates.  # noqa: E501
        :type submissions_opened: datetime
        """

        self._submissions_opened = submissions_opened

    @property
    def winners_selected(self):
        """Gets the winners_selected of this JamStateChangeDates.  # noqa: E501


        :return: The winners_selected of this JamStateChangeDates.  # noqa: E501
        :rtype: datetime
        """
        return self._winners_selected

    @winners_selected.setter
    def winners_selected(self, winners_selected):
        """Sets the winners_selected of this JamStateChangeDates.


        :param winners_selected: The winners_selected of this JamStateChangeDates.  # noqa: E501
        :type winners_selected: datetime
        """

        self._winners_selected = winners_selected

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
        if not isinstance(other, JamStateChangeDates):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, JamStateChangeDates):
            return True

        return self.to_dict() != other.to_dict()
