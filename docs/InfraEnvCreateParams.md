# InfraEnvCreateParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the infra-env. | 
**proxy** | [**Proxy**](Proxy.md) |  | [optional] 
**additional_ntp_sources** | **str** | A comma-separated list of NTP sources (name or IP) going to be added to all the hosts. | [optional] 
**ssh_authorized_key** | **str** | SSH public key for debugging the installation. | [optional] 
**pull_secret** | **str** | The pull secret obtained from Red Hat OpenShift Cluster Manager at console.redhat.com/openshift/install/pull-secret. | 
**static_network_config** | [**List[HostStaticNetworkConfig]**](HostStaticNetworkConfig.md) |  | [optional] 
**image_type** | [**ImageType**](ImageType.md) |  | [optional] 
**ignition_config_override** | **str** | JSON formatted string containing the user overrides for the initial ignition config. | [optional] 
**cluster_id** | **str** | If set, all hosts that register will be associated with the specified cluster. | [optional] 
**openshift_version** | **str** | Version of the OpenShift cluster (used to infer the RHCOS version - temporary until generic logic implemented). | [optional] 
**cpu_architecture** | **str** | The CPU architecture of the image (x86_64/arm64/etc). | [optional] [default to 'x86_64']
**kernel_arguments** | [**List[KernelArgument]**](KernelArgument.md) | List of kernel arugment objects that define the operations and values to be applied. | [optional] 
**additional_trust_bundle** | **str** | PEM-encoded X.509 certificate bundle. Hosts discovered by this infra-env will trust the certificates in this bundle. Clusters formed from the hosts discovered by this infra-env will also trust the certificates in this bundle. | [optional] 

## Example

```python
from openshift_assisted_service.models.infra_env_create_params import InfraEnvCreateParams

# TODO update the JSON string below
json = "{}"
# create an instance of InfraEnvCreateParams from a JSON string
infra_env_create_params_instance = InfraEnvCreateParams.from_json(json)
# print the JSON string representation of the object
print InfraEnvCreateParams.to_json()

# convert the object into a dict
infra_env_create_params_dict = infra_env_create_params_instance.to_dict()
# create an instance of InfraEnvCreateParams from a dict
infra_env_create_params_form_dict = infra_env_create_params.from_dict(infra_env_create_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


