# ConnectivityCheckNic


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**mac** | **str** |  | [optional] 
**ip_addresses** | **List[str]** |  | [optional] 

## Example

```python
from openshift_assisted_service.models.connectivity_check_nic import ConnectivityCheckNic

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectivityCheckNic from a JSON string
connectivity_check_nic_instance = ConnectivityCheckNic.from_json(json)
# print the JSON string representation of the object
print ConnectivityCheckNic.to_json()

# convert the object into a dict
connectivity_check_nic_dict = connectivity_check_nic_instance.to_dict()
# create an instance of ConnectivityCheckNic from a dict
connectivity_check_nic_form_dict = connectivity_check_nic.from_dict(connectivity_check_nic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


