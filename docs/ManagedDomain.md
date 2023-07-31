# ManagedDomain


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** |  | [optional] 
**provider** | **str** |  | [optional] 

## Example

```python
from openshift_assisted_service.models.managed_domain import ManagedDomain

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedDomain from a JSON string
managed_domain_instance = ManagedDomain.from_json(json)
# print the JSON string representation of the object
print ManagedDomain.to_json()

# convert the object into a dict
managed_domain_dict = managed_domain_instance.to_dict()
# create an instance of ManagedDomain from a dict
managed_domain_form_dict = managed_domain.from_dict(managed_domain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


