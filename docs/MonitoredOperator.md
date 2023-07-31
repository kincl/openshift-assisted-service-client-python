# MonitoredOperator


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **str** | The cluster that this operator is associated with. | [optional] 
**name** | **str** | Unique name of the operator. | [optional] 
**version** | **str** | Operator version | [optional] 
**namespace** | **str** | Namespace where to deploy an operator. Only some operators require a namespace. | [optional] 
**subscription_name** | **str** | The name of the subscription of the operator. | [optional] 
**operator_type** | [**OperatorType**](OperatorType.md) |  | [optional] 
**properties** | **str** | Blob of operator-dependent parameters that are required for installation. | [optional] 
**timeout_seconds** | **int** | Positive number represents a timeout in seconds for the operator to be available. | [optional] 
**status** | [**OperatorStatus**](OperatorStatus.md) |  | [optional] 
**status_info** | **str** | Detailed information about the operator state. | [optional] 
**status_updated_at** | **datetime** | Time at which the operator was last updated. | [optional] 

## Example

```python
from openshift_assisted_service.models.monitored_operator import MonitoredOperator

# TODO update the JSON string below
json = "{}"
# create an instance of MonitoredOperator from a JSON string
monitored_operator_instance = MonitoredOperator.from_json(json)
# print the JSON string representation of the object
print MonitoredOperator.to_json()

# convert the object into a dict
monitored_operator_dict = monitored_operator_instance.to_dict()
# create an instance of MonitoredOperator from a dict
monitored_operator_form_dict = monitored_operator.from_dict(monitored_operator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


