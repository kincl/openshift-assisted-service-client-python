# Disk


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Determine the disk&#39;s unique identifier which is the by-id field if it exists and fallback to the by-path field otherwise | [optional] 
**drive_type** | [**DriveType**](DriveType.md) |  | [optional] 
**has_uuid** | **bool** |  | [optional] 
**vendor** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**hctl** | **str** |  | [optional] 
**by_path** | **str** | by-path is the shortest physical path to the device | [optional] 
**by_id** | **str** | by-id is the World Wide Number of the device which guaranteed to be unique for every storage device | [optional] 
**model** | **str** |  | [optional] 
**wwn** | **str** |  | [optional] 
**serial** | **str** |  | [optional] 
**size_bytes** | **int** |  | [optional] 
**bootable** | **bool** |  | [optional] 
**removable** | **bool** |  | [optional] 
**is_installation_media** | **bool** | Whether the disk appears to be an installation media or not | [optional] 
**installation_eligibility** | [**DiskInstallationEligibility**](DiskInstallationEligibility.md) |  | [optional] 
**smart** | **str** |  | [optional] 
**io_perf** | [**IoPerf**](IoPerf.md) |  | [optional] 
**holders** | **str** | A comma-separated list of disk names that this disk belongs to | [optional] 

## Example

```python
from openshift_assisted_service.models.disk import Disk

# TODO update the JSON string below
json = "{}"
# create an instance of Disk from a JSON string
disk_instance = Disk.from_json(json)
# print the JSON string representation of the object
print Disk.to_json()

# convert the object into a dict
disk_dict = disk_instance.to_dict()
# create an instance of Disk from a dict
disk_form_dict = disk.from_dict(disk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


