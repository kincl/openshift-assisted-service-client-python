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
from openshift_assisted_service.models.api_vip_connectivity_response import ApiVipConnectivityResponse  # noqa: E501
from openshift_assisted_service.rest import ApiException

class TestApiVipConnectivityResponse(unittest.TestCase):
    """ApiVipConnectivityResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ApiVipConnectivityResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiVipConnectivityResponse`
        """
        model = openshift_assisted_service.models.api_vip_connectivity_response.ApiVipConnectivityResponse()  # noqa: E501
        if include_optional :
            return ApiVipConnectivityResponse(
                is_success = True, 
                url = '', 
                download_error = '', 
                ignition = ''
            )
        else :
            return ApiVipConnectivityResponse(
        )
        """

    def testApiVipConnectivityResponse(self):
        """Test ApiVipConnectivityResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
