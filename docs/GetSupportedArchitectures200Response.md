# GetSupportedArchitectures200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**architectures** | [**Dict[str, SupportLevel]**](SupportLevel.md) | Map of feature ID or CPU architecture alongside their support level | [optional] 

## Example

```python
from openshift_assisted_service.models.get_supported_architectures200_response import GetSupportedArchitectures200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetSupportedArchitectures200Response from a JSON string
get_supported_architectures200_response_instance = GetSupportedArchitectures200Response.from_json(json)
# print the JSON string representation of the object
print GetSupportedArchitectures200Response.to_json()

# convert the object into a dict
get_supported_architectures200_response_dict = get_supported_architectures200_response_instance.to_dict()
# create an instance of GetSupportedArchitectures200Response from a dict
get_supported_architectures200_response_form_dict = get_supported_architectures200_response.from_dict(get_supported_architectures200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


