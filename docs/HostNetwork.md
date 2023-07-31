# HostNetwork


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cidr** | **str** |  | [optional] 
**host_ids** | **List[str]** |  | [optional] 

## Example

```python
from openshift_assisted_service.models.host_network import HostNetwork

# TODO update the JSON string below
json = "{}"
# create an instance of HostNetwork from a JSON string
host_network_instance = HostNetwork.from_json(json)
# print the JSON string representation of the object
print HostNetwork.to_json()

# convert the object into a dict
host_network_dict = host_network_instance.to_dict()
# create an instance of HostNetwork from a dict
host_network_form_dict = host_network.from_dict(host_network_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


