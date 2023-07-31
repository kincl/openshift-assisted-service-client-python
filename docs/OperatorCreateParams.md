# OperatorCreateParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**properties** | **str** | Blob of operator-dependent parameters that are required for installation. | [optional] 

## Example

```python
from openshift_assisted_service.models.operator_create_params import OperatorCreateParams

# TODO update the JSON string below
json = "{}"
# create an instance of OperatorCreateParams from a JSON string
operator_create_params_instance = OperatorCreateParams.from_json(json)
# print the JSON string representation of the object
print OperatorCreateParams.to_json()

# convert the object into a dict
operator_create_params_dict = operator_create_params_instance.to_dict()
# create an instance of OperatorCreateParams from a dict
operator_create_params_form_dict = operator_create_params.from_dict(operator_create_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


