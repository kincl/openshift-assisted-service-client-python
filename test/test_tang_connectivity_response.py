# coding: utf-8

"""
    AssistedInstall

    Assisted installation  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import openshift_assisted_service
from openshift_assisted_service.models.tang_connectivity_response import TangConnectivityResponse  # noqa: E501
from openshift_assisted_service.rest import ApiException

class TestTangConnectivityResponse(unittest.TestCase):
    """TangConnectivityResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TangConnectivityResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TangConnectivityResponse`
        """
        model = openshift_assisted_service.models.tang_connectivity_response.TangConnectivityResponse()  # noqa: E501
        if include_optional :
            return TangConnectivityResponse(
                is_success = True, 
                tang_server_response = [
                    openshift_assisted_service.models.tang_connectivity_response_tang_server_response_inner.tang_connectivity_response_tang_server_response_inner(
                        tang_url = '', 
                        payload = '', 
                        signatures = [
                            openshift_assisted_service.models.tang_connectivity_response_tang_server_response_inner_signatures_inner.tang_connectivity_response_tang_server_response_inner_signatures_inner(
                                protected = '', 
                                signature = '', )
                            ], )
                    ]
            )
        else :
            return TangConnectivityResponse(
        )
        """

    def testTangConnectivityResponse(self):
        """Test TangConnectivityResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
