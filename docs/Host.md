# Host


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;Host&#39; if this is a complete object or &#39;HostLink&#39; if it is just a link, or &#39;AddToExistingClusterHost&#39; for host being added to existing OCP cluster, or  | 
**id** | **str** | Unique identifier of the object. | 
**href** | **str** | Self link. | 
**cluster_id** | **str** | The cluster that this host is associated with. | [optional] 
**infra_env_id** | **str** | The infra-env that this host is associated with. | [optional] 
**status** | **str** |  | 
**status_info** | **str** |  | 
**validations_info** | **str** | JSON-formatted string containing the validation results for each validation id grouped by category (network, hardware, etc.) | [optional] 
**logs_info** | [**LogsState**](LogsState.md) |  | [optional] 
**status_updated_at** | **datetime** | The last time that the host status was updated. | [optional] 
**progress** | [**HostProgressInfo**](HostProgressInfo.md) |  | [optional] 
**stage_started_at** | **datetime** | Time at which the current progress stage started. | [optional] 
**stage_updated_at** | **datetime** | Time at which the current progress stage was last updated. | [optional] 
**progress_stages** | [**List[HostStage]**](HostStage.md) |  | [optional] 
**connectivity** | **str** |  | [optional] 
**api_vip_connectivity** | **str** | Contains a serialized api_vip_connectivity_response | [optional] 
**tang_connectivity** | **str** |  | [optional] 
**inventory** | **str** |  | [optional] 
**free_addresses** | **str** |  | [optional] 
**ntp_sources** | **str** | The configured NTP sources on the host. | [optional] 
**disks_info** | **str** | Additional information about disks, formatted as JSON. | [optional] 
**role** | [**HostRole**](HostRole.md) |  | [optional] 
**suggested_role** | [**HostRole**](HostRole.md) |  | [optional] 
**bootstrap** | **bool** |  | [optional] 
**logs_collected_at** | **datetime** |  | [optional] 
**logs_started_at** | **datetime** |  | [optional] 
**installer_version** | **str** | Installer version. | [optional] 
**installation_disk_path** | **str** | Contains the inventory disk path, This field is replaced by installation_disk_id field and used for backward compatability with the old UI. | [optional] 
**installation_disk_id** | **str** | Contains the inventory disk id to install on. | [optional] 
**updated_at** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**checked_in_at** | **datetime** | The last time the host&#39;s agent communicated with the service. | [optional] 
**registered_at** | **datetime** | The last time the host&#39;s agent tried to register in the service. | [optional] 
**discovery_agent_version** | **str** |  | [optional] 
**requested_hostname** | **str** |  | [optional] 
**user_name** | **str** |  | [optional] 
**media_status** | **str** |  | [optional] [default to 'connected']
**deleted_at** | **object** | swagger:ignore | [optional] 
**ignition_config_overrides** | **str** | Json formatted string containing the user overrides for the host&#39;s pointer ignition | [optional] 
**installer_args** | **str** |  | [optional] 
**timestamp** | **int** | The time on the host as seconds since the Unix epoch. | [optional] 
**machine_config_pool_name** | **str** |  | [optional] 
**images_status** | **str** | Array of image statuses. | [optional] 
**domain_name_resolutions** | **str** | The domain name resolution result. | [optional] 
**ignition_endpoint_token_set** | **bool** | True if the token to fetch the ignition from ignition_endpoint_url is set. | [optional] 
**node_labels** | **str** | Json containing node&#39;s labels. | [optional] 
**disks_to_be_formatted** | **str** | A comma-separated list of disks that will be formatted once installation begins, unless otherwise set to be skipped by skip_formatting_disks. This means that this list also includes disks that appear in skip_formatting_disks. This property is managed by the service and cannot be modified by the user. | [optional] 
**skip_formatting_disks** | **str** | A comma-seperated list of host disks that the service will avoid formatting. | [optional] 

## Example

```python
from openshift_assisted_service.models.host import Host

# TODO update the JSON string below
json = "{}"
# create an instance of Host from a JSON string
host_instance = Host.from_json(json)
# print the JSON string representation of the object
print Host.to_json()

# convert the object into a dict
host_dict = host_instance.to_dict()
# create an instance of Host from a dict
host_form_dict = host.from_dict(host_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


