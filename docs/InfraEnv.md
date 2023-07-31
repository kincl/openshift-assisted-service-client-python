# InfraEnv


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. | 
**id** | **str** | Unique identifier of the object. | 
**href** | **str** | Self link. | 
**openshift_version** | **str** | Version of the OpenShift cluster (used to infer the RHCOS version - temporary until generic logic implemented). | [optional] 
**name** | **str** | Name of the infra-env. | 
**user_name** | **str** |  | [optional] 
**org_id** | **str** |  | [optional] 
**email_domain** | **str** |  | [optional] 
**proxy** | [**Proxy**](Proxy.md) |  | [optional] 
**additional_ntp_sources** | **str** | A comma-separated list of NTP sources (name or IP) going to be added to all the hosts. | [optional] 
**ssh_authorized_key** | **str** | SSH public key for debugging the installation. | [optional] 
**pull_secret_set** | **bool** | True if the pull secret has been added to the cluster. | [optional] 
**static_network_config** | **str** | static network configuration string in the format expected by discovery ignition generation. | [optional] 
**type** | [**ImageType**](ImageType.md) |  | 
**ignition_config_override** | **str** | Json formatted string containing the user overrides for the initial ignition config. | [optional] 
**cluster_id** | **str** | If set, all hosts that register will be associated with the specified cluster. | [optional] 
**size_bytes** | **int** |  | [optional] 
**download_url** | **str** |  | [optional] 
**generator_version** | **str** | Image generator version. | [optional] 
**updated_at** | **datetime** | The last time that this infra-env was updated. | 
**created_at** | **datetime** |  | 
**expires_at** | **datetime** |  | [optional] 
**cpu_architecture** | **str** | The CPU architecture of the image (x86_64/arm64/etc). | [optional] [default to 'x86_64']
**kernel_arguments** | **str** | JSON formatted string array representing the discovery image kernel arguments. | [optional] 
**additional_trust_bundle** | **str** | PEM-encoded X.509 certificate bundle. Hosts discovered by this infra-env will trust the certificates in this bundle. Clusters formed from the hosts discovered by this infra-env will also trust the certificates in this bundle. | [optional] 

## Example

```python
from openshift_assisted_service.models.infra_env import InfraEnv

# TODO update the JSON string below
json = "{}"
# create an instance of InfraEnv from a JSON string
infra_env_instance = InfraEnv.from_json(json)
# print the JSON string representation of the object
print InfraEnv.to_json()

# convert the object into a dict
infra_env_dict = infra_env_instance.to_dict()
# create an instance of InfraEnv from a dict
infra_env_form_dict = infra_env.from_dict(infra_env_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


