# DomainResolutionRequestDomainsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_name** | **str** | The domain name that should be resolved | 

## Example

```python
from openshift_assisted_service.models.domain_resolution_request_domains_inner import DomainResolutionRequestDomainsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DomainResolutionRequestDomainsInner from a JSON string
domain_resolution_request_domains_inner_instance = DomainResolutionRequestDomainsInner.from_json(json)
# print the JSON string representation of the object
print DomainResolutionRequestDomainsInner.to_json()

# convert the object into a dict
domain_resolution_request_domains_inner_dict = domain_resolution_request_domains_inner_instance.to_dict()
# create an instance of DomainResolutionRequestDomainsInner from a dict
domain_resolution_request_domains_inner_form_dict = domain_resolution_request_domains_inner.from_dict(domain_resolution_request_domains_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


