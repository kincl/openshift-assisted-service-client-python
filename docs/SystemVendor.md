# SystemVendor


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**serial_number** | **str** |  | [optional] 
**product_name** | **str** |  | [optional] 
**manufacturer** | **str** |  | [optional] 
**virtual** | **bool** | Whether the machine appears to be a virtual machine or not | [optional] 

## Example

```python
from openshift_assisted_service.models.system_vendor import SystemVendor

# TODO update the JSON string below
json = "{}"
# create an instance of SystemVendor from a JSON string
system_vendor_instance = SystemVendor.from_json(json)
# print the JSON string representation of the object
print SystemVendor.to_json()

# convert the object into a dict
system_vendor_dict = system_vendor_instance.to_dict()
# create an instance of SystemVendor from a dict
system_vendor_form_dict = system_vendor.from_dict(system_vendor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


