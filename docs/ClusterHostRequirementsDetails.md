# ClusterHostRequirementsDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu_cores** | **int** | Required number of CPU cores | [optional] 
**ram_mib** | **int** | Required number of RAM in MiB | [optional] 
**disk_size_gb** | **int** | Required disk size in GB | [optional] 
**installation_disk_speed_threshold_ms** | **int** | Required installation disk speed in ms | [optional] 
**network_latency_threshold_ms** | **float** | Maximum network average latency (RTT) at L3 for role. | [optional] 
**packet_loss_percentage** | **float** | Maximum packet loss allowed at L3 for role. | [optional] 
**tpm_enabled_in_bios** | **bool** | Whether TPM module should be enabled in host&#39;s BIOS. | [optional] 

## Example

```python
from openshift_assisted_service.models.cluster_host_requirements_details import ClusterHostRequirementsDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterHostRequirementsDetails from a JSON string
cluster_host_requirements_details_instance = ClusterHostRequirementsDetails.from_json(json)
# print the JSON string representation of the object
print ClusterHostRequirementsDetails.to_json()

# convert the object into a dict
cluster_host_requirements_details_dict = cluster_host_requirements_details_instance.to_dict()
# create an instance of ClusterHostRequirementsDetails from a dict
cluster_host_requirements_details_form_dict = cluster_host_requirements_details.from_dict(cluster_host_requirements_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


