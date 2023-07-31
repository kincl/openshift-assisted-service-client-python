# openshift_assisted_service.InstallerApi

All URIs are relative to *http://api.openshift.com/api/assisted-install*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bind_host**](InstallerApi.md#bind_host) | **POST** /v2/infra-envs/{infra_env_id}/hosts/{host_id}/actions/bind | 
[**deregister_infra_env**](InstallerApi.md#deregister_infra_env) | **DELETE** /v2/infra-envs/{infra_env_id} | 
[**download_minimal_initrd**](InstallerApi.md#download_minimal_initrd) | **GET** /v2/infra-envs/{infra_env_id}/downloads/minimal-initrd | 
[**get_cluster_supported_platforms**](InstallerApi.md#get_cluster_supported_platforms) | **GET** /v2/clusters/{cluster_id}/supported-platforms | 
[**get_infra_env**](InstallerApi.md#get_infra_env) | **GET** /v2/infra-envs/{infra_env_id} | 
[**get_infra_env_download_url**](InstallerApi.md#get_infra_env_download_url) | **GET** /v2/infra-envs/{infra_env_id}/downloads/image-url | 
[**get_infra_env_presigned_file_url**](InstallerApi.md#get_infra_env_presigned_file_url) | **GET** /v2/infra-envs/{infra_env_id}/downloads/files-presigned | 
[**get_supported_architectures**](InstallerApi.md#get_supported_architectures) | **GET** /v2/support-levels/architectures | 
[**get_supported_features**](InstallerApi.md#get_supported_features) | **GET** /v2/support-levels/features | 
[**list_cluster_hosts**](InstallerApi.md#list_cluster_hosts) | **GET** /v2/clusters/{cluster_id}/hosts | 
[**list_infra_envs**](InstallerApi.md#list_infra_envs) | **GET** /v2/infra-envs | 
[**regenerate_infra_env_signing_key**](InstallerApi.md#regenerate_infra_env_signing_key) | **POST** /v2/infra-envs/{infra_env_id}/regenerate-signing-key | 
[**register_infra_env**](InstallerApi.md#register_infra_env) | **POST** /v2/infra-envs | 
[**transform_cluster_to_adding_hosts**](InstallerApi.md#transform_cluster_to_adding_hosts) | **POST** /v2/clusters/{cluster_id}/actions/allow-add-hosts | 
[**transform_cluster_to_day2**](InstallerApi.md#transform_cluster_to_day2) | **POST** /v2/clusters/{cluster_id}/actions/allow-add-workers | 
[**unbind_host**](InstallerApi.md#unbind_host) | **POST** /v2/infra-envs/{infra_env_id}/hosts/{host_id}/actions/unbind | 
[**update_infra_env**](InstallerApi.md#update_infra_env) | **PATCH** /v2/infra-envs/{infra_env_id} | 
[**v2_cancel_installation**](InstallerApi.md#v2_cancel_installation) | **POST** /v2/clusters/{cluster_id}/actions/cancel | 
[**v2_complete_installation**](InstallerApi.md#v2_complete_installation) | **POST** /v2/clusters/{cluster_id}/actions/complete-installation | 
[**v2_deregister_cluster**](InstallerApi.md#v2_deregister_cluster) | **DELETE** /v2/clusters/{cluster_id} | 
[**v2_deregister_host**](InstallerApi.md#v2_deregister_host) | **DELETE** /v2/infra-envs/{infra_env_id}/hosts/{host_id} | 
[**v2_download_cluster_credentials**](InstallerApi.md#v2_download_cluster_credentials) | **GET** /v2/clusters/{cluster_id}/downloads/credentials | 
[**v2_download_cluster_files**](InstallerApi.md#v2_download_cluster_files) | **GET** /v2/clusters/{cluster_id}/downloads/files | 
[**v2_download_cluster_logs**](InstallerApi.md#v2_download_cluster_logs) | **GET** /v2/clusters/{cluster_id}/logs | 
[**v2_download_host_ignition**](InstallerApi.md#v2_download_host_ignition) | **GET** /v2/infra-env/{infra_env_id}/hosts/{host_id}/downloads/ignition | 
[**v2_download_infra_env_files**](InstallerApi.md#v2_download_infra_env_files) | **GET** /v2/infra-envs/{infra_env_id}/downloads/files | 
[**v2_get_cluster**](InstallerApi.md#v2_get_cluster) | **GET** /v2/clusters/{cluster_id} | 
[**v2_get_cluster_default_config**](InstallerApi.md#v2_get_cluster_default_config) | **GET** /v2/clusters/default-config | 
[**v2_get_cluster_install_config**](InstallerApi.md#v2_get_cluster_install_config) | **GET** /v2/clusters/{cluster_id}/install-config | 
[**v2_get_cluster_ui_settings**](InstallerApi.md#v2_get_cluster_ui_settings) | **GET** /v2/clusters/{cluster_id}/ui-settings | 
[**v2_get_credentials**](InstallerApi.md#v2_get_credentials) | **GET** /v2/clusters/{cluster_id}/credentials | 
[**v2_get_host**](InstallerApi.md#v2_get_host) | **GET** /v2/infra-envs/{infra_env_id}/hosts/{host_id} | 
[**v2_get_host_ignition**](InstallerApi.md#v2_get_host_ignition) | **GET** /v2/infra-envs/{infra_env_id}/hosts/{host_id}/ignition | 
[**v2_get_ignored_validations**](InstallerApi.md#v2_get_ignored_validations) | **GET** /v2/clusters/{cluster_id}/ignored-validations | 
[**v2_get_next_steps**](InstallerApi.md#v2_get_next_steps) | **GET** /v2/infra-envs/{infra_env_id}/hosts/{host_id}/instructions | 
[**v2_get_preflight_requirements**](InstallerApi.md#v2_get_preflight_requirements) | **GET** /v2/clusters/{cluster_id}/preflight-requirements | 
[**v2_get_presigned_for_cluster_credentials**](InstallerApi.md#v2_get_presigned_for_cluster_credentials) | **GET** /v2/clusters/{cluster_id}/downloads/credentials-presigned | 
[**v2_get_presigned_for_cluster_files**](InstallerApi.md#v2_get_presigned_for_cluster_files) | **GET** /v2/clusters/{cluster_id}/downloads/files-presigned | 
[**v2_import_cluster**](InstallerApi.md#v2_import_cluster) | **POST** /v2/clusters/import | 
[**v2_install_cluster**](InstallerApi.md#v2_install_cluster) | **POST** /v2/clusters/{cluster_id}/actions/install | 
[**v2_install_host**](InstallerApi.md#v2_install_host) | **POST** /v2/infra-envs/{infra_env_id}/hosts/{host_id}/actions/install | 
[**v2_list_clusters**](InstallerApi.md#v2_list_clusters) | **GET** /v2/clusters | 
[**v2_list_feature_support_levels**](InstallerApi.md#v2_list_feature_support_levels) | **GET** /v2/feature-support-levels | 
[**v2_list_hosts**](InstallerApi.md#v2_list_hosts) | **GET** /v2/infra-envs/{infra_env_id}/hosts | 
[**v2_list_of_cluster_operators**](InstallerApi.md#v2_list_of_cluster_operators) | **GET** /v2/clusters/{cluster_id}/monitored-operators | 
[**v2_post_step_reply**](InstallerApi.md#v2_post_step_reply) | **POST** /v2/infra-envs/{infra_env_id}/hosts/{host_id}/instructions | 
[**v2_register_cluster**](InstallerApi.md#v2_register_cluster) | **POST** /v2/clusters | 
[**v2_register_host**](InstallerApi.md#v2_register_host) | **POST** /v2/infra-envs/{infra_env_id}/hosts | 
[**v2_report_monitored_operator_status**](InstallerApi.md#v2_report_monitored_operator_status) | **PUT** /v2/clusters/{cluster_id}/monitored-operators | 
[**v2_reset_cluster**](InstallerApi.md#v2_reset_cluster) | **POST** /v2/clusters/{cluster_id}/actions/reset | 
[**v2_reset_host**](InstallerApi.md#v2_reset_host) | **POST** /v2/infra-envs/{infra_env_id}/hosts/{host_id}/actions/reset | 
[**v2_reset_host_validation**](InstallerApi.md#v2_reset_host_validation) | **PATCH** /v2/infra-envs/{infra_env_id}/hosts/{host_id}/actions/reset-validation/{validation_id} | Reset failed host validation.
[**v2_set_ignored_validations**](InstallerApi.md#v2_set_ignored_validations) | **PUT** /v2/clusters/{cluster_id}/ignored-validations | 
[**v2_update_cluster**](InstallerApi.md#v2_update_cluster) | **PATCH** /v2/clusters/{cluster_id} | 
[**v2_update_cluster_install_config**](InstallerApi.md#v2_update_cluster_install_config) | **PATCH** /v2/clusters/{cluster_id}/install-config | 
[**v2_update_cluster_logs_progress**](InstallerApi.md#v2_update_cluster_logs_progress) | **PUT** /v2/clusters/{cluster_id}/logs-progress | 
[**v2_update_cluster_ui_settings**](InstallerApi.md#v2_update_cluster_ui_settings) | **PUT** /v2/clusters/{cluster_id}/ui-settings | 
[**v2_update_host**](InstallerApi.md#v2_update_host) | **PATCH** /v2/infra-envs/{infra_env_id}/hosts/{host_id} | 
[**v2_update_host_ignition**](InstallerApi.md#v2_update_host_ignition) | **PATCH** /v2/infra-envs/{infra_env_id}/hosts/{host_id}/ignition | 
[**v2_update_host_install_progress**](InstallerApi.md#v2_update_host_install_progress) | **PUT** /v2/infra-envs/{infra_env_id}/hosts/{host_id}/progress | 
[**v2_update_host_installer_args**](InstallerApi.md#v2_update_host_installer_args) | **PATCH** /v2/infra-envs/{infra_env_id}/hosts/{host_id}/installer-args | 
[**v2_update_host_logs_progress**](InstallerApi.md#v2_update_host_logs_progress) | **PUT** /v2/infra-envs/{infra_env_id}/hosts/{host_id}/logs-progress | 
[**v2_upload_cluster_ingress_cert**](InstallerApi.md#v2_upload_cluster_ingress_cert) | **POST** /v2/clusters/{cluster_id}/uploads/ingress-cert | 
[**v2_upload_logs**](InstallerApi.md#v2_upload_logs) | **POST** /v2/clusters/{cluster_id}/logs | 


# **bind_host**
> Host bind_host(infra_env_id, host_id, bind_host_params)



Bind host to a cluster

### Example

* Api Key Authentication (userAuth):
```python
import time
import os
import openshift_assisted_service
from openshift_assisted_service.models.bind_host_params import BindHostParams
from openshift_assisted_service.models.host import Host
from openshift_assisted_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.openshift.com/api/assisted-install
# See configuration.py for a list of all supported configuration parameters.
configuration = openshift_assisted_service.Configuration(
    host = "http://api.openshift.com/api/assisted-install"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAuth
configuration.api_key['userAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openshift_assisted_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openshift_assisted_service.InstallerApi(api_client)
    infra_env_id = 'infra_env_id_example' # str | The infra-env of the host that is being bound.
    host_id = 'host_id_example' # str | The host that is being bound.
    bind_host_params = openshift_assisted_service.BindHostParams() # BindHostParams | The parameters for the host binding.

    try:
        api_response = api_instance.bind_host(infra_env_id, host_id, bind_host_params)
        print("The response of InstallerApi->bind_host:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallerApi->bind_host: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **infra_env_id** | **str**| The infra-env of the host that is being bound. | 
 **host_id** | **str**| The host that is being bound. | 
 **bind_host_params** | [**BindHostParams**](BindHostParams.md)| The parameters for the host binding. | 

### Return type

[**Host**](Host.md)

### Authorization

[userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**400** | Error. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Error. |  -  |
**405** | Method Not Allowed. |  -  |
**500** | Error. |  -  |
**501** | Not implemented. |  -  |
**503** | Unavailable. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deregister_infra_env**
> deregister_infra_env(infra_env_id)



Deletes an infra-env.

### Example

* Api Key Authentication (userAuth):
```python
import time
import os
import openshift_assisted_service
from openshift_assisted_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.openshift.com/api/assisted-install
# See configuration.py for a list of all supported configuration parameters.
configuration = openshift_assisted_service.Configuration(
    host = "http://api.openshift.com/api/assisted-install"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAuth
configuration.api_key['userAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openshift_assisted_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openshift_assisted_service.InstallerApi(api_client)
    infra_env_id = 'infra_env_id_example' # str | The infra-env to be deleted.

    try:
        api_instance.deregister_infra_env(infra_env_id)
    except Exception as e:
        print("Exception when calling InstallerApi->deregister_infra_env: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **infra_env_id** | **str**| The infra-env to be deleted. | 

### Return type

void (empty response body)

### Authorization

[userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Error. |  -  |
**405** | Method Not Allowed. |  -  |
**409** | Error. |  -  |
**500** | Error. |  -  |
**501** | Not implemented. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_minimal_initrd**
> bytearray download_minimal_initrd(infra_env_id)



Get the initial ramdisk for minimal ISO based installations. 

### Example

* Api Key Authentication (urlAuth):
* Api Key Authentication (userAuth):
* Api Key Authentication (imageAuth):
```python
import time
import os
import openshift_assisted_service
from openshift_assisted_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.openshift.com/api/assisted-install
# See configuration.py for a list of all supported configuration parameters.
configuration = openshift_assisted_service.Configuration(
    host = "http://api.openshift.com/api/assisted-install"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: urlAuth
configuration.api_key['urlAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['urlAuth'] = 'Bearer'

# Configure API key authorization: userAuth
configuration.api_key['userAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAuth'] = 'Bearer'

# Configure API key authorization: imageAuth
configuration.api_key['imageAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['imageAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openshift_assisted_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openshift_assisted_service.InstallerApi(api_client)
    infra_env_id = 'infra_env_id_example' # str | The infra-env of the host that should be retrieved.

    try:
        api_response = api_instance.download_minimal_initrd(infra_env_id)
        print("The response of InstallerApi->download_minimal_initrd:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallerApi->download_minimal_initrd: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **infra_env_id** | **str**| The infra-env of the host that should be retrieved. | 

### Return type

**bytearray**

### Authorization

[urlAuth](../README.md#urlAuth), [userAuth](../README.md#userAuth), [imageAuth](../README.md#imageAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**204** | Empty Success. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Error. |  -  |
**405** | Method Not Allowed. |  -  |
**409** | Conflict. |  -  |
**500** | Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_supported_platforms**
> List[PlatformType] get_cluster_supported_platforms(cluster_id)



A list of platforms that this cluster can support in its current configuration.

### Example

* Api Key Authentication (userAuth):
```python
import time
import os
import openshift_assisted_service
from openshift_assisted_service.models.platform_type import PlatformType
from openshift_assisted_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.openshift.com/api/assisted-install
# See configuration.py for a list of all supported configuration parameters.
configuration = openshift_assisted_service.Configuration(
    host = "http://api.openshift.com/api/assisted-install"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAuth
configuration.api_key['userAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openshift_assisted_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openshift_assisted_service.InstallerApi(api_client)
    cluster_id = 'cluster_id_example' # str | The cluster whose platform types should be retrieved.

    try:
        api_response = api_instance.get_cluster_supported_platforms(cluster_id)
        print("The response of InstallerApi->get_cluster_supported_platforms:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallerApi->get_cluster_supported_platforms: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The cluster whose platform types should be retrieved. | 

### Return type

[**List[PlatformType]**](PlatformType.md)

### Authorization

[userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Error. |  -  |
**500** | Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_infra_env**
> InfraEnv get_infra_env(infra_env_id)



Retrieves the details of the infra-env.

### Example

* Api Key Authentication (imageURLAuth):
* Api Key Authentication (urlAuth):
* Api Key Authentication (userAuth):
* Api Key Authentication (imageAuth):
* Api Key Authentication (agentAuth):
```python
import time
import os
import openshift_assisted_service
from openshift_assisted_service.models.infra_env import InfraEnv
from openshift_assisted_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.openshift.com/api/assisted-install
# See configuration.py for a list of all supported configuration parameters.
configuration = openshift_assisted_service.Configuration(
    host = "http://api.openshift.com/api/assisted-install"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: imageURLAuth
configuration.api_key['imageURLAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['imageURLAuth'] = 'Bearer'

# Configure API key authorization: urlAuth
configuration.api_key['urlAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['urlAuth'] = 'Bearer'

# Configure API key authorization: userAuth
configuration.api_key['userAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAuth'] = 'Bearer'

# Configure API key authorization: imageAuth
configuration.api_key['imageAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['imageAuth'] = 'Bearer'

# Configure API key authorization: agentAuth
configuration.api_key['agentAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['agentAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openshift_assisted_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openshift_assisted_service.InstallerApi(api_client)
    infra_env_id = 'infra_env_id_example' # str | The infra-env to be retrieved.

    try:
        api_response = api_instance.get_infra_env(infra_env_id)
        print("The response of InstallerApi->get_infra_env:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallerApi->get_infra_env: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **infra_env_id** | **str**| The infra-env to be retrieved. | 

### Return type

[**InfraEnv**](InfraEnv.md)

### Authorization

[imageURLAuth](../README.md#imageURLAuth), [urlAuth](../README.md#urlAuth), [userAuth](../README.md#userAuth), [imageAuth](../README.md#imageAuth), [agentAuth](../README.md#agentAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Error. |  -  |
**405** | Method Not Allowed. |  -  |
**500** | Error. |  -  |
**501** | Not implemented. |  -  |
**503** | Unavailable. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_infra_env_download_url**
> PresignedUrl get_infra_env_download_url(infra_env_id)



Creates a new pre-signed image download URL for the infra-env.

### Example

* Api Key Authentication (userAuth):
```python
import time
import os
import openshift_assisted_service
from openshift_assisted_service.models.presigned_url import PresignedUrl
from openshift_assisted_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.openshift.com/api/assisted-install
# See configuration.py for a list of all supported configuration parameters.
configuration = openshift_assisted_service.Configuration(
    host = "http://api.openshift.com/api/assisted-install"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAuth
configuration.api_key['userAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openshift_assisted_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openshift_assisted_service.InstallerApi(api_client)
    infra_env_id = 'infra_env_id_example' # str | The infra-env to be retrieved.

    try:
        api_response = api_instance.get_infra_env_download_url(infra_env_id)
        print("The response of InstallerApi->get_infra_env_download_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallerApi->get_infra_env_download_url: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **infra_env_id** | **str**| The infra-env to be retrieved. | 

### Return type

[**PresignedUrl**](PresignedUrl.md)

### Authorization

[userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**400** | Bad Request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Error. |  -  |
**405** | Method Not Allowed. |  -  |
**500** | Error. |  -  |
**501** | Not implemented. |  -  |
**503** | Unavailable. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_infra_env_presigned_file_url**
> PresignedUrl get_infra_env_presigned_file_url(infra_env_id, file_name, ipxe_script_type=ipxe_script_type)



Creates a new pre-signed download URL for the infra-env.

### Example

* Api Key Authentication (userAuth):
```python
import time
import os
import openshift_assisted_service
from openshift_assisted_service.models.presigned_url import PresignedUrl
from openshift_assisted_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.openshift.com/api/assisted-install
# See configuration.py for a list of all supported configuration parameters.
configuration = openshift_assisted_service.Configuration(
    host = "http://api.openshift.com/api/assisted-install"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAuth
configuration.api_key['userAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openshift_assisted_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openshift_assisted_service.InstallerApi(api_client)
    infra_env_id = 'infra_env_id_example' # str | The file's infra-env.
    file_name = 'file_name_example' # str | The file to be downloaded.
    ipxe_script_type = 'ipxe_script_type_example' # str | Specify the script type to be served for iPXE. (optional)

    try:
        api_response = api_instance.get_infra_env_presigned_file_url(infra_env_id, file_name, ipxe_script_type=ipxe_script_type)
        print("The response of InstallerApi->get_infra_env_presigned_file_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallerApi->get_infra_env_presigned_file_url: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **infra_env_id** | **str**| The file&#39;s infra-env. | 
 **file_name** | **str**| The file to be downloaded. | 
 **ipxe_script_type** | **str**| Specify the script type to be served for iPXE. | [optional] 

### Return type

[**PresignedUrl**](PresignedUrl.md)

### Authorization

[userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Error. |  -  |
**405** | Method Not Allowed. |  -  |
**500** | Error. |  -  |
**501** | Not implemented. |  -  |
**503** | Unavailable. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_supported_architectures**
> GetSupportedArchitectures200Response get_supported_architectures(openshift_version)



Retrieves the architecture support-levels for each OpenShift version.

### Example

* Api Key Authentication (userAuth):
```python
import time
import os
import openshift_assisted_service
from openshift_assisted_service.models.get_supported_architectures200_response import GetSupportedArchitectures200Response
from openshift_assisted_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.openshift.com/api/assisted-install
# See configuration.py for a list of all supported configuration parameters.
configuration = openshift_assisted_service.Configuration(
    host = "http://api.openshift.com/api/assisted-install"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAuth
configuration.api_key['userAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openshift_assisted_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openshift_assisted_service.InstallerApi(api_client)
    openshift_version = 'openshift_version_example' # str | Version of the OpenShift cluster.

    try:
        api_response = api_instance.get_supported_architectures(openshift_version)
        print("The response of InstallerApi->get_supported_architectures:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallerApi->get_supported_architectures: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **openshift_version** | **str**| Version of the OpenShift cluster. | 

### Return type

[**GetSupportedArchitectures200Response**](GetSupportedArchitectures200Response.md)

### Authorization

[userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**400** | Error. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Error. |  -  |
**503** | Unavailable. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_supported_features**
> GetSupportedFeatures200Response get_supported_features(openshift_version, cpu_architecture=cpu_architecture)



Retrieves the features support levels for each OpenShift version.

### Example

* Api Key Authentication (userAuth):
```python
import time
import os
import openshift_assisted_service
from openshift_assisted_service.models.get_supported_features200_response import GetSupportedFeatures200Response
from openshift_assisted_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.openshift.com/api/assisted-install
# See configuration.py for a list of all supported configuration parameters.
configuration = openshift_assisted_service.Configuration(
    host = "http://api.openshift.com/api/assisted-install"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAuth
configuration.api_key['userAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openshift_assisted_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openshift_assisted_service.InstallerApi(api_client)
    openshift_version = 'openshift_version_example' # str | Version of the OpenShift cluster.
    cpu_architecture = 'x86_64' # str | The CPU architecture of the image (x86_64/arm64/etc). (optional) (default to 'x86_64')

    try:
        api_response = api_instance.get_supported_features(openshift_version, cpu_architecture=cpu_architecture)
        print("The response of InstallerApi->get_supported_features:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallerApi->get_supported_features: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **openshift_version** | **str**| Version of the OpenShift cluster. | 
 **cpu_architecture** | **str**| The CPU architecture of the image (x86_64/arm64/etc). | [optional] [default to &#39;x86_64&#39;]

### Return type

[**GetSupportedFeatures200Response**](GetSupportedFeatures200Response.md)

### Authorization

[userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**400** | Error. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Error. |  -  |
**503** | Unavailable. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cluster_hosts**
> List[Host] list_cluster_hosts(cluster_id, role=role, status=status, with_inventory=with_inventory, with_connectivity=with_connectivity)



Get a list of cluster hosts according to supplied filters.

### Example

* Api Key Authentication (userAuth):
* Api Key Authentication (agentAuth):
```python
import time
import os
import openshift_assisted_service
from openshift_assisted_service.models.host import Host
from openshift_assisted_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.openshift.com/api/assisted-install
# See configuration.py for a list of all supported configuration parameters.
configuration = openshift_assisted_service.Configuration(
    host = "http://api.openshift.com/api/assisted-install"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAuth
configuration.api_key['userAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAuth'] = 'Bearer'

# Configure API key authorization: agentAuth
configuration.api_key['agentAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['agentAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openshift_assisted_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openshift_assisted_service.InstallerApi(api_client)
    cluster_id = 'cluster_id_example' # str | The cluster whose hosts should be retrieved.
    role = 'role_example' # str | Role to request. (optional)
    status = 'status_example' # str | Hosts status to request. (optional)
    with_inventory = True # bool | If true return the host's inventory. (optional)
    with_connectivity = True # bool | If true return the host's connectivity. (optional)

    try:
        api_response = api_instance.list_cluster_hosts(cluster_id, role=role, status=status, with_inventory=with_inventory, with_connectivity=with_connectivity)
        print("The response of InstallerApi->list_cluster_hosts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallerApi->list_cluster_hosts: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The cluster whose hosts should be retrieved. | 
 **role** | **str**| Role to request. | [optional] 
 **status** | **str**| Hosts status to request. | [optional] 
 **with_inventory** | **bool**| If true return the host&#39;s inventory. | [optional] 
 **with_connectivity** | **bool**| If true return the host&#39;s connectivity. | [optional] 

### Return type

[**List[Host]**](Host.md)

### Authorization

[userAuth](../README.md#userAuth), [agentAuth](../README.md#agentAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Error. |  -  |
**500** | Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_infra_envs**
> List[InfraEnv] list_infra_envs(cluster_id=cluster_id, owner=owner)



Retrieves the list of infra-envs.

### Example

* Api Key Authentication (userAuth):
```python
import time
import os
import openshift_assisted_service
from openshift_assisted_service.models.infra_env import InfraEnv
from openshift_assisted_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.openshift.com/api/assisted-install
# See configuration.py for a list of all supported configuration parameters.
configuration = openshift_assisted_service.Configuration(
    host = "http://api.openshift.com/api/assisted-install"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAuth
configuration.api_key['userAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openshift_assisted_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openshift_assisted_service.InstallerApi(api_client)
    cluster_id = 'cluster_id_example' # str | If provided, returns only infra-envs which directly reference this cluster. (optional)
    owner = 'owner_example' # str | If provided, returns only infra-envs that are owned by the specified user. (optional)

    try:
        api_response = api_instance.list_infra_envs(cluster_id=cluster_id, owner=owner)
        print("The response of InstallerApi->list_infra_envs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallerApi->list_infra_envs: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| If provided, returns only infra-envs which directly reference this cluster. | [optional] 
 **owner** | **str**| If provided, returns only infra-envs that are owned by the specified user. | [optional] 

### Return type

[**List[InfraEnv]**](InfraEnv.md)

### Authorization

[userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**405** | Method Not Allowed. |  -  |
**500** | Error. |  -  |
**501** | Not implemented. |  -  |
**503** | Unavailable. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **regenerate_infra_env_signing_key**
> regenerate_infra_env_signing_key(infra_env_id)



Regenerate InfraEnv token signing key.

### Example

* Api Key Authentication (userAuth):
```python
import time
import os
import openshift_assisted_service
from openshift_assisted_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.openshift.com/api/assisted-install
# See configuration.py for a list of all supported configuration parameters.
configuration = openshift_assisted_service.Configuration(
    host = "http://api.openshift.com/api/assisted-install"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAuth
configuration.api_key['userAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openshift_assisted_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openshift_assisted_service.InstallerApi(api_client)
    infra_env_id = 'infra_env_id_example' # str | The target InfraEnv.

    try:
        api_instance.regenerate_infra_env_signing_key(infra_env_id)
    except Exception as e:
        print("Exception when calling InstallerApi->regenerate_infra_env_signing_key: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **infra_env_id** | **str**| The target InfraEnv. | 

### Return type

void (empty response body)

### Authorization

[userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Error. |  -  |
**405** | Method Not Allowed. |  -  |
**500** | Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_infra_env**
> InfraEnv register_infra_env(infraenv_create_params)



Creates a new OpenShift Discovery ISO.

### Example

* Api Key Authentication (userAuth):
```python
import time
import os
import openshift_assisted_service
from openshift_assisted_service.models.infra_env import InfraEnv
from openshift_assisted_service.models.infra_env_create_params import InfraEnvCreateParams
from openshift_assisted_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.openshift.com/api/assisted-install
# See configuration.py for a list of all supported configuration parameters.
configuration = openshift_assisted_service.Configuration(
    host = "http://api.openshift.com/api/assisted-install"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAuth
configuration.api_key['userAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openshift_assisted_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openshift_assisted_service.InstallerApi(api_client)
    infraenv_create_params = openshift_assisted_service.InfraEnvCreateParams() # InfraEnvCreateParams | The parameters for the generated ISO.

    try:
        api_response = api_instance.register_infra_env(infraenv_create_params)
        print("The response of InstallerApi->register_infra_env:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallerApi->register_infra_env: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **infraenv_create_params** | [**InfraEnvCreateParams**](InfraEnvCreateParams.md)| The parameters for the generated ISO. | 

### Return type

[**InfraEnv**](InfraEnv.md)

### Authorization

[userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success. |  -  |
**400** | Error. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Error. |  -  |
**405** | Method Not Allowed. |  -  |
**409** | Error. |  -  |
**500** | Error. |  -  |
**501** | Not implemented. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transform_cluster_to_adding_hosts**
> Cluster transform_cluster_to_adding_hosts(cluster_id)



Transforms installed cluster to a state which allows adding hosts.

### Example

* Api Key Authentication (userAuth):
```python
import time
import os
import openshift_assisted_service
from openshift_assisted_service.models.cluster import Cluster
from openshift_assisted_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.openshift.com/api/assisted-install
# See configuration.py for a list of all supported configuration parameters.
configuration = openshift_assisted_service.Configuration(
    host = "http://api.openshift.com/api/assisted-install"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAuth
configuration.api_key['userAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openshift_assisted_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openshift_assisted_service.InstallerApi(api_client)
    cluster_id = 'cluster_id_example' # str | The cluster to transform.

    try:
        api_response = api_instance.transform_cluster_to_adding_hosts(cluster_id)
        print("The response of InstallerApi->transform_cluster_to_adding_hosts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallerApi->transform_cluster_to_adding_hosts: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The cluster to transform. | 

### Return type

[**Cluster**](Cluster.md)

### Authorization

[userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Success. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Error. |  -  |
**405** | Method Not Allowed. |  -  |
**409** | Error. |  -  |
**500** | Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transform_cluster_to_day2**
> Cluster transform_cluster_to_day2(cluster_id)



Deprecated, maintained for legacy purposes. Does the same thing as allow-add-hosts. Use allow-add-hosts instead.

### Example

* Api Key Authentication (userAuth):
```python
import time
import os
import openshift_assisted_service
from openshift_assisted_service.models.cluster import Cluster
from openshift_assisted_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.openshift.com/api/assisted-install
# See configuration.py for a list of all supported configuration parameters.
configuration = openshift_assisted_service.Configuration(
    host = "http://api.openshift.com/api/assisted-install"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAuth
configuration.api_key['userAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openshift_assisted_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openshift_assisted_service.InstallerApi(api_client)
    cluster_id = 'cluster_id_example' # str | The cluster to transform.

    try:
        api_response = api_instance.transform_cluster_to_day2(cluster_id)
        print("The response of InstallerApi->transform_cluster_to_day2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallerApi->transform_cluster_to_day2: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The cluster to transform. | 

### Return type

[**Cluster**](Cluster.md)

### Authorization

[userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Success. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Error. |  -  |
**405** | Method Not Allowed. |  -  |
**409** | Error. |  -  |
**500** | Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unbind_host**
> Host unbind_host(infra_env_id, host_id)



Unbind host to a cluster

### Example

* Api Key Authentication (userAuth):
```python
import time
import os
import openshift_assisted_service
from openshift_assisted_service.models.host import Host
from openshift_assisted_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.openshift.com/api/assisted-install
# See configuration.py for a list of all supported configuration parameters.
configuration = openshift_assisted_service.Configuration(
    host = "http://api.openshift.com/api/assisted-install"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAuth
configuration.api_key['userAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openshift_assisted_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openshift_assisted_service.InstallerApi(api_client)
    infra_env_id = 'infra_env_id_example' # str | The infra-env of the host that is being bound.
    host_id = 'host_id_example' # str | The host that is being bound.

    try:
        api_response = api_instance.unbind_host(infra_env_id, host_id)
        print("The response of InstallerApi->unbind_host:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallerApi->unbind_host: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **infra_env_id** | **str**| The infra-env of the host that is being bound. | 
 **host_id** | **str**| The host that is being bound. | 

### Return type

[**Host**](Host.md)

### Authorization

[userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**400** | Error. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Error. |  -  |
**405** | Method Not Allowed. |  -  |
**409** | Conflict. |  -  |
**500** | Error. |  -  |
**501** | Not implemented. |  -  |
**503** | Unavailable. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_infra_env**
> InfraEnv update_infra_env(infra_env_id, infra_env_update_params)



Updates an infra-env.

### Example

* Api Key Authentication (userAuth):
```python
import time
import os
import openshift_assisted_service
from openshift_assisted_service.models.infra_env import InfraEnv
from openshift_assisted_service.models.infra_env_update_params import InfraEnvUpdateParams
from openshift_assisted_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.openshift.com/api/assisted-install
# See configuration.py for a list of all supported configuration parameters.
configuration = openshift_assisted_service.Configuration(
    host = "http://api.openshift.com/api/assisted-install"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAuth
configuration.api_key['userAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openshift_assisted_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openshift_assisted_service.InstallerApi(api_client)
    infra_env_id = 'infra_env_id_example' # str | The infra-env to be updated.
    infra_env_update_params = openshift_assisted_service.InfraEnvUpdateParams() # InfraEnvUpdateParams | The properties to update.

    try:
        api_response = api_instance.update_infra_env(infra_env_id, infra_env_update_params)
        print("The response of InstallerApi->update_infra_env:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallerApi->update_infra_env: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **infra_env_id** | **str**| The infra-env to be updated. | 
 **infra_env_update_params** | [**InfraEnvUpdateParams**](InfraEnvUpdateParams.md)| The properties to update. | 

### Return type

[**InfraEnv**](InfraEnv.md)

### Authorization

[userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success. |  -  |
**400** | Error. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Error. |  -  |
**405** | Method Not Allowed. |  -  |
**409** | Error. |  -  |
**500** | Error. |  -  |
**501** | Not implemented. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_cancel_installation**
> Cluster v2_cancel_installation(cluster_id)



Cancels an ongoing installation.

### Example

* Api Key Authentication (userAuth):
```python
import time
import os
import openshift_assisted_service
from openshift_assisted_service.models.cluster import Cluster
from openshift_assisted_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.openshift.com/api/assisted-install
# See configuration.py for a list of all supported configuration parameters.
configuration = openshift_assisted_service.Configuration(
    host = "http://api.openshift.com/api/assisted-install"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAuth
configuration.api_key['userAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openshift_assisted_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openshift_assisted_service.InstallerApi(api_client)
    cluster_id = 'cluster_id_example' # str | The cluster whose installation is to be canceled.

    try:
        api_response = api_instance.v2_cancel_installation(cluster_id)
        print("The response of InstallerApi->v2_cancel_installation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallerApi->v2_cancel_installation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The cluster whose installation is to be canceled. | 

### Return type

[**Cluster**](Cluster.md)

### Authorization

[userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Success. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Error. |  -  |
**405** | Method Not Allowed. |  -  |
**409** | Error. |  -  |
**500** | Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_complete_installation**
> Cluster v2_complete_installation(cluster_id, completion_params, discovery_agent_version=discovery_agent_version)



Agent API to mark a finalizing installation as complete and progress to 100%.

### Example

* Api Key Authentication (agentAuth):
```python
import time
import os
import openshift_assisted_service
from openshift_assisted_service.models.cluster import Cluster
from openshift_assisted_service.models.completion_params import CompletionParams
from openshift_assisted_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.openshift.com/api/assisted-install
# See configuration.py for a list of all supported configuration parameters.
configuration = openshift_assisted_service.Configuration(
    host = "http://api.openshift.com/api/assisted-install"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: agentAuth
configuration.api_key['agentAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['agentAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openshift_assisted_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openshift_assisted_service.InstallerApi(api_client)
    cluster_id = 'cluster_id_example' # str | The cluster whose installation is being completing.
    completion_params = openshift_assisted_service.CompletionParams() # CompletionParams | The final status of the cluster installation.
    discovery_agent_version = 'discovery_agent_version_example' # str | The software version of the discovery agent that is completing the installation. (optional)

    try:
        api_response = api_instance.v2_complete_installation(cluster_id, completion_params, discovery_agent_version=discovery_agent_version)
        print("The response of InstallerApi->v2_complete_installation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallerApi->v2_complete_installation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The cluster whose installation is being completing. | 
 **completion_params** | [**CompletionParams**](CompletionParams.md)| The final status of the cluster installation. | 
 **discovery_agent_version** | **str**| The software version of the discovery agent that is completing the installation. | [optional] 

### Return type

[**Cluster**](Cluster.md)

### Authorization

[agentAuth](../README.md#agentAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Success. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Error. |  -  |
**405** | Method Not Allowed. |  -  |
**409** | Error. |  -  |
**500** | Error. |  -  |
**503** | Unavailable. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_deregister_cluster**
> v2_deregister_cluster(cluster_id)



Deletes an OpenShift cluster definition.

### Example

* Api Key Authentication (userAuth):
```python
import time
import os
import openshift_assisted_service
from openshift_assisted_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.openshift.com/api/assisted-install
# See configuration.py for a list of all supported configuration parameters.
configuration = openshift_assisted_service.Configuration(
    host = "http://api.openshift.com/api/assisted-install"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAuth
configuration.api_key['userAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openshift_assisted_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openshift_assisted_service.InstallerApi(api_client)
    cluster_id = 'cluster_id_example' # str | The cluster to be deregistered.

    try:
        api_instance.v2_deregister_cluster(cluster_id)
    except Exception as e:
        print("Exception when calling InstallerApi->v2_deregister_cluster: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The cluster to be deregistered. | 

### Return type

void (empty response body)

### Authorization

[userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Error. |  -  |
**405** | Method Not Allowed. |  -  |
**409** | Error. |  -  |
**500** | Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_deregister_host**
> v2_deregister_host(infra_env_id, host_id)



Deregisters an OpenShift host.

### Example

* Api Key Authentication (userAuth):
```python
import time
import os
import openshift_assisted_service
from openshift_assisted_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.openshift.com/api/assisted-install
# See configuration.py for a list of all supported configuration parameters.
configuration = openshift_assisted_service.Configuration(
    host = "http://api.openshift.com/api/assisted-install"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAuth
configuration.api_key['userAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openshift_assisted_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openshift_assisted_service.InstallerApi(api_client)
    infra_env_id = 'infra_env_id_example' # str | The infra-env of the host that should be deregistered.
    host_id = 'host_id_example' # str | The host that should be deregistered.

    try:
        api_instance.v2_deregister_host(infra_env_id, host_id)
    except Exception as e:
        print("Exception when calling InstallerApi->v2_deregister_host: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **infra_env_id** | **str**| The infra-env of the host that should be deregistered. | 
 **host_id** | **str**| The host that should be deregistered. | 

### Return type

void (empty response body)

### Authorization

[userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success. |  -  |
**400** | Error. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Error. |  -  |
**405** | Method Not Allowed. |  -  |
**500** | Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_download_cluster_credentials**
> bytearray v2_download_cluster_credentials(cluster_id, file_name)



Downloads credentials relating to the installed/installing cluster.

### Example

* Api Key Authentication (urlAuth):
* Api Key Authentication (userAuth):
* Api Key Authentication (agentAuth):
```python
import time
import os
import openshift_assisted_service
from openshift_assisted_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.openshift.com/api/assisted-install
# See configuration.py for a list of all supported configuration parameters.
configuration = openshift_assisted_service.Configuration(
    host = "http://api.openshift.com/api/assisted-install"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: urlAuth
configuration.api_key['urlAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['urlAuth'] = 'Bearer'

# Configure API key authorization: userAuth
configuration.api_key['userAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAuth'] = 'Bearer'

# Configure API key authorization: agentAuth
configuration.api_key['agentAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['agentAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openshift_assisted_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openshift_assisted_service.InstallerApi(api_client)
    cluster_id = 'cluster_id_example' # str | The cluster that owns the credential file that should be downloaded.
    file_name = 'file_name_example' # str | The credential file to be downloaded.

    try:
        api_response = api_instance.v2_download_cluster_credentials(cluster_id, file_name)
        print("The response of InstallerApi->v2_download_cluster_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallerApi->v2_download_cluster_credentials: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The cluster that owns the credential file that should be downloaded. | 
 **file_name** | **str**| The credential file to be downloaded. | 

### Return type

**bytearray**

### Authorization

[urlAuth](../README.md#urlAuth), [userAuth](../README.md#userAuth), [agentAuth](../README.md#agentAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Error. |  -  |
**405** | Method Not Allowed. |  -  |
**409** | Error. |  -  |
**500** | Error. |  -  |
**503** | Unavailable. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_download_cluster_files**
> bytearray v2_download_cluster_files(cluster_id, file_name, discovery_agent_version=discovery_agent_version)



Downloads files relating to the installed/installing cluster.

### Example

* Api Key Authentication (urlAuth):
* Api Key Authentication (userAuth):
* Api Key Authentication (agentAuth):
```python
import time
import os
import openshift_assisted_service
from openshift_assisted_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.openshift.com/api/assisted-install
# See configuration.py for a list of all supported configuration parameters.
configuration = openshift_assisted_service.Configuration(
    host = "http://api.openshift.com/api/assisted-install"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: urlAuth
configuration.api_key['urlAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['urlAuth'] = 'Bearer'

# Configure API key authorization: userAuth
configuration.api_key['userAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAuth'] = 'Bearer'

# Configure API key authorization: agentAuth
configuration.api_key['agentAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['agentAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openshift_assisted_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openshift_assisted_service.InstallerApi(api_client)
    cluster_id = 'cluster_id_example' # str | The cluster that owns the file that should be downloaded.
    file_name = 'file_name_example' # str | The file to be downloaded.
    discovery_agent_version = 'discovery_agent_version_example' # str | The software version of the discovery agent that is downloading the file. (optional)

    try:
        api_response = api_instance.v2_download_cluster_files(cluster_id, file_name, discovery_agent_version=discovery_agent_version)
        print("The response of InstallerApi->v2_download_cluster_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallerApi->v2_download_cluster_files: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The cluster that owns the file that should be downloaded. | 
 **file_name** | **str**| The file to be downloaded. | 
 **discovery_agent_version** | **str**| The software version of the discovery agent that is downloading the file. | [optional] 

### Return type

**bytearray**

### Authorization

[urlAuth](../README.md#urlAuth), [userAuth](../README.md#userAuth), [agentAuth](../README.md#agentAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Error. |  -  |
**405** | Method Not Allowed. |  -  |
**409** | Error. |  -  |
**500** | Error. |  -  |
**503** | Unavailable. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_download_cluster_logs**
> bytearray v2_download_cluster_logs(cluster_id, logs_type=logs_type, host_id=host_id)



Download cluster logs.

### Example

* Api Key Authentication (urlAuth):
* Api Key Authentication (userAuth):
```python
import time
import os
import openshift_assisted_service
from openshift_assisted_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.openshift.com/api/assisted-install
# See configuration.py for a list of all supported configuration parameters.
configuration = openshift_assisted_service.Configuration(
    host = "http://api.openshift.com/api/assisted-install"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: urlAuth
configuration.api_key['urlAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['urlAuth'] = 'Bearer'

# Configure API key authorization: userAuth
configuration.api_key['userAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openshift_assisted_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openshift_assisted_service.InstallerApi(api_client)
    cluster_id = 'cluster_id_example' # str | The cluster whose logs should be downloaded.
    logs_type = 'logs_type_example' # str | The type of logs to be downloaded. (optional)
    host_id = 'host_id_example' # str | A specific host in the cluster whose logs should be downloaded. (optional)

    try:
        api_response = api_instance.v2_download_cluster_logs(cluster_id, logs_type=logs_type, host_id=host_id)
        print("The response of InstallerApi->v2_download_cluster_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallerApi->v2_download_cluster_logs: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The cluster whose logs should be downloaded. | 
 **logs_type** | **str**| The type of logs to be downloaded. | [optional] 
 **host_id** | **str**| A specific host in the cluster whose logs should be downloaded. | [optional] 

### Return type

**bytearray**

### Authorization

[urlAuth](../README.md#urlAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Error. |  -  |
**405** | Method Not Allowed. |  -  |
**409** | Error. |  -  |
**500** | Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_download_host_ignition**
> bytearray v2_download_host_ignition(infra_env_id, host_id)



Downloads the customized ignition file for this bound host, produces octet stream. For unbound host - error is returned

### Example

* Api Key Authentication (userAuth):
* Api Key Authentication (agentAuth):
```python
import time
import os
import openshift_assisted_service
from openshift_assisted_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.openshift.com/api/assisted-install
# See configuration.py for a list of all supported configuration parameters.
configuration = openshift_assisted_service.Configuration(
    host = "http://api.openshift.com/api/assisted-install"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAuth
configuration.api_key['userAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAuth'] = 'Bearer'

# Configure API key authorization: agentAuth
configuration.api_key['agentAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['agentAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openshift_assisted_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openshift_assisted_service.InstallerApi(api_client)
    infra_env_id = 'infra_env_id_example' # str | The infra-env of the host whose ignition file should be downloaded.
    host_id = 'host_id_example' # str | The host whose ignition file should be downloaded.

    try:
        api_response = api_instance.v2_download_host_ignition(infra_env_id, host_id)
        print("The response of InstallerApi->v2_download_host_ignition:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallerApi->v2_download_host_ignition: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **infra_env_id** | **str**| The infra-env of the host whose ignition file should be downloaded. | 
 **host_id** | **str**| The host whose ignition file should be downloaded. | 

### Return type

**bytearray**

### Authorization

[userAuth](../README.md#userAuth), [agentAuth](../README.md#agentAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Error. |  -  |
**405** | Method Not Allowed. |  -  |
**409** | Error. |  -  |
**500** | Error. |  -  |
**503** | Unavailable. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_download_infra_env_files**
> bytearray v2_download_infra_env_files(infra_env_id, file_name, mac=mac, ipxe_script_type=ipxe_script_type, discovery_iso_type=discovery_iso_type)



Downloads the customized ignition file for this host

### Example

* Api Key Authentication (imageURLAuth):
* Api Key Authentication (urlAuth):
* Api Key Authentication (userAuth):
* Api Key Authentication (imageAuth):
* Api Key Authentication (agentAuth):
```python
import time
import os
import openshift_assisted_service
from openshift_assisted_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.openshift.com/api/assisted-install
# See configuration.py for a list of all supported configuration parameters.
configuration = openshift_assisted_service.Configuration(
    host = "http://api.openshift.com/api/assisted-install"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: imageURLAuth
configuration.api_key['imageURLAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['imageURLAuth'] = 'Bearer'

# Configure API key authorization: urlAuth
configuration.api_key['urlAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['urlAuth'] = 'Bearer'

# Configure API key authorization: userAuth
configuration.api_key['userAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAuth'] = 'Bearer'

# Configure API key authorization: imageAuth
configuration.api_key['imageAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['imageAuth'] = 'Bearer'

# Configure API key authorization: agentAuth
configuration.api_key['agentAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['agentAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openshift_assisted_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openshift_assisted_service.InstallerApi(api_client)
    infra_env_id = 'infra_env_id_example' # str | The infra-env whose file should be downloaded.
    file_name = 'file_name_example' # str | The file to be downloaded.
    mac = 'mac_example' # str | Mac address of the host running ipxe script. (optional)
    ipxe_script_type = 'ipxe_script_type_example' # str | Specify the script type to be served for iPXE. (optional)
    discovery_iso_type = 'discovery_iso_type_example' # str | Overrides the ISO type for the disovery ignition, either 'full-iso' or 'minimal-iso'. (optional)

    try:
        api_response = api_instance.v2_download_infra_env_files(infra_env_id, file_name, mac=mac, ipxe_script_type=ipxe_script_type, discovery_iso_type=discovery_iso_type)
        print("The response of InstallerApi->v2_download_infra_env_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallerApi->v2_download_infra_env_files: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **infra_env_id** | **str**| The infra-env whose file should be downloaded. | 
 **file_name** | **str**| The file to be downloaded. | 
 **mac** | **str**| Mac address of the host running ipxe script. | [optional] 
 **ipxe_script_type** | **str**| Specify the script type to be served for iPXE. | [optional] 
 **discovery_iso_type** | **str**| Overrides the ISO type for the disovery ignition, either &#39;full-iso&#39; or &#39;minimal-iso&#39;. | [optional] 

### Return type

**bytearray**

### Authorization

[imageURLAuth](../README.md#imageURLAuth), [urlAuth](../README.md#urlAuth), [userAuth](../README.md#userAuth), [imageAuth](../README.md#imageAuth), [agentAuth](../README.md#agentAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**400** | Bad Request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Error. |  -  |
**405** | Method Not Allowed. |  -  |
**409** | Error. |  -  |
**500** | Error. |  -  |
**501** | Not implemented. |  -  |
**503** | Unavailable. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_get_cluster**
> Cluster v2_get_cluster(cluster_id, discovery_agent_version=discovery_agent_version, get_unregistered_clusters=get_unregistered_clusters, exclude_hosts=exclude_hosts)



Retrieves the details of the OpenShift cluster.

### Example

* Api Key Authentication (userAuth):
* Api Key Authentication (agentAuth):
```python
import time
import os
import openshift_assisted_service
from openshift_assisted_service.models.cluster import Cluster
from openshift_assisted_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.openshift.com/api/assisted-install
# See configuration.py for a list of all supported configuration parameters.
configuration = openshift_assisted_service.Configuration(
    host = "http://api.openshift.com/api/assisted-install"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAuth
configuration.api_key['userAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAuth'] = 'Bearer'

# Configure API key authorization: agentAuth
configuration.api_key['agentAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['agentAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openshift_assisted_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openshift_assisted_service.InstallerApi(api_client)
    cluster_id = 'cluster_id_example' # str | The cluster to be retrieved.
    discovery_agent_version = 'discovery_agent_version_example' # str | The software version of the discovery agent that is retrieving the cluster details. (optional)
    get_unregistered_clusters = False # bool | Whether to return clusters that have been unregistered. (optional) (default to False)
    exclude_hosts = True # bool | If true, do not include hosts. (optional)

    try:
        api_response = api_instance.v2_get_cluster(cluster_id, discovery_agent_version=discovery_agent_version, get_unregistered_clusters=get_unregistered_clusters, exclude_hosts=exclude_hosts)
        print("The response of InstallerApi->v2_get_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallerApi->v2_get_cluster: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The cluster to be retrieved. | 
 **discovery_agent_version** | **str**| The software version of the discovery agent that is retrieving the cluster details. | [optional] 
 **get_unregistered_clusters** | **bool**| Whether to return clusters that have been unregistered. | [optional] [default to False]
 **exclude_hosts** | **bool**| If true, do not include hosts. | [optional] 

### Return type

[**Cluster**](Cluster.md)

### Authorization

[userAuth](../README.md#userAuth), [agentAuth](../README.md#agentAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Error. |  -  |
**405** | Method Not Allowed. |  -  |
**500** | Error. |  -  |
**503** | Unavailable. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_get_cluster_default_config**
> ClusterDefaultConfig v2_get_cluster_default_config()



Get the default values for various cluster properties.

### Example

* Api Key Authentication (userAuth):
```python
import time
import os
import openshift_assisted_service
from openshift_assisted_service.models.cluster_default_config import ClusterDefaultConfig
from openshift_assisted_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.openshift.com/api/assisted-install
# See configuration.py for a list of all supported configuration parameters.
configuration = openshift_assisted_service.Configuration(
    host = "http://api.openshift.com/api/assisted-install"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAuth
configuration.api_key['userAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openshift_assisted_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openshift_assisted_service.InstallerApi(api_client)

    try:
        api_response = api_instance.v2_get_cluster_default_config()
        print("The response of InstallerApi->v2_get_cluster_default_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallerApi->v2_get_cluster_default_config: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterDefaultConfig**](ClusterDefaultConfig.md)

### Authorization

[userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**500** | Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_get_cluster_install_config**
> str v2_get_cluster_install_config(cluster_id)



Get the cluster's install config YAML.

### Example

* Api Key Authentication (userAuth):
```python
import time
import os
import openshift_assisted_service
from openshift_assisted_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.openshift.com/api/assisted-install
# See configuration.py for a list of all supported configuration parameters.
configuration = openshift_assisted_service.Configuration(
    host = "http://api.openshift.com/api/assisted-install"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAuth
configuration.api_key['userAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openshift_assisted_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openshift_assisted_service.InstallerApi(api_client)
    cluster_id = 'cluster_id_example' # str | The cluster whose install config is being retrieved.

    try:
        api_response = api_instance.v2_get_cluster_install_config(cluster_id)
        print("The response of InstallerApi->v2_get_cluster_install_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallerApi->v2_get_cluster_install_config: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The cluster whose install config is being retrieved. | 

### Return type

**str**

### Authorization

[userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Error. |  -  |
**405** | Method Not Allowed. |  -  |
**500** | Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_get_cluster_ui_settings**
> str v2_get_cluster_ui_settings(cluster_id)



Fetch cluster specific UI settings.

### Example

* Api Key Authentication (userAuth):
```python
import time
import os
import openshift_assisted_service
from openshift_assisted_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.openshift.com/api/assisted-install
# See configuration.py for a list of all supported configuration parameters.
configuration = openshift_assisted_service.Configuration(
    host = "http://api.openshift.com/api/assisted-install"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAuth
configuration.api_key['userAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openshift_assisted_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openshift_assisted_service.InstallerApi(api_client)
    cluster_id = 'cluster_id_example' # str | The cluster for which UI settings should be retrieved.

    try:
        api_response = api_instance.v2_get_cluster_ui_settings(cluster_id)
        print("The response of InstallerApi->v2_get_cluster_ui_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallerApi->v2_get_cluster_ui_settings: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The cluster for which UI settings should be retrieved. | 

### Return type

**str**

### Authorization

[userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**400** | Error. |  -  |
**404** | Error. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**500** | Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_get_credentials**
> Credentials v2_get_credentials(cluster_id)



Get the cluster admin credentials.

### Example

* Api Key Authentication (userAuth):
```python
import time
import os
import openshift_assisted_service
from openshift_assisted_service.models.credentials import Credentials
from openshift_assisted_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.openshift.com/api/assisted-install
# See configuration.py for a list of all supported configuration parameters.
configuration = openshift_assisted_service.Configuration(
    host = "http://api.openshift.com/api/assisted-install"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAuth
configuration.api_key['userAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openshift_assisted_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openshift_assisted_service.InstallerApi(api_client)
    cluster_id = 'cluster_id_example' # str | The cluster whose admin credentials should be retrieved.

    try:
        api_response = api_instance.v2_get_credentials(cluster_id)
        print("The response of InstallerApi->v2_get_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallerApi->v2_get_credentials: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The cluster whose admin credentials should be retrieved. | 

### Return type

[**Credentials**](Credentials.md)

### Authorization

[userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Error. |  -  |
**405** | Method Not Allowed. |  -  |
**409** | Error. |  -  |
**500** | Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_get_host**
> Host v2_get_host(infra_env_id, host_id)



Retrieves the details of the OpenShift host.

### Example

* Api Key Authentication (userAuth):
```python
import time
import os
import openshift_assisted_service
from openshift_assisted_service.models.host import Host
from openshift_assisted_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.openshift.com/api/assisted-install
# See configuration.py for a list of all supported configuration parameters.
configuration = openshift_assisted_service.Configuration(
    host = "http://api.openshift.com/api/assisted-install"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAuth
configuration.api_key['userAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openshift_assisted_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openshift_assisted_service.InstallerApi(api_client)
    infra_env_id = 'infra_env_id_example' # str | The infra-env of the host that should be retrieved.
    host_id = 'host_id_example' # str | The host that should be retrieved.

    try:
        api_response = api_instance.v2_get_host(infra_env_id, host_id)
        print("The response of InstallerApi->v2_get_host:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallerApi->v2_get_host: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **infra_env_id** | **str**| The infra-env of the host that should be retrieved. | 
 **host_id** | **str**| The host that should be retrieved. | 

### Return type

[**Host**](Host.md)

### Authorization

[userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Error. |  -  |
**405** | Method Not Allowed. |  -  |
**500** | Error. |  -  |
**501** | Not implemented. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_get_host_ignition**
> HostIgnitionParams v2_get_host_ignition(infra_env_id, host_id)



Fetch the ignition file for this host as a string. In case of unbound host produces an error

### Example

* Api Key Authentication (userAuth):
```python
import time
import os
import openshift_assisted_service
from openshift_assisted_service.models.host_ignition_params import HostIgnitionParams
from openshift_assisted_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.openshift.com/api/assisted-install
# See configuration.py for a list of all supported configuration parameters.
configuration = openshift_assisted_service.Configuration(
    host = "http://api.openshift.com/api/assisted-install"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAuth
configuration.api_key['userAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openshift_assisted_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openshift_assisted_service.InstallerApi(api_client)
    infra_env_id = 'infra_env_id_example' # str | The infra-env of the host whose ignition file should be obtained.
    host_id = 'host_id_example' # str | The host whose ignition file should be obtained.

    try:
        api_response = api_instance.v2_get_host_ignition(infra_env_id, host_id)
        print("The response of InstallerApi->v2_get_host_ignition:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallerApi->v2_get_host_ignition: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **infra_env_id** | **str**| The infra-env of the host whose ignition file should be obtained. | 
 **host_id** | **str**| The host whose ignition file should be obtained. | 

### Return type

[**HostIgnitionParams**](HostIgnitionParams.md)

### Authorization

[userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Error. |  -  |
**405** | Method Not Allowed. |  -  |
**500** | Error. |  -  |
**501** | Not implemented. |  -  |
**503** | Unavailable. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_get_ignored_validations**
> IgnoredValidations v2_get_ignored_validations(cluster_id)



Fetch the validations which are to be ignored for this cluster.

### Example

* Api Key Authentication (userAuth):
```python
import time
import os
import openshift_assisted_service
from openshift_assisted_service.models.ignored_validations import IgnoredValidations
from openshift_assisted_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.openshift.com/api/assisted-install
# See configuration.py for a list of all supported configuration parameters.
configuration = openshift_assisted_service.Configuration(
    host = "http://api.openshift.com/api/assisted-install"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAuth
configuration.api_key['userAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openshift_assisted_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openshift_assisted_service.InstallerApi(api_client)
    cluster_id = 'cluster_id_example' # str | The cluster whose failing validations should be ignored according to this list.

    try:
        api_response = api_instance.v2_get_ignored_validations(cluster_id)
        print("The response of InstallerApi->v2_get_ignored_validations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallerApi->v2_get_ignored_validations: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The cluster whose failing validations should be ignored according to this list. | 

### Return type

[**IgnoredValidations**](IgnoredValidations.md)

### Authorization

[userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**400** | Error. |  -  |
**404** | Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_get_next_steps**
> Steps v2_get_next_steps(infra_env_id, host_id, timestamp=timestamp, discovery_agent_version=discovery_agent_version)



Retrieves the next operations that the host agent needs to perform.

### Example

* Api Key Authentication (agentAuth):
```python
import time
import os
import openshift_assisted_service
from openshift_assisted_service.models.steps import Steps
from openshift_assisted_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.openshift.com/api/assisted-install
# See configuration.py for a list of all supported configuration parameters.
configuration = openshift_assisted_service.Configuration(
    host = "http://api.openshift.com/api/assisted-install"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: agentAuth
configuration.api_key['agentAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['agentAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openshift_assisted_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openshift_assisted_service.InstallerApi(api_client)
    infra_env_id = 'infra_env_id_example' # str | The infra-env of the host that is retrieving instructions.
    host_id = 'host_id_example' # str | The host that is retrieving instructions.
    timestamp = 56 # int | The time on the host as seconds since the Unix epoch. (optional)
    discovery_agent_version = 'discovery_agent_version_example' # str | The software version of the discovery agent that is retrieving instructions. (optional)

    try:
        api_response = api_instance.v2_get_next_steps(infra_env_id, host_id, timestamp=timestamp, discovery_agent_version=discovery_agent_version)
        print("The response of InstallerApi->v2_get_next_steps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallerApi->v2_get_next_steps: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **infra_env_id** | **str**| The infra-env of the host that is retrieving instructions. | 
 **host_id** | **str**| The host that is retrieving instructions. | 
 **timestamp** | **int**| The time on the host as seconds since the Unix epoch. | [optional] 
 **discovery_agent_version** | **str**| The software version of the discovery agent that is retrieving instructions. | [optional] 

### Return type

[**Steps**](Steps.md)

### Authorization

[agentAuth](../README.md#agentAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Error. |  -  |
**405** | Method Not Allowed. |  -  |
**500** | Error. |  -  |
**501** | Not implemented. |  -  |
**503** | Unavailable. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_get_preflight_requirements**
> PreflightHardwareRequirements v2_get_preflight_requirements(cluster_id)



Get preflight requirements for a cluster.

### Example

* Api Key Authentication (userAuth):
```python
import time
import os
import openshift_assisted_service
from openshift_assisted_service.models.preflight_hardware_requirements import PreflightHardwareRequirements
from openshift_assisted_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.openshift.com/api/assisted-install
# See configuration.py for a list of all supported configuration parameters.
configuration = openshift_assisted_service.Configuration(
    host = "http://api.openshift.com/api/assisted-install"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAuth
configuration.api_key['userAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openshift_assisted_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openshift_assisted_service.InstallerApi(api_client)
    cluster_id = 'cluster_id_example' # str | The cluster to return preflight requirements for.

    try:
        api_response = api_instance.v2_get_preflight_requirements(cluster_id)
        print("The response of InstallerApi->v2_get_preflight_requirements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallerApi->v2_get_preflight_requirements: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The cluster to return preflight requirements for. | 

### Return type

[**PreflightHardwareRequirements**](PreflightHardwareRequirements.md)

### Authorization

[userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Error. |  -  |
**405** | Method Not Allowed. |  -  |
**500** | Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_get_presigned_for_cluster_credentials**
> PresignedUrl v2_get_presigned_for_cluster_credentials(cluster_id, file_name)



Get the cluster admin credentials.

### Example

* Api Key Authentication (userAuth):
```python
import time
import os
import openshift_assisted_service
from openshift_assisted_service.models.presigned_url import PresignedUrl
from openshift_assisted_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.openshift.com/api/assisted-install
# See configuration.py for a list of all supported configuration parameters.
configuration = openshift_assisted_service.Configuration(
    host = "http://api.openshift.com/api/assisted-install"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAuth
configuration.api_key['userAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openshift_assisted_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openshift_assisted_service.InstallerApi(api_client)
    cluster_id = 'cluster_id_example' # str | The cluster that owns the file that should be downloaded.
    file_name = 'file_name_example' # str | The file to be downloaded.

    try:
        api_response = api_instance.v2_get_presigned_for_cluster_credentials(cluster_id, file_name)
        print("The response of InstallerApi->v2_get_presigned_for_cluster_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallerApi->v2_get_presigned_for_cluster_credentials: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The cluster that owns the file that should be downloaded. | 
 **file_name** | **str**| The file to be downloaded. | 

### Return type

[**PresignedUrl**](PresignedUrl.md)

### Authorization

[userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**400** | Error. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Error. |  -  |
**405** | Method Not Allowed. |  -  |
**409** | Error. |  -  |
**500** | Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_get_presigned_for_cluster_files**
> PresignedUrl v2_get_presigned_for_cluster_files(cluster_id, file_name, logs_type=logs_type, host_id=host_id, additional_name=additional_name)



Retrieves a pre-signed S3 URL for downloading cluster files.

### Example

* Api Key Authentication (userAuth):
```python
import time
import os
import openshift_assisted_service
from openshift_assisted_service.models.presigned_url import PresignedUrl
from openshift_assisted_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.openshift.com/api/assisted-install
# See configuration.py for a list of all supported configuration parameters.
configuration = openshift_assisted_service.Configuration(
    host = "http://api.openshift.com/api/assisted-install"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAuth
configuration.api_key['userAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openshift_assisted_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openshift_assisted_service.InstallerApi(api_client)
    cluster_id = 'cluster_id_example' # str | The cluster that owns the file that should be downloaded.
    file_name = 'file_name_example' # str | The file to be downloaded.
    logs_type = 'logs_type_example' # str | If downloading logs, the type of logs to download. (optional)
    host_id = 'host_id_example' # str | If downloading a file related to a host, the relevant host. (optional)
    additional_name = 'additional_name_example' # str | If downloading a manifest, the file name, prefaced with folder name, for example, openshift/99-openshift-xyz.yaml. (optional)

    try:
        api_response = api_instance.v2_get_presigned_for_cluster_files(cluster_id, file_name, logs_type=logs_type, host_id=host_id, additional_name=additional_name)
        print("The response of InstallerApi->v2_get_presigned_for_cluster_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallerApi->v2_get_presigned_for_cluster_files: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The cluster that owns the file that should be downloaded. | 
 **file_name** | **str**| The file to be downloaded. | 
 **logs_type** | **str**| If downloading logs, the type of logs to download. | [optional] 
 **host_id** | **str**| If downloading a file related to a host, the relevant host. | [optional] 
 **additional_name** | **str**| If downloading a manifest, the file name, prefaced with folder name, for example, openshift/99-openshift-xyz.yaml. | [optional] 

### Return type

[**PresignedUrl**](PresignedUrl.md)

### Authorization

[userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**400** | Error. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Error. |  -  |
**405** | Method Not Allowed. |  -  |
**409** | Error. |  -  |
**500** | Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_import_cluster**
> Cluster v2_import_cluster(new_import_cluster_params)



Import an AI cluster using minimal data associated with existing OCP cluster, in order to allow adding day2 hosts to that cluster

### Example

* Api Key Authentication (userAuth):
```python
import time
import os
import openshift_assisted_service
from openshift_assisted_service.models.cluster import Cluster
from openshift_assisted_service.models.import_cluster_params import ImportClusterParams
from openshift_assisted_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.openshift.com/api/assisted-install
# See configuration.py for a list of all supported configuration parameters.
configuration = openshift_assisted_service.Configuration(
    host = "http://api.openshift.com/api/assisted-install"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAuth
configuration.api_key['userAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openshift_assisted_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openshift_assisted_service.InstallerApi(api_client)
    new_import_cluster_params = openshift_assisted_service.ImportClusterParams() # ImportClusterParams | Parameters for importing a OCP cluster for adding nodes.

    try:
        api_response = api_instance.v2_import_cluster(new_import_cluster_params)
        print("The response of InstallerApi->v2_import_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallerApi->v2_import_cluster: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_import_cluster_params** | [**ImportClusterParams**](ImportClusterParams.md)| Parameters for importing a OCP cluster for adding nodes. | 

### Return type

[**Cluster**](Cluster.md)

### Authorization

[userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success. |  -  |
**400** | Error. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**500** | Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_install_cluster**
> Cluster v2_install_cluster(cluster_id)



Installs the OpenShift cluster.

### Example

* Api Key Authentication (userAuth):
```python
import time
import os
import openshift_assisted_service
from openshift_assisted_service.models.cluster import Cluster
from openshift_assisted_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.openshift.com/api/assisted-install
# See configuration.py for a list of all supported configuration parameters.
configuration = openshift_assisted_service.Configuration(
    host = "http://api.openshift.com/api/assisted-install"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAuth
configuration.api_key['userAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openshift_assisted_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openshift_assisted_service.InstallerApi(api_client)
    cluster_id = 'cluster_id_example' # str | The cluster to be installed.

    try:
        api_response = api_instance.v2_install_cluster(cluster_id)
        print("The response of InstallerApi->v2_install_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallerApi->v2_install_cluster: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The cluster to be installed. | 

### Return type

[**Cluster**](Cluster.md)

### Authorization

[userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Success. |  -  |
**400** | Error. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Error. |  -  |
**405** | Method Not Allowed. |  -  |
**409** | Error. |  -  |
**500** | Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_install_host**
> Host v2_install_host(infra_env_id, host_id)



install specific host for day2 cluster.

### Example

* Api Key Authentication (userAuth):
```python
import time
import os
import openshift_assisted_service
from openshift_assisted_service.models.host import Host
from openshift_assisted_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.openshift.com/api/assisted-install
# See configuration.py for a list of all supported configuration parameters.
configuration = openshift_assisted_service.Configuration(
    host = "http://api.openshift.com/api/assisted-install"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAuth
configuration.api_key['userAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openshift_assisted_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openshift_assisted_service.InstallerApi(api_client)
    infra_env_id = 'infra_env_id_example' # str | The infra-env of the host that is being installed.
    host_id = 'host_id_example' # str | The host that is being installed.

    try:
        api_response = api_instance.v2_install_host(infra_env_id, host_id)
        print("The response of InstallerApi->v2_install_host:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallerApi->v2_install_host: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **infra_env_id** | **str**| The infra-env of the host that is being installed. | 
 **host_id** | **str**| The host that is being installed. | 

### Return type

[**Host**](Host.md)

### Authorization

[userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Success. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Error. |  -  |
**409** | Error. |  -  |
**500** | Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_list_clusters**
> List[Cluster] v2_list_clusters(get_unregistered_clusters=get_unregistered_clusters, openshift_cluster_id=openshift_cluster_id, ams_subscription_ids=ams_subscription_ids, with_hosts=with_hosts, owner=owner)



Retrieves the list of OpenShift clusters.

### Example

* Api Key Authentication (userAuth):
```python
import time
import os
import openshift_assisted_service
from openshift_assisted_service.models.cluster import Cluster
from openshift_assisted_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.openshift.com/api/assisted-install
# See configuration.py for a list of all supported configuration parameters.
configuration = openshift_assisted_service.Configuration(
    host = "http://api.openshift.com/api/assisted-install"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAuth
configuration.api_key['userAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openshift_assisted_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openshift_assisted_service.InstallerApi(api_client)
    get_unregistered_clusters = False # bool | Whether to return clusters that have been unregistered. (optional) (default to False)
    openshift_cluster_id = 'openshift_cluster_id_example' # str | A specific cluster to retrieve. (optional)
    ams_subscription_ids = ['ams_subscription_ids_example'] # List[str] | If non-empty, returned Clusters are filtered to those with matching subscription IDs. (optional)
    with_hosts = False # bool | Include hosts in the returned list. (optional) (default to False)
    owner = 'owner_example' # str | If provided, returns only clusters that are owned by the specified user. (optional)

    try:
        api_response = api_instance.v2_list_clusters(get_unregistered_clusters=get_unregistered_clusters, openshift_cluster_id=openshift_cluster_id, ams_subscription_ids=ams_subscription_ids, with_hosts=with_hosts, owner=owner)
        print("The response of InstallerApi->v2_list_clusters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallerApi->v2_list_clusters: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_unregistered_clusters** | **bool**| Whether to return clusters that have been unregistered. | [optional] [default to False]
 **openshift_cluster_id** | **str**| A specific cluster to retrieve. | [optional] 
 **ams_subscription_ids** | [**List[str]**](str.md)| If non-empty, returned Clusters are filtered to those with matching subscription IDs. | [optional] 
 **with_hosts** | **bool**| Include hosts in the returned list. | [optional] [default to False]
 **owner** | **str**| If provided, returns only clusters that are owned by the specified user. | [optional] 

### Return type

[**List[Cluster]**](Cluster.md)

### Authorization

[userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**405** | Method Not Allowed. |  -  |
**500** | Error. |  -  |
**503** | Unavailable. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_list_feature_support_levels**
> List[FeatureSupportLevel] v2_list_feature_support_levels()



(DEPRECATED) Retrieves the support levels for features for each OpenShift version.

### Example

* Api Key Authentication (userAuth):
```python
import time
import os
import openshift_assisted_service
from openshift_assisted_service.models.feature_support_level import FeatureSupportLevel
from openshift_assisted_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.openshift.com/api/assisted-install
# See configuration.py for a list of all supported configuration parameters.
configuration = openshift_assisted_service.Configuration(
    host = "http://api.openshift.com/api/assisted-install"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAuth
configuration.api_key['userAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openshift_assisted_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openshift_assisted_service.InstallerApi(api_client)

    try:
        api_response = api_instance.v2_list_feature_support_levels()
        print("The response of InstallerApi->v2_list_feature_support_levels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallerApi->v2_list_feature_support_levels: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[FeatureSupportLevel]**](FeatureSupportLevel.md)

### Authorization

[userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**503** | Unavailable. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_list_hosts**
> List[Host] v2_list_hosts(infra_env_id)



Retrieves the list of OpenShift hosts that belong the infra-env.

### Example

* Api Key Authentication (userAuth):
* Api Key Authentication (agentAuth):
```python
import time
import os
import openshift_assisted_service
from openshift_assisted_service.models.host import Host
from openshift_assisted_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.openshift.com/api/assisted-install
# See configuration.py for a list of all supported configuration parameters.
configuration = openshift_assisted_service.Configuration(
    host = "http://api.openshift.com/api/assisted-install"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAuth
configuration.api_key['userAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAuth'] = 'Bearer'

# Configure API key authorization: agentAuth
configuration.api_key['agentAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['agentAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openshift_assisted_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openshift_assisted_service.InstallerApi(api_client)
    infra_env_id = 'infra_env_id_example' # str | The infra-env that the hosts are asociated with.

    try:
        api_response = api_instance.v2_list_hosts(infra_env_id)
        print("The response of InstallerApi->v2_list_hosts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallerApi->v2_list_hosts: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **infra_env_id** | **str**| The infra-env that the hosts are asociated with. | 

### Return type

[**List[Host]**](Host.md)

### Authorization

[userAuth](../README.md#userAuth), [agentAuth](../README.md#agentAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**405** | Method Not Allowed. |  -  |
**500** | Error. |  -  |
**501** | Not implemented. |  -  |
**503** | Unavailable. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_list_of_cluster_operators**
> List[MonitoredOperator] v2_list_of_cluster_operators(cluster_id, operator_name=operator_name)



Lists operators to be monitored for a cluster.

### Example

* Api Key Authentication (agentAuth):
```python
import time
import os
import openshift_assisted_service
from openshift_assisted_service.models.monitored_operator import MonitoredOperator
from openshift_assisted_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.openshift.com/api/assisted-install
# See configuration.py for a list of all supported configuration parameters.
configuration = openshift_assisted_service.Configuration(
    host = "http://api.openshift.com/api/assisted-install"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: agentAuth
configuration.api_key['agentAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['agentAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openshift_assisted_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openshift_assisted_service.InstallerApi(api_client)
    cluster_id = 'cluster_id_example' # str | The cluster to return operators for.
    operator_name = 'operator_name_example' # str | An operator in the specified cluster to return its data. (optional)

    try:
        api_response = api_instance.v2_list_of_cluster_operators(cluster_id, operator_name=operator_name)
        print("The response of InstallerApi->v2_list_of_cluster_operators:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallerApi->v2_list_of_cluster_operators: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The cluster to return operators for. | 
 **operator_name** | **str**| An operator in the specified cluster to return its data. | [optional] 

### Return type

[**List[MonitoredOperator]**](MonitoredOperator.md)

### Authorization

[agentAuth](../README.md#agentAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Error. |  -  |
**405** | Method Not Allowed. |  -  |
**500** | Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_post_step_reply**
> v2_post_step_reply(infra_env_id, host_id, discovery_agent_version=discovery_agent_version, reply=reply)



Posts the result of the operations from the host agent.

### Example

* Api Key Authentication (agentAuth):
```python
import time
import os
import openshift_assisted_service
from openshift_assisted_service.models.step_reply import StepReply
from openshift_assisted_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.openshift.com/api/assisted-install
# See configuration.py for a list of all supported configuration parameters.
configuration = openshift_assisted_service.Configuration(
    host = "http://api.openshift.com/api/assisted-install"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: agentAuth
configuration.api_key['agentAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['agentAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openshift_assisted_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openshift_assisted_service.InstallerApi(api_client)
    infra_env_id = 'infra_env_id_example' # str | The infra-env of the host that is posting results.
    host_id = 'host_id_example' # str | The host that is posting results.
    discovery_agent_version = 'discovery_agent_version_example' # str | The software version of the discovery agent that is posting results. (optional)
    reply = openshift_assisted_service.StepReply() # StepReply | The results to be posted. (optional)

    try:
        api_instance.v2_post_step_reply(infra_env_id, host_id, discovery_agent_version=discovery_agent_version, reply=reply)
    except Exception as e:
        print("Exception when calling InstallerApi->v2_post_step_reply: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **infra_env_id** | **str**| The infra-env of the host that is posting results. | 
 **host_id** | **str**| The host that is posting results. | 
 **discovery_agent_version** | **str**| The software version of the discovery agent that is posting results. | [optional] 
 **reply** | [**StepReply**](StepReply.md)| The results to be posted. | [optional] 

### Return type

void (empty response body)

### Authorization

[agentAuth](../README.md#agentAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success. |  -  |
**400** | Error. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Error. |  -  |
**405** | Method Not Allowed. |  -  |
**500** | Error. |  -  |
**501** | Not implemented. |  -  |
**503** | Unavailable. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_register_cluster**
> Cluster v2_register_cluster(new_cluster_params)



Creates a new OpenShift cluster definition.

### Example

* Api Key Authentication (userAuth):
```python
import time
import os
import openshift_assisted_service
from openshift_assisted_service.models.cluster import Cluster
from openshift_assisted_service.models.cluster_create_params import ClusterCreateParams
from openshift_assisted_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.openshift.com/api/assisted-install
# See configuration.py for a list of all supported configuration parameters.
configuration = openshift_assisted_service.Configuration(
    host = "http://api.openshift.com/api/assisted-install"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAuth
configuration.api_key['userAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openshift_assisted_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openshift_assisted_service.InstallerApi(api_client)
    new_cluster_params = openshift_assisted_service.ClusterCreateParams() # ClusterCreateParams | The properties describing the new cluster.

    try:
        api_response = api_instance.v2_register_cluster(new_cluster_params)
        print("The response of InstallerApi->v2_register_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallerApi->v2_register_cluster: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_cluster_params** | [**ClusterCreateParams**](ClusterCreateParams.md)| The properties describing the new cluster. | 

### Return type

[**Cluster**](Cluster.md)

### Authorization

[userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success. |  -  |
**400** | Error. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**405** | Method Not Allowed. |  -  |
**500** | Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_register_host**
> HostRegistrationResponse v2_register_host(infra_env_id, new_host_params, discovery_agent_version=discovery_agent_version)



Registers a new OpenShift agent.

### Example

* Api Key Authentication (agentAuth):
```python
import time
import os
import openshift_assisted_service
from openshift_assisted_service.models.host_create_params import HostCreateParams
from openshift_assisted_service.models.host_registration_response import HostRegistrationResponse
from openshift_assisted_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.openshift.com/api/assisted-install
# See configuration.py for a list of all supported configuration parameters.
configuration = openshift_assisted_service.Configuration(
    host = "http://api.openshift.com/api/assisted-install"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: agentAuth
configuration.api_key['agentAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['agentAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openshift_assisted_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openshift_assisted_service.InstallerApi(api_client)
    infra_env_id = 'infra_env_id_example' # str | The infra-env that the agent is associated with.
    new_host_params = openshift_assisted_service.HostCreateParams() # HostCreateParams | The description of the agent being registered.
    discovery_agent_version = 'discovery_agent_version_example' # str | The software version of the discovery agent that is registering the agent. (optional)

    try:
        api_response = api_instance.v2_register_host(infra_env_id, new_host_params, discovery_agent_version=discovery_agent_version)
        print("The response of InstallerApi->v2_register_host:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallerApi->v2_register_host: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **infra_env_id** | **str**| The infra-env that the agent is associated with. | 
 **new_host_params** | [**HostCreateParams**](HostCreateParams.md)| The description of the agent being registered. | 
 **discovery_agent_version** | **str**| The software version of the discovery agent that is registering the agent. | [optional] 

### Return type

[**HostRegistrationResponse**](HostRegistrationResponse.md)

### Authorization

[agentAuth](../README.md#agentAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success. |  -  |
**400** | Error. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Error. |  -  |
**405** | Method Not Allowed. |  -  |
**409** | Cluster cannot accept new agents due to its current state. |  -  |
**500** | Error. |  -  |
**501** | Not implemented. |  -  |
**503** | Unavailable. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_report_monitored_operator_status**
> v2_report_monitored_operator_status(cluster_id, report_params)



Controller API to report of monitored operators.

### Example

* Api Key Authentication (agentAuth):
```python
import time
import os
import openshift_assisted_service
from openshift_assisted_service.models.operator_monitor_report import OperatorMonitorReport
from openshift_assisted_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.openshift.com/api/assisted-install
# See configuration.py for a list of all supported configuration parameters.
configuration = openshift_assisted_service.Configuration(
    host = "http://api.openshift.com/api/assisted-install"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: agentAuth
configuration.api_key['agentAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['agentAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openshift_assisted_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openshift_assisted_service.InstallerApi(api_client)
    cluster_id = 'cluster_id_example' # str | The cluster whose operators are being monitored.
    report_params = openshift_assisted_service.OperatorMonitorReport() # OperatorMonitorReport | The operators monitor report.

    try:
        api_instance.v2_report_monitored_operator_status(cluster_id, report_params)
    except Exception as e:
        print("Exception when calling InstallerApi->v2_report_monitored_operator_status: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The cluster whose operators are being monitored. | 
 **report_params** | [**OperatorMonitorReport**](OperatorMonitorReport.md)| The operators monitor report. | 

### Return type

void (empty response body)

### Authorization

[agentAuth](../README.md#agentAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Error. |  -  |
**405** | Method Not Allowed. |  -  |
**409** | Error. |  -  |
**500** | Error. |  -  |
**503** | Unavailable. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_reset_cluster**
> Cluster v2_reset_cluster(cluster_id)



Resets a failed installation.

### Example

* Api Key Authentication (userAuth):
```python
import time
import os
import openshift_assisted_service
from openshift_assisted_service.models.cluster import Cluster
from openshift_assisted_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.openshift.com/api/assisted-install
# See configuration.py for a list of all supported configuration parameters.
configuration = openshift_assisted_service.Configuration(
    host = "http://api.openshift.com/api/assisted-install"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAuth
configuration.api_key['userAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openshift_assisted_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openshift_assisted_service.InstallerApi(api_client)
    cluster_id = 'cluster_id_example' # str | The cluster whose installation is to be reset.

    try:
        api_response = api_instance.v2_reset_cluster(cluster_id)
        print("The response of InstallerApi->v2_reset_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallerApi->v2_reset_cluster: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The cluster whose installation is to be reset. | 

### Return type

[**Cluster**](Cluster.md)

### Authorization

[userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Success. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Error. |  -  |
**405** | Method Not Allowed. |  -  |
**409** | Error. |  -  |
**500** | Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_reset_host**
> Host v2_reset_host(infra_env_id, host_id)



reset a failed host for day2 cluster.

### Example

* Api Key Authentication (userAuth):
```python
import time
import os
import openshift_assisted_service
from openshift_assisted_service.models.host import Host
from openshift_assisted_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.openshift.com/api/assisted-install
# See configuration.py for a list of all supported configuration parameters.
configuration = openshift_assisted_service.Configuration(
    host = "http://api.openshift.com/api/assisted-install"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAuth
configuration.api_key['userAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openshift_assisted_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openshift_assisted_service.InstallerApi(api_client)
    infra_env_id = 'infra_env_id_example' # str | The infra-env of the host that is being reset.
    host_id = 'host_id_example' # str | The host that is being reset.

    try:
        api_response = api_instance.v2_reset_host(infra_env_id, host_id)
        print("The response of InstallerApi->v2_reset_host:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallerApi->v2_reset_host: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **infra_env_id** | **str**| The infra-env of the host that is being reset. | 
 **host_id** | **str**| The host that is being reset. | 

### Return type

[**Host**](Host.md)

### Authorization

[userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Error. |  -  |
**409** | Error. |  -  |
**500** | Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_reset_host_validation**
> Host v2_reset_host_validation(infra_env_id, host_id, validation_id)

Reset failed host validation.

Reset failed host validation. It may be performed on any host validation with persistent validation result.

### Example

* Api Key Authentication (userAuth):
```python
import time
import os
import openshift_assisted_service
from openshift_assisted_service.models.host import Host
from openshift_assisted_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.openshift.com/api/assisted-install
# See configuration.py for a list of all supported configuration parameters.
configuration = openshift_assisted_service.Configuration(
    host = "http://api.openshift.com/api/assisted-install"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAuth
configuration.api_key['userAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openshift_assisted_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openshift_assisted_service.InstallerApi(api_client)
    infra_env_id = 'infra_env_id_example' # str | The infra-env of the host that its validation is being reset.
    host_id = 'host_id_example' # str | The host that its validation is being reset.
    validation_id = 'validation_id_example' # str | The id of the validation being reset.

    try:
        # Reset failed host validation.
        api_response = api_instance.v2_reset_host_validation(infra_env_id, host_id, validation_id)
        print("The response of InstallerApi->v2_reset_host_validation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallerApi->v2_reset_host_validation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **infra_env_id** | **str**| The infra-env of the host that its validation is being reset. | 
 **host_id** | **str**| The host that its validation is being reset. | 
 **validation_id** | **str**| The id of the validation being reset. | 

### Return type

[**Host**](Host.md)

### Authorization

[userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Error. |  -  |
**409** | Error. |  -  |
**500** | Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_set_ignored_validations**
> IgnoredValidations v2_set_ignored_validations(cluster_id, ignored_validations)



Register the validations which are to be ignored for this cluster.

### Example

* Api Key Authentication (userAuth):
```python
import time
import os
import openshift_assisted_service
from openshift_assisted_service.models.ignored_validations import IgnoredValidations
from openshift_assisted_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.openshift.com/api/assisted-install
# See configuration.py for a list of all supported configuration parameters.
configuration = openshift_assisted_service.Configuration(
    host = "http://api.openshift.com/api/assisted-install"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAuth
configuration.api_key['userAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openshift_assisted_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openshift_assisted_service.InstallerApi(api_client)
    cluster_id = 'cluster_id_example' # str | The cluster whose failing validations should be ignored according to this list.
    ignored_validations = openshift_assisted_service.IgnoredValidations() # IgnoredValidations | The validations to be ignored.

    try:
        api_response = api_instance.v2_set_ignored_validations(cluster_id, ignored_validations)
        print("The response of InstallerApi->v2_set_ignored_validations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallerApi->v2_set_ignored_validations: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The cluster whose failing validations should be ignored according to this list. | 
 **ignored_validations** | [**IgnoredValidations**](IgnoredValidations.md)| The validations to be ignored. | 

### Return type

[**IgnoredValidations**](IgnoredValidations.md)

### Authorization

[userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success. |  -  |
**400** | Error. |  -  |
**404** | Error. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**500** | Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_update_cluster**
> Cluster v2_update_cluster(cluster_id, cluster_update_params)



Updates an OpenShift cluster definition.

### Example

* Api Key Authentication (userAuth):
```python
import time
import os
import openshift_assisted_service
from openshift_assisted_service.models.cluster import Cluster
from openshift_assisted_service.models.v2_cluster_update_params import V2ClusterUpdateParams
from openshift_assisted_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.openshift.com/api/assisted-install
# See configuration.py for a list of all supported configuration parameters.
configuration = openshift_assisted_service.Configuration(
    host = "http://api.openshift.com/api/assisted-install"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAuth
configuration.api_key['userAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openshift_assisted_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openshift_assisted_service.InstallerApi(api_client)
    cluster_id = 'cluster_id_example' # str | The cluster to be updated.
    cluster_update_params = openshift_assisted_service.V2ClusterUpdateParams() # V2ClusterUpdateParams | The properties to update.

    try:
        api_response = api_instance.v2_update_cluster(cluster_id, cluster_update_params)
        print("The response of InstallerApi->v2_update_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallerApi->v2_update_cluster: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The cluster to be updated. | 
 **cluster_update_params** | [**V2ClusterUpdateParams**](V2ClusterUpdateParams.md)| The properties to update. | 

### Return type

[**Cluster**](Cluster.md)

### Authorization

[userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success. |  -  |
**400** | Error. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Error. |  -  |
**405** | Method Not Allowed. |  -  |
**409** | Error. |  -  |
**500** | Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_update_cluster_install_config**
> v2_update_cluster_install_config(cluster_id, install_config_params)



Override values in the install config.

### Example

* Api Key Authentication (userAuth):
```python
import time
import os
import openshift_assisted_service
from openshift_assisted_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.openshift.com/api/assisted-install
# See configuration.py for a list of all supported configuration parameters.
configuration = openshift_assisted_service.Configuration(
    host = "http://api.openshift.com/api/assisted-install"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAuth
configuration.api_key['userAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openshift_assisted_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openshift_assisted_service.InstallerApi(api_client)
    cluster_id = 'cluster_id_example' # str | The cluster whose install config is being updated.
    install_config_params = 'install_config_params_example' # str | Install config overrides.

    try:
        api_instance.v2_update_cluster_install_config(cluster_id, install_config_params)
    except Exception as e:
        print("Exception when calling InstallerApi->v2_update_cluster_install_config: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The cluster whose install config is being updated. | 
 **install_config_params** | **str**| Install config overrides. | 

### Return type

void (empty response body)

### Authorization

[userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success. |  -  |
**400** | Error. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Error. |  -  |
**405** | Method Not Allowed. |  -  |
**500** | Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_update_cluster_logs_progress**
> v2_update_cluster_logs_progress(cluster_id, logs_progress_params)



Update log collection state and progress.

### Example

* Api Key Authentication (agentAuth):
```python
import time
import os
import openshift_assisted_service
from openshift_assisted_service.models.logs_progress_params import LogsProgressParams
from openshift_assisted_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.openshift.com/api/assisted-install
# See configuration.py for a list of all supported configuration parameters.
configuration = openshift_assisted_service.Configuration(
    host = "http://api.openshift.com/api/assisted-install"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: agentAuth
configuration.api_key['agentAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['agentAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openshift_assisted_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openshift_assisted_service.InstallerApi(api_client)
    cluster_id = 'cluster_id_example' # str | The cluster whose log progress is being updated.
    logs_progress_params = openshift_assisted_service.LogsProgressParams() # LogsProgressParams | Parameters for updating log progress.

    try:
        api_instance.v2_update_cluster_logs_progress(cluster_id, logs_progress_params)
    except Exception as e:
        print("Exception when calling InstallerApi->v2_update_cluster_logs_progress: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The cluster whose log progress is being updated. | 
 **logs_progress_params** | [**LogsProgressParams**](LogsProgressParams.md)| Parameters for updating log progress. | 

### Return type

void (empty response body)

### Authorization

[agentAuth](../README.md#agentAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Update cluster install progress. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Error. |  -  |
**405** | Method Not Allowed. |  -  |
**409** | Error. |  -  |
**500** | Error. |  -  |
**503** | Unavailable. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_update_cluster_ui_settings**
> str v2_update_cluster_ui_settings(cluster_id, ui_settings)



Update cluster specific UI settings.

### Example

* Api Key Authentication (userAuth):
```python
import time
import os
import openshift_assisted_service
from openshift_assisted_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.openshift.com/api/assisted-install
# See configuration.py for a list of all supported configuration parameters.
configuration = openshift_assisted_service.Configuration(
    host = "http://api.openshift.com/api/assisted-install"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAuth
configuration.api_key['userAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openshift_assisted_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openshift_assisted_service.InstallerApi(api_client)
    cluster_id = 'cluster_id_example' # str | The cluster for which UI settings should be updated.
    ui_settings = 'ui_settings_example' # str | Settings for the installer UI.

    try:
        api_response = api_instance.v2_update_cluster_ui_settings(cluster_id, ui_settings)
        print("The response of InstallerApi->v2_update_cluster_ui_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallerApi->v2_update_cluster_ui_settings: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The cluster for which UI settings should be updated. | 
 **ui_settings** | **str**| Settings for the installer UI. | 

### Return type

**str**

### Authorization

[userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**400** | Error. |  -  |
**404** | Error. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**500** | Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_update_host**
> Host v2_update_host(infra_env_id, host_id, host_update_params)



Update an Openshift host

### Example

* Api Key Authentication (userAuth):
```python
import time
import os
import openshift_assisted_service
from openshift_assisted_service.models.host import Host
from openshift_assisted_service.models.host_update_params import HostUpdateParams
from openshift_assisted_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.openshift.com/api/assisted-install
# See configuration.py for a list of all supported configuration parameters.
configuration = openshift_assisted_service.Configuration(
    host = "http://api.openshift.com/api/assisted-install"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAuth
configuration.api_key['userAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openshift_assisted_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openshift_assisted_service.InstallerApi(api_client)
    infra_env_id = 'infra_env_id_example' # str | The infra-env ID of the host to be updated.
    host_id = 'host_id_example' # str | The host that should be updated.
    host_update_params = openshift_assisted_service.HostUpdateParams() # HostUpdateParams | The properties to update.

    try:
        api_response = api_instance.v2_update_host(infra_env_id, host_id, host_update_params)
        print("The response of InstallerApi->v2_update_host:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallerApi->v2_update_host: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **infra_env_id** | **str**| The infra-env ID of the host to be updated. | 
 **host_id** | **str**| The host that should be updated. | 
 **host_update_params** | [**HostUpdateParams**](HostUpdateParams.md)| The properties to update. | 

### Return type

[**Host**](Host.md)

### Authorization

[userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success. |  -  |
**400** | Error. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Error. |  -  |
**405** | Method Not Allowed. |  -  |
**409** | Error. |  -  |
**500** | Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_update_host_ignition**
> v2_update_host_ignition(infra_env_id, host_id, host_ignition_params)



Patch the ignition file for this host

### Example

* Api Key Authentication (userAuth):
```python
import time
import os
import openshift_assisted_service
from openshift_assisted_service.models.host_ignition_params import HostIgnitionParams
from openshift_assisted_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.openshift.com/api/assisted-install
# See configuration.py for a list of all supported configuration parameters.
configuration = openshift_assisted_service.Configuration(
    host = "http://api.openshift.com/api/assisted-install"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAuth
configuration.api_key['userAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openshift_assisted_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openshift_assisted_service.InstallerApi(api_client)
    infra_env_id = 'infra_env_id_example' # str | The infra-env of the host whose ignition file should be updated.
    host_id = 'host_id_example' # str | The host whose ignition file should be updated.
    host_ignition_params = openshift_assisted_service.HostIgnitionParams() # HostIgnitionParams | Ignition config overrides.

    try:
        api_instance.v2_update_host_ignition(infra_env_id, host_id, host_ignition_params)
    except Exception as e:
        print("Exception when calling InstallerApi->v2_update_host_ignition: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **infra_env_id** | **str**| The infra-env of the host whose ignition file should be updated. | 
 **host_id** | **str**| The host whose ignition file should be updated. | 
 **host_ignition_params** | [**HostIgnitionParams**](HostIgnitionParams.md)| Ignition config overrides. | 

### Return type

void (empty response body)

### Authorization

[userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success. |  -  |
**400** | Error. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Error. |  -  |
**405** | Method Not Allowed. |  -  |
**500** | Error. |  -  |
**501** | Not implemented. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_update_host_install_progress**
> v2_update_host_install_progress(infra_env_id, host_id, host_progress, discovery_agent_version=discovery_agent_version)



Update installation progress.

### Example

* Api Key Authentication (agentAuth):
```python
import time
import os
import openshift_assisted_service
from openshift_assisted_service.models.host_progress import HostProgress
from openshift_assisted_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.openshift.com/api/assisted-install
# See configuration.py for a list of all supported configuration parameters.
configuration = openshift_assisted_service.Configuration(
    host = "http://api.openshift.com/api/assisted-install"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: agentAuth
configuration.api_key['agentAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['agentAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openshift_assisted_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openshift_assisted_service.InstallerApi(api_client)
    infra_env_id = 'infra_env_id_example' # str | The infra-env of the host being updated.
    host_id = 'host_id_example' # str | The ID of the host to update.
    host_progress = openshift_assisted_service.HostProgress() # HostProgress | New progress value.
    discovery_agent_version = 'discovery_agent_version_example' # str | The software version of the discovery agent that is updating progress. (optional)

    try:
        api_instance.v2_update_host_install_progress(infra_env_id, host_id, host_progress, discovery_agent_version=discovery_agent_version)
    except Exception as e:
        print("Exception when calling InstallerApi->v2_update_host_install_progress: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **infra_env_id** | **str**| The infra-env of the host being updated. | 
 **host_id** | **str**| The ID of the host to update. | 
 **host_progress** | [**HostProgress**](HostProgress.md)| New progress value. | 
 **discovery_agent_version** | **str**| The software version of the discovery agent that is updating progress. | [optional] 

### Return type

void (empty response body)

### Authorization

[agentAuth](../README.md#agentAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update install progress. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Error. |  -  |
**405** | Method Not Allowed. |  -  |
**500** | Error. |  -  |
**503** | Unavailable. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_update_host_installer_args**
> Host v2_update_host_installer_args(infra_env_id, host_id, installer_args_params)



Updates a host's installer arguments.

### Example

* Api Key Authentication (userAuth):
```python
import time
import os
import openshift_assisted_service
from openshift_assisted_service.models.host import Host
from openshift_assisted_service.models.installer_args_params import InstallerArgsParams
from openshift_assisted_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.openshift.com/api/assisted-install
# See configuration.py for a list of all supported configuration parameters.
configuration = openshift_assisted_service.Configuration(
    host = "http://api.openshift.com/api/assisted-install"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAuth
configuration.api_key['userAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openshift_assisted_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openshift_assisted_service.InstallerApi(api_client)
    infra_env_id = 'infra_env_id_example' # str | The infra-env of the host whose installer arguments should be updated.
    host_id = 'host_id_example' # str | The host whose installer arguments should be updated.
    installer_args_params = openshift_assisted_service.InstallerArgsParams() # InstallerArgsParams | The updated installer arguments.

    try:
        api_response = api_instance.v2_update_host_installer_args(infra_env_id, host_id, installer_args_params)
        print("The response of InstallerApi->v2_update_host_installer_args:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallerApi->v2_update_host_installer_args: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **infra_env_id** | **str**| The infra-env of the host whose installer arguments should be updated. | 
 **host_id** | **str**| The host whose installer arguments should be updated. | 
 **installer_args_params** | [**InstallerArgsParams**](InstallerArgsParams.md)| The updated installer arguments. | 

### Return type

[**Host**](Host.md)

### Authorization

[userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success. |  -  |
**400** | Error. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Error. |  -  |
**405** | Method Not Allowed. |  -  |
**409** | Error. |  -  |
**500** | Error. |  -  |
**501** | Not implemented. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_update_host_logs_progress**
> v2_update_host_logs_progress(infra_env_id, host_id, logs_progress_params)



Update log collection state and progress.

### Example

* Api Key Authentication (agentAuth):
```python
import time
import os
import openshift_assisted_service
from openshift_assisted_service.models.logs_progress_params import LogsProgressParams
from openshift_assisted_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.openshift.com/api/assisted-install
# See configuration.py for a list of all supported configuration parameters.
configuration = openshift_assisted_service.Configuration(
    host = "http://api.openshift.com/api/assisted-install"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: agentAuth
configuration.api_key['agentAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['agentAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openshift_assisted_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openshift_assisted_service.InstallerApi(api_client)
    infra_env_id = 'infra_env_id_example' # str | The infra-env whose log progress is being updated.
    host_id = 'host_id_example' # str | The host whose log progress is being updated.
    logs_progress_params = openshift_assisted_service.LogsProgressParams() # LogsProgressParams | Parameters for updating log progress.

    try:
        api_instance.v2_update_host_logs_progress(infra_env_id, host_id, logs_progress_params)
    except Exception as e:
        print("Exception when calling InstallerApi->v2_update_host_logs_progress: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **infra_env_id** | **str**| The infra-env whose log progress is being updated. | 
 **host_id** | **str**| The host whose log progress is being updated. | 
 **logs_progress_params** | [**LogsProgressParams**](LogsProgressParams.md)| Parameters for updating log progress. | 

### Return type

void (empty response body)

### Authorization

[agentAuth](../README.md#agentAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Update cluster install progress. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Error. |  -  |
**405** | Method Not Allowed. |  -  |
**409** | Error. |  -  |
**500** | Error. |  -  |
**501** | Not implemented. |  -  |
**503** | Unavailable. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_upload_cluster_ingress_cert**
> v2_upload_cluster_ingress_cert(cluster_id, ingress_cert_params, discovery_agent_version=discovery_agent_version)



Transfer the ingress certificate for the cluster.

### Example

* Api Key Authentication (agentAuth):
```python
import time
import os
import openshift_assisted_service
from openshift_assisted_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.openshift.com/api/assisted-install
# See configuration.py for a list of all supported configuration parameters.
configuration = openshift_assisted_service.Configuration(
    host = "http://api.openshift.com/api/assisted-install"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: agentAuth
configuration.api_key['agentAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['agentAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openshift_assisted_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openshift_assisted_service.InstallerApi(api_client)
    cluster_id = 'cluster_id_example' # str | The cluster to associate with the ingress certificate.
    ingress_cert_params = 'ingress_cert_params_example' # str | The ingress certificate.
    discovery_agent_version = 'discovery_agent_version_example' # str | The software version of the discovery agent that is uploading the ingress certificate. (optional)

    try:
        api_instance.v2_upload_cluster_ingress_cert(cluster_id, ingress_cert_params, discovery_agent_version=discovery_agent_version)
    except Exception as e:
        print("Exception when calling InstallerApi->v2_upload_cluster_ingress_cert: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The cluster to associate with the ingress certificate. | 
 **ingress_cert_params** | **str**| The ingress certificate. | 
 **discovery_agent_version** | **str**| The software version of the discovery agent that is uploading the ingress certificate. | [optional] 

### Return type

void (empty response body)

### Authorization

[agentAuth](../README.md#agentAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success. |  -  |
**400** | Error. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Error. |  -  |
**405** | Method Not Allowed. |  -  |
**500** | Error. |  -  |
**503** | Unavailable. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_upload_logs**
> v2_upload_logs(cluster_id, logs_type, infra_env_id=infra_env_id, host_id=host_id, upfile=upfile)



Agent API to upload logs.

### Example

* Api Key Authentication (agentAuth):
```python
import time
import os
import openshift_assisted_service
from openshift_assisted_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.openshift.com/api/assisted-install
# See configuration.py for a list of all supported configuration parameters.
configuration = openshift_assisted_service.Configuration(
    host = "http://api.openshift.com/api/assisted-install"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: agentAuth
configuration.api_key['agentAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['agentAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openshift_assisted_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openshift_assisted_service.InstallerApi(api_client)
    cluster_id = 'cluster_id_example' # str | The cluster whose logs should be uploaded.
    logs_type = 'logs_type_example' # str | The type of log file to be uploaded.
    infra_env_id = 'infra_env_id_example' # str | The infra-env ID of the host. (optional)
    host_id = 'host_id_example' # str | The host whose logs should be uploaded. (optional)
    upfile = None # bytearray | The log file to be uploaded. (optional)

    try:
        api_instance.v2_upload_logs(cluster_id, logs_type, infra_env_id=infra_env_id, host_id=host_id, upfile=upfile)
    except Exception as e:
        print("Exception when calling InstallerApi->v2_upload_logs: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The cluster whose logs should be uploaded. | 
 **logs_type** | **str**| The type of log file to be uploaded. | 
 **infra_env_id** | **str**| The infra-env ID of the host. | [optional] 
 **host_id** | **str**| The host whose logs should be uploaded. | [optional] 
 **upfile** | **bytearray**| The log file to be uploaded. | [optional] 

### Return type

void (empty response body)

### Authorization

[agentAuth](../README.md#agentAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Error. |  -  |
**405** | Method Not Allowed. |  -  |
**409** | Error. |  -  |
**500** | Error. |  -  |
**503** | Unavailable. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

