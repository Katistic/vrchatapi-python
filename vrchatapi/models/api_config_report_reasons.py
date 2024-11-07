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


class APIConfigReportReasons(object):
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
        'billing': 'ReportReason',
        'botting': 'ReportReason',
        'cancellation': 'ReportReason',
        'gore': 'ReportReason',
        'hacking': 'ReportReason',
        'harassing': 'ReportReason',
        'hateful': 'ReportReason',
        'impersonation': 'ReportReason',
        'inappropriate': 'ReportReason',
        'leaking': 'ReportReason',
        'malicious': 'ReportReason',
        'missing': 'ReportReason',
        'nudity': 'ReportReason',
        'renewal': 'ReportReason',
        'security': 'ReportReason',
        'service': 'ReportReason',
        'sexual': 'ReportReason',
        'threatening': 'ReportReason',
        'visuals': 'ReportReason'
    }

    attribute_map = {
        'billing': 'billing',
        'botting': 'botting',
        'cancellation': 'cancellation',
        'gore': 'gore',
        'hacking': 'hacking',
        'harassing': 'harassing',
        'hateful': 'hateful',
        'impersonation': 'impersonation',
        'inappropriate': 'inappropriate',
        'leaking': 'leaking',
        'malicious': 'malicious',
        'missing': 'missing',
        'nudity': 'nudity',
        'renewal': 'renewal',
        'security': 'security',
        'service': 'service',
        'sexual': 'sexual',
        'threatening': 'threatening',
        'visuals': 'visuals'
    }

    def __init__(self, billing=None, botting=None, cancellation=None, gore=None, hacking=None, harassing=None, hateful=None, impersonation=None, inappropriate=None, leaking=None, malicious=None, missing=None, nudity=None, renewal=None, security=None, service=None, sexual=None, threatening=None, visuals=None, local_vars_configuration=None):  # noqa: E501
        """APIConfigReportReasons - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._billing = None
        self._botting = None
        self._cancellation = None
        self._gore = None
        self._hacking = None
        self._harassing = None
        self._hateful = None
        self._impersonation = None
        self._inappropriate = None
        self._leaking = None
        self._malicious = None
        self._missing = None
        self._nudity = None
        self._renewal = None
        self._security = None
        self._service = None
        self._sexual = None
        self._threatening = None
        self._visuals = None
        self.discriminator = None

        self.billing = billing
        self.botting = botting
        self.cancellation = cancellation
        self.gore = gore
        self.hacking = hacking
        self.harassing = harassing
        self.hateful = hateful
        self.impersonation = impersonation
        self.inappropriate = inappropriate
        self.leaking = leaking
        self.malicious = malicious
        self.missing = missing
        self.nudity = nudity
        self.renewal = renewal
        self.security = security
        self.service = service
        self.sexual = sexual
        self.threatening = threatening
        self.visuals = visuals

    @property
    def billing(self):
        """Gets the billing of this APIConfigReportReasons.  # noqa: E501


        :return: The billing of this APIConfigReportReasons.  # noqa: E501
        :rtype: ReportReason
        """
        return self._billing

    @billing.setter
    def billing(self, billing):
        """Sets the billing of this APIConfigReportReasons.


        :param billing: The billing of this APIConfigReportReasons.  # noqa: E501
        :type billing: ReportReason
        """
        if self.local_vars_configuration.client_side_validation and billing is None:  # noqa: E501
            raise ValueError("Invalid value for `billing`, must not be `None`")  # noqa: E501

        self._billing = billing

    @property
    def botting(self):
        """Gets the botting of this APIConfigReportReasons.  # noqa: E501


        :return: The botting of this APIConfigReportReasons.  # noqa: E501
        :rtype: ReportReason
        """
        return self._botting

    @botting.setter
    def botting(self, botting):
        """Sets the botting of this APIConfigReportReasons.


        :param botting: The botting of this APIConfigReportReasons.  # noqa: E501
        :type botting: ReportReason
        """
        if self.local_vars_configuration.client_side_validation and botting is None:  # noqa: E501
            raise ValueError("Invalid value for `botting`, must not be `None`")  # noqa: E501

        self._botting = botting

    @property
    def cancellation(self):
        """Gets the cancellation of this APIConfigReportReasons.  # noqa: E501


        :return: The cancellation of this APIConfigReportReasons.  # noqa: E501
        :rtype: ReportReason
        """
        return self._cancellation

    @cancellation.setter
    def cancellation(self, cancellation):
        """Sets the cancellation of this APIConfigReportReasons.


        :param cancellation: The cancellation of this APIConfigReportReasons.  # noqa: E501
        :type cancellation: ReportReason
        """
        if self.local_vars_configuration.client_side_validation and cancellation is None:  # noqa: E501
            raise ValueError("Invalid value for `cancellation`, must not be `None`")  # noqa: E501

        self._cancellation = cancellation

    @property
    def gore(self):
        """Gets the gore of this APIConfigReportReasons.  # noqa: E501


        :return: The gore of this APIConfigReportReasons.  # noqa: E501
        :rtype: ReportReason
        """
        return self._gore

    @gore.setter
    def gore(self, gore):
        """Sets the gore of this APIConfigReportReasons.


        :param gore: The gore of this APIConfigReportReasons.  # noqa: E501
        :type gore: ReportReason
        """
        if self.local_vars_configuration.client_side_validation and gore is None:  # noqa: E501
            raise ValueError("Invalid value for `gore`, must not be `None`")  # noqa: E501

        self._gore = gore

    @property
    def hacking(self):
        """Gets the hacking of this APIConfigReportReasons.  # noqa: E501


        :return: The hacking of this APIConfigReportReasons.  # noqa: E501
        :rtype: ReportReason
        """
        return self._hacking

    @hacking.setter
    def hacking(self, hacking):
        """Sets the hacking of this APIConfigReportReasons.


        :param hacking: The hacking of this APIConfigReportReasons.  # noqa: E501
        :type hacking: ReportReason
        """
        if self.local_vars_configuration.client_side_validation and hacking is None:  # noqa: E501
            raise ValueError("Invalid value for `hacking`, must not be `None`")  # noqa: E501

        self._hacking = hacking

    @property
    def harassing(self):
        """Gets the harassing of this APIConfigReportReasons.  # noqa: E501


        :return: The harassing of this APIConfigReportReasons.  # noqa: E501
        :rtype: ReportReason
        """
        return self._harassing

    @harassing.setter
    def harassing(self, harassing):
        """Sets the harassing of this APIConfigReportReasons.


        :param harassing: The harassing of this APIConfigReportReasons.  # noqa: E501
        :type harassing: ReportReason
        """
        if self.local_vars_configuration.client_side_validation and harassing is None:  # noqa: E501
            raise ValueError("Invalid value for `harassing`, must not be `None`")  # noqa: E501

        self._harassing = harassing

    @property
    def hateful(self):
        """Gets the hateful of this APIConfigReportReasons.  # noqa: E501


        :return: The hateful of this APIConfigReportReasons.  # noqa: E501
        :rtype: ReportReason
        """
        return self._hateful

    @hateful.setter
    def hateful(self, hateful):
        """Sets the hateful of this APIConfigReportReasons.


        :param hateful: The hateful of this APIConfigReportReasons.  # noqa: E501
        :type hateful: ReportReason
        """
        if self.local_vars_configuration.client_side_validation and hateful is None:  # noqa: E501
            raise ValueError("Invalid value for `hateful`, must not be `None`")  # noqa: E501

        self._hateful = hateful

    @property
    def impersonation(self):
        """Gets the impersonation of this APIConfigReportReasons.  # noqa: E501


        :return: The impersonation of this APIConfigReportReasons.  # noqa: E501
        :rtype: ReportReason
        """
        return self._impersonation

    @impersonation.setter
    def impersonation(self, impersonation):
        """Sets the impersonation of this APIConfigReportReasons.


        :param impersonation: The impersonation of this APIConfigReportReasons.  # noqa: E501
        :type impersonation: ReportReason
        """
        if self.local_vars_configuration.client_side_validation and impersonation is None:  # noqa: E501
            raise ValueError("Invalid value for `impersonation`, must not be `None`")  # noqa: E501

        self._impersonation = impersonation

    @property
    def inappropriate(self):
        """Gets the inappropriate of this APIConfigReportReasons.  # noqa: E501


        :return: The inappropriate of this APIConfigReportReasons.  # noqa: E501
        :rtype: ReportReason
        """
        return self._inappropriate

    @inappropriate.setter
    def inappropriate(self, inappropriate):
        """Sets the inappropriate of this APIConfigReportReasons.


        :param inappropriate: The inappropriate of this APIConfigReportReasons.  # noqa: E501
        :type inappropriate: ReportReason
        """
        if self.local_vars_configuration.client_side_validation and inappropriate is None:  # noqa: E501
            raise ValueError("Invalid value for `inappropriate`, must not be `None`")  # noqa: E501

        self._inappropriate = inappropriate

    @property
    def leaking(self):
        """Gets the leaking of this APIConfigReportReasons.  # noqa: E501


        :return: The leaking of this APIConfigReportReasons.  # noqa: E501
        :rtype: ReportReason
        """
        return self._leaking

    @leaking.setter
    def leaking(self, leaking):
        """Sets the leaking of this APIConfigReportReasons.


        :param leaking: The leaking of this APIConfigReportReasons.  # noqa: E501
        :type leaking: ReportReason
        """
        if self.local_vars_configuration.client_side_validation and leaking is None:  # noqa: E501
            raise ValueError("Invalid value for `leaking`, must not be `None`")  # noqa: E501

        self._leaking = leaking

    @property
    def malicious(self):
        """Gets the malicious of this APIConfigReportReasons.  # noqa: E501


        :return: The malicious of this APIConfigReportReasons.  # noqa: E501
        :rtype: ReportReason
        """
        return self._malicious

    @malicious.setter
    def malicious(self, malicious):
        """Sets the malicious of this APIConfigReportReasons.


        :param malicious: The malicious of this APIConfigReportReasons.  # noqa: E501
        :type malicious: ReportReason
        """
        if self.local_vars_configuration.client_side_validation and malicious is None:  # noqa: E501
            raise ValueError("Invalid value for `malicious`, must not be `None`")  # noqa: E501

        self._malicious = malicious

    @property
    def missing(self):
        """Gets the missing of this APIConfigReportReasons.  # noqa: E501


        :return: The missing of this APIConfigReportReasons.  # noqa: E501
        :rtype: ReportReason
        """
        return self._missing

    @missing.setter
    def missing(self, missing):
        """Sets the missing of this APIConfigReportReasons.


        :param missing: The missing of this APIConfigReportReasons.  # noqa: E501
        :type missing: ReportReason
        """
        if self.local_vars_configuration.client_side_validation and missing is None:  # noqa: E501
            raise ValueError("Invalid value for `missing`, must not be `None`")  # noqa: E501

        self._missing = missing

    @property
    def nudity(self):
        """Gets the nudity of this APIConfigReportReasons.  # noqa: E501


        :return: The nudity of this APIConfigReportReasons.  # noqa: E501
        :rtype: ReportReason
        """
        return self._nudity

    @nudity.setter
    def nudity(self, nudity):
        """Sets the nudity of this APIConfigReportReasons.


        :param nudity: The nudity of this APIConfigReportReasons.  # noqa: E501
        :type nudity: ReportReason
        """
        if self.local_vars_configuration.client_side_validation and nudity is None:  # noqa: E501
            raise ValueError("Invalid value for `nudity`, must not be `None`")  # noqa: E501

        self._nudity = nudity

    @property
    def renewal(self):
        """Gets the renewal of this APIConfigReportReasons.  # noqa: E501


        :return: The renewal of this APIConfigReportReasons.  # noqa: E501
        :rtype: ReportReason
        """
        return self._renewal

    @renewal.setter
    def renewal(self, renewal):
        """Sets the renewal of this APIConfigReportReasons.


        :param renewal: The renewal of this APIConfigReportReasons.  # noqa: E501
        :type renewal: ReportReason
        """
        if self.local_vars_configuration.client_side_validation and renewal is None:  # noqa: E501
            raise ValueError("Invalid value for `renewal`, must not be `None`")  # noqa: E501

        self._renewal = renewal

    @property
    def security(self):
        """Gets the security of this APIConfigReportReasons.  # noqa: E501


        :return: The security of this APIConfigReportReasons.  # noqa: E501
        :rtype: ReportReason
        """
        return self._security

    @security.setter
    def security(self, security):
        """Sets the security of this APIConfigReportReasons.


        :param security: The security of this APIConfigReportReasons.  # noqa: E501
        :type security: ReportReason
        """
        if self.local_vars_configuration.client_side_validation and security is None:  # noqa: E501
            raise ValueError("Invalid value for `security`, must not be `None`")  # noqa: E501

        self._security = security

    @property
    def service(self):
        """Gets the service of this APIConfigReportReasons.  # noqa: E501


        :return: The service of this APIConfigReportReasons.  # noqa: E501
        :rtype: ReportReason
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this APIConfigReportReasons.


        :param service: The service of this APIConfigReportReasons.  # noqa: E501
        :type service: ReportReason
        """
        if self.local_vars_configuration.client_side_validation and service is None:  # noqa: E501
            raise ValueError("Invalid value for `service`, must not be `None`")  # noqa: E501

        self._service = service

    @property
    def sexual(self):
        """Gets the sexual of this APIConfigReportReasons.  # noqa: E501


        :return: The sexual of this APIConfigReportReasons.  # noqa: E501
        :rtype: ReportReason
        """
        return self._sexual

    @sexual.setter
    def sexual(self, sexual):
        """Sets the sexual of this APIConfigReportReasons.


        :param sexual: The sexual of this APIConfigReportReasons.  # noqa: E501
        :type sexual: ReportReason
        """
        if self.local_vars_configuration.client_side_validation and sexual is None:  # noqa: E501
            raise ValueError("Invalid value for `sexual`, must not be `None`")  # noqa: E501

        self._sexual = sexual

    @property
    def threatening(self):
        """Gets the threatening of this APIConfigReportReasons.  # noqa: E501


        :return: The threatening of this APIConfigReportReasons.  # noqa: E501
        :rtype: ReportReason
        """
        return self._threatening

    @threatening.setter
    def threatening(self, threatening):
        """Sets the threatening of this APIConfigReportReasons.


        :param threatening: The threatening of this APIConfigReportReasons.  # noqa: E501
        :type threatening: ReportReason
        """
        if self.local_vars_configuration.client_side_validation and threatening is None:  # noqa: E501
            raise ValueError("Invalid value for `threatening`, must not be `None`")  # noqa: E501

        self._threatening = threatening

    @property
    def visuals(self):
        """Gets the visuals of this APIConfigReportReasons.  # noqa: E501


        :return: The visuals of this APIConfigReportReasons.  # noqa: E501
        :rtype: ReportReason
        """
        return self._visuals

    @visuals.setter
    def visuals(self, visuals):
        """Sets the visuals of this APIConfigReportReasons.


        :param visuals: The visuals of this APIConfigReportReasons.  # noqa: E501
        :type visuals: ReportReason
        """
        if self.local_vars_configuration.client_side_validation and visuals is None:  # noqa: E501
            raise ValueError("Invalid value for `visuals`, must not be `None`")  # noqa: E501

        self._visuals = visuals

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
        if not isinstance(other, APIConfigReportReasons):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, APIConfigReportReasons):
            return True

        return self.to_dict() != other.to_dict()
