# ConnectivityReport


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**remote_hosts** | [**List[ConnectivityRemoteHost]**](ConnectivityRemoteHost.md) |  | [optional] 

## Example

```python
from openshift_assisted_service.models.connectivity_report import ConnectivityReport

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectivityReport from a JSON string
connectivity_report_instance = ConnectivityReport.from_json(json)
# print the JSON string representation of the object
print ConnectivityReport.to_json()

# convert the object into a dict
connectivity_report_dict = connectivity_report_instance.to_dict()
# create an instance of ConnectivityReport from a dict
connectivity_report_form_dict = connectivity_report.from_dict(connectivity_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


