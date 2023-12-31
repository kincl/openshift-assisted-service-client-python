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
from openshift_assisted_service.models.operator_host_requirements import OperatorHostRequirements  # noqa: E501
from openshift_assisted_service.rest import ApiException

class TestOperatorHostRequirements(unittest.TestCase):
    """OperatorHostRequirements unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test OperatorHostRequirements
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OperatorHostRequirements`
        """
        model = openshift_assisted_service.models.operator_host_requirements.OperatorHostRequirements()  # noqa: E501
        if include_optional :
            return OperatorHostRequirements(
                operator_name = '', 
                requirements = openshift_assisted_service.models.cluster_host_requirements_details.cluster-host-requirements-details(
                    cpu_cores = 56, 
                    ram_mib = 56, 
                    disk_size_gb = 56, 
                    installation_disk_speed_threshold_ms = 56, 
                    network_latency_threshold_ms = 1.337, 
                    packet_loss_percentage = 1.337, 
                    tpm_enabled_in_bios = True, )
            )
        else :
            return OperatorHostRequirements(
        )
        """

    def testOperatorHostRequirements(self):
        """Test OperatorHostRequirements"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
