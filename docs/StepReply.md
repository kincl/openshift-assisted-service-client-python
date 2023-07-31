# StepReply


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**step_type** | [**StepType**](StepType.md) |  | [optional] 
**step_id** | **str** |  | [optional] 
**exit_code** | **int** |  | [optional] 
**output** | **str** |  | [optional] 
**error** | **str** |  | [optional] 

## Example

```python
from openshift_assisted_service.models.step_reply import StepReply

# TODO update the JSON string below
json = "{}"
# create an instance of StepReply from a JSON string
step_reply_instance = StepReply.from_json(json)
# print the JSON string representation of the object
print StepReply.to_json()

# convert the object into a dict
step_reply_dict = step_reply_instance.to_dict()
# create an instance of StepReply from a dict
step_reply_form_dict = step_reply.from_dict(step_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


