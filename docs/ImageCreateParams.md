# ImageCreateParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ssh_public_key** | **str** | SSH public key for debugging the installation. | [optional] 
**static_network_config** | [**List[HostStaticNetworkConfig]**](HostStaticNetworkConfig.md) |  | [optional] 
**image_type** | [**ImageType**](ImageType.md) |  | [optional] 

## Example

```python
from openshift_assisted_service.models.image_create_params import ImageCreateParams

# TODO update the JSON string below
json = "{}"
# create an instance of ImageCreateParams from a JSON string
image_create_params_instance = ImageCreateParams.from_json(json)
# print the JSON string representation of the object
print ImageCreateParams.to_json()

# convert the object into a dict
image_create_params_dict = image_create_params_instance.to_dict()
# create an instance of ImageCreateParams from a dict
image_create_params_form_dict = image_create_params.from_dict(image_create_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


