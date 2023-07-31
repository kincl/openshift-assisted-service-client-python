# ListVersions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**versions** | **Dict[str, str]** |  | [optional] 
**release_tag** | **str** |  | [optional] 

## Example

```python
from openshift_assisted_service.models.list_versions import ListVersions

# TODO update the JSON string below
json = "{}"
# create an instance of ListVersions from a JSON string
list_versions_instance = ListVersions.from_json(json)
# print the JSON string representation of the object
print ListVersions.to_json()

# convert the object into a dict
list_versions_dict = list_versions_instance.to_dict()
# create an instance of ListVersions from a dict
list_versions_form_dict = list_versions.from_dict(list_versions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


