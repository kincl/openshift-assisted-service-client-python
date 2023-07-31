# DiskSkipFormattingParams

Allows an addition or removal of a host disk from the host's skip_formatting_disks list

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disk_id** | **str** | The ID of the disk that is being added to or removed from the host&#39;s skip_formatting_disks list | 
**skip_formatting** | **bool** | True if you wish to add the disk to the skip_formatting_disks list, false if you wish to remove it | 

## Example

```python
from openshift_assisted_service.models.disk_skip_formatting_params import DiskSkipFormattingParams

# TODO update the JSON string below
json = "{}"
# create an instance of DiskSkipFormattingParams from a JSON string
disk_skip_formatting_params_instance = DiskSkipFormattingParams.from_json(json)
# print the JSON string representation of the object
print DiskSkipFormattingParams.to_json()

# convert the object into a dict
disk_skip_formatting_params_dict = disk_skip_formatting_params_instance.to_dict()
# create an instance of DiskSkipFormattingParams from a dict
disk_skip_formatting_params_form_dict = disk_skip_formatting_params.from_dict(disk_skip_formatting_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


