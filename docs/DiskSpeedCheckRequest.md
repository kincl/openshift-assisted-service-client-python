# DiskSpeedCheckRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | --filename argument for fio (expects a file or a block device path). | 

## Example

```python
from openshift_assisted_service.models.disk_speed_check_request import DiskSpeedCheckRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DiskSpeedCheckRequest from a JSON string
disk_speed_check_request_instance = DiskSpeedCheckRequest.from_json(json)
# print the JSON string representation of the object
print DiskSpeedCheckRequest.to_json()

# convert the object into a dict
disk_speed_check_request_dict = disk_speed_check_request_instance.to_dict()
# create an instance of DiskSpeedCheckRequest from a dict
disk_speed_check_request_form_dict = disk_speed_check_request.from_dict(disk_speed_check_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


