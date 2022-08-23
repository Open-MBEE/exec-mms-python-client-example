# mms_python_client.ArtifactsApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_or_update_artifacts**](ArtifactsApi.md#create_or_update_artifacts) | **POST** /projects/{projectId}/refs/{refId}/elements/{elementId} | 
[**delete_artifact_by_extension**](ArtifactsApi.md#delete_artifact_by_extension) | **DELETE** /projects/{projectId}/refs/{refId}/elements/{elementId}/{extension} | 
[**get_artifact_by_extension**](ArtifactsApi.md#get_artifact_by_extension) | **GET** /projects/{projectId}/refs/{refId}/elements/{elementId}/{extension} | 


# **create_or_update_artifacts**
> ElementsResponse create_or_update_artifacts(project_id, ref_id, element_id)



### Example

* Basic Authentication (basicAuth):
* Bearer (JWT) Authentication (bearerToken):

```python
import time
import mms_python_client
from mms_python_client.api import artifacts_api
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
    api_instance = artifacts_api.ArtifactsApi(api_client)
    project_id = "projectId_example" # str | 
    ref_id = "refId_example" # str | 
    element_id = "elementId_example" # str | 
    file = open('/path/to/file', 'rb') # file_type |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_or_update_artifacts(project_id, ref_id, element_id)
        pprint(api_response)
    except mms_python_client.ApiException as e:
        print("Exception when calling ArtifactsApi->create_or_update_artifacts: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_or_update_artifacts(project_id, ref_id, element_id, file=file)
        pprint(api_response)
    except mms_python_client.ApiException as e:
        print("Exception when calling ArtifactsApi->create_or_update_artifacts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **ref_id** | **str**|  |
 **element_id** | **str**|  |
 **file** | **file_type**|  | [optional]

### Return type

[**ElementsResponse**](ElementsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_artifact_by_extension**
> ElementsResponse delete_artifact_by_extension(project_id, ref_id, element_id, extension)



### Example

* Basic Authentication (basicAuth):
* Bearer (JWT) Authentication (bearerToken):

```python
import time
import mms_python_client
from mms_python_client.api import artifacts_api
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
    api_instance = artifacts_api.ArtifactsApi(api_client)
    project_id = "projectId_example" # str | 
    ref_id = "refId_example" # str | 
    element_id = "elementId_example" # str | 
    extension = "extension_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.delete_artifact_by_extension(project_id, ref_id, element_id, extension)
        pprint(api_response)
    except mms_python_client.ApiException as e:
        print("Exception when calling ArtifactsApi->delete_artifact_by_extension: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **ref_id** | **str**|  |
 **element_id** | **str**|  |
 **extension** | **str**|  |

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

# **get_artifact_by_extension**
> str get_artifact_by_extension(project_id, ref_id, element_id, extension)



### Example

* Basic Authentication (basicAuth):
* Bearer (JWT) Authentication (bearerToken):

```python
import time
import mms_python_client
from mms_python_client.api import artifacts_api
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
    api_instance = artifacts_api.ArtifactsApi(api_client)
    project_id = "projectId_example" # str | 
    ref_id = "refId_example" # str | 
    element_id = "elementId_example" # str | 
    extension = "extension_example" # str | 
    commit_id = "commitId_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_artifact_by_extension(project_id, ref_id, element_id, extension)
        pprint(api_response)
    except mms_python_client.ApiException as e:
        print("Exception when calling ArtifactsApi->get_artifact_by_extension: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_artifact_by_extension(project_id, ref_id, element_id, extension, commit_id=commit_id)
        pprint(api_response)
    except mms_python_client.ApiException as e:
        print("Exception when calling ArtifactsApi->get_artifact_by_extension: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **ref_id** | **str**|  |
 **element_id** | **str**|  |
 **extension** | **str**|  |
 **commit_id** | **str**|  | [optional]

### Return type

**str**

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

