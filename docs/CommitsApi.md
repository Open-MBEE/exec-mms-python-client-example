# mms_python_client.CommitsApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_commit**](CommitsApi.md#get_commit) | **GET** /projects/{projectId}/commits/{commitId} | 
[**get_commits**](CommitsApi.md#get_commits) | **PUT** /projects/{projectId}/commits | 
[**get_element_commits**](CommitsApi.md#get_element_commits) | **GET** /projects/{projectId}/refs/{refId}/elements/{elementId}/commits | 
[**get_ref_commits**](CommitsApi.md#get_ref_commits) | **GET** /projects/{projectId}/refs/{refId}/commits | 


# **get_commit**
> CommitsResponse get_commit(project_id, commit_id)



### Example

* Basic Authentication (basicAuth):
* Bearer (JWT) Authentication (bearerToken):

```python
import time
import mms_python_client
from mms_python_client.api import commits_api
from mms_python_client.model.commits_response import CommitsResponse
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
    api_instance = commits_api.CommitsApi(api_client)
    project_id = "projectId_example" # str | 
    commit_id = "commitId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_commit(project_id, commit_id)
        pprint(api_response)
    except mms_python_client.ApiException as e:
        print("Exception when calling CommitsApi->get_commit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **commit_id** | **str**|  |

### Return type

[**CommitsResponse**](CommitsResponse.md)

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

# **get_commits**
> CommitsResponse get_commits(project_id, commits_request)



### Example

* Basic Authentication (basicAuth):
* Bearer (JWT) Authentication (bearerToken):

```python
import time
import mms_python_client
from mms_python_client.api import commits_api
from mms_python_client.model.commits_request import CommitsRequest
from mms_python_client.model.commits_response import CommitsResponse
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
    api_instance = commits_api.CommitsApi(api_client)
    project_id = "projectId_example" # str | 
    commits_request = CommitsRequest(
        commits=[
            Commit(),
        ],
    ) # CommitsRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_commits(project_id, commits_request)
        pprint(api_response)
    except mms_python_client.ApiException as e:
        print("Exception when calling CommitsApi->get_commits: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **commits_request** | [**CommitsRequest**](CommitsRequest.md)|  |

### Return type

[**CommitsResponse**](CommitsResponse.md)

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

# **get_element_commits**
> CommitsResponse get_element_commits(project_id, ref_id, element_id)



### Example

* Basic Authentication (basicAuth):
* Bearer (JWT) Authentication (bearerToken):

```python
import time
import mms_python_client
from mms_python_client.api import commits_api
from mms_python_client.model.commits_response import CommitsResponse
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
    api_instance = commits_api.CommitsApi(api_client)
    project_id = "projectId_example" # str | 
    ref_id = "refId_example" # str | 
    element_id = "elementId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_element_commits(project_id, ref_id, element_id)
        pprint(api_response)
    except mms_python_client.ApiException as e:
        print("Exception when calling CommitsApi->get_element_commits: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **ref_id** | **str**|  |
 **element_id** | **str**|  |

### Return type

[**CommitsResponse**](CommitsResponse.md)

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

# **get_ref_commits**
> CommitsResponse get_ref_commits(project_id, ref_id)



### Example

* Basic Authentication (basicAuth):
* Bearer (JWT) Authentication (bearerToken):

```python
import time
import mms_python_client
from mms_python_client.api import commits_api
from mms_python_client.model.commits_response import CommitsResponse
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
    api_instance = commits_api.CommitsApi(api_client)
    project_id = "projectId_example" # str | 
    ref_id = "refId_example" # str | 
    limit = "limit_example" # str |  (optional)
    max_timestamp = "maxTimestamp_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_ref_commits(project_id, ref_id)
        pprint(api_response)
    except mms_python_client.ApiException as e:
        print("Exception when calling CommitsApi->get_ref_commits: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_ref_commits(project_id, ref_id, limit=limit, max_timestamp=max_timestamp)
        pprint(api_response)
    except mms_python_client.ApiException as e:
        print("Exception when calling CommitsApi->get_ref_commits: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **ref_id** | **str**|  |
 **limit** | **str**|  | [optional]
 **max_timestamp** | **str**|  | [optional]

### Return type

[**CommitsResponse**](CommitsResponse.md)

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

