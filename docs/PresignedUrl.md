# PresignedUrl


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | Pre-signed URL for downloading the infra-env discovery image. | 
**expires_at** | **datetime** | Expiration time for the URL token. | [optional] 

## Example

```python
from openshift_assisted_service.models.presigned_url import PresignedUrl

# TODO update the JSON string below
json = "{}"
# create an instance of PresignedUrl from a JSON string
presigned_url_instance = PresignedUrl.from_json(json)
# print the JSON string representation of the object
print PresignedUrl.to_json()

# convert the object into a dict
presigned_url_dict = presigned_url_instance.to_dict()
# create an instance of PresignedUrl from a dict
presigned_url_form_dict = presigned_url.from_dict(presigned_url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


