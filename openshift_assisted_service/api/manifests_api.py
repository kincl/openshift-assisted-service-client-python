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

from typing import List, Optional, Union

from openshift_assisted_service.models.create_manifest_params import CreateManifestParams
from openshift_assisted_service.models.manifest import Manifest
from openshift_assisted_service.models.update_manifest_params import UpdateManifestParams

from openshift_assisted_service.api_client import ApiClient
from openshift_assisted_service.api_response import ApiResponse
from openshift_assisted_service.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class ManifestsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def v2_create_cluster_manifest(self, cluster_id : Annotated[StrictStr, Field(..., description="The cluster for which a new manifest should be created.")], create_manifest_params : Annotated[CreateManifestParams, Field(..., description="The new manifest to create.")], **kwargs) -> Manifest:  # noqa: E501
        """v2_create_cluster_manifest  # noqa: E501

        Creates a manifest for customizing cluster installation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.v2_create_cluster_manifest(cluster_id, create_manifest_params, async_req=True)
        >>> result = thread.get()

        :param cluster_id: The cluster for which a new manifest should be created. (required)
        :type cluster_id: str
        :param create_manifest_params: The new manifest to create. (required)
        :type create_manifest_params: CreateManifestParams
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Manifest
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the v2_create_cluster_manifest_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.v2_create_cluster_manifest_with_http_info(cluster_id, create_manifest_params, **kwargs)  # noqa: E501

    @validate_arguments
    def v2_create_cluster_manifest_with_http_info(self, cluster_id : Annotated[StrictStr, Field(..., description="The cluster for which a new manifest should be created.")], create_manifest_params : Annotated[CreateManifestParams, Field(..., description="The new manifest to create.")], **kwargs) -> ApiResponse:  # noqa: E501
        """v2_create_cluster_manifest  # noqa: E501

        Creates a manifest for customizing cluster installation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.v2_create_cluster_manifest_with_http_info(cluster_id, create_manifest_params, async_req=True)
        >>> result = thread.get()

        :param cluster_id: The cluster for which a new manifest should be created. (required)
        :type cluster_id: str
        :param create_manifest_params: The new manifest to create. (required)
        :type create_manifest_params: CreateManifestParams
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
        :rtype: tuple(Manifest, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'cluster_id',
            'create_manifest_params'
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
                    " to method v2_create_cluster_manifest" % _key
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
        if _params['create_manifest_params'] is not None:
            _body_params = _params['create_manifest_params']

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
        _auth_settings = ['userAuth']  # noqa: E501

        _response_types_map = {
            '201': "Manifest",
            '400': "Error",
            '401': "InfraError",
            '403': "InfraError",
            '404': "Error",
            '405': "Error",
            '409': "Error",
            '500': "Error",
        }

        return self.api_client.call_api(
            '/v2/clusters/{cluster_id}/manifests', 'POST',
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
    def v2_delete_cluster_manifest(self, cluster_id : Annotated[StrictStr, Field(..., description="The cluster whose manifest should be deleted.")], file_name : Annotated[StrictStr, Field(..., description="The manifest file name to delete from the cluster.")], folder : Annotated[Optional[StrictStr], Field(description="The folder that contains the files. Manifests can be placed in 'manifests' or 'openshift' directories.")] = None, **kwargs) -> None:  # noqa: E501
        """v2_delete_cluster_manifest  # noqa: E501

        Deletes a manifest from the cluster.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.v2_delete_cluster_manifest(cluster_id, file_name, folder, async_req=True)
        >>> result = thread.get()

        :param cluster_id: The cluster whose manifest should be deleted. (required)
        :type cluster_id: str
        :param file_name: The manifest file name to delete from the cluster. (required)
        :type file_name: str
        :param folder: The folder that contains the files. Manifests can be placed in 'manifests' or 'openshift' directories.
        :type folder: str
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
            raise ValueError("Error! Please call the v2_delete_cluster_manifest_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.v2_delete_cluster_manifest_with_http_info(cluster_id, file_name, folder, **kwargs)  # noqa: E501

    @validate_arguments
    def v2_delete_cluster_manifest_with_http_info(self, cluster_id : Annotated[StrictStr, Field(..., description="The cluster whose manifest should be deleted.")], file_name : Annotated[StrictStr, Field(..., description="The manifest file name to delete from the cluster.")], folder : Annotated[Optional[StrictStr], Field(description="The folder that contains the files. Manifests can be placed in 'manifests' or 'openshift' directories.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """v2_delete_cluster_manifest  # noqa: E501

        Deletes a manifest from the cluster.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.v2_delete_cluster_manifest_with_http_info(cluster_id, file_name, folder, async_req=True)
        >>> result = thread.get()

        :param cluster_id: The cluster whose manifest should be deleted. (required)
        :type cluster_id: str
        :param file_name: The manifest file name to delete from the cluster. (required)
        :type file_name: str
        :param folder: The folder that contains the files. Manifests can be placed in 'manifests' or 'openshift' directories.
        :type folder: str
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
            'file_name',
            'folder'
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
                    " to method v2_delete_cluster_manifest" % _key
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
        if _params.get('folder') is not None:  # noqa: E501
            _query_params.append(('folder', _params['folder']))

        if _params.get('file_name') is not None:  # noqa: E501
            _query_params.append(('file_name', _params['file_name']))

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

        _response_types_map = {}

        return self.api_client.call_api(
            '/v2/clusters/{cluster_id}/manifests', 'DELETE',
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
    def v2_download_cluster_manifest(self, cluster_id : Annotated[StrictStr, Field(..., description="The cluster whose manifest should be downloaded.")], file_name : Annotated[StrictStr, Field(..., description="The manifest file name to download.")], folder : Annotated[Optional[StrictStr], Field(description="The folder that contains the files. Manifests can be placed in 'manifests' or 'openshift' directories.")] = None, **kwargs) -> bytearray:  # noqa: E501
        """v2_download_cluster_manifest  # noqa: E501

        Downloads cluster manifest.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.v2_download_cluster_manifest(cluster_id, file_name, folder, async_req=True)
        >>> result = thread.get()

        :param cluster_id: The cluster whose manifest should be downloaded. (required)
        :type cluster_id: str
        :param file_name: The manifest file name to download. (required)
        :type file_name: str
        :param folder: The folder that contains the files. Manifests can be placed in 'manifests' or 'openshift' directories.
        :type folder: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: bytearray
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the v2_download_cluster_manifest_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.v2_download_cluster_manifest_with_http_info(cluster_id, file_name, folder, **kwargs)  # noqa: E501

    @validate_arguments
    def v2_download_cluster_manifest_with_http_info(self, cluster_id : Annotated[StrictStr, Field(..., description="The cluster whose manifest should be downloaded.")], file_name : Annotated[StrictStr, Field(..., description="The manifest file name to download.")], folder : Annotated[Optional[StrictStr], Field(description="The folder that contains the files. Manifests can be placed in 'manifests' or 'openshift' directories.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """v2_download_cluster_manifest  # noqa: E501

        Downloads cluster manifest.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.v2_download_cluster_manifest_with_http_info(cluster_id, file_name, folder, async_req=True)
        >>> result = thread.get()

        :param cluster_id: The cluster whose manifest should be downloaded. (required)
        :type cluster_id: str
        :param file_name: The manifest file name to download. (required)
        :type file_name: str
        :param folder: The folder that contains the files. Manifests can be placed in 'manifests' or 'openshift' directories.
        :type folder: str
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
        :rtype: tuple(bytearray, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'cluster_id',
            'file_name',
            'folder'
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
                    " to method v2_download_cluster_manifest" % _key
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
        if _params.get('folder') is not None:  # noqa: E501
            _query_params.append(('folder', _params['folder']))

        if _params.get('file_name') is not None:  # noqa: E501
            _query_params.append(('file_name', _params['file_name']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/octet-stream'])  # noqa: E501

        # authentication setting
        _auth_settings = ['userAuth']  # noqa: E501

        _response_types_map = {
            '200': "bytearray",
            '401': "InfraError",
            '403': "InfraError",
            '404': "Error",
            '405': "Error",
            '409': "Error",
            '500': "Error",
        }

        return self.api_client.call_api(
            '/v2/clusters/{cluster_id}/manifests/files', 'GET',
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
    def v2_list_cluster_manifests(self, cluster_id : Annotated[StrictStr, Field(..., description="The cluster for which the manifests should be listed.")], **kwargs) -> List[Manifest]:  # noqa: E501
        """v2_list_cluster_manifests  # noqa: E501

        Lists manifests for customizing cluster installation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.v2_list_cluster_manifests(cluster_id, async_req=True)
        >>> result = thread.get()

        :param cluster_id: The cluster for which the manifests should be listed. (required)
        :type cluster_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: List[Manifest]
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the v2_list_cluster_manifests_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.v2_list_cluster_manifests_with_http_info(cluster_id, **kwargs)  # noqa: E501

    @validate_arguments
    def v2_list_cluster_manifests_with_http_info(self, cluster_id : Annotated[StrictStr, Field(..., description="The cluster for which the manifests should be listed.")], **kwargs) -> ApiResponse:  # noqa: E501
        """v2_list_cluster_manifests  # noqa: E501

        Lists manifests for customizing cluster installation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.v2_list_cluster_manifests_with_http_info(cluster_id, async_req=True)
        >>> result = thread.get()

        :param cluster_id: The cluster for which the manifests should be listed. (required)
        :type cluster_id: str
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
        :rtype: tuple(List[Manifest], status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'cluster_id'
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
                    " to method v2_list_cluster_manifests" % _key
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
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['userAuth']  # noqa: E501

        _response_types_map = {
            '200': "List[Manifest]",
            '401': "InfraError",
            '403': "InfraError",
            '404': "Error",
            '405': "Error",
            '409': "Error",
            '500': "Error",
        }

        return self.api_client.call_api(
            '/v2/clusters/{cluster_id}/manifests', 'GET',
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
    def v2_update_cluster_manifest(self, cluster_id : Annotated[StrictStr, Field(..., description="The cluster for which a new manifest should be updated.")], update_manifest_params : Annotated[UpdateManifestParams, Field(..., description="The manifest to be updated.")], **kwargs) -> Manifest:  # noqa: E501
        """v2_update_cluster_manifest  # noqa: E501

        Updates a manifest for customizing cluster installation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.v2_update_cluster_manifest(cluster_id, update_manifest_params, async_req=True)
        >>> result = thread.get()

        :param cluster_id: The cluster for which a new manifest should be updated. (required)
        :type cluster_id: str
        :param update_manifest_params: The manifest to be updated. (required)
        :type update_manifest_params: UpdateManifestParams
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Manifest
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the v2_update_cluster_manifest_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.v2_update_cluster_manifest_with_http_info(cluster_id, update_manifest_params, **kwargs)  # noqa: E501

    @validate_arguments
    def v2_update_cluster_manifest_with_http_info(self, cluster_id : Annotated[StrictStr, Field(..., description="The cluster for which a new manifest should be updated.")], update_manifest_params : Annotated[UpdateManifestParams, Field(..., description="The manifest to be updated.")], **kwargs) -> ApiResponse:  # noqa: E501
        """v2_update_cluster_manifest  # noqa: E501

        Updates a manifest for customizing cluster installation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.v2_update_cluster_manifest_with_http_info(cluster_id, update_manifest_params, async_req=True)
        >>> result = thread.get()

        :param cluster_id: The cluster for which a new manifest should be updated. (required)
        :type cluster_id: str
        :param update_manifest_params: The manifest to be updated. (required)
        :type update_manifest_params: UpdateManifestParams
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
        :rtype: tuple(Manifest, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'cluster_id',
            'update_manifest_params'
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
                    " to method v2_update_cluster_manifest" % _key
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
        if _params['update_manifest_params'] is not None:
            _body_params = _params['update_manifest_params']

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
        _auth_settings = ['userAuth']  # noqa: E501

        _response_types_map = {
            '200': "Manifest",
            '400': "Error",
            '401': "InfraError",
            '403': "InfraError",
            '404': "Error",
            '405': "Error",
            '409': "Error",
            '500': "Error",
        }

        return self.api_client.call_api(
            '/v2/clusters/{cluster_id}/manifests', 'PATCH',
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