# DhcpAllocationResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_vip_address** | **str** | The IPv4 address that was allocated by DHCP for the API virtual IP. | 
**ingress_vip_address** | **str** | The IPv4 address that was allocated by DHCP for the Ingress virtual IP. | 
**api_vip_lease** | **str** | Contents of last acquired lease for API virtual IP. | [optional] 
**ingress_vip_lease** | **str** | Contents of last acquired lease for Ingress virtual IP. | [optional] 

## Example

```python
from openshift_assisted_service.models.dhcp_allocation_response import DhcpAllocationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DhcpAllocationResponse from a JSON string
dhcp_allocation_response_instance = DhcpAllocationResponse.from_json(json)
# print the JSON string representation of the object
print DhcpAllocationResponse.to_json()

# convert the object into a dict
dhcp_allocation_response_dict = dhcp_allocation_response_instance.to_dict()
# create an instance of DhcpAllocationResponse from a dict
dhcp_allocation_response_form_dict = dhcp_allocation_response.from_dict(dhcp_allocation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


