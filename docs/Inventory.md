# Inventory


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostname** | **str** |  | [optional] 
**bmc_address** | **str** |  | [optional] 
**interfaces** | [**List[Interface]**](Interface.md) |  | [optional] 
**disks** | [**List[Disk]**](Disk.md) |  | [optional] 
**boot** | [**Boot**](Boot.md) |  | [optional] 
**system_vendor** | [**SystemVendor**](SystemVendor.md) |  | [optional] 
**bmc_v6address** | **str** |  | [optional] 
**memory** | [**Memory**](Memory.md) |  | [optional] 
**cpu** | [**Cpu**](Cpu.md) |  | [optional] 
**gpus** | [**List[Gpu]**](Gpu.md) |  | [optional] 
**routes** | [**List[Route]**](Route.md) |  | [optional] 
**tpm_version** | **str** |  | [optional] 

## Example

```python
from openshift_assisted_service.models.inventory import Inventory

# TODO update the JSON string below
json = "{}"
# create an instance of Inventory from a JSON string
inventory_instance = Inventory.from_json(json)
# print the JSON string representation of the object
print Inventory.to_json()

# convert the object into a dict
inventory_dict = inventory_instance.to_dict()
# create an instance of Inventory from a dict
inventory_form_dict = inventory.from_dict(inventory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


