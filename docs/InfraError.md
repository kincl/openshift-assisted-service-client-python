# InfraError


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | Numeric identifier of the error. | 
**message** | **str** | Human-readable description of the error. | 

## Example

```python
from openshift_assisted_service.models.infra_error import InfraError

# TODO update the JSON string below
json = "{}"
# create an instance of InfraError from a JSON string
infra_error_instance = InfraError.from_json(json)
# print the JSON string representation of the object
print InfraError.to_json()

# convert the object into a dict
infra_error_dict = infra_error_instance.to_dict()
# create an instance of InfraError from a dict
infra_error_form_dict = infra_error.from_dict(infra_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


