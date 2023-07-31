# LogsGatherCmdRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **str** | Cluster id | 
**infra_env_id** | **str** | Infra env id | 
**host_id** | **str** | Host id | 
**bootstrap** | **bool** | Host is bootstrap or not | 
**installer_gather** | **bool** | Run installer gather logs | [default to True]
**master_ips** | **List[str]** | List of master ips | [optional] 

## Example

```python
from openshift_assisted_service.models.logs_gather_cmd_request import LogsGatherCmdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LogsGatherCmdRequest from a JSON string
logs_gather_cmd_request_instance = LogsGatherCmdRequest.from_json(json)
# print the JSON string representation of the object
print LogsGatherCmdRequest.to_json()

# convert the object into a dict
logs_gather_cmd_request_dict = logs_gather_cmd_request_instance.to_dict()
# create an instance of LogsGatherCmdRequest from a dict
logs_gather_cmd_request_form_dict = logs_gather_cmd_request.from_dict(logs_gather_cmd_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


