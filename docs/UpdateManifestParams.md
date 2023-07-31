# UpdateManifestParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folder** | **str** | The folder for the manifest to modify. | [default to 'manifests']
**file_name** | **str** | The file name for the manifest to modify. | 
**updated_folder** | **str** | The new folder for the manifest. Manifests can be placed in &#39;manifests&#39; or &#39;openshift&#39; directories. | [optional] [default to 'manifests']
**updated_file_name** | **str** | The new file name for the manifest. | [optional] 
**updated_content** | **str** | The new base64 encoded manifest content. | [optional] 

## Example

```python
from openshift_assisted_service.models.update_manifest_params import UpdateManifestParams

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateManifestParams from a JSON string
update_manifest_params_instance = UpdateManifestParams.from_json(json)
# print the JSON string representation of the object
print UpdateManifestParams.to_json()

# convert the object into a dict
update_manifest_params_dict = update_manifest_params_instance.to_dict()
# create an instance of UpdateManifestParams from a dict
update_manifest_params_form_dict = update_manifest_params.from_dict(update_manifest_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


