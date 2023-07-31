# TangConnectivityRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tang_servers** | **str** | JSON-formatted string containing additional information regarding tang&#39;s configuration | 

## Example

```python
from openshift_assisted_service.models.tang_connectivity_request import TangConnectivityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TangConnectivityRequest from a JSON string
tang_connectivity_request_instance = TangConnectivityRequest.from_json(json)
# print the JSON string representation of the object
print TangConnectivityRequest.to_json()

# convert the object into a dict
tang_connectivity_request_dict = tang_connectivity_request_instance.to_dict()
# create an instance of TangConnectivityRequest from a dict
tang_connectivity_request_form_dict = tang_connectivity_request.from_dict(tang_connectivity_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


