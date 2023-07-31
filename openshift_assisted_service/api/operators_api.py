# coding: utf-8

"""
    AssistedInstall

    Assisted installation  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError
from typing_extensions import Annotated

from pydantic import Field, StrictStr

from typing import List, Optional

from openshift_assisted_service.models.monitored_operator import MonitoredOperator
from openshift_assisted_service.models.operator_monitor_report import OperatorMonitorReport
from openshift_assisted_service.models.operator_property import OperatorProperty

from openshift_assisted_service.api_client import ApiClient
from openshift_assisted_service.api_response import ApiResponse
from openshift_assisted_service.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class OperatorsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def v2_list_of_cluster_operators(self, cluster_id : Annotated[StrictStr, Field(..., description="The cluster to return operators for.")], operator_name : Annotated[Optional[StrictStr], Field(description="An operator in the specified cluster to return its data.")] = None, **kwargs) -> List[MonitoredOperator]:  # noqa: E501
        """v2_list_of_cluster_operators  # noqa: E501

        Lists operators to be monitored for a cluster.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.v2_list_of_cluster_operators(cluster_id, operator_name, async_req=True)
        >>> result = thread.get()

        :param cluster_id: The cluster to return operators for. (required)
        :type cluster_id: str
        :param operator_name: An operator in the specified cluster to return its data.
        :type operator_name: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: List[MonitoredOperator]
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the v2_list_of_cluster_operators_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.v2_list_of_cluster_operators_with_http_info(cluster_id, operator_name, **kwargs)  # noqa: E501

    @validate_arguments
    def v2_list_of_cluster_operators_with_http_info(self, cluster_id : Annotated[StrictStr, Field(..., description="The cluster to return operators for.")], operator_name : Annotated[Optional[StrictStr], Field(description="An operator in the specified cluster to return its data.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """v2_list_of_cluster_operators  # noqa: E501

        Lists operators to be monitored for a cluster.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.v2_list_of_cluster_operators_with_http_info(cluster_id, operator_name, async_req=True)
        >>> result = thread.get()

        :param cluster_id: The cluster to return operators for. (required)
        :type cluster_id: str
        :param operator_name: An operator in the specified cluster to return its data.
        :type operator_name: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(List[MonitoredOperator], status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'cluster_id',
            'operator_name'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v2_list_of_cluster_operators" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['cluster_id']:
            _path_params['cluster_id'] = _params['cluster_id']


        # process the query parameters
        _query_params = []
        if _params.get('operator_name') is not None:  # noqa: E501
            _query_params.append(('operator_name', _params['operator_name']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['agentAuth']  # noqa: E501

        _response_types_map = {
            '200': "List[MonitoredOperator]",
            '401': "InfraError",
            '403': "InfraError",
            '404': "Error",
            '405': "Error",
            '500': "Error",
        }

        return self.api_client.call_api(
            '/v2/clusters/{cluster_id}/monitored-operators', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def v2_list_operator_properties(self, operator_name : Annotated[StrictStr, Field(..., description="The operator name.")], **kwargs) -> List[OperatorProperty]:  # noqa: E501
        """v2_list_operator_properties  # noqa: E501

        Lists properties for an operator.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.v2_list_operator_properties(operator_name, async_req=True)
        >>> result = thread.get()

        :param operator_name: The operator name. (required)
        :type operator_name: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: List[OperatorProperty]
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the v2_list_operator_properties_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.v2_list_operator_properties_with_http_info(operator_name, **kwargs)  # noqa: E501

    @validate_arguments
    def v2_list_operator_properties_with_http_info(self, operator_name : Annotated[StrictStr, Field(..., description="The operator name.")], **kwargs) -> ApiResponse:  # noqa: E501
        """v2_list_operator_properties  # noqa: E501

        Lists properties for an operator.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.v2_list_operator_properties_with_http_info(operator_name, async_req=True)
        >>> result = thread.get()

        :param operator_name: The operator name. (required)
        :type operator_name: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(List[OperatorProperty], status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'operator_name'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v2_list_operator_properties" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['operator_name']:
            _path_params['operator_name'] = _params['operator_name']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['userAuth']  # noqa: E501

        _response_types_map = {
            '200': "List[OperatorProperty]",
            '401': "InfraError",
            '403': "InfraError",
            '404': "Error",
            '500': "Error",
        }

        return self.api_client.call_api(
            '/v2/supported-operators/{operator_name}', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def v2_list_supported_operators(self, **kwargs) -> List[str]:  # noqa: E501
        """v2_list_supported_operators  # noqa: E501

        Retrieves the list of supported operators.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.v2_list_supported_operators(async_req=True)
        >>> result = thread.get()

        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: List[str]
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the v2_list_supported_operators_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.v2_list_supported_operators_with_http_info(**kwargs)  # noqa: E501

    @validate_arguments
    def v2_list_supported_operators_with_http_info(self, **kwargs) -> ApiResponse:  # noqa: E501
        """v2_list_supported_operators  # noqa: E501

        Retrieves the list of supported operators.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.v2_list_supported_operators_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(List[str], status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v2_list_supported_operators" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['userAuth']  # noqa: E501

        _response_types_map = {
            '200': "List[str]",
            '401': "InfraError",
            '403': "InfraError",
            '500': "Error",
        }

        return self.api_client.call_api(
            '/v2/supported-operators', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def v2_report_monitored_operator_status(self, cluster_id : Annotated[StrictStr, Field(..., description="The cluster whose operators are being monitored.")], report_params : Annotated[OperatorMonitorReport, Field(..., description="The operators monitor report.")], **kwargs) -> None:  # noqa: E501
        """v2_report_monitored_operator_status  # noqa: E501

        Controller API to report of monitored operators.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.v2_report_monitored_operator_status(cluster_id, report_params, async_req=True)
        >>> result = thread.get()

        :param cluster_id: The cluster whose operators are being monitored. (required)
        :type cluster_id: str
        :param report_params: The operators monitor report. (required)
        :type report_params: OperatorMonitorReport
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the v2_report_monitored_operator_status_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.v2_report_monitored_operator_status_with_http_info(cluster_id, report_params, **kwargs)  # noqa: E501

    @validate_arguments
    def v2_report_monitored_operator_status_with_http_info(self, cluster_id : Annotated[StrictStr, Field(..., description="The cluster whose operators are being monitored.")], report_params : Annotated[OperatorMonitorReport, Field(..., description="The operators monitor report.")], **kwargs) -> ApiResponse:  # noqa: E501
        """v2_report_monitored_operator_status  # noqa: E501

        Controller API to report of monitored operators.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.v2_report_monitored_operator_status_with_http_info(cluster_id, report_params, async_req=True)
        >>> result = thread.get()

        :param cluster_id: The cluster whose operators are being monitored. (required)
        :type cluster_id: str
        :param report_params: The operators monitor report. (required)
        :type report_params: OperatorMonitorReport
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        _params = locals()

        _all_params = [
            'cluster_id',
            'report_params'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v2_report_monitored_operator_status" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['cluster_id']:
            _path_params['cluster_id'] = _params['cluster_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['report_params'] is not None:
            _body_params = _params['report_params']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['agentAuth']  # noqa: E501

        _response_types_map = {}

        return self.api_client.call_api(
            '/v2/clusters/{cluster_id}/monitored-operators', 'PUT',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
