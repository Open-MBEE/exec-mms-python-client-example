# mms_python_client.ElementsApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_or_update_elements**](ElementsApi.md#create_or_update_elements) | **POST** /projects/{projectId}/refs/{refId}/elements | 
[**delete_element**](ElementsApi.md#delete_element) | **DELETE** /projects/{projectId}/refs/{refId}/elements/{elementId} | 
[**delete_elements**](ElementsApi.md#delete_elements) | **DELETE** /projects/{projectId}/refs/{refId}/elements | 
[**get_all_elements**](ElementsApi.md#get_all_elements) | **GET** /projects/{projectId}/refs/{refId}/elements | 
[**get_element**](ElementsApi.md#get_element) | **GET** /projects/{projectId}/refs/{refId}/elements/{elementId} | 
[**get_elements**](ElementsApi.md#get_elements) | **PUT** /projects/{projectId}/refs/{refId}/elements | 


# **create_or_update_elements**
> ElementsResponse create_or_update_elements(project_id, ref_id, elements_request)



### Example

* Basic Authentication (basicAuth):
* Bearer (JWT) Authentication (bearerToken):

```python
import time
import mms_python_client
from mms_python_client.api import elements_api
from mms_python_client.model.elements_response import ElementsResponse
from mms_python_client.model.elements_request import ElementsRequest
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
    api_instance = elements_api.ElementsApi(api_client)
    project_id = "projectId_example" # str | 
    ref_id = "refId_example" # str | 
    elements_request = ElementsRequest(
        source="source_example",
        comment="comment_example",
        elements=[
            Element(),
        ],
    ) # ElementsRequest | 
    overwrite = "overwrite_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_or_update_elements(project_id, ref_id, elements_request)
        pprint(api_response)
    except mms_python_client.ApiException as e:
        print("Exception when calling ElementsApi->create_or_update_elements: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_or_update_elements(project_id, ref_id, elements_request, overwrite=overwrite)
        pprint(api_response)
    except mms_python_client.ApiException as e:
        print("Exception when calling ElementsApi->create_or_update_elements: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **ref_id** | **str**|  |
 **elements_request** | [**ElementsRequest**](ElementsRequest.md)|  |
 **overwrite** | **str**|  | [optional]

### Return type

[**ElementsResponse**](ElementsResponse.md)

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

# **delete_element**
> ElementsResponse delete_element(project_id, ref_id, element_id)



### Example

* Basic Authentication (basicAuth):
* Bearer (JWT) Authentication (bearerToken):

```python
import time
import mms_python_client
from mms_python_client.api import elements_api
from mms_python_client.model.elements_response import ElementsResponse
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
    api_instance = elements_api.ElementsApi(api_client)
    project_id = "projectId_example" # str | 
    ref_id = "refId_example" # str | 
    element_id = "elementId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.delete_element(project_id, ref_id, element_id)
        pprint(api_response)
    except mms_python_client.ApiException as e:
        print("Exception when calling ElementsApi->delete_element: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **ref_id** | **str**|  |
 **element_id** | **str**|  |

### Return type

[**ElementsResponse**](ElementsResponse.md)

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

# **delete_elements**
> ElementsResponse delete_elements(project_id, ref_id, elements_request)



### Example

* Basic Authentication (basicAuth):
* Bearer (JWT) Authentication (bearerToken):

```python
import time
import mms_python_client
from mms_python_client.api import elements_api
from mms_python_client.model.elements_response import ElementsResponse
from mms_python_client.model.elements_request import ElementsRequest
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
    api_instance = elements_api.ElementsApi(api_client)
    project_id = "projectId_example" # str | 
    ref_id = "refId_example" # str | 
    elements_request = ElementsRequest(
        source="source_example",
        comment="comment_example",
        elements=[
            Element(),
        ],
    ) # ElementsRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.delete_elements(project_id, ref_id, elements_request)
        pprint(api_response)
    except mms_python_client.ApiException as e:
        print("Exception when calling ElementsApi->delete_elements: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **ref_id** | **str**|  |
 **elements_request** | [**ElementsRequest**](ElementsRequest.md)|  |

### Return type

[**ElementsResponse**](ElementsResponse.md)

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

# **get_all_elements**
> ElementsResponse get_all_elements(project_id, ref_id)



### Example

* Basic Authentication (basicAuth):
* Bearer (JWT) Authentication (bearerToken):

```python
import time
import mms_python_client
from mms_python_client.api import elements_api
from mms_python_client.model.elements_response import ElementsResponse
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
    api_instance = elements_api.ElementsApi(api_client)
    project_id = "projectId_example" # str | 
    ref_id = "refId_example" # str | 
    commit_id = "commitId_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_all_elements(project_id, ref_id)
        pprint(api_response)
    except mms_python_client.ApiException as e:
        print("Exception when calling ElementsApi->get_all_elements: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_elements(project_id, ref_id, commit_id=commit_id)
        pprint(api_response)
    except mms_python_client.ApiException as e:
        print("Exception when calling ElementsApi->get_all_elements: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **ref_id** | **str**|  |
 **commit_id** | **str**|  | [optional]

### Return type

[**ElementsResponse**](ElementsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-ndjson


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_element**
> ElementsResponse get_element(project_id, ref_id, element_id)



### Example

* Basic Authentication (basicAuth):
* Bearer (JWT) Authentication (bearerToken):

```python
import time
import mms_python_client
from mms_python_client.api import elements_api
from mms_python_client.model.elements_response import ElementsResponse
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
    api_instance = elements_api.ElementsApi(api_client)
    project_id = "projectId_example" # str | 
    ref_id = "refId_example" # str | 
    element_id = "elementId_example" # str | 
    commit_id = "commitId_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_element(project_id, ref_id, element_id)
        pprint(api_response)
    except mms_python_client.ApiException as e:
        print("Exception when calling ElementsApi->get_element: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_element(project_id, ref_id, element_id, commit_id=commit_id)
        pprint(api_response)
    except mms_python_client.ApiException as e:
        print("Exception when calling ElementsApi->get_element: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **ref_id** | **str**|  |
 **element_id** | **str**|  |
 **commit_id** | **str**|  | [optional]

### Return type

[**ElementsResponse**](ElementsResponse.md)

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

# **get_elements**
> ElementsResponse get_elements(project_id, ref_id, elements_request)



### Example

* Basic Authentication (basicAuth):
* Bearer (JWT) Authentication (bearerToken):

```python
import time
import mms_python_client
from mms_python_client.api import elements_api
from mms_python_client.model.elements_response import ElementsResponse
from mms_python_client.model.elements_request import ElementsRequest
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
    api_instance = elements_api.ElementsApi(api_client)
    project_id = "projectId_example" # str | 
    ref_id = "refId_example" # str | 
    elements_request = ElementsRequest(
        source="source_example",
        comment="comment_example",
        elements=[
            Element(),
        ],
    ) # ElementsRequest | 
    commit_id = "commitId_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_elements(project_id, ref_id, elements_request)
        pprint(api_response)
    except mms_python_client.ApiException as e:
        print("Exception when calling ElementsApi->get_elements: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_elements(project_id, ref_id, elements_request, commit_id=commit_id)
        pprint(api_response)
    except mms_python_client.ApiException as e:
        print("Exception when calling ElementsApi->get_elements: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **ref_id** | **str**|  |
 **elements_request** | [**ElementsRequest**](ElementsRequest.md)|  |
 **commit_id** | **str**|  | [optional]

### Return type

[**ElementsResponse**](ElementsResponse.md)

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

