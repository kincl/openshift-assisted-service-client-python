# DomainResolutionResponseResolutionsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_name** | **str** | The domain that was resolved | 
**ipv4_addresses** | **List[str]** | The IPv4 addresses of the domain, empty if none | [optional] 
**ipv6_addresses** | **List[str]** | The IPv6 addresses of the domain, empty if none | [optional] 

## Example

```python
from openshift_assisted_service.models.domain_resolution_response_resolutions_inner import DomainResolutionResponseResolutionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DomainResolutionResponseResolutionsInner from a JSON string
domain_resolution_response_resolutions_inner_instance = DomainResolutionResponseResolutionsInner.from_json(json)
# print the JSON string representation of the object
print DomainResolutionResponseResolutionsInner.to_json()

# convert the object into a dict
domain_resolution_response_resolutions_inner_dict = domain_resolution_response_resolutions_inner_instance.to_dict()
# create an instance of DomainResolutionResponseResolutionsInner from a dict
domain_resolution_response_resolutions_inner_form_dict = domain_resolution_response_resolutions_inner.from_dict(domain_resolution_response_resolutions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


