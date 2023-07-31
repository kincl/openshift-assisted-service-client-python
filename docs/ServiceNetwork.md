# ServiceNetwork

IP address block for service IP blocks.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **str** | A network to use for service IP addresses. If you need to access the services from an external network, configure load balancers and routers to manage the traffic. | [optional] 
**cidr** | **str** |  | [optional] 

## Example

```python
from openshift_assisted_service.models.service_network import ServiceNetwork

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceNetwork from a JSON string
service_network_instance = ServiceNetwork.from_json(json)
# print the JSON string representation of the object
print ServiceNetwork.to_json()

# convert the object into a dict
service_network_dict = service_network_instance.to_dict()
# create an instance of ServiceNetwork from a dict
service_network_form_dict = service_network.from_dict(service_network_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


