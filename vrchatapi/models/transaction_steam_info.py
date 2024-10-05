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


class TransactionSteamInfo(object):
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
        'wallet_info': 'TransactionSteamWalletInfo',
        'steam_id': 'str',
        'order_id': 'str',
        'steam_url': 'str',
        'trans_id': 'str'
    }

    attribute_map = {
        'wallet_info': 'walletInfo',
        'steam_id': 'steamId',
        'order_id': 'orderId',
        'steam_url': 'steamUrl',
        'trans_id': 'transId'
    }

    def __init__(self, wallet_info=None, steam_id=None, order_id=None, steam_url=None, trans_id=None, local_vars_configuration=None):  # noqa: E501
        """TransactionSteamInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._wallet_info = None
        self._steam_id = None
        self._order_id = None
        self._steam_url = None
        self._trans_id = None
        self.discriminator = None

        self.wallet_info = wallet_info
        self.steam_id = steam_id
        self.order_id = order_id
        self.steam_url = steam_url
        self.trans_id = trans_id

    @property
    def wallet_info(self):
        """Gets the wallet_info of this TransactionSteamInfo.  # noqa: E501


        :return: The wallet_info of this TransactionSteamInfo.  # noqa: E501
        :rtype: TransactionSteamWalletInfo
        """
        return self._wallet_info

    @wallet_info.setter
    def wallet_info(self, wallet_info):
        """Sets the wallet_info of this TransactionSteamInfo.


        :param wallet_info: The wallet_info of this TransactionSteamInfo.  # noqa: E501
        :type wallet_info: TransactionSteamWalletInfo
        """
        if self.local_vars_configuration.client_side_validation and wallet_info is None:  # noqa: E501
            raise ValueError("Invalid value for `wallet_info`, must not be `None`")  # noqa: E501

        self._wallet_info = wallet_info

    @property
    def steam_id(self):
        """Gets the steam_id of this TransactionSteamInfo.  # noqa: E501

        Steam User ID  # noqa: E501

        :return: The steam_id of this TransactionSteamInfo.  # noqa: E501
        :rtype: str
        """
        return self._steam_id

    @steam_id.setter
    def steam_id(self, steam_id):
        """Sets the steam_id of this TransactionSteamInfo.

        Steam User ID  # noqa: E501

        :param steam_id: The steam_id of this TransactionSteamInfo.  # noqa: E501
        :type steam_id: str
        """
        if self.local_vars_configuration.client_side_validation and steam_id is None:  # noqa: E501
            raise ValueError("Invalid value for `steam_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                steam_id is not None and len(steam_id) < 1):
            raise ValueError("Invalid value for `steam_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._steam_id = steam_id

    @property
    def order_id(self):
        """Gets the order_id of this TransactionSteamInfo.  # noqa: E501

        Steam Order ID  # noqa: E501

        :return: The order_id of this TransactionSteamInfo.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this TransactionSteamInfo.

        Steam Order ID  # noqa: E501

        :param order_id: The order_id of this TransactionSteamInfo.  # noqa: E501
        :type order_id: str
        """
        if self.local_vars_configuration.client_side_validation and order_id is None:  # noqa: E501
            raise ValueError("Invalid value for `order_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                order_id is not None and len(order_id) < 1):
            raise ValueError("Invalid value for `order_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._order_id = order_id

    @property
    def steam_url(self):
        """Gets the steam_url of this TransactionSteamInfo.  # noqa: E501

        Empty  # noqa: E501

        :return: The steam_url of this TransactionSteamInfo.  # noqa: E501
        :rtype: str
        """
        return self._steam_url

    @steam_url.setter
    def steam_url(self, steam_url):
        """Sets the steam_url of this TransactionSteamInfo.

        Empty  # noqa: E501

        :param steam_url: The steam_url of this TransactionSteamInfo.  # noqa: E501
        :type steam_url: str
        """
        if self.local_vars_configuration.client_side_validation and steam_url is None:  # noqa: E501
            raise ValueError("Invalid value for `steam_url`, must not be `None`")  # noqa: E501

        self._steam_url = steam_url

    @property
    def trans_id(self):
        """Gets the trans_id of this TransactionSteamInfo.  # noqa: E501

        Steam Transaction ID, NOT the same as VRChat TransactionID  # noqa: E501

        :return: The trans_id of this TransactionSteamInfo.  # noqa: E501
        :rtype: str
        """
        return self._trans_id

    @trans_id.setter
    def trans_id(self, trans_id):
        """Sets the trans_id of this TransactionSteamInfo.

        Steam Transaction ID, NOT the same as VRChat TransactionID  # noqa: E501

        :param trans_id: The trans_id of this TransactionSteamInfo.  # noqa: E501
        :type trans_id: str
        """
        if self.local_vars_configuration.client_side_validation and trans_id is None:  # noqa: E501
            raise ValueError("Invalid value for `trans_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                trans_id is not None and len(trans_id) < 1):
            raise ValueError("Invalid value for `trans_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._trans_id = trans_id

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
        if not isinstance(other, TransactionSteamInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TransactionSteamInfo):
            return True

        return self.to_dict() != other.to_dict()
