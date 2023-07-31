# ClusterCreateParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the OpenShift cluster. | 
**high_availability_mode** | **str** | Guaranteed availability of the installed cluster. &#39;Full&#39; installs a Highly-Available cluster over multiple master nodes whereas &#39;None&#39; installs a full cluster over one node.  | [optional] [default to 'Full']
**openshift_version** | **str** | Version of the OpenShift cluster. | 
**ocp_release_image** | **str** | OpenShift release image URI. | [optional] 
**base_dns_domain** | **str** | Base domain of the cluster. All DNS records must be sub-domains of this base and include the cluster name. | [optional] 
**cluster_network_cidr** | **str** | IP address block from which Pod IPs are allocated. This block must not overlap with existing physical networks. These IP addresses are used for the Pod network, and if you need to access the Pods from an external network, configure load balancers and routers to manage the traffic. | [optional] [default to '10.128.0.0/14']
**cluster_network_host_prefix** | **int** | The subnet prefix length to assign to each individual node. For example, if clusterNetworkHostPrefix is set to 23, then each node is assigned a /23 subnet out of the given cidr (clusterNetworkCIDR), which allows for 510 (2^(32 - 23) - 2) pod IPs addresses. If you are required to provide access to nodes from an external network, configure load balancers and routers to manage the traffic. | [optional] 
**service_network_cidr** | **str** | The IP address pool to use for service IP addresses. You can enter only one IP address pool. If you need to access the services from an external network, configure load balancers and routers to manage the traffic. | [optional] [default to '172.30.0.0/16']
**api_vip** | **str** | (DEPRECATED) The virtual IP used to reach the OpenShift cluster&#39;s API. | [optional] 
**api_vips** | [**List[ApiVip]**](ApiVip.md) | The virtual IPs used to reach the OpenShift cluster&#39;s API. Enter one IP address for single-stack clusters, or up to two for dual-stack clusters (at most one IP address per IP stack used). The order of stacks should be the same as order of subnets in Cluster Networks, Service Networks, and Machine Networks. | [optional] 
**ingress_vip** | **str** | (DEPRECATED) The virtual IP used for cluster ingress traffic. | [optional] 
**ingress_vips** | [**List[IngressVip]**](IngressVip.md) | The virtual IPs used for cluster ingress traffic. Enter one IP address for single-stack clusters, or up to two for dual-stack clusters (at most one IP address per IP stack used). The order of stacks should be the same as order of subnets in Cluster Networks, Service Networks, and Machine Networks. | [optional] 
**pull_secret** | **str** | The pull secret obtained from Red Hat OpenShift Cluster Manager at console.redhat.com/openshift/install/pull-secret. | 
**ssh_public_key** | **str** | SSH public key for debugging OpenShift nodes. | [optional] 
**vip_dhcp_allocation** | **bool** | Indicate if virtual IP DHCP allocation mode is enabled. | [optional] [default to False]
**http_proxy** | **str** | A proxy URL to use for creating HTTP connections outside the cluster. http://\\&lt;username\\&gt;:\\&lt;pswd\\&gt;@\\&lt;ip\\&gt;:\\&lt;port\\&gt;  | [optional] 
**https_proxy** | **str** | A proxy URL to use for creating HTTPS connections outside the cluster. http://\\&lt;username\\&gt;:\\&lt;pswd\\&gt;@\\&lt;ip\\&gt;:\\&lt;port\\&gt;  | [optional] 
**no_proxy** | **str** | An \&quot;*\&quot; or a comma-separated list of destination domain names, domains, IP addresses, or other network CIDRs to exclude from proxying. | [optional] 
**user_managed_networking** | **bool** | (DEPRECATED) Indicate if the networking is managed by the user. | [optional] [default to False]
**additional_ntp_source** | **str** | A comma-separated list of NTP sources (name or IP) going to be added to all the hosts. | [optional] 
**olm_operators** | [**List[OperatorCreateParams]**](OperatorCreateParams.md) | List of OLM operators to be installed. | [optional] 
**hyperthreading** | **str** | Enable/disable hyperthreading on master nodes, worker nodes, or all nodes. | [optional] [default to 'all']
**network_type** | **str** | The desired network type used. | [optional] 
**schedulable_masters** | **bool** | Schedule workloads on masters | [optional] [default to False]
**cluster_networks** | [**List[ClusterNetwork]**](ClusterNetwork.md) | Cluster networks that are associated with this cluster. | [optional] 
**service_networks** | [**List[ServiceNetwork]**](ServiceNetwork.md) | Service networks that are associated with this cluster. | [optional] 
**machine_networks** | [**List[MachineNetwork]**](MachineNetwork.md) | Machine networks that are associated with this cluster. | [optional] 
**platform** | [**Platform**](Platform.md) |  | [optional] 
**cpu_architecture** | **str** | The CPU architecture of the image (x86_64/arm64/etc). | [optional] [default to 'x86_64']
**disk_encryption** | [**DiskEncryption**](DiskEncryption.md) |  | [optional] 
**ignition_endpoint** | [**IgnitionEndpoint**](IgnitionEndpoint.md) |  | [optional] 
**tags** | **str** | A comma-separated list of tags that are associated to the cluster. | [optional] 

## Example

```python
from openshift_assisted_service.models.cluster_create_params import ClusterCreateParams

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterCreateParams from a JSON string
cluster_create_params_instance = ClusterCreateParams.from_json(json)
# print the JSON string representation of the object
print ClusterCreateParams.to_json()

# convert the object into a dict
cluster_create_params_dict = cluster_create_params_instance.to_dict()
# create an instance of ClusterCreateParams from a dict
cluster_create_params_form_dict = cluster_create_params.from_dict(cluster_create_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


