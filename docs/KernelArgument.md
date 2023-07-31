# KernelArgument

pair of [operation, argument] specifying the argument and what operation should be applied on it.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | **str** | The operation to apply on the kernel argument. | [optional] 
**value** | **str** | Kernel argument can have the form &lt;parameter&gt; or &lt;parameter&gt;&#x3D;&lt;value&gt;. The following examples should be supported: rd.net.timeout.carrier&#x3D;60 isolcpus&#x3D;1,2,10-20,100-2000:2/25 quiet The parsing by the command line parser in linux kernel is much looser and this pattern follows it.  | [optional] 

## Example

```python
from openshift_assisted_service.models.kernel_argument import KernelArgument

# TODO update the JSON string below
json = "{}"
# create an instance of KernelArgument from a JSON string
kernel_argument_instance = KernelArgument.from_json(json)
# print the JSON string representation of the object
print KernelArgument.to_json()

# convert the object into a dict
kernel_argument_dict = kernel_argument_instance.to_dict()
# create an instance of KernelArgument from a dict
kernel_argument_form_dict = kernel_argument.from_dict(kernel_argument_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


