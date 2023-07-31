# Event


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Event Name. | [optional] 
**cluster_id** | **str** | Unique identifier of the cluster this event relates to. | [optional] 
**host_id** | **str** | Unique identifier of the host this event relates to. | [optional] 
**infra_env_id** | **str** | Unique identifier of the infra-env this event relates to. | [optional] 
**severity** | **str** |  | 
**category** | **str** |  | [optional] 
**message** | **str** |  | 
**event_time** | **datetime** |  | 
**request_id** | **str** | Unique identifier of the request that caused this event to occur. | [optional] 
**props** | **str** | Additional properties for the event in JSON format. | [optional] 

## Example

```python
from openshift_assisted_service.models.event import Event

# TODO update the JSON string below
json = "{}"
# create an instance of Event from a JSON string
event_instance = Event.from_json(json)
# print the JSON string representation of the object
print Event.to_json()

# convert the object into a dict
event_dict = event_instance.to_dict()
# create an instance of Event from a dict
event_form_dict = event.from_dict(event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


