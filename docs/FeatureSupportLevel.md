# FeatureSupportLevel

(DEPRECATED) List of features attached to openshift version

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**openshift_version** | **str** | Version of the OpenShift cluster. | [optional] 
**features** | [**List[FeatureSupportLevelFeaturesInner]**](FeatureSupportLevelFeaturesInner.md) |  | [optional] 

## Example

```python
from openshift_assisted_service.models.feature_support_level import FeatureSupportLevel

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureSupportLevel from a JSON string
feature_support_level_instance = FeatureSupportLevel.from_json(json)
# print the JSON string representation of the object
print FeatureSupportLevel.to_json()

# convert the object into a dict
feature_support_level_dict = feature_support_level_instance.to_dict()
# create an instance of FeatureSupportLevel from a dict
feature_support_level_form_dict = feature_support_level.from_dict(feature_support_level_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


