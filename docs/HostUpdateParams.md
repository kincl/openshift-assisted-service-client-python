# HostUpdateParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_role** | **str** |  | [optional] 
**host_name** | **str** |  | [optional] 
**disks_selected_config** | [**List[DiskConfigParams]**](DiskConfigParams.md) |  | [optional] 
**disks_skip_formatting** | [**List[DiskSkipFormattingParams]**](DiskSkipFormattingParams.md) | Allows changing the host&#39;s skip_formatting_disks parameter | [optional] 
**machine_config_pool_name** | **str** |  | [optional] 
**ignition_endpoint_token** | **str** | A string which will be used as Authorization Bearer token to fetch the ignition from ignition_endpoint_url. | [optional] 
**node_labels** | [**List[NodeLabelParams]**](NodeLabelParams.md) | Labels to be added to the corresponding node. | [optional] 

## Example

```python
from openshift_assisted_service.models.host_update_params import HostUpdateParams

# TODO update the JSON string below
json = "{}"
# create an instance of HostUpdateParams from a JSON string
host_update_params_instance = HostUpdateParams.from_json(json)
# print the JSON string representation of the object
print HostUpdateParams.to_json()

# convert the object into a dict
host_update_params_dict = host_update_params_instance.to_dict()
# create an instance of HostUpdateParams from a dict
host_update_params_form_dict = host_update_params.from_dict(host_update_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


