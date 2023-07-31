# DiskConfigParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**role** | [**DiskRole**](DiskRole.md) |  | [optional] 

## Example

```python
from openshift_assisted_service.models.disk_config_params import DiskConfigParams

# TODO update the JSON string below
json = "{}"
# create an instance of DiskConfigParams from a JSON string
disk_config_params_instance = DiskConfigParams.from_json(json)
# print the JSON string representation of the object
print DiskConfigParams.to_json()

# convert the object into a dict
disk_config_params_dict = disk_config_params_instance.to_dict()
# create an instance of DiskConfigParams from a dict
disk_config_params_form_dict = disk_config_params.from_dict(disk_config_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


