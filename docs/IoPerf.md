# IoPerf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sync_duration** | **int** | 99th percentile of fsync duration in milliseconds | [optional] 

## Example

```python
from openshift_assisted_service.models.io_perf import IoPerf

# TODO update the JSON string below
json = "{}"
# create an instance of IoPerf from a JSON string
io_perf_instance = IoPerf.from_json(json)
# print the JSON string representation of the object
print IoPerf.to_json()

# convert the object into a dict
io_perf_dict = io_perf_instance.to_dict()
# create an instance of IoPerf from a dict
io_perf_form_dict = io_perf.from_dict(io_perf_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


