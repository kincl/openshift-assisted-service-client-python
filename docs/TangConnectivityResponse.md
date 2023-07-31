# TangConnectivityResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** | Tang check result. | [optional] 
**tang_server_response** | [**List[TangConnectivityResponseTangServerResponseInner]**](TangConnectivityResponseTangServerResponseInner.md) |  | [optional] 

## Example

```python
from openshift_assisted_service.models.tang_connectivity_response import TangConnectivityResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TangConnectivityResponse from a JSON string
tang_connectivity_response_instance = TangConnectivityResponse.from_json(json)
# print the JSON string representation of the object
print TangConnectivityResponse.to_json()

# convert the object into a dict
tang_connectivity_response_dict = tang_connectivity_response_instance.to_dict()
# create an instance of TangConnectivityResponse from a dict
tang_connectivity_response_form_dict = tang_connectivity_response.from_dict(tang_connectivity_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


