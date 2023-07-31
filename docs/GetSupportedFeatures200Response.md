# GetSupportedFeatures200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**features** | [**Dict[str, SupportLevel]**](SupportLevel.md) | Map of feature ID or CPU architecture alongside their support level | [optional] 

## Example

```python
from openshift_assisted_service.models.get_supported_features200_response import GetSupportedFeatures200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetSupportedFeatures200Response from a JSON string
get_supported_features200_response_instance = GetSupportedFeatures200Response.from_json(json)
# print the JSON string representation of the object
print GetSupportedFeatures200Response.to_json()

# convert the object into a dict
get_supported_features200_response_dict = get_supported_features200_response_instance.to_dict()
# create an instance of GetSupportedFeatures200Response from a dict
get_supported_features200_response_form_dict = get_supported_features200_response.from_dict(get_supported_features200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


