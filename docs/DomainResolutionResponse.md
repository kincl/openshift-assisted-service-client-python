# DomainResolutionResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resolutions** | [**List[DomainResolutionResponseResolutionsInner]**](DomainResolutionResponseResolutionsInner.md) |  | 

## Example

```python
from openshift_assisted_service.models.domain_resolution_response import DomainResolutionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DomainResolutionResponse from a JSON string
domain_resolution_response_instance = DomainResolutionResponse.from_json(json)
# print the JSON string representation of the object
print DomainResolutionResponse.to_json()

# convert the object into a dict
domain_resolution_response_dict = domain_resolution_response_instance.to_dict()
# create an instance of DomainResolutionResponse from a dict
domain_resolution_response_form_dict = domain_resolution_response.from_dict(domain_resolution_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


