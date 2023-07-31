# OsImage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**openshift_version** | **str** | Version of the operating system image | 
**cpu_architecture** | **str** | The CPU architecture of the image (x86_64/arm64/etc). | [default to 'x86_64']
**url** | **str** | The base OS image used for the discovery iso. | 
**version** | **str** | Build ID of the OS image. | 

## Example

```python
from openshift_assisted_service.models.os_image import OsImage

# TODO update the JSON string below
json = "{}"
# create an instance of OsImage from a JSON string
os_image_instance = OsImage.from_json(json)
# print the JSON string representation of the object
print OsImage.to_json()

# convert the object into a dict
os_image_dict = os_image_instance.to_dict()
# create an instance of OsImage from a dict
os_image_form_dict = os_image.from_dict(os_image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


