# L2Connectivity


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**outgoing_nic** | **str** |  | [optional] 
**outgoing_ip_address** | **str** |  | [optional] 
**remote_ip_address** | **str** |  | [optional] 
**remote_mac** | **str** |  | [optional] 
**successful** | **bool** |  | [optional] 

## Example

```python
from openshift_assisted_service.models.l2_connectivity import L2Connectivity

# TODO update the JSON string below
json = "{}"
# create an instance of L2Connectivity from a JSON string
l2_connectivity_instance = L2Connectivity.from_json(json)
# print the JSON string representation of the object
print L2Connectivity.to_json()

# convert the object into a dict
l2_connectivity_dict = l2_connectivity_instance.to_dict()
# create an instance of L2Connectivity from a dict
l2_connectivity_form_dict = l2_connectivity.from_dict(l2_connectivity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


