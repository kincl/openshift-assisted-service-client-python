# OpenshiftVersion


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | Name of the version to be presented to the user. | 
**support_level** | **str** | Level of support of the version. | 
**default** | **bool** | Indication that the version is the recommended one. | [optional] 
**cpu_architectures** | **List[str]** | Available CPU architectures. | 

## Example

```python
from openshift_assisted_service.models.openshift_version import OpenshiftVersion

# TODO update the JSON string below
json = "{}"
# create an instance of OpenshiftVersion from a JSON string
openshift_version_instance = OpenshiftVersion.from_json(json)
# print the JSON string representation of the object
print OpenshiftVersion.to_json()

# convert the object into a dict
openshift_version_dict = openshift_version_instance.to_dict()
# create an instance of OpenshiftVersion from a dict
openshift_version_form_dict = openshift_version.from_dict(openshift_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


