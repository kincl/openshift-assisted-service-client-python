# ApiVipConnectivityRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | URL address of the API. | 
**verify_cidr** | **bool** | Whether to verify if the API VIP belongs to one of the interfaces (DEPRECATED). | [optional] 
**ca_certificate** | **str** | A CA certficate to be used when contacting the URL via https. | [optional] 
**ignition_endpoint_token** | **str** | A string which will be used as Authorization Bearer token to fetch the ignition from ignition_endpoint_url. | [optional] 

## Example

```python
from openshift_assisted_service.models.api_vip_connectivity_request import ApiVipConnectivityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiVipConnectivityRequest from a JSON string
api_vip_connectivity_request_instance = ApiVipConnectivityRequest.from_json(json)
# print the JSON string representation of the object
print ApiVipConnectivityRequest.to_json()

# convert the object into a dict
api_vip_connectivity_request_dict = api_vip_connectivity_request_instance.to_dict()
# create an instance of ApiVipConnectivityRequest from a dict
api_vip_connectivity_request_form_dict = api_vip_connectivity_request.from_dict(api_vip_connectivity_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


