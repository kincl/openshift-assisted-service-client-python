# DhcpAllocationRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interface** | **str** | The network interface (NIC) to run the DHCP requests on. | 
**api_vip_mac** | **str** | MAC address for the API virtual IP. | 
**ingress_vip_mac** | **str** | MAC address for the Ingress virtual IP. | 
**api_vip_lease** | **str** | Contents of lease file to be used for API virtual IP. | [optional] 
**ingress_vip_lease** | **str** | Contents of lease file to be used for for Ingress virtual IP. | [optional] 

## Example

```python
from openshift_assisted_service.models.dhcp_allocation_request import DhcpAllocationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DhcpAllocationRequest from a JSON string
dhcp_allocation_request_instance = DhcpAllocationRequest.from_json(json)
# print the JSON string representation of the object
print DhcpAllocationRequest.to_json()

# convert the object into a dict
dhcp_allocation_request_dict = dhcp_allocation_request_instance.to_dict()
# create an instance of DhcpAllocationRequest from a dict
dhcp_allocation_request_form_dict = dhcp_allocation_request.from_dict(dhcp_allocation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


