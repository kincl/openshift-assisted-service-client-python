# MacInterfaceMapInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mac_address** | **str** | mac address present on the host | [optional] 
**logical_nic_name** | **str** | nic name used in the yaml, which relates 1:1 to the mac address | [optional] 

## Example

```python
from openshift_assisted_service.models.mac_interface_map_inner import MacInterfaceMapInner

# TODO update the JSON string below
json = "{}"
# create an instance of MacInterfaceMapInner from a JSON string
mac_interface_map_inner_instance = MacInterfaceMapInner.from_json(json)
# print the JSON string representation of the object
print MacInterfaceMapInner.to_json()

# convert the object into a dict
mac_interface_map_inner_dict = mac_interface_map_inner_instance.to_dict()
# create an instance of MacInterfaceMapInner from a dict
mac_interface_map_inner_form_dict = mac_interface_map_inner.from_dict(mac_interface_map_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


