# DiskSpeed


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tested** | **bool** |  | [optional] 
**exit_code** | **int** |  | [optional] 
**speed_ms** | **int** |  | [optional] 

## Example

```python
from openshift_assisted_service.models.disk_speed import DiskSpeed

# TODO update the JSON string below
json = "{}"
# create an instance of DiskSpeed from a JSON string
disk_speed_instance = DiskSpeed.from_json(json)
# print the JSON string representation of the object
print DiskSpeed.to_json()

# convert the object into a dict
disk_speed_dict = disk_speed_instance.to_dict()
# create an instance of DiskSpeed from a dict
disk_speed_form_dict = disk_speed.from_dict(disk_speed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


