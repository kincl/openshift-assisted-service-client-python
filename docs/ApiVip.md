# ApiVip

The virtual IP used to reach the OpenShift cluster's API.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **str** | The cluster that this VIP is associated with. | [optional] 
**ip** | **str** |  | [optional] 
**verification** | [**VipVerification**](VipVerification.md) |  | [optional] 

## Example

```python
from openshift_assisted_service.models.api_vip import ApiVip

# TODO update the JSON string below
json = "{}"
# create an instance of ApiVip from a JSON string
api_vip_instance = ApiVip.from_json(json)
# print the JSON string representation of the object
print ApiVip.to_json()

# convert the object into a dict
api_vip_dict = api_vip_instance.to_dict()
# create an instance of ApiVip from a dict
api_vip_form_dict = api_vip.from_dict(api_vip_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


