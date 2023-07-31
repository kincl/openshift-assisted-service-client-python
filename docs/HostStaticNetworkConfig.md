# HostStaticNetworkConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network_yaml** | **str** | yaml string that can be processed by nmstate | [optional] 
**mac_interface_map** | [**List[MacInterfaceMapInner]**](MacInterfaceMapInner.md) |  | [optional] 

## Example

```python
from openshift_assisted_service.models.host_static_network_config import HostStaticNetworkConfig

# TODO update the JSON string below
json = "{}"
# create an instance of HostStaticNetworkConfig from a JSON string
host_static_network_config_instance = HostStaticNetworkConfig.from_json(json)
# print the JSON string representation of the object
print HostStaticNetworkConfig.to_json()

# convert the object into a dict
host_static_network_config_dict = host_static_network_config_instance.to_dict()
# create an instance of HostStaticNetworkConfig from a dict
host_static_network_config_form_dict = host_static_network_config.from_dict(host_static_network_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


