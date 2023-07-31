# FeatureSupportLevelFeaturesInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature_id** | **str** | (DEPRECATED) The ID of the feature | 
**support_level** | [**SupportLevel**](SupportLevel.md) |  | 

## Example

```python
from openshift_assisted_service.models.feature_support_level_features_inner import FeatureSupportLevelFeaturesInner

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureSupportLevelFeaturesInner from a JSON string
feature_support_level_features_inner_instance = FeatureSupportLevelFeaturesInner.from_json(json)
# print the JSON string representation of the object
print FeatureSupportLevelFeaturesInner.to_json()

# convert the object into a dict
feature_support_level_features_inner_dict = feature_support_level_features_inner_instance.to_dict()
# create an instance of FeatureSupportLevelFeaturesInner from a dict
feature_support_level_features_inner_form_dict = feature_support_level_features_inner.from_dict(feature_support_level_features_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


