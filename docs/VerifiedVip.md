# VerifiedVip

Single VIP verification result.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vip** | **str** |  | [optional] 
**vip_type** | [**VipType**](VipType.md) |  | [optional] 
**verification** | [**VipVerification**](VipVerification.md) |  | [optional] 

## Example

```python
from openshift_assisted_service.models.verified_vip import VerifiedVip

# TODO update the JSON string below
json = "{}"
# create an instance of VerifiedVip from a JSON string
verified_vip_instance = VerifiedVip.from_json(json)
# print the JSON string representation of the object
print VerifiedVip.to_json()

# convert the object into a dict
verified_vip_dict = verified_vip_instance.to_dict()
# create an instance of VerifiedVip from a dict
verified_vip_form_dict = verified_vip.from_dict(verified_vip_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


