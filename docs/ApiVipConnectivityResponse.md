# ApiVipConnectivityResponse

The response from the day-2 agent's attempt to download the worker ignition file from the API machine config server of the target cluster. Note - the name \"API VIP connectivity\" is old and misleading and is preserved for backwards compatibility.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** | Whether the agent was able to download the ignition or not | [optional] 
**url** | **str** | This parameter mirrors the url parameter of the corresponding api_vip_connectivity_request | [optional] 
**download_error** | **str** | The error that occurred while downloading the worker ignition file, ignored when is_success is true | [optional] 
**ignition** | **str** | Ignition file fetched from the target cluster&#39;s API machine config server. This ignition file may be incomplete as almost all files / systemd units are removed from it by the agent in order to save space. | [optional] 

## Example

```python
from openshift_assisted_service.models.api_vip_connectivity_response import ApiVipConnectivityResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiVipConnectivityResponse from a JSON string
api_vip_connectivity_response_instance = ApiVipConnectivityResponse.from_json(json)
# print the JSON string representation of the object
print ApiVipConnectivityResponse.to_json()

# convert the object into a dict
api_vip_connectivity_response_dict = api_vip_connectivity_response_instance.to_dict()
# create an instance of ApiVipConnectivityResponse from a dict
api_vip_connectivity_response_form_dict = api_vip_connectivity_response.from_dict(api_vip_connectivity_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


