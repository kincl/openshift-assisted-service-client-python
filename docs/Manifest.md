# Manifest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folder** | **str** | The folder that contains the files. Manifests can be placed in &#39;manifests&#39; or &#39;openshift&#39; directories. | [optional] 
**file_name** | **str** | The file name prefaced by the folder that contains it. | [optional] 

## Example

```python
from openshift_assisted_service.models.manifest import Manifest

# TODO update the JSON string below
json = "{}"
# create an instance of Manifest from a JSON string
manifest_instance = Manifest.from_json(json)
# print the JSON string representation of the object
print Manifest.to_json()

# convert the object into a dict
manifest_dict = manifest_instance.to_dict()
# create an instance of Manifest from a dict
manifest_form_dict = manifest.from_dict(manifest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


