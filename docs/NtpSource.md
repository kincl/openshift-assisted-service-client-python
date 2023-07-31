# NtpSource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_name** | **str** | NTP source name or IP. | [optional] 
**source_state** | [**SourceState**](SourceState.md) |  | [optional] 

## Example

```python
from openshift_assisted_service.models.ntp_source import NtpSource

# TODO update the JSON string below
json = "{}"
# create an instance of NtpSource from a JSON string
ntp_source_instance = NtpSource.from_json(json)
# print the JSON string representation of the object
print NtpSource.to_json()

# convert the object into a dict
ntp_source_dict = ntp_source_instance.to_dict()
# create an instance of NtpSource from a dict
ntp_source_form_dict = ntp_source.from_dict(ntp_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


