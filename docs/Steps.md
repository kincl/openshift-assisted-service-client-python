# Steps


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_instruction_seconds** | **int** |  | [optional] 
**post_step_action** | **str** | What to do after finishing to run step instructions | [optional] [default to 'continue']
**instructions** | [**List[Step]**](Step.md) |  | [optional] 

## Example

```python
from openshift_assisted_service.models.steps import Steps

# TODO update the JSON string below
json = "{}"
# create an instance of Steps from a JSON string
steps_instance = Steps.from_json(json)
# print the JSON string representation of the object
print Steps.to_json()

# convert the object into a dict
steps_dict = steps_instance.to_dict()
# create an instance of Steps from a dict
steps_form_dict = steps.from_dict(steps_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


