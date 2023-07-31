# NtpSynchronizationResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ntp_sources** | [**List[NtpSource]**](NtpSource.md) |  | [optional] 

## Example

```python
from openshift_assisted_service.models.ntp_synchronization_response import NtpSynchronizationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NtpSynchronizationResponse from a JSON string
ntp_synchronization_response_instance = NtpSynchronizationResponse.from_json(json)
# print the JSON string representation of the object
print NtpSynchronizationResponse.to_json()

# convert the object into a dict
ntp_synchronization_response_dict = ntp_synchronization_response_instance.to_dict()
# create an instance of NtpSynchronizationResponse from a dict
ntp_synchronization_response_form_dict = ntp_synchronization_response.from_dict(ntp_synchronization_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


