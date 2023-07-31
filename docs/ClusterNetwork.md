# ClusterNetwork

A network from which Pod IPs are allocated. This block must not overlap with existing physical networks. These IP addresses are used for the Pod network, and if you need to access the Pods from an external network, configure load balancers and routers to manage the traffic.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **str** | The cluster that this network is associated with. | [optional] 
**cidr** | **str** |  | [optional] 
**host_prefix** | **int** | The subnet prefix length to assign to each individual node. For example if is set to 23, then each node is assigned a /23 subnet out of the given CIDR, which allows for 510 (2^(32 - 23) - 2) pod IPs addresses. | [optional] 

## Example

```python
from openshift_assisted_service.models.cluster_network import ClusterNetwork

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterNetwork from a JSON string
cluster_network_instance = ClusterNetwork.from_json(json)
# print the JSON string representation of the object
print ClusterNetwork.to_json()

# convert the object into a dict
cluster_network_dict = cluster_network_instance.to_dict()
# create an instance of ClusterNetwork from a dict
cluster_network_form_dict = cluster_network.from_dict(cluster_network_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


