# VersionedHostRequirements


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | Version of the component for which requirements are defined | [optional] 
**master** | [**ClusterHostRequirementsDetails**](ClusterHostRequirementsDetails.md) |  | [optional] 
**worker** | [**ClusterHostRequirementsDetails**](ClusterHostRequirementsDetails.md) |  | [optional] 
**sno** | [**ClusterHostRequirementsDetails**](ClusterHostRequirementsDetails.md) |  | [optional] 
**edge_worker** | [**ClusterHostRequirementsDetails**](ClusterHostRequirementsDetails.md) |  | [optional] 

## Example

```python
from openshift_assisted_service.models.versioned_host_requirements import VersionedHostRequirements

# TODO update the JSON string below
json = "{}"
# create an instance of VersionedHostRequirements from a JSON string
versioned_host_requirements_instance = VersionedHostRequirements.from_json(json)
# print the JSON string representation of the object
print VersionedHostRequirements.to_json()

# convert the object into a dict
versioned_host_requirements_dict = versioned_host_requirements_instance.to_dict()
# create an instance of VersionedHostRequirements from a dict
versioned_host_requirements_form_dict = versioned_host_requirements.from_dict(versioned_host_requirements_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


