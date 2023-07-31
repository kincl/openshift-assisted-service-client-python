# ClusterHostRequirements


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_id** | **str** | Unique identifier of the host the requirements relate to. | [optional] 
**total** | [**ClusterHostRequirementsDetails**](ClusterHostRequirementsDetails.md) |  | [optional] 
**ocp** | [**ClusterHostRequirementsDetails**](ClusterHostRequirementsDetails.md) |  | [optional] 
**operators** | [**List[OperatorHostRequirements]**](OperatorHostRequirements.md) | Host requirements related to requested operators | [optional] 

## Example

```python
from openshift_assisted_service.models.cluster_host_requirements import ClusterHostRequirements

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterHostRequirements from a JSON string
cluster_host_requirements_instance = ClusterHostRequirements.from_json(json)
# print the JSON string representation of the object
print ClusterHostRequirements.to_json()

# convert the object into a dict
cluster_host_requirements_dict = cluster_host_requirements_instance.to_dict()
# create an instance of ClusterHostRequirements from a dict
cluster_host_requirements_form_dict = cluster_host_requirements.from_dict(cluster_host_requirements_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


