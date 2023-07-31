# Cluster


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;Cluster&#39; if this is a complete object, &#39;AddHostsCluster&#39; for cluster that add hosts to existing OCP cluster,  | 
**high_availability_mode** | **str** | Guaranteed availability of the installed cluster. &#39;Full&#39; installs a Highly-Available cluster over multiple master nodes whereas &#39;None&#39; installs a full cluster over one node.  | [optional] [default to 'Full']
**id** | **str** | Unique identifier of the object. | 
**href** | **str** | Self link. | 
**name** | **str** | Name of the OpenShift cluster. | [optional] 
**user_name** | **str** |  | [optional] 
**org_id** | **str** |  | [optional] 
**email_domain** | **str** |  | [optional] 
**openshift_version** | **str** | Version of the OpenShift cluster. | [optional] 
**ocp_release_image** | **str** | OpenShift release image URI. | [optional] 
**openshift_cluster_id** | **str** | Cluster ID on OCP system. | [optional] 
**image_info** | [**ImageInfo**](ImageInfo.md) |  | 
**platform** | [**Platform**](Platform.md) |  | [optional] 
**base_dns_domain** | **str** | Base domain of the cluster. All DNS records must be sub-domains of this base and include the cluster name. | [optional] 
**cluster_network_cidr** | **str** | IP address block from which Pod IPs are allocated. This block must not overlap with existing physical networks. These IP addresses are used for the Pod network, and if you need to access the Pods from an external network, configure load balancers and routers to manage the traffic. | [optional] 
**cluster_network_host_prefix** | **int** | The subnet prefix length to assign to each individual node. For example, if clusterNetworkHostPrefix is set to 23, then each node is assigned a /23 subnet out of the given cidr (clusterNetworkCIDR), which allows for 510 (2^(32 - 23) - 2) pod IPs addresses. If you are required to provide access to nodes from an external network, configure load balancers and routers to manage the traffic. | [optional] 
**service_network_cidr** | **str** | The IP address pool to use for service IP addresses. You can enter only one IP address pool. If you need to access the services from an external network, configure load balancers and routers to manage the traffic. | [optional] 
**api_vip** | **str** | (DEPRECATED) The virtual IP used to reach the OpenShift cluster&#39;s API. | [optional] 
**api_vips** | [**List[ApiVip]**](ApiVip.md) | The virtual IPs used to reach the OpenShift cluster&#39;s API. Enter one IP address for single-stack clusters, or up to two for dual-stack clusters (at most one IP address per IP stack used). The order of stacks should be the same as order of subnets in Cluster Networks, Service Networks, and Machine Networks. | [optional] 
**api_vip_dns_name** | **str** | The domain name used to reach the OpenShift cluster API. | [optional] 
**machine_network_cidr** | **str** | A CIDR that all hosts belonging to the cluster should have an interfaces with IP address that belongs to this CIDR. The api_vip belongs to this CIDR. | [optional] 
**ingress_vip** | **str** | (DEPRECATED) The virtual IP used for cluster ingress traffic. | [optional] 
**ingress_vips** | [**List[IngressVip]**](IngressVip.md) | The virtual IPs used for cluster ingress traffic. Enter one IP address for single-stack clusters, or up to two for dual-stack clusters (at most one IP address per IP stack used). The order of stacks should be the same as order of subnets in Cluster Networks, Service Networks, and Machine Networks. | [optional] 
**ssh_public_key** | **str** | SSH public key for debugging OpenShift nodes. | [optional] 
**http_proxy** | **str** | A proxy URL to use for creating HTTP connections outside the cluster. http://\\&lt;username\\&gt;:\\&lt;pswd\\&gt;@\\&lt;ip\\&gt;:\\&lt;port\\&gt;  | [optional] 
**https_proxy** | **str** | A proxy URL to use for creating HTTPS connections outside the cluster. http://\\&lt;username\\&gt;:\\&lt;pswd\\&gt;@\\&lt;ip\\&gt;:\\&lt;port\\&gt;  | [optional] 
**no_proxy** | **str** | A comma-separated list of destination domain names, domains, IP addresses, or other network CIDRs to exclude from proxying. | [optional] 
**status** | **str** | Status of the OpenShift cluster. | 
**status_info** | **str** | Additional information pertaining to the status of the OpenShift cluster. | 
**status_updated_at** | **datetime** | The last time that the cluster status was updated. | [optional] 
**progress** | [**ClusterProgressInfo**](ClusterProgressInfo.md) |  | [optional] 
**disk_encryption** | [**DiskEncryption**](DiskEncryption.md) |  | [optional] 
**hosts** | [**List[Host]**](Host.md) | Hosts that are associated with this cluster. | [optional] 
**ready_host_count** | **int** | hosts associated to this cluster that are in &#39;known&#39; state. | [optional] 
**enabled_host_count** | **int** | hosts associated to this cluster that are not in &#39;disabled&#39; state. | [optional] 
**total_host_count** | **int** | All hosts associated to this cluster. | [optional] 
**schedulable_masters** | **bool** | Schedule workloads on masters | [optional] [default to False]
**schedulable_masters_forced_true** | **bool** | Indicates if schedule workloads on masters will be enabled regardless the value of &#39;schedulable_masters&#39; property. Set to &#39;true&#39; when not enough hosts are associated with this cluster to disable the scheduling on masters.  | [optional] [default to True]
**updated_at** | **datetime** | The last time that this cluster was updated. | [optional] 
**created_at** | **datetime** | The time that this cluster was created. | [optional] 
**install_started_at** | **datetime** | The time that this cluster started installation. | [optional] 
**install_completed_at** | **datetime** | The time that this cluster completed installation. | [optional] 
**host_networks** | [**List[HostNetwork]**](HostNetwork.md) | List of host networks to be filled during query. | [optional] 
**pull_secret_set** | **bool** | True if the pull secret has been added to the cluster. | [optional] 
**vip_dhcp_allocation** | **bool** | Indicate if virtual IP DHCP allocation mode is enabled. | [optional] 
**validations_info** | **str** | JSON-formatted string containing the validation results for each validation id grouped by category (network, hosts-data, etc.) | [optional] 
**logs_info** | [**LogsState**](LogsState.md) |  | [optional] 
**install_config_overrides** | **str** | JSON-formatted string containing the user overrides for the install-config.yaml file. | [optional] 
**controller_logs_collected_at** | **datetime** |  | [optional] 
**controller_logs_started_at** | **datetime** |  | [optional] 
**connectivity_majority_groups** | **str** | Json formatted string containing the majority groups for connectivity checks. | [optional] 
**ip_collisions** | **str** | Json formatted string containing ip collisions detected in the cluster. | [optional] 
**ignored_host_validations** | **str** | Json formatted string containing a list of host validations to be ignored. May also contain a list with a single string \&quot;all\&quot; to ignore all host validations. Some validations cannot be ignored. | [optional] 
**ignored_cluster_validations** | **str** | Json formatted string containing a list of cluster validations to be ignored. May also contain a list with a single string \&quot;all\&quot; to ignore all cluster validations. Some validations cannot be ignored. | [optional] 
**deleted_at** | **object** | swagger:ignore | [optional] 
**user_managed_networking** | **bool** | (DEPRECATED) Indicate if the networking is managed by the user. | [optional] 
**additional_ntp_source** | **str** | A comma-separated list of NTP sources (name or IP) going to be added to all the hosts. | [optional] 
**monitored_operators** | [**List[MonitoredOperator]**](MonitoredOperator.md) | Operators that are associated with this cluster. | [optional] 
**ams_subscription_id** | **str** | Unique identifier of the AMS subscription in OCM. | [optional] 
**hyperthreading** | **str** | Enable/disable hyperthreading on master nodes, worker nodes, or all nodes | [optional] 
**feature_usage** | **str** | JSON-formatted string containing the usage information by feature name | [optional] 
**network_type** | **str** | The desired network type used. | [optional] 
**cluster_networks** | [**List[ClusterNetwork]**](ClusterNetwork.md) | Cluster networks that are associated with this cluster. | [optional] 
**service_networks** | [**List[ServiceNetwork]**](ServiceNetwork.md) | Service networks that are associated with this cluster. | [optional] 
**machine_networks** | [**List[MachineNetwork]**](MachineNetwork.md) | Machine networks that are associated with this cluster. | [optional] 
**cpu_architecture** | **str** | The CPU architecture of the image (x86_64/arm64/etc). | [optional] [default to 'x86_64']
**ignition_endpoint** | [**IgnitionEndpoint**](IgnitionEndpoint.md) |  | [optional] 
**imported** | **bool** | Indicates whether this cluster is an imported day-2 cluster or a regular cluster. Clusters are considered imported when they are created via the ../clusters/import endpoint. Day-2 clusters converted from day-1 clusters by kube-api controllers or the ../clusters/&lt;cluster_id&gt;/actions/allow-add-hosts endpoint are not considered imported. Imported clusters usually lack a lot of information and are filled with default values that don&#39;t necessarily reflect the actual cluster they represent | [optional] [default to False]
**tags** | **str** | A comma-separated list of tags that are associated to the cluster. | [optional] 

## Example

```python
from openshift_assisted_service.models.cluster import Cluster

# TODO update the JSON string below
json = "{}"
# create an instance of Cluster from a JSON string
cluster_instance = Cluster.from_json(json)
# print the JSON string representation of the object
print Cluster.to_json()

# convert the object into a dict
cluster_dict = cluster_instance.to_dict()
# create an instance of Cluster from a dict
cluster_form_dict = cluster.from_dict(cluster_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


