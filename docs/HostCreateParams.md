# HostCreateParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_id** | **str** |  | 
**discovery_agent_version** | **str** |  | [optional] 

## Example

```python
from openshift_assisted_service.models.host_create_params import HostCreateParams

# TODO update the JSON string below
json = "{}"
# create an instance of HostCreateParams from a JSON string
host_create_params_instance = HostCreateParams.from_json(json)
# print the JSON string representation of the object
print HostCreateParams.to_json()

# convert the object into a dict
host_create_params_dict = host_create_params_instance.to_dict()
# create an instance of HostCreateParams from a dict
host_create_params_form_dict = host_create_params.from_dict(host_create_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


