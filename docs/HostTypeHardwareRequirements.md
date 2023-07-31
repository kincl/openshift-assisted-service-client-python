# HostTypeHardwareRequirements


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantitative** | [**ClusterHostRequirementsDetails**](ClusterHostRequirementsDetails.md) |  | [optional] 
**qualitative** | **List[str]** | Host requirements that cannot be quantified at the time of calculation. Descriptions or formulas of requiements | [optional] 

## Example

```python
from openshift_assisted_service.models.host_type_hardware_requirements import HostTypeHardwareRequirements

# TODO update the JSON string below
json = "{}"
# create an instance of HostTypeHardwareRequirements from a JSON string
host_type_hardware_requirements_instance = HostTypeHardwareRequirements.from_json(json)
# print the JSON string representation of the object
print HostTypeHardwareRequirements.to_json()

# convert the object into a dict
host_type_hardware_requirements_dict = host_type_hardware_requirements_instance.to_dict()
# create an instance of HostTypeHardwareRequirements from a dict
host_type_hardware_requirements_form_dict = host_type_hardware_requirements.from_dict(host_type_hardware_requirements_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


