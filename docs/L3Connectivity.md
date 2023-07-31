# L3Connectivity


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**outgoing_nic** | **str** |  | [optional] 
**remote_ip_address** | **str** |  | [optional] 
**successful** | **bool** |  | [optional] 
**average_rtt_ms** | **float** | Average round trip time in milliseconds. | [optional] 
**packet_loss_percentage** | **float** | Percentage of packets lost during connectivity check. | [optional] 

## Example

```python
from openshift_assisted_service.models.l3_connectivity import L3Connectivity

# TODO update the JSON string below
json = "{}"
# create an instance of L3Connectivity from a JSON string
l3_connectivity_instance = L3Connectivity.from_json(json)
# print the JSON string representation of the object
print L3Connectivity.to_json()

# convert the object into a dict
l3_connectivity_dict = l3_connectivity_instance.to_dict()
# create an instance of L3Connectivity from a dict
l3_connectivity_form_dict = l3_connectivity.from_dict(l3_connectivity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


