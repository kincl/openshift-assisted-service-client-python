# VerifyVip

Request to verify single vip.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vip** | **str** |  | [optional] 
**vip_type** | [**VipType**](VipType.md) |  | [optional] 

## Example

```python
from openshift_assisted_service.models.verify_vip import VerifyVip

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyVip from a JSON string
verify_vip_instance = VerifyVip.from_json(json)
# print the JSON string representation of the object
print VerifyVip.to_json()

# convert the object into a dict
verify_vip_dict = verify_vip_instance.to_dict()
# create an instance of VerifyVip from a dict
verify_vip_form_dict = verify_vip.from_dict(verify_vip_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


