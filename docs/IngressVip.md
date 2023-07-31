# IngressVip

The virtual IP used for cluster ingress traffic.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **str** | The cluster that this VIP is associated with. | [optional] 
**ip** | **str** |  | [optional] 
**verification** | [**VipVerification**](VipVerification.md) |  | [optional] 

## Example

```python
from openshift_assisted_service.models.ingress_vip import IngressVip

# TODO update the JSON string below
json = "{}"
# create an instance of IngressVip from a JSON string
ingress_vip_instance = IngressVip.from_json(json)
# print the JSON string representation of the object
print IngressVip.to_json()

# convert the object into a dict
ingress_vip_dict = ingress_vip_instance.to_dict()
# create an instance of IngressVip from a dict
ingress_vip_form_dict = ingress_vip.from_dict(ingress_vip_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


