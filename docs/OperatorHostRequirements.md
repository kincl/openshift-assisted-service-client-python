# OperatorHostRequirements


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operator_name** | **str** | Name of the operator | [optional] 
**requirements** | [**ClusterHostRequirementsDetails**](ClusterHostRequirementsDetails.md) |  | [optional] 

## Example

```python
from openshift_assisted_service.models.operator_host_requirements import OperatorHostRequirements

# TODO update the JSON string below
json = "{}"
# create an instance of OperatorHostRequirements from a JSON string
operator_host_requirements_instance = OperatorHostRequirements.from_json(json)
# print the JSON string representation of the object
print OperatorHostRequirements.to_json()

# convert the object into a dict
operator_host_requirements_dict = operator_host_requirements_instance.to_dict()
# create an instance of OperatorHostRequirements from a dict
operator_host_requirements_form_dict = operator_host_requirements.from_dict(operator_host_requirements_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


