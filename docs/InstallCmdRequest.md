# InstallCmdRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **str** | Cluster id | 
**infra_env_id** | **str** | Infra env id | 
**host_id** | **str** | Host id | 
**role** | [**HostRole**](HostRole.md) |  | 
**boot_device** | **str** | Boot device to write image on | 
**controller_image** | **str** | Assisted installer controller image | 
**installer_image** | **str** | Assisted installer image | 
**high_availability_mode** | **str** | Guaranteed availability of the installed cluster. &#39;Full&#39; installs a Highly-Available cluster over multiple master nodes whereas &#39;None&#39; installs a full cluster over one node.  | [optional] [default to 'Full']
**proxy** | [**Proxy**](Proxy.md) |  | [optional] 
**check_cvo** | **bool** | Check CVO status if needed | [optional] [default to True]
**disks_to_format** | **List[str]** | List of disks to format | [optional] 
**must_gather_image** | **str** | Must-gather images to use | [optional] 
**mco_image** | **str** | Machine config operator image | [optional] 
**openshift_version** | **str** | Version of the OpenShift cluster. | [optional] 
**service_ips** | **List[str]** | List of service ips | [optional] 
**installer_args** | **str** | Core-os installer addtional args | [optional] 
**skip_installation_disk_cleanup** | **bool** | Skip formatting installation disk | [optional] 

## Example

```python
from openshift_assisted_service.models.install_cmd_request import InstallCmdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InstallCmdRequest from a JSON string
install_cmd_request_instance = InstallCmdRequest.from_json(json)
# print the JSON string representation of the object
print InstallCmdRequest.to_json()

# convert the object into a dict
install_cmd_request_dict = install_cmd_request_instance.to_dict()
# create an instance of InstallCmdRequest from a dict
install_cmd_request_form_dict = install_cmd_request.from_dict(install_cmd_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


