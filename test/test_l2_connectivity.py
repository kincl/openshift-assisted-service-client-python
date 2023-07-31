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
from openshift_assisted_service.models.l2_connectivity import L2Connectivity  # noqa: E501
from openshift_assisted_service.rest import ApiException

class TestL2Connectivity(unittest.TestCase):
    """L2Connectivity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test L2Connectivity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `L2Connectivity`
        """
        model = openshift_assisted_service.models.l2_connectivity.L2Connectivity()  # noqa: E501
        if include_optional :
            return L2Connectivity(
                outgoing_nic = '', 
                outgoing_ip_address = '', 
                remote_ip_address = '', 
                remote_mac = '', 
                successful = True
            )
        else :
            return L2Connectivity(
        )
        """

    def testL2Connectivity(self):
        """Test L2Connectivity"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()