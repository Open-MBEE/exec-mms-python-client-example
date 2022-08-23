# mms_python_client.ProjectsApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_or_update_projects**](ProjectsApi.md#create_or_update_projects) | **POST** /projects | 
[**delete_project**](ProjectsApi.md#delete_project) | **DELETE** /projects/{projectId} | 
[**get_all_projects**](ProjectsApi.md#get_all_projects) | **GET** /projects | 
[**get_project**](ProjectsApi.md#get_project) | **GET** /projects/{projectId} | 
[**get_project_schema_options**](ProjectsApi.md#get_project_schema_options) | **GET** /schemas | 


# **create_or_update_projects**
> ProjectsResponse create_or_update_projects(projects_request)



### Example

* Basic Authentication (basicAuth):
* Bearer (JWT) Authentication (bearerToken):

```python
import time
import mms_python_client
from mms_python_client.api import projects_api
from mms_python_client.model.projects_response import ProjectsResponse
from mms_python_client.model.projects_request import ProjectsRequest
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
    api_instance = projects_api.ProjectsApi(api_client)
    projects_request = ProjectsRequest(
        projects=[
            Project(),
        ],
    ) # ProjectsRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_or_update_projects(projects_request)
        pprint(api_response)
    except mms_python_client.ApiException as e:
        print("Exception when calling ProjectsApi->create_or_update_projects: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_request** | [**ProjectsRequest**](ProjectsRequest.md)|  |

### Return type

[**ProjectsResponse**](ProjectsResponse.md)

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

# **delete_project**
> ProjectsResponse delete_project(project_id)



### Example

* Basic Authentication (basicAuth):
* Bearer (JWT) Authentication (bearerToken):

```python
import time
import mms_python_client
from mms_python_client.api import projects_api
from mms_python_client.model.projects_response import ProjectsResponse
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
    api_instance = projects_api.ProjectsApi(api_client)
    project_id = "projectId_example" # str | 
    hard = False # bool |  (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.delete_project(project_id)
        pprint(api_response)
    except mms_python_client.ApiException as e:
        print("Exception when calling ProjectsApi->delete_project: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.delete_project(project_id, hard=hard)
        pprint(api_response)
    except mms_python_client.ApiException as e:
        print("Exception when calling ProjectsApi->delete_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **hard** | **bool**|  | [optional] if omitted the server will use the default value of False

### Return type

[**ProjectsResponse**](ProjectsResponse.md)

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

# **get_all_projects**
> ProjectsResponse get_all_projects()



### Example

* Basic Authentication (basicAuth):
* Bearer (JWT) Authentication (bearerToken):

```python
import time
import mms_python_client
from mms_python_client.api import projects_api
from mms_python_client.model.projects_response import ProjectsResponse
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
    api_instance = projects_api.ProjectsApi(api_client)
    org_id = "orgId_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_projects(org_id=org_id)
        pprint(api_response)
    except mms_python_client.ApiException as e:
        print("Exception when calling ProjectsApi->get_all_projects: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | [optional]

### Return type

[**ProjectsResponse**](ProjectsResponse.md)

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

# **get_project**
> ProjectsResponse get_project(project_id)



### Example

* Basic Authentication (basicAuth):
* Bearer (JWT) Authentication (bearerToken):

```python
import time
import mms_python_client
from mms_python_client.api import projects_api
from mms_python_client.model.projects_response import ProjectsResponse
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
    api_instance = projects_api.ProjectsApi(api_client)
    project_id = "projectId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_project(project_id)
        pprint(api_response)
    except mms_python_client.ApiException as e:
        print("Exception when calling ProjectsApi->get_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |

### Return type

[**ProjectsResponse**](ProjectsResponse.md)

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

# **get_project_schema_options**
> SchemasResponse get_project_schema_options()



### Example


```python
import time
import mms_python_client
from mms_python_client.api import projects_api
from mms_python_client.model.schemas_response import SchemasResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = mms_python_client.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
with mms_python_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = projects_api.ProjectsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_project_schema_options()
        pprint(api_response)
    except mms_python_client.ApiException as e:
        print("Exception when calling ProjectsApi->get_project_schema_options: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**SchemasResponse**](SchemasResponse.md)

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

