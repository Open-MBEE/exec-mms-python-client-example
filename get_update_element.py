#!/bin/env python

import os
import time
import mms_python_client
from mms_python_client.api import elements_api
from mms_python_client.model.elements_response import ElementsResponse
from mms_python_client.model.elements_request import ElementsRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = mms_python_client.Configuration(
    host = "https://YOUR-MMS-SERVER-ADDRESS",
    username = os.environ.get('MMS_CREDS_USR'),
    password = os.environ.get('MMS_CREDS_PSW')
)

configuration.verify_ssl = False
configuration.ssl_ca_cert = None
configuration.assert_hostname = False
configuration.cert_file = None

# Enter a context with an instance of the API client
with mms_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_api.ElementsApi(api_client)
    project_id = "SOME-PROJECT-ID" # str | 
    ref_id = "master" # str | 
    element_id = "SOME-ELEMENT-ID" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_element(project_id, ref_id, element_id)
        element = api_response.elements[0]

        pprint(element)

        element.name = "Name Changed"

        elements_request = ElementsRequest(
            source="Python Client Example",
            comment="This is a commit message",
            elements=[
                element
            ],
        )

        try:
            element_response = api_instance.create_or_update_elements(project_id, ref_id, elements_request)
            pprint(element_response)
        except mms_python_client.ApiException as e:
            print("Exception when calling ElementsApi->create_or_update_elements: %s\n" % e)
    except mms_python_client.ApiException as e:
        print("Exception when calling ElementsApi->get_element: %s\n" % e)
