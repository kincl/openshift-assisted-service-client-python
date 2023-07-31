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
from openshift_assisted_service.models.operator_create_params import OperatorCreateParams  # noqa: E501
from openshift_assisted_service.rest import ApiException

class TestOperatorCreateParams(unittest.TestCase):
    """OperatorCreateParams unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test OperatorCreateParams
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OperatorCreateParams`
        """
        model = openshift_assisted_service.models.operator_create_params.OperatorCreateParams()  # noqa: E501
        if include_optional :
            return OperatorCreateParams(
                name = '', 
                properties = ''
            )
        else :
            return OperatorCreateParams(
        )
        """

    def testOperatorCreateParams(self):
        """Test OperatorCreateParams"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
