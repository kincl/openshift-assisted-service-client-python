# InfraEnvUpdateParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**proxy** | [**Proxy**](Proxy.md) |  | [optional] 
**additional_ntp_sources** | **str** | A comma-separated list of NTP sources (name or IP) going to be added to all the hosts. | [optional] 
**ssh_authorized_key** | **str** | SSH public key for debugging the installation. | [optional] 
**pull_secret** | **str** | The pull secret obtained from Red Hat OpenShift Cluster Manager at console.redhat.com/openshift/install/pull-secret. | [optional] 
**static_network_config** | [**List[HostStaticNetworkConfig]**](HostStaticNetworkConfig.md) |  | [optional] 
**image_type** | [**ImageType**](ImageType.md) |  | [optional] 
**ignition_config_override** | **str** | JSON formatted string containing the user overrides for the initial ignition config. | [optional] 
**kernel_arguments** | [**List[KernelArgument]**](KernelArgument.md) | List of kernel arugment objects that define the operations and values to be applied. | [optional] 
**additional_trust_bundle** | **str** | Allows users to change the additional_trust_bundle infra-env field | [optional] 

## Example

```python
from openshift_assisted_service.models.infra_env_update_params import InfraEnvUpdateParams

# TODO update the JSON string below
json = "{}"
# create an instance of InfraEnvUpdateParams from a JSON string
infra_env_update_params_instance = InfraEnvUpdateParams.from_json(json)
# print the JSON string representation of the object
print InfraEnvUpdateParams.to_json()

# convert the object into a dict
infra_env_update_params_dict = infra_env_update_params_instance.to_dict()
# create an instance of InfraEnvUpdateParams from a dict
infra_env_update_params_form_dict = infra_env_update_params.from_dict(infra_env_update_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


