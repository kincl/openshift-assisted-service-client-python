# DomainResolutionRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domains** | [**List[DomainResolutionRequestDomainsInner]**](DomainResolutionRequestDomainsInner.md) |  | 

## Example

```python
from openshift_assisted_service.models.domain_resolution_request import DomainResolutionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DomainResolutionRequest from a JSON string
domain_resolution_request_instance = DomainResolutionRequest.from_json(json)
# print the JSON string representation of the object
print DomainResolutionRequest.to_json()

# convert the object into a dict
domain_resolution_request_dict = domain_resolution_request_instance.to_dict()
# create an instance of DomainResolutionRequest from a dict
domain_resolution_request_form_dict = domain_resolution_request.from_dict(domain_resolution_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


