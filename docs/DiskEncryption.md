# DiskEncryption


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_on** | **str** | Enable/disable disk encryption on master nodes, worker nodes, or all nodes. | [optional] [default to 'none']
**mode** | **str** | The disk encryption mode to use. | [optional] [default to 'tpmv2']
**tang_servers** | **str** | JSON-formatted string containing additional information regarding tang&#39;s configuration | [optional] 

## Example

```python
from openshift_assisted_service.models.disk_encryption import DiskEncryption

# TODO update the JSON string below
json = "{}"
# create an instance of DiskEncryption from a JSON string
disk_encryption_instance = DiskEncryption.from_json(json)
# print the JSON string representation of the object
print DiskEncryption.to_json()

# convert the object into a dict
disk_encryption_dict = disk_encryption_instance.to_dict()
# create an instance of DiskEncryption from a dict
disk_encryption_form_dict = disk_encryption.from_dict(disk_encryption_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


