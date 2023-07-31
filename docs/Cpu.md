# Cpu


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**frequency** | **float** |  | [optional] 
**flags** | **List[str]** |  | [optional] 
**model_name** | **str** |  | [optional] 
**architecture** | **str** |  | [optional] 

## Example

```python
from openshift_assisted_service.models.cpu import Cpu

# TODO update the JSON string below
json = "{}"
# create an instance of Cpu from a JSON string
cpu_instance = Cpu.from_json(json)
# print the JSON string representation of the object
print Cpu.to_json()

# convert the object into a dict
cpu_dict = cpu_instance.to_dict()
# create an instance of Cpu from a dict
cpu_form_dict = cpu.from_dict(cpu_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


