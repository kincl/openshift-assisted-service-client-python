# DiskSpeedCheckResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**io_sync_duration** | **int** | The 99th percentile of fdatasync durations in milliseconds. | [optional] 
**path** | **str** | The device path. | [optional] 

## Example

```python
from openshift_assisted_service.models.disk_speed_check_response import DiskSpeedCheckResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DiskSpeedCheckResponse from a JSON string
disk_speed_check_response_instance = DiskSpeedCheckResponse.from_json(json)
# print the JSON string representation of the object
print DiskSpeedCheckResponse.to_json()

# convert the object into a dict
disk_speed_check_response_dict = disk_speed_check_response_instance.to_dict()
# create an instance of DiskSpeedCheckResponse from a dict
disk_speed_check_response_form_dict = disk_speed_check_response.from_dict(disk_speed_check_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


