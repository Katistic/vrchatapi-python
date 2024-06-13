# coding: utf-8

"""
    VRChat API Documentation


    The version of the OpenAPI document: 1.17.6
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


class Subscription(object):
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
        'steam_item_id': 'str',
        'oculus_sku': 'str',
        'google_product_id': 'str',
        'google_plan_id': 'str',
        'pico_sku': 'str',
        'amount': 'float',
        'description': 'str',
        'period': 'SubscriptionPeriod',
        'tier': 'float'
    }

    attribute_map = {
        'id': 'id',
        'steam_item_id': 'steamItemId',
        'oculus_sku': 'oculusSku',
        'google_product_id': 'googleProductId',
        'google_plan_id': 'googlePlanId',
        'pico_sku': 'picoSku',
        'amount': 'amount',
        'description': 'description',
        'period': 'period',
        'tier': 'tier'
    }

    def __init__(self, id=None, steam_item_id=None, oculus_sku=None, google_product_id=None, google_plan_id=None, pico_sku=None, amount=None, description=None, period=None, tier=None, local_vars_configuration=None):  # noqa: E501
        """Subscription - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._steam_item_id = None
        self._oculus_sku = None
        self._google_product_id = None
        self._google_plan_id = None
        self._pico_sku = None
        self._amount = None
        self._description = None
        self._period = None
        self._tier = None
        self.discriminator = None

        self.id = id
        self.steam_item_id = steam_item_id
        if oculus_sku is not None:
            self.oculus_sku = oculus_sku
        if google_product_id is not None:
            self.google_product_id = google_product_id
        if google_plan_id is not None:
            self.google_plan_id = google_plan_id
        if pico_sku is not None:
            self.pico_sku = pico_sku
        self.amount = amount
        self.description = description
        self.period = period
        self.tier = tier

    @property
    def id(self):
        """Gets the id of this Subscription.  # noqa: E501


        :return: The id of this Subscription.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Subscription.


        :param id: The id of this Subscription.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                id is not None and len(id) < 1):
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `1`")  # noqa: E501

        self._id = id

    @property
    def steam_item_id(self):
        """Gets the steam_item_id of this Subscription.  # noqa: E501


        :return: The steam_item_id of this Subscription.  # noqa: E501
        :rtype: str
        """
        return self._steam_item_id

    @steam_item_id.setter
    def steam_item_id(self, steam_item_id):
        """Sets the steam_item_id of this Subscription.


        :param steam_item_id: The steam_item_id of this Subscription.  # noqa: E501
        :type steam_item_id: str
        """
        if self.local_vars_configuration.client_side_validation and steam_item_id is None:  # noqa: E501
            raise ValueError("Invalid value for `steam_item_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                steam_item_id is not None and len(steam_item_id) < 1):
            raise ValueError("Invalid value for `steam_item_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._steam_item_id = steam_item_id

    @property
    def oculus_sku(self):
        """Gets the oculus_sku of this Subscription.  # noqa: E501


        :return: The oculus_sku of this Subscription.  # noqa: E501
        :rtype: str
        """
        return self._oculus_sku

    @oculus_sku.setter
    def oculus_sku(self, oculus_sku):
        """Sets the oculus_sku of this Subscription.


        :param oculus_sku: The oculus_sku of this Subscription.  # noqa: E501
        :type oculus_sku: str
        """
        if (self.local_vars_configuration.client_side_validation and
                oculus_sku is not None and len(oculus_sku) < 1):
            raise ValueError("Invalid value for `oculus_sku`, length must be greater than or equal to `1`")  # noqa: E501

        self._oculus_sku = oculus_sku

    @property
    def google_product_id(self):
        """Gets the google_product_id of this Subscription.  # noqa: E501


        :return: The google_product_id of this Subscription.  # noqa: E501
        :rtype: str
        """
        return self._google_product_id

    @google_product_id.setter
    def google_product_id(self, google_product_id):
        """Sets the google_product_id of this Subscription.


        :param google_product_id: The google_product_id of this Subscription.  # noqa: E501
        :type google_product_id: str
        """
        if (self.local_vars_configuration.client_side_validation and
                google_product_id is not None and len(google_product_id) < 1):
            raise ValueError("Invalid value for `google_product_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._google_product_id = google_product_id

    @property
    def google_plan_id(self):
        """Gets the google_plan_id of this Subscription.  # noqa: E501


        :return: The google_plan_id of this Subscription.  # noqa: E501
        :rtype: str
        """
        return self._google_plan_id

    @google_plan_id.setter
    def google_plan_id(self, google_plan_id):
        """Sets the google_plan_id of this Subscription.


        :param google_plan_id: The google_plan_id of this Subscription.  # noqa: E501
        :type google_plan_id: str
        """

        self._google_plan_id = google_plan_id

    @property
    def pico_sku(self):
        """Gets the pico_sku of this Subscription.  # noqa: E501


        :return: The pico_sku of this Subscription.  # noqa: E501
        :rtype: str
        """
        return self._pico_sku

    @pico_sku.setter
    def pico_sku(self, pico_sku):
        """Sets the pico_sku of this Subscription.


        :param pico_sku: The pico_sku of this Subscription.  # noqa: E501
        :type pico_sku: str
        """
        if (self.local_vars_configuration.client_side_validation and
                pico_sku is not None and len(pico_sku) < 1):
            raise ValueError("Invalid value for `pico_sku`, length must be greater than or equal to `1`")  # noqa: E501

        self._pico_sku = pico_sku

    @property
    def amount(self):
        """Gets the amount of this Subscription.  # noqa: E501


        :return: The amount of this Subscription.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this Subscription.


        :param amount: The amount of this Subscription.  # noqa: E501
        :type amount: float
        """
        if self.local_vars_configuration.client_side_validation and amount is None:  # noqa: E501
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def description(self):
        """Gets the description of this Subscription.  # noqa: E501


        :return: The description of this Subscription.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Subscription.


        :param description: The description of this Subscription.  # noqa: E501
        :type description: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def period(self):
        """Gets the period of this Subscription.  # noqa: E501


        :return: The period of this Subscription.  # noqa: E501
        :rtype: SubscriptionPeriod
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this Subscription.


        :param period: The period of this Subscription.  # noqa: E501
        :type period: SubscriptionPeriod
        """
        if self.local_vars_configuration.client_side_validation and period is None:  # noqa: E501
            raise ValueError("Invalid value for `period`, must not be `None`")  # noqa: E501

        self._period = period

    @property
    def tier(self):
        """Gets the tier of this Subscription.  # noqa: E501


        :return: The tier of this Subscription.  # noqa: E501
        :rtype: float
        """
        return self._tier

    @tier.setter
    def tier(self, tier):
        """Sets the tier of this Subscription.


        :param tier: The tier of this Subscription.  # noqa: E501
        :type tier: float
        """
        if self.local_vars_configuration.client_side_validation and tier is None:  # noqa: E501
            raise ValueError("Invalid value for `tier`, must not be `None`")  # noqa: E501

        self._tier = tier

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
        if not isinstance(other, Subscription):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Subscription):
            return True

        return self.to_dict() != other.to_dict()
