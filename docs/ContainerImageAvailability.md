# ContainerImageAvailability


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A fully qualified image name (FQIN). | [optional] 
**size_bytes** | **float** | Size of the image in bytes. | [optional] 
**time** | **float** | Seconds it took to pull the image. | [optional] 
**download_rate** | **float** | The rate of size/time in seconds MBps. | [optional] 
**result** | [**ContainerImageAvailabilityResult**](ContainerImageAvailabilityResult.md) |  | [optional] 

## Example

```python
from openshift_assisted_service.models.container_image_availability import ContainerImageAvailability

# TODO update the JSON string below
json = "{}"
# create an instance of ContainerImageAvailability from a JSON string
container_image_availability_instance = ContainerImageAvailability.from_json(json)
# print the JSON string representation of the object
print ContainerImageAvailability.to_json()

# convert the object into a dict
container_image_availability_dict = container_image_availability_instance.to_dict()
# create an instance of ContainerImageAvailability from a dict
container_image_availability_form_dict = container_image_availability.from_dict(container_image_availability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


