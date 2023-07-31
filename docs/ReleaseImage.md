# ReleaseImage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**openshift_version** | **str** | Version of the OpenShift cluster. | 
**cpu_architecture** | **str** | (DEPRECATED) The CPU architecture of the image (x86_64/arm64/etc). | [default to 'x86_64']
**cpu_architectures** | **List[str]** | List of CPU architectures provided by the image. | [optional] 
**url** | **str** | The installation image of the OpenShift cluster. | 
**version** | **str** | OCP version from the release metadata. | 
**default** | **bool** | Indication that the version is the recommended one. | [optional] 
**support_level** | **str** | Level of support of the version. | [optional] 

## Example

```python
from openshift_assisted_service.models.release_image import ReleaseImage

# TODO update the JSON string below
json = "{}"
# create an instance of ReleaseImage from a JSON string
release_image_instance = ReleaseImage.from_json(json)
# print the JSON string representation of the object
print ReleaseImage.to_json()

# convert the object into a dict
release_image_dict = release_image_instance.to_dict()
# create an instance of ReleaseImage from a dict
release_image_form_dict = release_image.from_dict(release_image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


