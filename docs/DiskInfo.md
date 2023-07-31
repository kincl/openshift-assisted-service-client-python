# DiskInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**disk_speed** | [**DiskSpeed**](DiskSpeed.md) |  | [optional] 

## Example

```python
from openshift_assisted_service.models.disk_info import DiskInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DiskInfo from a JSON string
disk_info_instance = DiskInfo.from_json(json)
# print the JSON string representation of the object
print DiskInfo.to_json()

# convert the object into a dict
disk_info_dict = disk_info_instance.to_dict()
# create an instance of DiskInfo from a dict
disk_info_form_dict = disk_info.from_dict(disk_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


