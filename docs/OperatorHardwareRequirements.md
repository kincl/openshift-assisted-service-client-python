# OperatorHardwareRequirements


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operator_name** | **str** | Unique name of the operator. Corresponds to name property of the monitored-operator, i.e. \&quot;lso\&quot;, \&quot;cnv\&quot;, etc. | [optional] 
**dependencies** | **List[str]** | List of other operator unique names that are required to be installed. Corresponds to name property of the monitored-operator, i.e. \&quot;lso\&quot;, \&quot;cnv\&quot;, etc. | [optional] 
**requirements** | [**HostTypeHardwareRequirementsWrapper**](HostTypeHardwareRequirementsWrapper.md) |  | [optional] 

## Example

```python
from openshift_assisted_service.models.operator_hardware_requirements import OperatorHardwareRequirements

# TODO update the JSON string below
json = "{}"
# create an instance of OperatorHardwareRequirements from a JSON string
operator_hardware_requirements_instance = OperatorHardwareRequirements.from_json(json)
# print the JSON string representation of the object
print OperatorHardwareRequirements.to_json()

# convert the object into a dict
operator_hardware_requirements_dict = operator_hardware_requirements_instance.to_dict()
# create an instance of OperatorHardwareRequirements from a dict
operator_hardware_requirements_form_dict = operator_hardware_requirements.from_dict(operator_hardware_requirements_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


