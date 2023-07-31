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
from openshift_assisted_service.models.upgrade_agent_response import UpgradeAgentResponse  # noqa: E501
from openshift_assisted_service.rest import ApiException

class TestUpgradeAgentResponse(unittest.TestCase):
    """UpgradeAgentResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UpgradeAgentResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpgradeAgentResponse`
        """
        model = openshift_assisted_service.models.upgrade_agent_response.UpgradeAgentResponse()  # noqa: E501
        if include_optional :
            return UpgradeAgentResponse(
                agent_image = '', 
                result = 'success'
            )
        else :
            return UpgradeAgentResponse(
        )
        """

    def testUpgradeAgentResponse(self):
        """Test UpgradeAgentResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
