# ImageInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ssh_public_key** | **str** | SSH public key for debugging the installation. | [optional] 
**size_bytes** | **int** |  | [optional] 
**download_url** | **str** |  | [optional] 
**generator_version** | **str** | Image generator version. | [optional] 
**created_at** | **datetime** |  | [optional] 
**expires_at** | **datetime** |  | [optional] 
**static_network_config** | **str** | static network configuration string in the format expected by discovery ignition generation | [optional] 
**type** | [**ImageType**](ImageType.md) |  | [optional] 

## Example

```python
from openshift_assisted_service.models.image_info import ImageInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ImageInfo from a JSON string
image_info_instance = ImageInfo.from_json(json)
# print the JSON string representation of the object
print ImageInfo.to_json()

# convert the object into a dict
image_info_dict = image_info_instance.to_dict()
# create an instance of ImageInfo from a dict
image_info_form_dict = image_info.from_dict(image_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


