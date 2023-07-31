# Route


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interface** | **str** | Interface to which packets for this route will be sent | [optional] 
**gateway** | **str** | Gateway address where the packets are sent | [optional] 
**destination** | **str** | The destination network or destination host | [optional] 
**family** | **int** | Defines whether this is an IPv4 (4) or IPv6 route (6) | [optional] 
**metric** | **int** | Route priority metric | [optional] 

## Example

```python
from openshift_assisted_service.models.route import Route

# TODO update the JSON string below
json = "{}"
# create an instance of Route from a JSON string
route_instance = Route.from_json(json)
# print the JSON string representation of the object
print Route.to_json()

# convert the object into a dict
route_dict = route_instance.to_dict()
# create an instance of Route from a dict
route_form_dict = route.from_dict(route_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


