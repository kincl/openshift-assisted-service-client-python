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
from openshift_assisted_service.models.connectivity_report import ConnectivityReport  # noqa: E501
from openshift_assisted_service.rest import ApiException

class TestConnectivityReport(unittest.TestCase):
    """ConnectivityReport unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ConnectivityReport
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConnectivityReport`
        """
        model = openshift_assisted_service.models.connectivity_report.ConnectivityReport()  # noqa: E501
        if include_optional :
            return ConnectivityReport(
                remote_hosts = [
                    openshift_assisted_service.models.connectivity_remote_host.connectivity-remote-host(
                        host_id = '', 
                        l2_connectivity = [
                            openshift_assisted_service.models.l2_connectivity.l2-connectivity(
                                outgoing_nic = '', 
                                outgoing_ip_address = '', 
                                remote_ip_address = '', 
                                remote_mac = '', 
                                successful = True, )
                            ], 
                        l3_connectivity = [
                            openshift_assisted_service.models.l3_connectivity.l3-connectivity(
                                outgoing_nic = '', 
                                remote_ip_address = '', 
                                successful = True, 
                                average_rtt_ms = 1.337, 
                                packet_loss_percentage = 1.337, )
                            ], )
                    ]
            )
        else :
            return ConnectivityReport(
        )
        """

    def testConnectivityReport(self):
        """Test ConnectivityReport"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
