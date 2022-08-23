# mms_python_client.MMSVersionApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_mms_version**](MMSVersionApi.md#get_mms_version) | **GET** /mmsversion | 


# **get_mms_version**
> GetMMSVersion200Response get_mms_version()



### Example


```python
import time
import mms_python_client
from mms_python_client.api import mms_version_api
from mms_python_client.model.get_mms_version200_response import GetMMSVersion200Response
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = mms_python_client.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
with mms_python_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mms_version_api.MMSVersionApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_mms_version()
        pprint(api_response)
    except mms_python_client.ApiException as e:
        print("Exception when calling MMSVersionApi->get_mms_version: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetMMSVersion200Response**](GetMMSVersion200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

