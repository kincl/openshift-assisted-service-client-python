# Interface


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ipv6_addresses** | **List[str]** |  | [optional] 
**vendor** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**has_carrier** | **bool** |  | [optional] 
**product** | **str** |  | [optional] 
**mtu** | **int** |  | [optional] 
**ipv4_addresses** | **List[str]** |  | [optional] 
**biosdevname** | **str** |  | [optional] 
**client_id** | **str** |  | [optional] 
**mac_address** | **str** |  | [optional] 
**flags** | **List[str]** |  | [optional] 
**speed_mbps** | **int** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from openshift_assisted_service.models.interface import Interface

# TODO update the JSON string below
json = "{}"
# create an instance of Interface from a JSON string
interface_instance = Interface.from_json(json)
# print the JSON string representation of the object
print Interface.to_json()

# convert the object into a dict
interface_dict = interface_instance.to_dict()
# create an instance of Interface from a dict
interface_form_dict = interface.from_dict(interface_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


