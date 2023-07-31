# OperatorProperty


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the property | [optional] 
**data_type** | **str** | Type of the property | [optional] 
**mandatory** | **bool** | Indicates whether the property is reqired | [optional] 
**options** | **List[str]** | Values to select from | [optional] 
**description** | **str** | Description of a property | [optional] 
**default_value** | **str** | Default value for the property | [optional] 

## Example

```python
from openshift_assisted_service.models.operator_property import OperatorProperty

# TODO update the JSON string below
json = "{}"
# create an instance of OperatorProperty from a JSON string
operator_property_instance = OperatorProperty.from_json(json)
# print the JSON string representation of the object
print OperatorProperty.to_json()

# convert the object into a dict
operator_property_dict = operator_property_instance.to_dict()
# create an instance of OperatorProperty from a dict
operator_property_form_dict = operator_property.from_dict(operator_property_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


