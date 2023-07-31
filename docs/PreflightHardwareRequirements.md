# PreflightHardwareRequirements


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operators** | [**List[OperatorHardwareRequirements]**](OperatorHardwareRequirements.md) | Preflight operators hardware requirements | [optional] 
**ocp** | [**HostTypeHardwareRequirementsWrapper**](HostTypeHardwareRequirementsWrapper.md) |  | [optional] 

## Example

```python
from openshift_assisted_service.models.preflight_hardware_requirements import PreflightHardwareRequirements

# TODO update the JSON string below
json = "{}"
# create an instance of PreflightHardwareRequirements from a JSON string
preflight_hardware_requirements_instance = PreflightHardwareRequirements.from_json(json)
# print the JSON string representation of the object
print PreflightHardwareRequirements.to_json()

# convert the object into a dict
preflight_hardware_requirements_dict = preflight_hardware_requirements_instance.to_dict()
# create an instance of PreflightHardwareRequirements from a dict
preflight_hardware_requirements_form_dict = preflight_hardware_requirements.from_dict(preflight_hardware_requirements_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


