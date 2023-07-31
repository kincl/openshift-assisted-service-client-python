# IgnitionEndpoint

Explicit ignition endpoint overrides the default ignition endpoint.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The URL for the ignition endpoint. | [optional] 
**ca_certificate** | **str** | base64 encoded CA certficate to be used when contacting the URL via https. | [optional] 

## Example

```python
from openshift_assisted_service.models.ignition_endpoint import IgnitionEndpoint

# TODO update the JSON string below
json = "{}"
# create an instance of IgnitionEndpoint from a JSON string
ignition_endpoint_instance = IgnitionEndpoint.from_json(json)
# print the JSON string representation of the object
print IgnitionEndpoint.to_json()

# convert the object into a dict
ignition_endpoint_dict = ignition_endpoint_instance.to_dict()
# create an instance of IgnitionEndpoint from a dict
ignition_endpoint_form_dict = ignition_endpoint.from_dict(ignition_endpoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


