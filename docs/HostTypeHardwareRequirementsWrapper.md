# HostTypeHardwareRequirementsWrapper


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**worker** | [**HostTypeHardwareRequirements**](HostTypeHardwareRequirements.md) |  | [optional] 
**master** | [**HostTypeHardwareRequirements**](HostTypeHardwareRequirements.md) |  | [optional] 

## Example

```python
from openshift_assisted_service.models.host_type_hardware_requirements_wrapper import HostTypeHardwareRequirementsWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of HostTypeHardwareRequirementsWrapper from a JSON string
host_type_hardware_requirements_wrapper_instance = HostTypeHardwareRequirementsWrapper.from_json(json)
# print the JSON string representation of the object
print HostTypeHardwareRequirementsWrapper.to_json()

# convert the object into a dict
host_type_hardware_requirements_wrapper_dict = host_type_hardware_requirements_wrapper_instance.to_dict()
# create an instance of HostTypeHardwareRequirementsWrapper from a dict
host_type_hardware_requirements_wrapper_form_dict = host_type_hardware_requirements_wrapper.from_dict(host_type_hardware_requirements_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


