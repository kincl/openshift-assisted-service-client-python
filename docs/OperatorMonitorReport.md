# OperatorMonitorReport


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Unique name of the operator. | [optional] 
**version** | **str** | operator version. | [optional] 
**status** | [**OperatorStatus**](OperatorStatus.md) |  | [optional] 
**status_info** | **str** | Detailed information about the operator state. | [optional] 

## Example

```python
from openshift_assisted_service.models.operator_monitor_report import OperatorMonitorReport

# TODO update the JSON string below
json = "{}"
# create an instance of OperatorMonitorReport from a JSON string
operator_monitor_report_instance = OperatorMonitorReport.from_json(json)
# print the JSON string representation of the object
print OperatorMonitorReport.to_json()

# convert the object into a dict
operator_monitor_report_dict = operator_monitor_report_instance.to_dict()
# create an instance of OperatorMonitorReport from a dict
operator_monitor_report_form_dict = operator_monitor_report.from_dict(operator_monitor_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


