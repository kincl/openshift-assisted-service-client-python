# CreateManifestParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folder** | **str** | The folder that contains the files. Manifests can be placed in &#39;manifests&#39; or &#39;openshift&#39; directories. | [optional] [default to 'manifests']
**file_name** | **str** | The name of the manifest to customize the installed OCP cluster. | 
**content** | **str** | base64 encoded manifest content. | 

## Example

```python
from openshift_assisted_service.models.create_manifest_params import CreateManifestParams

# TODO update the JSON string below
json = "{}"
# create an instance of CreateManifestParams from a JSON string
create_manifest_params_instance = CreateManifestParams.from_json(json)
# print the JSON string representation of the object
print CreateManifestParams.to_json()

# convert the object into a dict
create_manifest_params_dict = create_manifest_params_instance.to_dict()
# create an instance of CreateManifestParams from a dict
create_manifest_params_form_dict = create_manifest_params.from_dict(create_manifest_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


