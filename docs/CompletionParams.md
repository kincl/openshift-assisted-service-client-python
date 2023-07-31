# CompletionParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | 
**error_info** | **str** |  | [optional] 
**data** | **Dict[str, object]** | additional data from the cluster | [optional] 

## Example

```python
from openshift_assisted_service.models.completion_params import CompletionParams

# TODO update the JSON string below
json = "{}"
# create an instance of CompletionParams from a JSON string
completion_params_instance = CompletionParams.from_json(json)
# print the JSON string representation of the object
print CompletionParams.to_json()

# convert the object into a dict
completion_params_dict = completion_params_instance.to_dict()
# create an instance of CompletionParams from a dict
completion_params_form_dict = completion_params.from_dict(completion_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


