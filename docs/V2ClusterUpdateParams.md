# V2ClusterUpdateParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | OpenShift cluster name. | [optional] 
**base_dns_domain** | **str** | Base domain of the cluster. All DNS records must be sub-domains of this base and include the cluster name. | [optional] 
**cluster_network_cidr** | **str** | IP address block from which Pod IPs are allocated. This block must not overlap with existing physical networks. These IP addresses are used for the Pod network, and if you need to access the Pods from an external network, configure load balancers and routers to manage the traffic. | [optional] 
**platform** | [**Platform**](Platform.md) |  | [optional] 
**cluster_network_host_prefix** | **int** | The subnet prefix length to assign to each individual node. For example, if clusterNetworkHostPrefix is set to 23, then each node is assigned a /23 subnet out of the given cidr (clusterNetworkCIDR), which allows for 510 (2^(32 - 23) - 2) pod IPs addresses. If you are required to provide access to nodes from an external network, configure load balancers and routers to manage the traffic. | [optional] 
**service_network_cidr** | **str** | The IP address pool to use for service IP addresses. You can enter only one IP address pool. If you need to access the services from an external network, configure load balancers and routers to manage the traffic. | [optional] 
**api_vip** | **str** | (DEPRECATED) The virtual IP used to reach the OpenShift cluster&#39;s API. | [optional] 
**api_vips** | [**List[ApiVip]**](ApiVip.md) | The virtual IPs used to reach the OpenShift cluster&#39;s API. Enter one IP address for single-stack clusters, or up to two for dual-stack clusters (at most one IP address per IP stack used). The order of stacks should be the same as order of subnets in Cluster Networks, Service Networks, and Machine Networks. | [optional] 
**ingress_vip** | **str** | (DEPRECATED) The virtual IP used for cluster ingress traffic. | [optional] 
**ingress_vips** | [**List[IngressVip]**](IngressVip.md) | The virtual IPs used for cluster ingress traffic. Enter one IP address for single-stack clusters, or up to two for dual-stack clusters (at most one IP address per IP stack used). The order of stacks should be the same as order of subnets in Cluster Networks, Service Networks, and Machine Networks. | [optional] 
**api_vip_dns_name** | **str** | The domain name used to reach the OpenShift cluster API. | [optional] 
**machine_network_cidr** | **str** | A CIDR that all hosts belonging to the cluster should have an interfaces with IP address that belongs to this CIDR. The api_vip belongs to this CIDR. | [optional] 
**pull_secret** | **str** | The pull secret obtained from Red Hat OpenShift Cluster Manager at console.redhat.com/openshift/install/pull-secret. | [optional] 
**ssh_public_key** | **str** | SSH public key for debugging OpenShift nodes. | [optional] 
**vip_dhcp_allocation** | **bool** | Indicate if virtual IP DHCP allocation mode is enabled. | [optional] 
**http_proxy** | **str** | A proxy URL to use for creating HTTP connections outside the cluster. http://\\&lt;username\\&gt;:\\&lt;pswd\\&gt;@\\&lt;ip\\&gt;:\\&lt;port\\&gt;  | [optional] 
**https_proxy** | **str** | A proxy URL to use for creating HTTPS connections outside the cluster. http://\\&lt;username\\&gt;:\\&lt;pswd\\&gt;@\\&lt;ip\\&gt;:\\&lt;port\\&gt;  | [optional] 
**no_proxy** | **str** | An \&quot;*\&quot; or a comma-separated list of destination domain names, domains, IP addresses, or other network CIDRs to exclude from proxying. | [optional] 
**user_managed_networking** | **bool** | (DEPRECATED) Indicate if the networking is managed by the user. | [optional] 
**additional_ntp_source** | **str** | A comma-separated list of NTP sources (name or IP) going to be added to all the hosts. | [optional] 
**olm_operators** | [**List[OperatorCreateParams]**](OperatorCreateParams.md) | List of OLM operators to be installed. | [optional] 
**hyperthreading** | **str** | Enable/disable hyperthreading on master nodes, worker nodes, or all nodes. | [optional] 
**network_type** | **str** | The desired network type used. | [optional] 
**schedulable_masters** | **bool** | Schedule workloads on masters | [optional] [default to False]
**cluster_networks** | [**List[ClusterNetwork]**](ClusterNetwork.md) | Cluster networks that are associated with this cluster. | [optional] 
**service_networks** | [**List[ServiceNetwork]**](ServiceNetwork.md) | Service networks that are associated with this cluster. | [optional] 
**machine_networks** | [**List[MachineNetwork]**](MachineNetwork.md) | Machine networks that are associated with this cluster. | [optional] 
**disk_encryption** | [**DiskEncryption**](DiskEncryption.md) |  | [optional] 
**ignition_endpoint** | [**IgnitionEndpoint**](IgnitionEndpoint.md) |  | [optional] 
**tags** | **str** | A comma-separated list of tags that are associated to the cluster. | [optional] 

## Example

```python
from openshift_assisted_service.models.v2_cluster_update_params import V2ClusterUpdateParams

# TODO update the JSON string below
json = "{}"
# create an instance of V2ClusterUpdateParams from a JSON string
v2_cluster_update_params_instance = V2ClusterUpdateParams.from_json(json)
# print the JSON string representation of the object
print V2ClusterUpdateParams.to_json()

# convert the object into a dict
v2_cluster_update_params_dict = v2_cluster_update_params_instance.to_dict()
# create an instance of V2ClusterUpdateParams from a dict
v2_cluster_update_params_form_dict = v2_cluster_update_params.from_dict(v2_cluster_update_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


