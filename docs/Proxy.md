# Proxy


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**http_proxy** | **str** | A proxy URL to use for creating HTTP connections outside the cluster. http://\\&lt;username\\&gt;:\\&lt;pswd\\&gt;@\\&lt;ip\\&gt;:\\&lt;port\\&gt;  | [optional] 
**https_proxy** | **str** | A proxy URL to use for creating HTTPS connections outside the cluster. http://\\&lt;username\\&gt;:\\&lt;pswd\\&gt;@\\&lt;ip\\&gt;:\\&lt;port\\&gt;  | [optional] 
**no_proxy** | **str** | An \&quot;*\&quot; or a comma-separated list of destination domain names, domains, IP addresses, or other network CIDRs to exclude from proxying. | [optional] 

## Example

```python
from openshift_assisted_service.models.proxy import Proxy

# TODO update the JSON string below
json = "{}"
# create an instance of Proxy from a JSON string
proxy_instance = Proxy.from_json(json)
# print the JSON string representation of the object
print Proxy.to_json()

# convert the object into a dict
proxy_dict = proxy_instance.to_dict()
# create an instance of Proxy from a dict
proxy_form_dict = proxy.from_dict(proxy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


