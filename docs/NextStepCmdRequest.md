# NextStepCmdRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**infra_env_id** | **str** | Infra env id | 
**host_id** | **str** | Host id | 
**agent_version** | **str** | Agent image version | 

## Example

```python
from openshift_assisted_service.models.next_step_cmd_request import NextStepCmdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NextStepCmdRequest from a JSON string
next_step_cmd_request_instance = NextStepCmdRequest.from_json(json)
# print the JSON string representation of the object
print NextStepCmdRequest.to_json()

# convert the object into a dict
next_step_cmd_request_dict = next_step_cmd_request_instance.to_dict()
# create an instance of NextStepCmdRequest from a dict
next_step_cmd_request_form_dict = next_step_cmd_request.from_dict(next_step_cmd_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


