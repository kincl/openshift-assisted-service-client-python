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
from openshift_assisted_service.models.installer_args_params import InstallerArgsParams  # noqa: E501
from openshift_assisted_service.rest import ApiException

class TestInstallerArgsParams(unittest.TestCase):
    """InstallerArgsParams unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InstallerArgsParams
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InstallerArgsParams`
        """
        model = openshift_assisted_service.models.installer_args_params.InstallerArgsParams()  # noqa: E501
        if include_optional :
            return InstallerArgsParams(
                args = [--append-karg, ip=192.0.2.2::192.0.2.254:255.255.255.0:core0.example.com:enp1s0:none, --save-partindex, 1, -n]
            )
        else :
            return InstallerArgsParams(
        )
        """

    def testInstallerArgsParams(self):
        """Test InstallerArgsParams"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
