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


class APIConfigMinSupportedClientBuildNumber(object):
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
        'app_store': 'PlatformBuildInfo',
        'default': 'PlatformBuildInfo',
        'firebase': 'PlatformBuildInfo',
        'firebasei_os': 'PlatformBuildInfo',
        'google_play': 'PlatformBuildInfo',
        'pc': 'PlatformBuildInfo',
        'pico_store': 'PlatformBuildInfo',
        'quest_app_lab': 'PlatformBuildInfo',
        'quest_store': 'PlatformBuildInfo',
        'test_flight': 'PlatformBuildInfo',
        'xr_elite': 'PlatformBuildInfo'
    }

    attribute_map = {
        'app_store': 'AppStore',
        'default': 'Default',
        'firebase': 'Firebase',
        'firebasei_os': 'FirebaseiOS',
        'google_play': 'GooglePlay',
        'pc': 'PC',
        'pico_store': 'PicoStore',
        'quest_app_lab': 'QuestAppLab',
        'quest_store': 'QuestStore',
        'test_flight': 'TestFlight',
        'xr_elite': 'XRElite'
    }

    def __init__(self, app_store=None, default=None, firebase=None, firebasei_os=None, google_play=None, pc=None, pico_store=None, quest_app_lab=None, quest_store=None, test_flight=None, xr_elite=None, local_vars_configuration=None):  # noqa: E501
        """APIConfigMinSupportedClientBuildNumber - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._app_store = None
        self._default = None
        self._firebase = None
        self._firebasei_os = None
        self._google_play = None
        self._pc = None
        self._pico_store = None
        self._quest_app_lab = None
        self._quest_store = None
        self._test_flight = None
        self._xr_elite = None
        self.discriminator = None

        self.app_store = app_store
        self.default = default
        self.firebase = firebase
        self.firebasei_os = firebasei_os
        self.google_play = google_play
        self.pc = pc
        self.pico_store = pico_store
        self.quest_app_lab = quest_app_lab
        self.quest_store = quest_store
        self.test_flight = test_flight
        self.xr_elite = xr_elite

    @property
    def app_store(self):
        """Gets the app_store of this APIConfigMinSupportedClientBuildNumber.  # noqa: E501


        :return: The app_store of this APIConfigMinSupportedClientBuildNumber.  # noqa: E501
        :rtype: PlatformBuildInfo
        """
        return self._app_store

    @app_store.setter
    def app_store(self, app_store):
        """Sets the app_store of this APIConfigMinSupportedClientBuildNumber.


        :param app_store: The app_store of this APIConfigMinSupportedClientBuildNumber.  # noqa: E501
        :type app_store: PlatformBuildInfo
        """
        if self.local_vars_configuration.client_side_validation and app_store is None:  # noqa: E501
            raise ValueError("Invalid value for `app_store`, must not be `None`")  # noqa: E501

        self._app_store = app_store

    @property
    def default(self):
        """Gets the default of this APIConfigMinSupportedClientBuildNumber.  # noqa: E501


        :return: The default of this APIConfigMinSupportedClientBuildNumber.  # noqa: E501
        :rtype: PlatformBuildInfo
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this APIConfigMinSupportedClientBuildNumber.


        :param default: The default of this APIConfigMinSupportedClientBuildNumber.  # noqa: E501
        :type default: PlatformBuildInfo
        """
        if self.local_vars_configuration.client_side_validation and default is None:  # noqa: E501
            raise ValueError("Invalid value for `default`, must not be `None`")  # noqa: E501

        self._default = default

    @property
    def firebase(self):
        """Gets the firebase of this APIConfigMinSupportedClientBuildNumber.  # noqa: E501


        :return: The firebase of this APIConfigMinSupportedClientBuildNumber.  # noqa: E501
        :rtype: PlatformBuildInfo
        """
        return self._firebase

    @firebase.setter
    def firebase(self, firebase):
        """Sets the firebase of this APIConfigMinSupportedClientBuildNumber.


        :param firebase: The firebase of this APIConfigMinSupportedClientBuildNumber.  # noqa: E501
        :type firebase: PlatformBuildInfo
        """
        if self.local_vars_configuration.client_side_validation and firebase is None:  # noqa: E501
            raise ValueError("Invalid value for `firebase`, must not be `None`")  # noqa: E501

        self._firebase = firebase

    @property
    def firebasei_os(self):
        """Gets the firebasei_os of this APIConfigMinSupportedClientBuildNumber.  # noqa: E501


        :return: The firebasei_os of this APIConfigMinSupportedClientBuildNumber.  # noqa: E501
        :rtype: PlatformBuildInfo
        """
        return self._firebasei_os

    @firebasei_os.setter
    def firebasei_os(self, firebasei_os):
        """Sets the firebasei_os of this APIConfigMinSupportedClientBuildNumber.


        :param firebasei_os: The firebasei_os of this APIConfigMinSupportedClientBuildNumber.  # noqa: E501
        :type firebasei_os: PlatformBuildInfo
        """
        if self.local_vars_configuration.client_side_validation and firebasei_os is None:  # noqa: E501
            raise ValueError("Invalid value for `firebasei_os`, must not be `None`")  # noqa: E501

        self._firebasei_os = firebasei_os

    @property
    def google_play(self):
        """Gets the google_play of this APIConfigMinSupportedClientBuildNumber.  # noqa: E501


        :return: The google_play of this APIConfigMinSupportedClientBuildNumber.  # noqa: E501
        :rtype: PlatformBuildInfo
        """
        return self._google_play

    @google_play.setter
    def google_play(self, google_play):
        """Sets the google_play of this APIConfigMinSupportedClientBuildNumber.


        :param google_play: The google_play of this APIConfigMinSupportedClientBuildNumber.  # noqa: E501
        :type google_play: PlatformBuildInfo
        """
        if self.local_vars_configuration.client_side_validation and google_play is None:  # noqa: E501
            raise ValueError("Invalid value for `google_play`, must not be `None`")  # noqa: E501

        self._google_play = google_play

    @property
    def pc(self):
        """Gets the pc of this APIConfigMinSupportedClientBuildNumber.  # noqa: E501


        :return: The pc of this APIConfigMinSupportedClientBuildNumber.  # noqa: E501
        :rtype: PlatformBuildInfo
        """
        return self._pc

    @pc.setter
    def pc(self, pc):
        """Sets the pc of this APIConfigMinSupportedClientBuildNumber.


        :param pc: The pc of this APIConfigMinSupportedClientBuildNumber.  # noqa: E501
        :type pc: PlatformBuildInfo
        """
        if self.local_vars_configuration.client_side_validation and pc is None:  # noqa: E501
            raise ValueError("Invalid value for `pc`, must not be `None`")  # noqa: E501

        self._pc = pc

    @property
    def pico_store(self):
        """Gets the pico_store of this APIConfigMinSupportedClientBuildNumber.  # noqa: E501


        :return: The pico_store of this APIConfigMinSupportedClientBuildNumber.  # noqa: E501
        :rtype: PlatformBuildInfo
        """
        return self._pico_store

    @pico_store.setter
    def pico_store(self, pico_store):
        """Sets the pico_store of this APIConfigMinSupportedClientBuildNumber.


        :param pico_store: The pico_store of this APIConfigMinSupportedClientBuildNumber.  # noqa: E501
        :type pico_store: PlatformBuildInfo
        """
        if self.local_vars_configuration.client_side_validation and pico_store is None:  # noqa: E501
            raise ValueError("Invalid value for `pico_store`, must not be `None`")  # noqa: E501

        self._pico_store = pico_store

    @property
    def quest_app_lab(self):
        """Gets the quest_app_lab of this APIConfigMinSupportedClientBuildNumber.  # noqa: E501


        :return: The quest_app_lab of this APIConfigMinSupportedClientBuildNumber.  # noqa: E501
        :rtype: PlatformBuildInfo
        """
        return self._quest_app_lab

    @quest_app_lab.setter
    def quest_app_lab(self, quest_app_lab):
        """Sets the quest_app_lab of this APIConfigMinSupportedClientBuildNumber.


        :param quest_app_lab: The quest_app_lab of this APIConfigMinSupportedClientBuildNumber.  # noqa: E501
        :type quest_app_lab: PlatformBuildInfo
        """
        if self.local_vars_configuration.client_side_validation and quest_app_lab is None:  # noqa: E501
            raise ValueError("Invalid value for `quest_app_lab`, must not be `None`")  # noqa: E501

        self._quest_app_lab = quest_app_lab

    @property
    def quest_store(self):
        """Gets the quest_store of this APIConfigMinSupportedClientBuildNumber.  # noqa: E501


        :return: The quest_store of this APIConfigMinSupportedClientBuildNumber.  # noqa: E501
        :rtype: PlatformBuildInfo
        """
        return self._quest_store

    @quest_store.setter
    def quest_store(self, quest_store):
        """Sets the quest_store of this APIConfigMinSupportedClientBuildNumber.


        :param quest_store: The quest_store of this APIConfigMinSupportedClientBuildNumber.  # noqa: E501
        :type quest_store: PlatformBuildInfo
        """
        if self.local_vars_configuration.client_side_validation and quest_store is None:  # noqa: E501
            raise ValueError("Invalid value for `quest_store`, must not be `None`")  # noqa: E501

        self._quest_store = quest_store

    @property
    def test_flight(self):
        """Gets the test_flight of this APIConfigMinSupportedClientBuildNumber.  # noqa: E501


        :return: The test_flight of this APIConfigMinSupportedClientBuildNumber.  # noqa: E501
        :rtype: PlatformBuildInfo
        """
        return self._test_flight

    @test_flight.setter
    def test_flight(self, test_flight):
        """Sets the test_flight of this APIConfigMinSupportedClientBuildNumber.


        :param test_flight: The test_flight of this APIConfigMinSupportedClientBuildNumber.  # noqa: E501
        :type test_flight: PlatformBuildInfo
        """
        if self.local_vars_configuration.client_side_validation and test_flight is None:  # noqa: E501
            raise ValueError("Invalid value for `test_flight`, must not be `None`")  # noqa: E501

        self._test_flight = test_flight

    @property
    def xr_elite(self):
        """Gets the xr_elite of this APIConfigMinSupportedClientBuildNumber.  # noqa: E501


        :return: The xr_elite of this APIConfigMinSupportedClientBuildNumber.  # noqa: E501
        :rtype: PlatformBuildInfo
        """
        return self._xr_elite

    @xr_elite.setter
    def xr_elite(self, xr_elite):
        """Sets the xr_elite of this APIConfigMinSupportedClientBuildNumber.


        :param xr_elite: The xr_elite of this APIConfigMinSupportedClientBuildNumber.  # noqa: E501
        :type xr_elite: PlatformBuildInfo
        """
        if self.local_vars_configuration.client_side_validation and xr_elite is None:  # noqa: E501
            raise ValueError("Invalid value for `xr_elite`, must not be `None`")  # noqa: E501

        self._xr_elite = xr_elite

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
        if not isinstance(other, APIConfigMinSupportedClientBuildNumber):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, APIConfigMinSupportedClientBuildNumber):
            return True

        return self.to_dict() != other.to_dict()
