# Error


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will always be &#39;Error&#39;. | 
**id** | **int** | Numeric identifier of the error. | 
**href** | **str** | Self link. | 
**code** | **str** | Globally unique code of the error, composed of the unique identifier of the API and the numeric identifier of the error. For example, if the numeric identifier of the error is 93 and the identifier of the API is assisted_install then the code will be ASSISTED-INSTALL-93. | 
**reason** | **str** | Human-readable description of the error. | 

## Example

```python
from openshift_assisted_service.models.error import Error

# TODO update the JSON string below
json = "{}"
# create an instance of Error from a JSON string
error_instance = Error.from_json(json)
# print the JSON string representation of the object
print Error.to_json()

# convert the object into a dict
error_dict = error_instance.to_dict()
# create an instance of Error from a dict
error_form_dict = error.from_dict(error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


