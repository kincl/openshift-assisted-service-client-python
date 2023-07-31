# NodeLabelParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key for the label&#39;s key-value pair. | 
**value** | **str** | The value for the label&#39;s key-value pair. | 

## Example

```python
from openshift_assisted_service.models.node_label_params import NodeLabelParams

# TODO update the JSON string below
json = "{}"
# create an instance of NodeLabelParams from a JSON string
node_label_params_instance = NodeLabelParams.from_json(json)
# print the JSON string representation of the object
print NodeLabelParams.to_json()

# convert the object into a dict
node_label_params_dict = node_label_params_instance.to_dict()
# create an instance of NodeLabelParams from a dict
node_label_params_form_dict = node_label_params.from_dict(node_label_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


