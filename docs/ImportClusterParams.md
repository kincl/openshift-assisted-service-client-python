# ImportClusterParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | OpenShift cluster name. | 
**api_vip_dnsname** | **str** | The domain name used to reach the OpenShift cluster API. | 
**openshift_version** | **str** | Version of the OpenShift cluster. | [optional] 
**openshift_cluster_id** | **str** | The id of the OCP cluster, that hosts will be added to | 

## Example

```python
from openshift_assisted_service.models.import_cluster_params import ImportClusterParams

# TODO update the JSON string below
json = "{}"
# create an instance of ImportClusterParams from a JSON string
import_cluster_params_instance = ImportClusterParams.from_json(json)
# print the JSON string representation of the object
print ImportClusterParams.to_json()

# convert the object into a dict
import_cluster_params_dict = import_cluster_params_instance.to_dict()
# create an instance of ImportClusterParams from a dict
import_cluster_params_form_dict = import_cluster_params.from_dict(import_cluster_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


