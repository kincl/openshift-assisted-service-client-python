# UpgradeAgentResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_image** | **str** | Full image reference of the image that the agent has upgraded to, for example &#x60;quay.io/registry-proxy.engineering.redhat.com/rh-osbs/openshift4-assisted-installer-agent-rhel8:v1.0.0-142&#x60;.  | [optional] 
**result** | [**UpgradeAgentResult**](UpgradeAgentResult.md) |  | [optional] 

## Example

```python
from openshift_assisted_service.models.upgrade_agent_response import UpgradeAgentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpgradeAgentResponse from a JSON string
upgrade_agent_response_instance = UpgradeAgentResponse.from_json(json)
# print the JSON string representation of the object
print UpgradeAgentResponse.to_json()

# convert the object into a dict
upgrade_agent_response_dict = upgrade_agent_response_instance.to_dict()
# create an instance of UpgradeAgentResponse from a dict
upgrade_agent_response_form_dict = upgrade_agent_response.from_dict(upgrade_agent_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


