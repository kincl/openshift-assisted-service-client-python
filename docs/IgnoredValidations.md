# IgnoredValidations


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_validation_ids** | **str** | JSON-formatted list of cluster validation IDs that will be ignored for all hosts that belong to this cluster. It may also contain a list with a single string \&quot;all\&quot; to ignore all cluster validations. Some validations cannot be ignored. | [optional] 
**host_validation_ids** | **str** | JSON-formatted list of host validation IDs that will be ignored for all hosts that belong to this cluster. It may also contain a list with a single string \&quot;all\&quot; to ignore all host validations. Some validations cannot be ignored. | [optional] 

## Example

```python
from openshift_assisted_service.models.ignored_validations import IgnoredValidations

# TODO update the JSON string below
json = "{}"
# create an instance of IgnoredValidations from a JSON string
ignored_validations_instance = IgnoredValidations.from_json(json)
# print the JSON string representation of the object
print IgnoredValidations.to_json()

# convert the object into a dict
ignored_validations_dict = ignored_validations_instance.to_dict()
# create an instance of IgnoredValidations from a dict
ignored_validations_form_dict = ignored_validations.from_dict(ignored_validations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


