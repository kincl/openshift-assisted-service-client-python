# ClusterProgressInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_percentage** | **int** |  | [optional] 
**preparing_for_installation_stage_percentage** | **int** |  | [optional] 
**installing_stage_percentage** | **int** |  | [optional] 
**finalizing_stage_percentage** | **int** |  | [optional] 

## Example

```python
from openshift_assisted_service.models.cluster_progress_info import ClusterProgressInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterProgressInfo from a JSON string
cluster_progress_info_instance = ClusterProgressInfo.from_json(json)
# print the JSON string representation of the object
print ClusterProgressInfo.to_json()

# convert the object into a dict
cluster_progress_info_dict = cluster_progress_info_instance.to_dict()
# create an instance of ClusterProgressInfo from a dict
cluster_progress_info_form_dict = cluster_progress_info.from_dict(cluster_progress_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


