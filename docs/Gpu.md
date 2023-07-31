# Gpu


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vendor** | **str** | The name of the device vendor (for example \&quot;Intel Corporation\&quot;) | [optional] 
**vendor_id** | **str** | ID of the vendor (for example \&quot;8086\&quot;) | [optional] 
**device_id** | **str** | ID of the device (for example \&quot;3ea0\&quot;) | [optional] 
**name** | **str** | Product name of the device (for example \&quot;UHD Graphics 620 (Whiskey Lake)\&quot;) | [optional] 
**address** | **str** | Device address (for example \&quot;0000:00:02.0\&quot;) | [optional] 

## Example

```python
from openshift_assisted_service.models.gpu import Gpu

# TODO update the JSON string below
json = "{}"
# create an instance of Gpu from a JSON string
gpu_instance = Gpu.from_json(json)
# print the JSON string representation of the object
print Gpu.to_json()

# convert the object into a dict
gpu_dict = gpu_instance.to_dict()
# create an instance of Gpu from a dict
gpu_form_dict = gpu.from_dict(gpu_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


