# MachineNetwork

A network that all hosts belonging to the cluster should have an interface with IP address in. The VIPs (if exist) belong to this network.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **str** | The cluster that this network is associated with. | [optional] 
**cidr** | **str** |  | [optional] 

## Example

```python
from openshift_assisted_service.models.machine_network import MachineNetwork

# TODO update the JSON string below
json = "{}"
# create an instance of MachineNetwork from a JSON string
machine_network_instance = MachineNetwork.from_json(json)
# print the JSON string representation of the object
print MachineNetwork.to_json()

# convert the object into a dict
machine_network_dict = machine_network_instance.to_dict()
# create an instance of MachineNetwork from a dict
machine_network_form_dict = machine_network.from_dict(machine_network_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


