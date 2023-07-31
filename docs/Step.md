# Step


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**step_type** | [**StepType**](StepType.md) |  | [optional] 
**step_id** | **str** |  | [optional] 
**args** | **List[str]** |  | [optional] 

## Example

```python
from openshift_assisted_service.models.step import Step

# TODO update the JSON string below
json = "{}"
# create an instance of Step from a JSON string
step_instance = Step.from_json(json)
# print the JSON string representation of the object
print Step.to_json()

# convert the object into a dict
step_dict = step_instance.to_dict()
# create an instance of Step from a dict
step_form_dict = step.from_dict(step_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


