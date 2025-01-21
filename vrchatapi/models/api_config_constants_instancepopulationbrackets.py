# coding: utf-8

"""
    VRChat API Documentation


    The version of the OpenAPI document: 1.19.0
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


class APIConfigConstantsINSTANCEPOPULATIONBRACKETS(object):
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
        'crowded': 'APIConfigConstantsINSTANCEPOPULATIONBRACKETSCROWDED',
        'few': 'APIConfigConstantsINSTANCEPOPULATIONBRACKETSFEW',
        'many': 'APIConfigConstantsINSTANCEPOPULATIONBRACKETSMANY'
    }

    attribute_map = {
        'crowded': 'CROWDED',
        'few': 'FEW',
        'many': 'MANY'
    }

    def __init__(self, crowded=None, few=None, many=None, local_vars_configuration=None):  # noqa: E501
        """APIConfigConstantsINSTANCEPOPULATIONBRACKETS - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._crowded = None
        self._few = None
        self._many = None
        self.discriminator = None

        if crowded is not None:
            self.crowded = crowded
        if few is not None:
            self.few = few
        if many is not None:
            self.many = many

    @property
    def crowded(self):
        """Gets the crowded of this APIConfigConstantsINSTANCEPOPULATIONBRACKETS.  # noqa: E501


        :return: The crowded of this APIConfigConstantsINSTANCEPOPULATIONBRACKETS.  # noqa: E501
        :rtype: APIConfigConstantsINSTANCEPOPULATIONBRACKETSCROWDED
        """
        return self._crowded

    @crowded.setter
    def crowded(self, crowded):
        """Sets the crowded of this APIConfigConstantsINSTANCEPOPULATIONBRACKETS.


        :param crowded: The crowded of this APIConfigConstantsINSTANCEPOPULATIONBRACKETS.  # noqa: E501
        :type crowded: APIConfigConstantsINSTANCEPOPULATIONBRACKETSCROWDED
        """

        self._crowded = crowded

    @property
    def few(self):
        """Gets the few of this APIConfigConstantsINSTANCEPOPULATIONBRACKETS.  # noqa: E501


        :return: The few of this APIConfigConstantsINSTANCEPOPULATIONBRACKETS.  # noqa: E501
        :rtype: APIConfigConstantsINSTANCEPOPULATIONBRACKETSFEW
        """
        return self._few

    @few.setter
    def few(self, few):
        """Sets the few of this APIConfigConstantsINSTANCEPOPULATIONBRACKETS.


        :param few: The few of this APIConfigConstantsINSTANCEPOPULATIONBRACKETS.  # noqa: E501
        :type few: APIConfigConstantsINSTANCEPOPULATIONBRACKETSFEW
        """

        self._few = few

    @property
    def many(self):
        """Gets the many of this APIConfigConstantsINSTANCEPOPULATIONBRACKETS.  # noqa: E501


        :return: The many of this APIConfigConstantsINSTANCEPOPULATIONBRACKETS.  # noqa: E501
        :rtype: APIConfigConstantsINSTANCEPOPULATIONBRACKETSMANY
        """
        return self._many

    @many.setter
    def many(self, many):
        """Sets the many of this APIConfigConstantsINSTANCEPOPULATIONBRACKETS.


        :param many: The many of this APIConfigConstantsINSTANCEPOPULATIONBRACKETS.  # noqa: E501
        :type many: APIConfigConstantsINSTANCEPOPULATIONBRACKETSMANY
        """

        self._many = many

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
        if not isinstance(other, APIConfigConstantsINSTANCEPOPULATIONBRACKETS):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, APIConfigConstantsINSTANCEPOPULATIONBRACKETS):
            return True

        return self.to_dict() != other.to_dict()
