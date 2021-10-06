"""
    VRChat API Documentation


    The version of the OpenAPI document: 1.4.1
    Contact: me@ruby.js.org
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from vrchatapi.api_client import ApiClient, Endpoint as _Endpoint
from vrchatapi.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from vrchatapi.model.inline_response400 import InlineResponse400
from vrchatapi.model.invite_message import InviteMessage
from vrchatapi.model.invite_request import InviteRequest
from vrchatapi.model.invite_response import InviteResponse
from vrchatapi.model.notification import Notification


class InviteApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __get_invite_message(
            self,
            user_id,
            message_type,
            message_id,
            **kwargs
        ):
            """Get Invite Messages  # noqa: E501

            Returns a single Invite Message. This returns the exact same information but less than `getInviteMessages`. Admin Credentials are required to view messages of other users!  Message type refers to a different collection of messages, used during different types of responses.  * `message` = Message during a normal invite * `response` = Message when replying to a message * `request` = Message when requesting an invite * `requestResponse` = Message when replying to a request for invite  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_invite_message(user_id, message_type, message_id, async_req=True)
            >>> result = thread.get()

            Args:
                user_id (str):
                message_type (str):
                message_id (int):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                InviteMessage
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['user_id'] = \
                user_id
            kwargs['message_type'] = \
                message_type
            kwargs['message_id'] = \
                message_id
            return self.call_with_http_info(**kwargs)

        self.get_invite_message = _Endpoint(
            settings={
                'response_type': (InviteMessage,),
                'auth': [
                    'apiKeyCookie',
                    'authCookie'
                ],
                'endpoint_path': '/message/{userId}/{messageType}/{messageId}',
                'operation_id': 'get_invite_message',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'user_id',
                    'message_type',
                    'message_id',
                ],
                'required': [
                    'user_id',
                    'message_type',
                    'message_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'message_type',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('message_type',): {

                        "MESSAGE": "message",
                        "RESPONSE": "response",
                        "REQUEST": "request",
                        "REQUESTRESPONSE": "requestResponse"
                    },
                },
                'openapi_types': {
                    'user_id':
                        (str,),
                    'message_type':
                        (str,),
                    'message_id':
                        (int,),
                },
                'attribute_map': {
                    'user_id': 'userId',
                    'message_type': 'messageType',
                    'message_id': 'messageId',
                },
                'location_map': {
                    'user_id': 'path',
                    'message_type': 'path',
                    'message_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_invite_message
        )

        def __get_invite_messages(
            self,
            user_id,
            message_type,
            **kwargs
        ):
            """List Invite Messages  # noqa: E501

            Returns a list of all the users Invite Messages. Admin Credentials are required to view messages of other users!  Message type refers to a different collection of messages, used during different types of responses.  * `message` = Message during a normal invite * `response` = Message when replying to a message * `request` = Message when requesting an invite * `requestResponse` = Message when replying to a request for invite  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_invite_messages(user_id, message_type, async_req=True)
            >>> result = thread.get()

            Args:
                user_id (str):
                message_type (str):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                [InviteMessage]
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['user_id'] = \
                user_id
            kwargs['message_type'] = \
                message_type
            return self.call_with_http_info(**kwargs)

        self.get_invite_messages = _Endpoint(
            settings={
                'response_type': ([InviteMessage],),
                'auth': [
                    'apiKeyCookie',
                    'authCookie'
                ],
                'endpoint_path': '/message/{userId}/{messageType}',
                'operation_id': 'get_invite_messages',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'user_id',
                    'message_type',
                ],
                'required': [
                    'user_id',
                    'message_type',
                ],
                'nullable': [
                ],
                'enum': [
                    'message_type',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('message_type',): {

                        "MESSAGE": "message",
                        "RESPONSE": "response",
                        "REQUEST": "request",
                        "REQUESTRESPONSE": "requestResponse"
                    },
                },
                'openapi_types': {
                    'user_id':
                        (str,),
                    'message_type':
                        (str,),
                },
                'attribute_map': {
                    'user_id': 'userId',
                    'message_type': 'messageType',
                },
                'location_map': {
                    'user_id': 'path',
                    'message_type': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_invite_messages
        )

        def __invite_user(
            self,
            user_id,
            **kwargs
        ):
            """Invite User  # noqa: E501

            Sends an invite to a user. Returns the Notification of type `invite` that was sent.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.invite_user(user_id, async_req=True)
            >>> result = thread.get()

            Args:
                user_id (str):

            Keyword Args:
                invite_request (InviteRequest): Instance ID when inviting a user.. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                Notification
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['user_id'] = \
                user_id
            return self.call_with_http_info(**kwargs)

        self.invite_user = _Endpoint(
            settings={
                'response_type': (Notification,),
                'auth': [
                    'apiKeyCookie',
                    'authCookie'
                ],
                'endpoint_path': '/invite/{userId}',
                'operation_id': 'invite_user',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'user_id',
                    'invite_request',
                ],
                'required': [
                    'user_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'user_id':
                        (str,),
                    'invite_request':
                        (InviteRequest,),
                },
                'attribute_map': {
                    'user_id': 'userId',
                },
                'location_map': {
                    'user_id': 'path',
                    'invite_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__invite_user
        )

        def __request_invite(
            self,
            user_id,
            **kwargs
        ):
            """Request Invite  # noqa: E501

            Requests an invite from a user. Returns the Notification of type `requestInvite` that was sent.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.request_invite(user_id, async_req=True)
            >>> result = thread.get()

            Args:
                user_id (str):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                Notification
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['user_id'] = \
                user_id
            return self.call_with_http_info(**kwargs)

        self.request_invite = _Endpoint(
            settings={
                'response_type': (Notification,),
                'auth': [
                    'apiKeyCookie',
                    'authCookie'
                ],
                'endpoint_path': '/requestInvite/{userId}',
                'operation_id': 'request_invite',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'user_id',
                ],
                'required': [
                    'user_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'user_id':
                        (str,),
                },
                'attribute_map': {
                    'user_id': 'userId',
                },
                'location_map': {
                    'user_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__request_invite
        )

        def __reset_invite_message(
            self,
            user_id,
            message_type,
            message_id,
            **kwargs
        ):
            """Reset Invite Message  # noqa: E501

            Resets a single Invite Message back to it's original message, and then returns a list of all of them. Admin Credentials are required to update messages of other users!  Resetting a message respects the rate-limit, but resetting it does not set the rate-limit to 60 like when editing it. It is possible to edit it right after resetting it. Trying to edit a message before the cooldown timer expires results in a 429 Too Fast Error.  Message type refers to a different collection of messages, used during different types of responses.  * `message` = Message during a normal invite * `response` = Message when replying to a message * `request` = Message when requesting an invite * `requestResponse` = Message when replying to a request for invite  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.reset_invite_message(user_id, message_type, message_id, async_req=True)
            >>> result = thread.get()

            Args:
                user_id (str):
                message_type (str):
                message_id (int):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                [InviteMessage]
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['user_id'] = \
                user_id
            kwargs['message_type'] = \
                message_type
            kwargs['message_id'] = \
                message_id
            return self.call_with_http_info(**kwargs)

        self.reset_invite_message = _Endpoint(
            settings={
                'response_type': ([InviteMessage],),
                'auth': [
                    'apiKeyCookie',
                    'authCookie'
                ],
                'endpoint_path': '/message/{userId}/{messageType}/{messageId}',
                'operation_id': 'reset_invite_message',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'user_id',
                    'message_type',
                    'message_id',
                ],
                'required': [
                    'user_id',
                    'message_type',
                    'message_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'message_type',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('message_type',): {

                        "MESSAGE": "message",
                        "RESPONSE": "response",
                        "REQUEST": "request",
                        "REQUESTRESPONSE": "requestResponse"
                    },
                },
                'openapi_types': {
                    'user_id':
                        (str,),
                    'message_type':
                        (str,),
                    'message_id':
                        (int,),
                },
                'attribute_map': {
                    'user_id': 'userId',
                    'message_type': 'messageType',
                    'message_id': 'messageId',
                },
                'location_map': {
                    'user_id': 'path',
                    'message_type': 'path',
                    'message_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__reset_invite_message
        )

        def __respond_invite(
            self,
            notification_id,
            **kwargs
        ):
            """Respond Invite  # noqa: E501

            Sends a world invite to a user.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.respond_invite(notification_id, async_req=True)
            >>> result = thread.get()

            Args:
                notification_id (str):

            Keyword Args:
                invite_response (InviteResponse): Instance ID when inviting a user.. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                Notification
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['notification_id'] = \
                notification_id
            return self.call_with_http_info(**kwargs)

        self.respond_invite = _Endpoint(
            settings={
                'response_type': (Notification,),
                'auth': [
                    'apiKeyCookie',
                    'authCookie'
                ],
                'endpoint_path': '/invite/{notificationId}/response',
                'operation_id': 'respond_invite',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'notification_id',
                    'invite_response',
                ],
                'required': [
                    'notification_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'notification_id':
                        (str,),
                    'invite_response':
                        (InviteResponse,),
                },
                'attribute_map': {
                    'notification_id': 'notificationId',
                },
                'location_map': {
                    'notification_id': 'path',
                    'invite_response': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__respond_invite
        )

        def __update_invite_message(
            self,
            user_id,
            message_type,
            message_id,
            **kwargs
        ):
            """Update Invite Message  # noqa: E501

            Updates a single Invite Message and then returns a list of all of them. Admin Credentials are required to update messages of other users!  Updating a message automatically sets the cooldown timer to 60 minutes. Trying to edit a message before the cooldown timer expires results in a 429 Too Fast Error.  Message type refers to a different collection of messages, used during different types of responses.  * `message` = Message during a normal invite * `response` = Message when replying to a message * `request` = Message when requesting an invite * `requestResponse` = Message when replying to a request for invite  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.update_invite_message(user_id, message_type, message_id, async_req=True)
            >>> result = thread.get()

            Args:
                user_id (str):
                message_type (str):
                message_id (int):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                [InviteMessage]
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['user_id'] = \
                user_id
            kwargs['message_type'] = \
                message_type
            kwargs['message_id'] = \
                message_id
            return self.call_with_http_info(**kwargs)

        self.update_invite_message = _Endpoint(
            settings={
                'response_type': ([InviteMessage],),
                'auth': [
                    'apiKeyCookie',
                    'authCookie'
                ],
                'endpoint_path': '/message/{userId}/{messageType}/{messageId}',
                'operation_id': 'update_invite_message',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'user_id',
                    'message_type',
                    'message_id',
                ],
                'required': [
                    'user_id',
                    'message_type',
                    'message_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'message_type',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('message_type',): {

                        "MESSAGE": "message",
                        "RESPONSE": "response",
                        "REQUEST": "request",
                        "REQUESTRESPONSE": "requestResponse"
                    },
                },
                'openapi_types': {
                    'user_id':
                        (str,),
                    'message_type':
                        (str,),
                    'message_id':
                        (int,),
                },
                'attribute_map': {
                    'user_id': 'userId',
                    'message_type': 'messageType',
                    'message_id': 'messageId',
                },
                'location_map': {
                    'user_id': 'path',
                    'message_type': 'path',
                    'message_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__update_invite_message
        )
