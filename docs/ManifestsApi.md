# openshift_assisted_service.ManifestsApi

All URIs are relative to *http://api.openshift.com/api/assisted-install*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2_create_cluster_manifest**](ManifestsApi.md#v2_create_cluster_manifest) | **POST** /v2/clusters/{cluster_id}/manifests | 
[**v2_delete_cluster_manifest**](ManifestsApi.md#v2_delete_cluster_manifest) | **DELETE** /v2/clusters/{cluster_id}/manifests | 
[**v2_download_cluster_manifest**](ManifestsApi.md#v2_download_cluster_manifest) | **GET** /v2/clusters/{cluster_id}/manifests/files | 
[**v2_list_cluster_manifests**](ManifestsApi.md#v2_list_cluster_manifests) | **GET** /v2/clusters/{cluster_id}/manifests | 
[**v2_update_cluster_manifest**](ManifestsApi.md#v2_update_cluster_manifest) | **PATCH** /v2/clusters/{cluster_id}/manifests | 


# **v2_create_cluster_manifest**
> Manifest v2_create_cluster_manifest(cluster_id, create_manifest_params)



Creates a manifest for customizing cluster installation.

### Example

* Api Key Authentication (userAuth):
```python
import time
import os
import openshift_assisted_service
from openshift_assisted_service.models.create_manifest_params import CreateManifestParams
from openshift_assisted_service.models.manifest import Manifest
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
    api_instance = openshift_assisted_service.ManifestsApi(api_client)
    cluster_id = 'cluster_id_example' # str | The cluster for which a new manifest should be created.
    create_manifest_params = openshift_assisted_service.CreateManifestParams() # CreateManifestParams | The new manifest to create.

    try:
        api_response = api_instance.v2_create_cluster_manifest(cluster_id, create_manifest_params)
        print("The response of ManifestsApi->v2_create_cluster_manifest:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManifestsApi->v2_create_cluster_manifest: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The cluster for which a new manifest should be created. | 
 **create_manifest_params** | [**CreateManifestParams**](CreateManifestParams.md)| The new manifest to create. | 

### Return type

[**Manifest**](Manifest.md)

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

# **v2_delete_cluster_manifest**
> v2_delete_cluster_manifest(cluster_id, file_name, folder=folder)



Deletes a manifest from the cluster.

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
    api_instance = openshift_assisted_service.ManifestsApi(api_client)
    cluster_id = 'cluster_id_example' # str | The cluster whose manifest should be deleted.
    file_name = 'file_name_example' # str | The manifest file name to delete from the cluster.
    folder = 'manifests' # str | The folder that contains the files. Manifests can be placed in 'manifests' or 'openshift' directories. (optional) (default to 'manifests')

    try:
        api_instance.v2_delete_cluster_manifest(cluster_id, file_name, folder=folder)
    except Exception as e:
        print("Exception when calling ManifestsApi->v2_delete_cluster_manifest: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The cluster whose manifest should be deleted. | 
 **file_name** | **str**| The manifest file name to delete from the cluster. | 
 **folder** | **str**| The folder that contains the files. Manifests can be placed in &#39;manifests&#39; or &#39;openshift&#39; directories. | [optional] [default to &#39;manifests&#39;]

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
**200** | Success. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Error. |  -  |
**405** | Method Not Allowed. |  -  |
**409** | Error. |  -  |
**500** | Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_download_cluster_manifest**
> bytearray v2_download_cluster_manifest(cluster_id, file_name, folder=folder)



Downloads cluster manifest.

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
    api_instance = openshift_assisted_service.ManifestsApi(api_client)
    cluster_id = 'cluster_id_example' # str | The cluster whose manifest should be downloaded.
    file_name = 'file_name_example' # str | The manifest file name to download.
    folder = 'manifests' # str | The folder that contains the files. Manifests can be placed in 'manifests' or 'openshift' directories. (optional) (default to 'manifests')

    try:
        api_response = api_instance.v2_download_cluster_manifest(cluster_id, file_name, folder=folder)
        print("The response of ManifestsApi->v2_download_cluster_manifest:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManifestsApi->v2_download_cluster_manifest: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The cluster whose manifest should be downloaded. | 
 **file_name** | **str**| The manifest file name to download. | 
 **folder** | **str**| The folder that contains the files. Manifests can be placed in &#39;manifests&#39; or &#39;openshift&#39; directories. | [optional] [default to &#39;manifests&#39;]

### Return type

**bytearray**

### Authorization

[userAuth](../README.md#userAuth)

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

# **v2_list_cluster_manifests**
> List[Manifest] v2_list_cluster_manifests(cluster_id)



Lists manifests for customizing cluster installation.

### Example

* Api Key Authentication (userAuth):
```python
import time
import os
import openshift_assisted_service
from openshift_assisted_service.models.manifest import Manifest
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
    api_instance = openshift_assisted_service.ManifestsApi(api_client)
    cluster_id = 'cluster_id_example' # str | The cluster for which the manifests should be listed.

    try:
        api_response = api_instance.v2_list_cluster_manifests(cluster_id)
        print("The response of ManifestsApi->v2_list_cluster_manifests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManifestsApi->v2_list_cluster_manifests: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The cluster for which the manifests should be listed. | 

### Return type

[**List[Manifest]**](Manifest.md)

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

# **v2_update_cluster_manifest**
> Manifest v2_update_cluster_manifest(cluster_id, update_manifest_params)



Updates a manifest for customizing cluster installation.

### Example

* Api Key Authentication (userAuth):
```python
import time
import os
import openshift_assisted_service
from openshift_assisted_service.models.manifest import Manifest
from openshift_assisted_service.models.update_manifest_params import UpdateManifestParams
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
    api_instance = openshift_assisted_service.ManifestsApi(api_client)
    cluster_id = 'cluster_id_example' # str | The cluster for which a new manifest should be updated.
    update_manifest_params = openshift_assisted_service.UpdateManifestParams() # UpdateManifestParams | The manifest to be updated.

    try:
        api_response = api_instance.v2_update_cluster_manifest(cluster_id, update_manifest_params)
        print("The response of ManifestsApi->v2_update_cluster_manifest:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManifestsApi->v2_update_cluster_manifest: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The cluster for which a new manifest should be updated. | 
 **update_manifest_params** | [**UpdateManifestParams**](UpdateManifestParams.md)| The manifest to be updated. | 

### Return type

[**Manifest**](Manifest.md)

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
**409** | Error. |  -  |
**500** | Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

