# FreeNetworkAddresses


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network** | **str** |  | [optional] 
**free_addresses** | **List[str]** |  | [optional] 

## Example

```python
from openshift_assisted_service.models.free_network_addresses import FreeNetworkAddresses

# TODO update the JSON string below
json = "{}"
# create an instance of FreeNetworkAddresses from a JSON string
free_network_addresses_instance = FreeNetworkAddresses.from_json(json)
# print the JSON string representation of the object
print FreeNetworkAddresses.to_json()

# convert the object into a dict
free_network_addresses_dict = free_network_addresses_instance.to_dict()
# create an instance of FreeNetworkAddresses from a dict
free_network_addresses_form_dict = free_network_addresses.from_dict(free_network_addresses_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


