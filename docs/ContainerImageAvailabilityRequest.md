# ContainerImageAvailabilityRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timeout** | **int** | Positive number represents a timeout in seconds for a pull operation. | [optional] 
**images** | **List[str]** | List of image names to be checked. | 

## Example

```python
from openshift_assisted_service.models.container_image_availability_request import ContainerImageAvailabilityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ContainerImageAvailabilityRequest from a JSON string
container_image_availability_request_instance = ContainerImageAvailabilityRequest.from_json(json)
# print the JSON string representation of the object
print ContainerImageAvailabilityRequest.to_json()

# convert the object into a dict
container_image_availability_request_dict = container_image_availability_request_instance.to_dict()
# create an instance of ContainerImageAvailabilityRequest from a dict
container_image_availability_request_form_dict = container_image_availability_request.from_dict(container_image_availability_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


