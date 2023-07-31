# ContainerImageAvailabilityResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**images** | [**List[ContainerImageAvailability]**](ContainerImageAvailability.md) | List of images that were checked. | 

## Example

```python
from openshift_assisted_service.models.container_image_availability_response import ContainerImageAvailabilityResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ContainerImageAvailabilityResponse from a JSON string
container_image_availability_response_instance = ContainerImageAvailabilityResponse.from_json(json)
# print the JSON string representation of the object
print ContainerImageAvailabilityResponse.to_json()

# convert the object into a dict
container_image_availability_response_dict = container_image_availability_response_instance.to_dict()
# create an instance of ContainerImageAvailabilityResponse from a dict
container_image_availability_response_form_dict = container_image_availability_response.from_dict(container_image_availability_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


