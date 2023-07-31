# HostProgressInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**installation_percentage** | **int** |  | [optional] 
**current_stage** | [**HostStage**](HostStage.md) |  | [optional] 
**progress_info** | **str** |  | [optional] 
**stage_started_at** | **datetime** | Time at which the current progress stage started. | [optional] 
**stage_updated_at** | **datetime** | Time at which the current progress stage was last updated. | [optional] 

## Example

```python
from openshift_assisted_service.models.host_progress_info import HostProgressInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostProgressInfo from a JSON string
host_progress_info_instance = HostProgressInfo.from_json(json)
# print the JSON string representation of the object
print HostProgressInfo.to_json()

# convert the object into a dict
host_progress_info_dict = host_progress_info_instance.to_dict()
# create an instance of HostProgressInfo from a dict
host_progress_info_form_dict = host_progress_info.from_dict(host_progress_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


