# ClusterDefaultConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_network_cidr** | **str** |  | [optional] 
**cluster_network_host_prefix** | **int** |  | [optional] 
**inactive_deletion_hours** | **int** |  | [optional] 
**service_network_cidr** | **str** |  | [optional] 
**ntp_source** | **str** |  | [optional] 
**cluster_networks_ipv4** | [**List[ClusterNetwork]**](ClusterNetwork.md) |  | [optional] 
**cluster_networks_dualstack** | [**List[ClusterNetwork]**](ClusterNetwork.md) |  | [optional] 
**service_networks_ipv4** | [**List[ServiceNetwork]**](ServiceNetwork.md) |  | [optional] 
**service_networks_dualstack** | [**List[ServiceNetwork]**](ServiceNetwork.md) |  | [optional] 
**forbidden_hostnames** | **List[str]** | This provides a list of forbidden hostnames. If this list is empty or not present, this implies that the UI should fall back to a hard coded list. | [optional] 

## Example

```python
from openshift_assisted_service.models.cluster_default_config import ClusterDefaultConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterDefaultConfig from a JSON string
cluster_default_config_instance = ClusterDefaultConfig.from_json(json)
# print the JSON string representation of the object
print ClusterDefaultConfig.to_json()

# convert the object into a dict
cluster_default_config_dict = cluster_default_config_instance.to_dict()
# create an instance of ClusterDefaultConfig from a dict
cluster_default_config_form_dict = cluster_default_config.from_dict(cluster_default_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


