# openshift_assisted_service.OperatorsApi

All URIs are relative to *http://api.openshift.com/api/assisted-install*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2_list_of_cluster_operators**](OperatorsApi.md#v2_list_of_cluster_operators) | **GET** /v2/clusters/{cluster_id}/monitored-operators | 
[**v2_list_operator_properties**](OperatorsApi.md#v2_list_operator_properties) | **GET** /v2/supported-operators/{operator_name} | 
[**v2_list_supported_operators**](OperatorsApi.md#v2_list_supported_operators) | **GET** /v2/supported-operators | 
[**v2_report_monitored_operator_status**](OperatorsApi.md#v2_report_monitored_operator_status) | **PUT** /v2/clusters/{cluster_id}/monitored-operators | 


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
    api_instance = openshift_assisted_service.OperatorsApi(api_client)
    cluster_id = 'cluster_id_example' # str | The cluster to return operators for.
    operator_name = 'operator_name_example' # str | An operator in the specified cluster to return its data. (optional)

    try:
        api_response = api_instance.v2_list_of_cluster_operators(cluster_id, operator_name=operator_name)
        print("The response of OperatorsApi->v2_list_of_cluster_operators:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperatorsApi->v2_list_of_cluster_operators: %s\n" % e)
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

# **v2_list_operator_properties**
> List[OperatorProperty] v2_list_operator_properties(operator_name)



Lists properties for an operator.

### Example

* Api Key Authentication (userAuth):
```python
import time
import os
import openshift_assisted_service
from openshift_assisted_service.models.operator_property import OperatorProperty
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
    api_instance = openshift_assisted_service.OperatorsApi(api_client)
    operator_name = 'operator_name_example' # str | The operator name.

    try:
        api_response = api_instance.v2_list_operator_properties(operator_name)
        print("The response of OperatorsApi->v2_list_operator_properties:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperatorsApi->v2_list_operator_properties: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_name** | **str**| The operator name. | 

### Return type

[**List[OperatorProperty]**](OperatorProperty.md)

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

# **v2_list_supported_operators**
> List[str] v2_list_supported_operators()



Retrieves the list of supported operators.

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
    api_instance = openshift_assisted_service.OperatorsApi(api_client)

    try:
        api_response = api_instance.v2_list_supported_operators()
        print("The response of OperatorsApi->v2_list_supported_operators:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperatorsApi->v2_list_supported_operators: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

**List[str]**

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
    api_instance = openshift_assisted_service.OperatorsApi(api_client)
    cluster_id = 'cluster_id_example' # str | The cluster whose operators are being monitored.
    report_params = openshift_assisted_service.OperatorMonitorReport() # OperatorMonitorReport | The operators monitor report.

    try:
        api_instance.v2_report_monitored_operator_status(cluster_id, report_params)
    except Exception as e:
        print("Exception when calling OperatorsApi->v2_report_monitored_operator_status: %s\n" % e)
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

