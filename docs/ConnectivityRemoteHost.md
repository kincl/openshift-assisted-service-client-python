# ConnectivityRemoteHost


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_id** | **str** |  | [optional] 
**l2_connectivity** | [**List[L2Connectivity]**](L2Connectivity.md) |  | [optional] 
**l3_connectivity** | [**List[L3Connectivity]**](L3Connectivity.md) |  | [optional] 

## Example

```python
from openshift_assisted_service.models.connectivity_remote_host import ConnectivityRemoteHost

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectivityRemoteHost from a JSON string
connectivity_remote_host_instance = ConnectivityRemoteHost.from_json(json)
# print the JSON string representation of the object
print ConnectivityRemoteHost.to_json()

# convert the object into a dict
connectivity_remote_host_dict = connectivity_remote_host_instance.to_dict()
# create an instance of ConnectivityRemoteHost from a dict
connectivity_remote_host_form_dict = connectivity_remote_host.from_dict(connectivity_remote_host_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


