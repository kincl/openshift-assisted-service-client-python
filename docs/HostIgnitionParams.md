# HostIgnitionParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **str** |  | [optional] 

## Example

```python
from openshift_assisted_service.models.host_ignition_params import HostIgnitionParams

# TODO update the JSON string below
json = "{}"
# create an instance of HostIgnitionParams from a JSON string
host_ignition_params_instance = HostIgnitionParams.from_json(json)
# print the JSON string representation of the object
print HostIgnitionParams.to_json()

# convert the object into a dict
host_ignition_params_dict = host_ignition_params_instance.to_dict()
# create an instance of HostIgnitionParams from a dict
host_ignition_params_form_dict = host_ignition_params.from_dict(host_ignition_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


