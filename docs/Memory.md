# Memory


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**physical_bytes** | **int** |  | [optional] 
**usable_bytes** | **int** |  | [optional] 
**physical_bytes_method** | [**MemoryMethod**](MemoryMethod.md) |  | [optional] 

## Example

```python
from openshift_assisted_service.models.memory import Memory

# TODO update the JSON string below
json = "{}"
# create an instance of Memory from a JSON string
memory_instance = Memory.from_json(json)
# print the JSON string representation of the object
print Memory.to_json()

# convert the object into a dict
memory_dict = memory_instance.to_dict()
# create an instance of Memory from a dict
memory_form_dict = memory.from_dict(memory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


