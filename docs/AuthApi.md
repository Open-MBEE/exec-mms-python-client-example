# mms_python_client.AuthApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_authentication_token**](AuthApi.md#check_authentication_token) | **GET** /checkAuth | 
[**create_authentication_token**](AuthApi.md#create_authentication_token) | **POST** /authentication | 
[**create_user**](AuthApi.md#create_user) | **POST** /user | 
[**get_authentication_token**](AuthApi.md#get_authentication_token) | **GET** /authentication | 
[**get_branch_permissions**](AuthApi.md#get_branch_permissions) | **GET** /projects/{projectId}/refs/{refId}/permissions | 
[**get_org_permissions**](AuthApi.md#get_org_permissions) | **GET** /orgs/{orgId}/permissions | 
[**get_project_permissions**](AuthApi.md#get_project_permissions) | **GET** /projects/{projectId}/permissions | 
[**get_users**](AuthApi.md#get_users) | **GET** /users | 
[**lookup_permissions**](AuthApi.md#lookup_permissions) | **PUT** /permissions | 
[**update_branch_permissions**](AuthApi.md#update_branch_permissions) | **POST** /projects/{projectId}/refs/{refId}/permissions | 
[**update_org_permissions**](AuthApi.md#update_org_permissions) | **POST** /orgs/{orgId}/permissions | 
[**update_password**](AuthApi.md#update_password) | **POST** /password | 
[**update_project_permissions**](AuthApi.md#update_project_permissions) | **POST** /projects/{projectId}/permissions | 


# **check_authentication_token**
> JwtTokenValidationResponse check_authentication_token()



### Example

* Basic Authentication (basicAuth):
* Bearer (JWT) Authentication (bearerToken):

```python
import time
import mms_python_client
from mms_python_client.api import auth_api
from mms_python_client.model.jwt_token_validation_response import JwtTokenValidationResponse
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
    api_instance = auth_api.AuthApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.check_authentication_token()
        pprint(api_response)
    except mms_python_client.ApiException as e:
        print("Exception when calling AuthApi->check_authentication_token: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**JwtTokenValidationResponse**](JwtTokenValidationResponse.md)

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

# **create_authentication_token**
> JwtAuthenticationResponse create_authentication_token(jwt_authentication_request)



### Example


```python
import time
import mms_python_client
from mms_python_client.api import auth_api
from mms_python_client.model.jwt_authentication_request import JwtAuthenticationRequest
from mms_python_client.model.jwt_authentication_response import JwtAuthenticationResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = mms_python_client.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
with mms_python_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_api.AuthApi(api_client)
    jwt_authentication_request = JwtAuthenticationRequest(
        username="username_example",
        password="password_example",
    ) # JwtAuthenticationRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_authentication_token(jwt_authentication_request)
        pprint(api_response)
    except mms_python_client.ApiException as e:
        print("Exception when calling AuthApi->create_authentication_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jwt_authentication_request** | [**JwtAuthenticationRequest**](JwtAuthenticationRequest.md)|  |

### Return type

[**JwtAuthenticationResponse**](JwtAuthenticationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user**
> UserCreateRequest create_user(user_create_request)



### Example

* Basic Authentication (basicAuth):
* Bearer (JWT) Authentication (bearerToken):

```python
import time
import mms_python_client
from mms_python_client.api import auth_api
from mms_python_client.model.user_create_request import UserCreateRequest
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
    api_instance = auth_api.AuthApi(api_client)
    user_create_request = UserCreateRequest(
        username="username_example",
        password="password_example",
        email="email_example",
        firstname="firstname_example",
        lastname="lastname_example",
        admin=True,
    ) # UserCreateRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_user(user_create_request)
        pprint(api_response)
    except mms_python_client.ApiException as e:
        print("Exception when calling AuthApi->create_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_create_request** | [**UserCreateRequest**](UserCreateRequest.md)|  |

### Return type

[**UserCreateRequest**](UserCreateRequest.md)

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

# **get_authentication_token**
> JwtAuthenticationResponse get_authentication_token()



### Example

* Basic Authentication (basicAuth):
* Bearer (JWT) Authentication (bearerToken):

```python
import time
import mms_python_client
from mms_python_client.api import auth_api
from mms_python_client.model.jwt_authentication_response import JwtAuthenticationResponse
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
    api_instance = auth_api.AuthApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_authentication_token()
        pprint(api_response)
    except mms_python_client.ApiException as e:
        print("Exception when calling AuthApi->get_authentication_token: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**JwtAuthenticationResponse**](JwtAuthenticationResponse.md)

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

# **get_branch_permissions**
> PermissionsResponse get_branch_permissions(project_id, ref_id)



### Example

* Basic Authentication (basicAuth):
* Bearer (JWT) Authentication (bearerToken):

```python
import time
import mms_python_client
from mms_python_client.api import auth_api
from mms_python_client.model.permissions_response import PermissionsResponse
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
    api_instance = auth_api.AuthApi(api_client)
    project_id = "projectId_example" # str | 
    ref_id = "refId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_branch_permissions(project_id, ref_id)
        pprint(api_response)
    except mms_python_client.ApiException as e:
        print("Exception when calling AuthApi->get_branch_permissions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **ref_id** | **str**|  |

### Return type

[**PermissionsResponse**](PermissionsResponse.md)

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

# **get_org_permissions**
> PermissionsResponse get_org_permissions(org_id)



### Example

* Basic Authentication (basicAuth):
* Bearer (JWT) Authentication (bearerToken):

```python
import time
import mms_python_client
from mms_python_client.api import auth_api
from mms_python_client.model.permissions_response import PermissionsResponse
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
    api_instance = auth_api.AuthApi(api_client)
    org_id = "orgId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_org_permissions(org_id)
        pprint(api_response)
    except mms_python_client.ApiException as e:
        print("Exception when calling AuthApi->get_org_permissions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  |

### Return type

[**PermissionsResponse**](PermissionsResponse.md)

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

# **get_project_permissions**
> PermissionsResponse get_project_permissions(project_id)



### Example

* Basic Authentication (basicAuth):
* Bearer (JWT) Authentication (bearerToken):

```python
import time
import mms_python_client
from mms_python_client.api import auth_api
from mms_python_client.model.permissions_response import PermissionsResponse
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
    api_instance = auth_api.AuthApi(api_client)
    project_id = "projectId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_project_permissions(project_id)
        pprint(api_response)
    except mms_python_client.ApiException as e:
        print("Exception when calling AuthApi->get_project_permissions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |

### Return type

[**PermissionsResponse**](PermissionsResponse.md)

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

# **get_users**
> UsersResponse get_users()



### Example

* Basic Authentication (basicAuth):
* Bearer (JWT) Authentication (bearerToken):

```python
import time
import mms_python_client
from mms_python_client.api import auth_api
from mms_python_client.model.users_response import UsersResponse
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
    api_instance = auth_api.AuthApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_users()
        pprint(api_response)
    except mms_python_client.ApiException as e:
        print("Exception when calling AuthApi->get_users: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**UsersResponse**](UsersResponse.md)

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

# **lookup_permissions**
> PermissionLookupResponse lookup_permissions(permission_lookup_request)



### Example

* Basic Authentication (basicAuth):
* Bearer (JWT) Authentication (bearerToken):

```python
import time
import mms_python_client
from mms_python_client.api import auth_api
from mms_python_client.model.permission_lookup_request import PermissionLookupRequest
from mms_python_client.model.permission_lookup_response import PermissionLookupResponse
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
    api_instance = auth_api.AuthApi(api_client)
    permission_lookup_request = PermissionLookupRequest(
        lookups=[
            PermissionLookup(
                type="ORG",
                org_id="org_id_example",
                project_id="project_id_example",
                ref_id="ref_id_example",
                privilege="ORG_READ",
                allow_anon_if_public=True,
                has_privilege=True,
            ),
        ],
    ) # PermissionLookupRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.lookup_permissions(permission_lookup_request)
        pprint(api_response)
    except mms_python_client.ApiException as e:
        print("Exception when calling AuthApi->lookup_permissions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permission_lookup_request** | [**PermissionLookupRequest**](PermissionLookupRequest.md)|  |

### Return type

[**PermissionLookupResponse**](PermissionLookupResponse.md)

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

# **update_branch_permissions**
> PermissionUpdatesResponse update_branch_permissions(project_id, ref_id, permissions_request)



### Example

* Basic Authentication (basicAuth):
* Bearer (JWT) Authentication (bearerToken):

```python
import time
import mms_python_client
from mms_python_client.api import auth_api
from mms_python_client.model.permission_updates_response import PermissionUpdatesResponse
from mms_python_client.model.permissions_request import PermissionsRequest
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
    api_instance = auth_api.AuthApi(api_client)
    project_id = "projectId_example" # str | 
    ref_id = "refId_example" # str | 
    permissions_request = PermissionsRequest(
        users=PermissionUpdateRequest(
            action="MODIFY",
            permissions=[
                Permission(
                    name="name_example",
                    role="role_example",
                ),
            ],
        ),
        groups=PermissionUpdateRequest(
            action="MODIFY",
            permissions=[
                Permission(
                    name="name_example",
                    role="role_example",
                ),
            ],
        ),
        inherit=True,
        public=True,
    ) # PermissionsRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_branch_permissions(project_id, ref_id, permissions_request)
        pprint(api_response)
    except mms_python_client.ApiException as e:
        print("Exception when calling AuthApi->update_branch_permissions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **ref_id** | **str**|  |
 **permissions_request** | [**PermissionsRequest**](PermissionsRequest.md)|  |

### Return type

[**PermissionUpdatesResponse**](PermissionUpdatesResponse.md)

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

# **update_org_permissions**
> PermissionUpdatesResponse update_org_permissions(org_id, permissions_request)



### Example

* Basic Authentication (basicAuth):
* Bearer (JWT) Authentication (bearerToken):

```python
import time
import mms_python_client
from mms_python_client.api import auth_api
from mms_python_client.model.permission_updates_response import PermissionUpdatesResponse
from mms_python_client.model.permissions_request import PermissionsRequest
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
    api_instance = auth_api.AuthApi(api_client)
    org_id = "orgId_example" # str | 
    permissions_request = PermissionsRequest(
        users=PermissionUpdateRequest(
            action="MODIFY",
            permissions=[
                Permission(
                    name="name_example",
                    role="role_example",
                ),
            ],
        ),
        groups=PermissionUpdateRequest(
            action="MODIFY",
            permissions=[
                Permission(
                    name="name_example",
                    role="role_example",
                ),
            ],
        ),
        inherit=True,
        public=True,
    ) # PermissionsRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_org_permissions(org_id, permissions_request)
        pprint(api_response)
    except mms_python_client.ApiException as e:
        print("Exception when calling AuthApi->update_org_permissions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  |
 **permissions_request** | [**PermissionsRequest**](PermissionsRequest.md)|  |

### Return type

[**PermissionUpdatesResponse**](PermissionUpdatesResponse.md)

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

# **update_password**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} update_password(user_create_request)



### Example

* Basic Authentication (basicAuth):
* Bearer (JWT) Authentication (bearerToken):

```python
import time
import mms_python_client
from mms_python_client.api import auth_api
from mms_python_client.model.user_create_request import UserCreateRequest
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
    api_instance = auth_api.AuthApi(api_client)
    user_create_request = UserCreateRequest(
        username="username_example",
        password="password_example",
        email="email_example",
        firstname="firstname_example",
        lastname="lastname_example",
        admin=True,
    ) # UserCreateRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_password(user_create_request)
        pprint(api_response)
    except mms_python_client.ApiException as e:
        print("Exception when calling AuthApi->update_password: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_create_request** | [**UserCreateRequest**](UserCreateRequest.md)|  |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

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

# **update_project_permissions**
> PermissionUpdatesResponse update_project_permissions(project_id, permissions_request)



### Example

* Basic Authentication (basicAuth):
* Bearer (JWT) Authentication (bearerToken):

```python
import time
import mms_python_client
from mms_python_client.api import auth_api
from mms_python_client.model.permission_updates_response import PermissionUpdatesResponse
from mms_python_client.model.permissions_request import PermissionsRequest
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
    api_instance = auth_api.AuthApi(api_client)
    project_id = "projectId_example" # str | 
    permissions_request = PermissionsRequest(
        users=PermissionUpdateRequest(
            action="MODIFY",
            permissions=[
                Permission(
                    name="name_example",
                    role="role_example",
                ),
            ],
        ),
        groups=PermissionUpdateRequest(
            action="MODIFY",
            permissions=[
                Permission(
                    name="name_example",
                    role="role_example",
                ),
            ],
        ),
        inherit=True,
        public=True,
    ) # PermissionsRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_project_permissions(project_id, permissions_request)
        pprint(api_response)
    except mms_python_client.ApiException as e:
        print("Exception when calling AuthApi->update_project_permissions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **permissions_request** | [**PermissionsRequest**](PermissionsRequest.md)|  |

### Return type

[**PermissionUpdatesResponse**](PermissionUpdatesResponse.md)

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

