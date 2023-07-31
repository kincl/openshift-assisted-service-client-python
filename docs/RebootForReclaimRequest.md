# RebootForReclaimRequest

Information sent to the agent for rebooting a host into discovery.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_fs_mount_dir** | **str** | The base directory on the host that contains the /boot folder. The host needs to chroot into this directory in order to properly reboot. | 

## Example

```python
from openshift_assisted_service.models.reboot_for_reclaim_request import RebootForReclaimRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RebootForReclaimRequest from a JSON string
reboot_for_reclaim_request_instance = RebootForReclaimRequest.from_json(json)
# print the JSON string representation of the object
print RebootForReclaimRequest.to_json()

# convert the object into a dict
reboot_for_reclaim_request_dict = reboot_for_reclaim_request_instance.to_dict()
# create an instance of RebootForReclaimRequest from a dict
reboot_for_reclaim_request_form_dict = reboot_for_reclaim_request.from_dict(reboot_for_reclaim_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


