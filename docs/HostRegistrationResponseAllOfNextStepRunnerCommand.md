# HostRegistrationResponseAllOfNextStepRunnerCommand

Command for starting the next step runner

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**command** | **str** |  | [optional] 
**args** | **List[str]** |  | [optional] 
**retry_seconds** | **int** | How long in seconds to wait before retrying registration if the command fails | [optional] 

## Example

```python
from openshift_assisted_service.models.host_registration_response_all_of_next_step_runner_command import HostRegistrationResponseAllOfNextStepRunnerCommand

# TODO update the JSON string below
json = "{}"
# create an instance of HostRegistrationResponseAllOfNextStepRunnerCommand from a JSON string
host_registration_response_all_of_next_step_runner_command_instance = HostRegistrationResponseAllOfNextStepRunnerCommand.from_json(json)
# print the JSON string representation of the object
print HostRegistrationResponseAllOfNextStepRunnerCommand.to_json()

# convert the object into a dict
host_registration_response_all_of_next_step_runner_command_dict = host_registration_response_all_of_next_step_runner_command_instance.to_dict()
# create an instance of HostRegistrationResponseAllOfNextStepRunnerCommand from a dict
host_registration_response_all_of_next_step_runner_command_form_dict = host_registration_response_all_of_next_step_runner_command.from_dict(host_registration_response_all_of_next_step_runner_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


