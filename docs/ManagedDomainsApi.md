# openshift_assisted_service.ManagedDomainsApi

All URIs are relative to *http://api.openshift.com/api/assisted-install*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2_list_managed_domains**](ManagedDomainsApi.md#v2_list_managed_domains) | **GET** /v2/domains | 


# **v2_list_managed_domains**
> List[ManagedDomain] v2_list_managed_domains()



List of managed DNS domains.

### Example

* Api Key Authentication (userAuth):
```python
import time
import os
import openshift_assisted_service
from openshift_assisted_service.models.managed_domain import ManagedDomain
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
    api_instance = openshift_assisted_service.ManagedDomainsApi(api_client)

    try:
        api_response = api_instance.v2_list_managed_domains()
        print("The response of ManagedDomainsApi->v2_list_managed_domains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedDomainsApi->v2_list_managed_domains: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[ManagedDomain]**](ManagedDomain.md)

### Authorization

[userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**500** | Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

