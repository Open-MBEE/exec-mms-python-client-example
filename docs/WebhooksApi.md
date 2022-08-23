# mms_python_client.WebhooksApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_or_update_webhooks**](WebhooksApi.md#create_or_update_webhooks) | **POST** /projects/{projectId}/webhooks | 
[**delete_webhooks**](WebhooksApi.md#delete_webhooks) | **DELETE** /projects/{projectId}/webhooks | 
[**get_all_webhooks**](WebhooksApi.md#get_all_webhooks) | **GET** /projects/{projectId}/webhooks | 


# **create_or_update_webhooks**
> WebhookResponse create_or_update_webhooks(project_id, webhook_request)



### Example

* Basic Authentication (basicAuth):
* Bearer (JWT) Authentication (bearerToken):

```python
import time
import mms_python_client
from mms_python_client.api import webhooks_api
from mms_python_client.model.webhook_request import WebhookRequest
from mms_python_client.model.webhook_response import WebhookResponse
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
    api_instance = webhooks_api.WebhooksApi(api_client)
    project_id = "projectId_example" # str | 
    webhook_request = WebhookRequest(
        webhooks=[
            Webhook(
                url="url_example",
                type="type_example",
                id="id_example",
            ),
        ],
    ) # WebhookRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_or_update_webhooks(project_id, webhook_request)
        pprint(api_response)
    except mms_python_client.ApiException as e:
        print("Exception when calling WebhooksApi->create_or_update_webhooks: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **webhook_request** | [**WebhookRequest**](WebhookRequest.md)|  |

### Return type

[**WebhookResponse**](WebhookResponse.md)

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

# **delete_webhooks**
> WebhookResponse delete_webhooks(project_id, webhook_request)



### Example

* Basic Authentication (basicAuth):
* Bearer (JWT) Authentication (bearerToken):

```python
import time
import mms_python_client
from mms_python_client.api import webhooks_api
from mms_python_client.model.webhook_request import WebhookRequest
from mms_python_client.model.webhook_response import WebhookResponse
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
    api_instance = webhooks_api.WebhooksApi(api_client)
    project_id = "projectId_example" # str | 
    webhook_request = WebhookRequest(
        webhooks=[
            Webhook(
                url="url_example",
                type="type_example",
                id="id_example",
            ),
        ],
    ) # WebhookRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.delete_webhooks(project_id, webhook_request)
        pprint(api_response)
    except mms_python_client.ApiException as e:
        print("Exception when calling WebhooksApi->delete_webhooks: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **webhook_request** | [**WebhookRequest**](WebhookRequest.md)|  |

### Return type

[**WebhookResponse**](WebhookResponse.md)

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

# **get_all_webhooks**
> WebhookResponse get_all_webhooks(project_id)



### Example

* Basic Authentication (basicAuth):
* Bearer (JWT) Authentication (bearerToken):

```python
import time
import mms_python_client
from mms_python_client.api import webhooks_api
from mms_python_client.model.webhook_response import WebhookResponse
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
    api_instance = webhooks_api.WebhooksApi(api_client)
    project_id = "projectId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_all_webhooks(project_id)
        pprint(api_response)
    except mms_python_client.ApiException as e:
        print("Exception when calling WebhooksApi->get_all_webhooks: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |

### Return type

[**WebhookResponse**](WebhookResponse.md)

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

