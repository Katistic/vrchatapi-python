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


class FileVersionUploadStatus(object):
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
        'upload_id': 'str',
        'file_name': 'str',
        'next_part_number': 'int',
        'max_parts': 'int',
        'parts': 'list[object]',
        'etags': 'list[object]'
    }

    attribute_map = {
        'upload_id': 'uploadId',
        'file_name': 'fileName',
        'next_part_number': 'nextPartNumber',
        'max_parts': 'maxParts',
        'parts': 'parts',
        'etags': 'etags'
    }

    def __init__(self, upload_id=None, file_name=None, next_part_number=None, max_parts=None, parts=None, etags=None, local_vars_configuration=None):  # noqa: E501
        """FileVersionUploadStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._upload_id = None
        self._file_name = None
        self._next_part_number = None
        self._max_parts = None
        self._parts = None
        self._etags = None
        self.discriminator = None

        self.upload_id = upload_id
        self.file_name = file_name
        self.next_part_number = next_part_number
        self.max_parts = max_parts
        self.parts = parts
        self.etags = etags

    @property
    def upload_id(self):
        """Gets the upload_id of this FileVersionUploadStatus.  # noqa: E501


        :return: The upload_id of this FileVersionUploadStatus.  # noqa: E501
        :rtype: str
        """
        return self._upload_id

    @upload_id.setter
    def upload_id(self, upload_id):
        """Sets the upload_id of this FileVersionUploadStatus.


        :param upload_id: The upload_id of this FileVersionUploadStatus.  # noqa: E501
        :type upload_id: str
        """
        if self.local_vars_configuration.client_side_validation and upload_id is None:  # noqa: E501
            raise ValueError("Invalid value for `upload_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                upload_id is not None and len(upload_id) < 1):
            raise ValueError("Invalid value for `upload_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._upload_id = upload_id

    @property
    def file_name(self):
        """Gets the file_name of this FileVersionUploadStatus.  # noqa: E501


        :return: The file_name of this FileVersionUploadStatus.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this FileVersionUploadStatus.


        :param file_name: The file_name of this FileVersionUploadStatus.  # noqa: E501
        :type file_name: str
        """
        if self.local_vars_configuration.client_side_validation and file_name is None:  # noqa: E501
            raise ValueError("Invalid value for `file_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                file_name is not None and len(file_name) < 1):
            raise ValueError("Invalid value for `file_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._file_name = file_name

    @property
    def next_part_number(self):
        """Gets the next_part_number of this FileVersionUploadStatus.  # noqa: E501


        :return: The next_part_number of this FileVersionUploadStatus.  # noqa: E501
        :rtype: int
        """
        return self._next_part_number

    @next_part_number.setter
    def next_part_number(self, next_part_number):
        """Sets the next_part_number of this FileVersionUploadStatus.


        :param next_part_number: The next_part_number of this FileVersionUploadStatus.  # noqa: E501
        :type next_part_number: int
        """
        if self.local_vars_configuration.client_side_validation and next_part_number is None:  # noqa: E501
            raise ValueError("Invalid value for `next_part_number`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                next_part_number is not None and next_part_number < 0):  # noqa: E501
            raise ValueError("Invalid value for `next_part_number`, must be a value greater than or equal to `0`")  # noqa: E501

        self._next_part_number = next_part_number

    @property
    def max_parts(self):
        """Gets the max_parts of this FileVersionUploadStatus.  # noqa: E501


        :return: The max_parts of this FileVersionUploadStatus.  # noqa: E501
        :rtype: int
        """
        return self._max_parts

    @max_parts.setter
    def max_parts(self, max_parts):
        """Sets the max_parts of this FileVersionUploadStatus.


        :param max_parts: The max_parts of this FileVersionUploadStatus.  # noqa: E501
        :type max_parts: int
        """
        if self.local_vars_configuration.client_side_validation and max_parts is None:  # noqa: E501
            raise ValueError("Invalid value for `max_parts`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                max_parts is not None and max_parts < 1):  # noqa: E501
            raise ValueError("Invalid value for `max_parts`, must be a value greater than or equal to `1`")  # noqa: E501

        self._max_parts = max_parts

    @property
    def parts(self):
        """Gets the parts of this FileVersionUploadStatus.  # noqa: E501


        :return: The parts of this FileVersionUploadStatus.  # noqa: E501
        :rtype: list[object]
        """
        return self._parts

    @parts.setter
    def parts(self, parts):
        """Sets the parts of this FileVersionUploadStatus.


        :param parts: The parts of this FileVersionUploadStatus.  # noqa: E501
        :type parts: list[object]
        """
        if self.local_vars_configuration.client_side_validation and parts is None:  # noqa: E501
            raise ValueError("Invalid value for `parts`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                parts is not None and len(parts) < 0):
            raise ValueError("Invalid value for `parts`, number of items must be greater than or equal to `0`")  # noqa: E501

        self._parts = parts

    @property
    def etags(self):
        """Gets the etags of this FileVersionUploadStatus.  # noqa: E501

        Unknown  # noqa: E501

        :return: The etags of this FileVersionUploadStatus.  # noqa: E501
        :rtype: list[object]
        """
        return self._etags

    @etags.setter
    def etags(self, etags):
        """Sets the etags of this FileVersionUploadStatus.

        Unknown  # noqa: E501

        :param etags: The etags of this FileVersionUploadStatus.  # noqa: E501
        :type etags: list[object]
        """
        if self.local_vars_configuration.client_side_validation and etags is None:  # noqa: E501
            raise ValueError("Invalid value for `etags`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                etags is not None and len(etags) < 0):
            raise ValueError("Invalid value for `etags`, number of items must be greater than or equal to `0`")  # noqa: E501

        self._etags = etags

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
        if not isinstance(other, FileVersionUploadStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FileVersionUploadStatus):
            return True

        return self.to_dict() != other.to_dict()
