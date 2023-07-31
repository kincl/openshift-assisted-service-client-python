# TangConnectivityResponseTangServerResponseInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tang_url** | **str** | Tang URL. | [optional] 
**payload** | **str** | Tang response payload. | [optional] 
**signatures** | [**List[TangConnectivityResponseTangServerResponseInnerSignaturesInner]**](TangConnectivityResponseTangServerResponseInnerSignaturesInner.md) |  | [optional] 

## Example

```python
from openshift_assisted_service.models.tang_connectivity_response_tang_server_response_inner import TangConnectivityResponseTangServerResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of TangConnectivityResponseTangServerResponseInner from a JSON string
tang_connectivity_response_tang_server_response_inner_instance = TangConnectivityResponseTangServerResponseInner.from_json(json)
# print the JSON string representation of the object
print TangConnectivityResponseTangServerResponseInner.to_json()

# convert the object into a dict
tang_connectivity_response_tang_server_response_inner_dict = tang_connectivity_response_tang_server_response_inner_instance.to_dict()
# create an instance of TangConnectivityResponseTangServerResponseInner from a dict
tang_connectivity_response_tang_server_response_inner_form_dict = tang_connectivity_response_tang_server_response_inner.from_dict(tang_connectivity_response_tang_server_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


