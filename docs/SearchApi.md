# mms_python_client.SearchApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_basic_search**](SearchApi.md#get_basic_search) | **GET** /projects/{projectId}/refs/{refId}/search | 
[**post_basic_search**](SearchApi.md#post_basic_search) | **POST** /projects/{projectId}/refs/{refId}/search | 


# **get_basic_search**
> ElementsSearchResponse get_basic_search(project_id, ref_id)



### Example

* Basic Authentication (basicAuth):
* Bearer (JWT) Authentication (bearerToken):

```python
import time
import mms_python_client
from mms_python_client.api import search_api
from mms_python_client.model.elements_search_response import ElementsSearchResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = mms_python_client.Configuration(
    host = "http://localhost:8080"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = mms_python_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): bearerToken
configuration = mms_python_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with mms_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = search_api.SearchApi(api_client)
    project_id = "projectId_example" # str | 
    ref_id = "refId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_basic_search(project_id, ref_id)
        pprint(api_response)
    except mms_python_client.ApiException as e:
        print("Exception when calling SearchApi->get_basic_search: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **ref_id** | **str**|  |

### Return type

[**ElementsSearchResponse**](ElementsSearchResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_basic_search**
> ElementsSearchResponse post_basic_search(project_id, ref_id, basic_search_request)



### Example

* Basic Authentication (basicAuth):
* Bearer (JWT) Authentication (bearerToken):

```python
import time
import mms_python_client
from mms_python_client.api import search_api
from mms_python_client.model.elements_search_response import ElementsSearchResponse
from mms_python_client.model.basic_search_request import BasicSearchRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = mms_python_client.Configuration(
    host = "http://localhost:8080"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = mms_python_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): bearerToken
configuration = mms_python_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with mms_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = search_api.SearchApi(api_client)
    project_id = "projectId_example" # str | 
    ref_id = "refId_example" # str | 
    basic_search_request = BasicSearchRequest(
        params={
            "key": "key_example",
        },
        recurse={
            "key": "key_example",
        },
        _from=1,
        size=1,
    ) # BasicSearchRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.post_basic_search(project_id, ref_id, basic_search_request)
        pprint(api_response)
    except mms_python_client.ApiException as e:
        print("Exception when calling SearchApi->post_basic_search: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **ref_id** | **str**|  |
 **basic_search_request** | [**BasicSearchRequest**](BasicSearchRequest.md)|  |

### Return type

[**ElementsSearchResponse**](ElementsSearchResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

