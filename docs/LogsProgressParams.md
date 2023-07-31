# LogsProgressParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logs_state** | [**LogsState**](LogsState.md) |  | 

## Example

```python
from openshift_assisted_service.models.logs_progress_params import LogsProgressParams

# TODO update the JSON string below
json = "{}"
# create an instance of LogsProgressParams from a JSON string
logs_progress_params_instance = LogsProgressParams.from_json(json)
# print the JSON string representation of the object
print LogsProgressParams.to_json()

# convert the object into a dict
logs_progress_params_dict = logs_progress_params_instance.to_dict()
# create an instance of LogsProgressParams from a dict
logs_progress_params_form_dict = logs_progress_params.from_dict(logs_progress_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


