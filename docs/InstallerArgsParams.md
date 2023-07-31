# InstallerArgsParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**args** | **List[str]** | List of additional arguments passed to coreos-installer | [optional] 

## Example

```python
from openshift_assisted_service.models.installer_args_params import InstallerArgsParams

# TODO update the JSON string below
json = "{}"
# create an instance of InstallerArgsParams from a JSON string
installer_args_params_instance = InstallerArgsParams.from_json(json)
# print the JSON string representation of the object
print InstallerArgsParams.to_json()

# convert the object into a dict
installer_args_params_dict = installer_args_params_instance.to_dict()
# create an instance of InstallerArgsParams from a dict
installer_args_params_form_dict = installer_args_params.from_dict(installer_args_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


