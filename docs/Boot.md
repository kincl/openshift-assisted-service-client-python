# Boot


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_boot_mode** | **str** |  | [optional] 
**pxe_interface** | **str** |  | [optional] 

## Example

```python
from openshift_assisted_service.models.boot import Boot

# TODO update the JSON string below
json = "{}"
# create an instance of Boot from a JSON string
boot_instance = Boot.from_json(json)
# print the JSON string representation of the object
print Boot.to_json()

# convert the object into a dict
boot_dict = boot_instance.to_dict()
# create an instance of Boot from a dict
boot_form_dict = boot.from_dict(boot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


