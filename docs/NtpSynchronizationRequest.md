# NtpSynchronizationRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ntp_source** | **str** | A comma-separated list of NTP sources (name or IP) going to be added to all the hosts. | 

## Example

```python
from openshift_assisted_service.models.ntp_synchronization_request import NtpSynchronizationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NtpSynchronizationRequest from a JSON string
ntp_synchronization_request_instance = NtpSynchronizationRequest.from_json(json)
# print the JSON string representation of the object
print NtpSynchronizationRequest.to_json()

# convert the object into a dict
ntp_synchronization_request_dict = ntp_synchronization_request_instance.to_dict()
# create an instance of NtpSynchronizationRequest from a dict
ntp_synchronization_request_form_dict = ntp_synchronization_request.from_dict(ntp_synchronization_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


