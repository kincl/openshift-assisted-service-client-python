# ConnectivityCheckHost


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_id** | **str** |  | [optional] 
**nics** | [**List[ConnectivityCheckNic]**](ConnectivityCheckNic.md) |  | [optional] 

## Example

```python
from openshift_assisted_service.models.connectivity_check_host import ConnectivityCheckHost

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectivityCheckHost from a JSON string
connectivity_check_host_instance = ConnectivityCheckHost.from_json(json)
# print the JSON string representation of the object
print ConnectivityCheckHost.to_json()

# convert the object into a dict
connectivity_check_host_dict = connectivity_check_host_instance.to_dict()
# create an instance of ConnectivityCheckHost from a dict
connectivity_check_host_form_dict = connectivity_check_host.from_dict(connectivity_check_host_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


