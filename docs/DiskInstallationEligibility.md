# DiskInstallationEligibility


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eligible** | **bool** | Whether the disk is eligible for installation or not. | [optional] 
**not_eligible_reasons** | **List[str]** | Reasons for why this disk is not eligible for installation. | [optional] 

## Example

```python
from openshift_assisted_service.models.disk_installation_eligibility import DiskInstallationEligibility

# TODO update the JSON string below
json = "{}"
# create an instance of DiskInstallationEligibility from a JSON string
disk_installation_eligibility_instance = DiskInstallationEligibility.from_json(json)
# print the JSON string representation of the object
print DiskInstallationEligibility.to_json()

# convert the object into a dict
disk_installation_eligibility_dict = disk_installation_eligibility_instance.to_dict()
# create an instance of DiskInstallationEligibility from a dict
disk_installation_eligibility_form_dict = disk_installation_eligibility.from_dict(disk_installation_eligibility_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


