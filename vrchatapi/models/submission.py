# coding: utf-8

"""
    VRChat API Documentation


    The version of the OpenAPI document: 1.18.7
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


class Submission(object):
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
        'content_id': 'str',
        'created_at': 'datetime',
        'description': 'str',
        'id': 'str',
        'jam_id': 'str',
        'rating_score': 'int',
        'submitter_id': 'str'
    }

    attribute_map = {
        'content_id': 'contentId',
        'created_at': 'created_at',
        'description': 'description',
        'id': 'id',
        'jam_id': 'jamId',
        'rating_score': 'ratingScore',
        'submitter_id': 'submitterId'
    }

    def __init__(self, content_id=None, created_at=None, description=None, id=None, jam_id=None, rating_score=None, submitter_id=None, local_vars_configuration=None):  # noqa: E501
        """Submission - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._content_id = None
        self._created_at = None
        self._description = None
        self._id = None
        self._jam_id = None
        self._rating_score = None
        self._submitter_id = None
        self.discriminator = None

        self.content_id = content_id
        self.created_at = created_at
        self.description = description
        self.id = id
        self.jam_id = jam_id
        if rating_score is not None:
            self.rating_score = rating_score
        self.submitter_id = submitter_id

    @property
    def content_id(self):
        """Gets the content_id of this Submission.  # noqa: E501

        Either world ID or avatar ID  # noqa: E501

        :return: The content_id of this Submission.  # noqa: E501
        :rtype: str
        """
        return self._content_id

    @content_id.setter
    def content_id(self, content_id):
        """Sets the content_id of this Submission.

        Either world ID or avatar ID  # noqa: E501

        :param content_id: The content_id of this Submission.  # noqa: E501
        :type content_id: str
        """
        if self.local_vars_configuration.client_side_validation and content_id is None:  # noqa: E501
            raise ValueError("Invalid value for `content_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                content_id is not None and len(content_id) < 1):
            raise ValueError("Invalid value for `content_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._content_id = content_id

    @property
    def created_at(self):
        """Gets the created_at of this Submission.  # noqa: E501


        :return: The created_at of this Submission.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Submission.


        :param created_at: The created_at of this Submission.  # noqa: E501
        :type created_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def description(self):
        """Gets the description of this Submission.  # noqa: E501


        :return: The description of this Submission.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Submission.


        :param description: The description of this Submission.  # noqa: E501
        :type description: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def id(self):
        """Gets the id of this Submission.  # noqa: E501


        :return: The id of this Submission.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Submission.


        :param id: The id of this Submission.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                id is not None and len(id) < 1):
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `1`")  # noqa: E501

        self._id = id

    @property
    def jam_id(self):
        """Gets the jam_id of this Submission.  # noqa: E501


        :return: The jam_id of this Submission.  # noqa: E501
        :rtype: str
        """
        return self._jam_id

    @jam_id.setter
    def jam_id(self, jam_id):
        """Sets the jam_id of this Submission.


        :param jam_id: The jam_id of this Submission.  # noqa: E501
        :type jam_id: str
        """
        if self.local_vars_configuration.client_side_validation and jam_id is None:  # noqa: E501
            raise ValueError("Invalid value for `jam_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                jam_id is not None and len(jam_id) < 1):
            raise ValueError("Invalid value for `jam_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._jam_id = jam_id

    @property
    def rating_score(self):
        """Gets the rating_score of this Submission.  # noqa: E501


        :return: The rating_score of this Submission.  # noqa: E501
        :rtype: int
        """
        return self._rating_score

    @rating_score.setter
    def rating_score(self, rating_score):
        """Sets the rating_score of this Submission.


        :param rating_score: The rating_score of this Submission.  # noqa: E501
        :type rating_score: int
        """
        if (self.local_vars_configuration.client_side_validation and
                rating_score is not None and rating_score < 0):  # noqa: E501
            raise ValueError("Invalid value for `rating_score`, must be a value greater than or equal to `0`")  # noqa: E501

        self._rating_score = rating_score

    @property
    def submitter_id(self):
        """Gets the submitter_id of this Submission.  # noqa: E501

        A users unique ID, usually in the form of `usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469`. Legacy players can have old IDs in the form of `8JoV9XEdpo`. The ID can never be changed.  # noqa: E501

        :return: The submitter_id of this Submission.  # noqa: E501
        :rtype: str
        """
        return self._submitter_id

    @submitter_id.setter
    def submitter_id(self, submitter_id):
        """Sets the submitter_id of this Submission.

        A users unique ID, usually in the form of `usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469`. Legacy players can have old IDs in the form of `8JoV9XEdpo`. The ID can never be changed.  # noqa: E501

        :param submitter_id: The submitter_id of this Submission.  # noqa: E501
        :type submitter_id: str
        """
        if self.local_vars_configuration.client_side_validation and submitter_id is None:  # noqa: E501
            raise ValueError("Invalid value for `submitter_id`, must not be `None`")  # noqa: E501

        self._submitter_id = submitter_id

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
        if not isinstance(other, Submission):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Submission):
            return True

        return self.to_dict() != other.to_dict()
