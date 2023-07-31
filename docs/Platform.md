# Platform

The configuration for the specific platform upon which to perform the installation.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**PlatformType**](PlatformType.md) |  | 
**is_external** | **bool** | Used by the service to indicate that the platform-specific components are not included in OpenShift and must be provided as manifests separately. | [optional] [readonly] 

## Example

```python
from openshift_assisted_service.models.platform import Platform

# TODO update the JSON string below
json = "{}"
# create an instance of Platform from a JSON string
platform_instance = Platform.from_json(json)
# print the JSON string representation of the object
print Platform.to_json()

# convert the object into a dict
platform_dict = platform_instance.to_dict()
# create an instance of Platform from a dict
platform_form_dict = platform.from_dict(platform_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


