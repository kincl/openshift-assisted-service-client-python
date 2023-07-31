# HostProgress


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_stage** | [**HostStage**](HostStage.md) |  | [optional] 
**progress_info** | **str** |  | [optional] 

## Example

```python
from openshift_assisted_service.models.host_progress import HostProgress

# TODO update the JSON string below
json = "{}"
# create an instance of HostProgress from a JSON string
host_progress_instance = HostProgress.from_json(json)
# print the JSON string representation of the object
print HostProgress.to_json()

# convert the object into a dict
host_progress_dict = host_progress_instance.to_dict()
# create an instance of HostProgress from a dict
host_progress_form_dict = host_progress.from_dict(host_progress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


