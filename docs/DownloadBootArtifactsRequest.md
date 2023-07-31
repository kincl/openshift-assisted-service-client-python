# DownloadBootArtifactsRequest

Information sent to the agent for downloading artifacts to boot a host into discovery.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kernel_url** | **str** | URL address to download the kernel. | 
**rootfs_url** | **str** | URL address to download the rootfs. | 
**initrd_url** | **str** | URL address to download the initrd. | 
**host_fs_mount_dir** | **str** | The base directory on the host that contains the /boot folder. The host will download boot artifacts into a folder in this directory. | 

## Example

```python
from openshift_assisted_service.models.download_boot_artifacts_request import DownloadBootArtifactsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DownloadBootArtifactsRequest from a JSON string
download_boot_artifacts_request_instance = DownloadBootArtifactsRequest.from_json(json)
# print the JSON string representation of the object
print DownloadBootArtifactsRequest.to_json()

# convert the object into a dict
download_boot_artifacts_request_dict = download_boot_artifacts_request_instance.to_dict()
# create an instance of DownloadBootArtifactsRequest from a dict
download_boot_artifacts_request_form_dict = download_boot_artifacts_request.from_dict(download_boot_artifacts_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


