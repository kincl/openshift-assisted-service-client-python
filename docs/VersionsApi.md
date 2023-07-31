# openshift_assisted_service.VersionsApi

All URIs are relative to *http://api.openshift.com/api/assisted-install*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2_list_component_versions**](VersionsApi.md#v2_list_component_versions) | **GET** /v2/component-versions | 
[**v2_list_supported_openshift_versions**](VersionsApi.md#v2_list_supported_openshift_versions) | **GET** /v2/openshift-versions | 


# **v2_list_component_versions**
> ListVersions v2_list_component_versions()



List of component versions.

### Example

* Api Key Authentication (userAuth):
```python
import time
import os
import openshift_assisted_service
from openshift_assisted_service.models.list_versions import ListVersions
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
    api_instance = openshift_assisted_service.VersionsApi(api_client)

    try:
        api_response = api_instance.v2_list_component_versions()
        print("The response of VersionsApi->v2_list_component_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VersionsApi->v2_list_component_versions: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**ListVersions**](ListVersions.md)

### Authorization

[userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_list_supported_openshift_versions**
> Dict[str, OpenshiftVersion] v2_list_supported_openshift_versions()



Retrieves the list of OpenShift supported versions.

### Example

* Api Key Authentication (userAuth):
```python
import time
import os
import openshift_assisted_service
from openshift_assisted_service.models.openshift_version import OpenshiftVersion
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
    api_instance = openshift_assisted_service.VersionsApi(api_client)

    try:
        api_response = api_instance.v2_list_supported_openshift_versions()
        print("The response of VersionsApi->v2_list_supported_openshift_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VersionsApi->v2_list_supported_openshift_versions: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**Dict[str, OpenshiftVersion]**](OpenshiftVersion.md)

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
**500** | Error. |  -  |
**503** | Unavailable. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

