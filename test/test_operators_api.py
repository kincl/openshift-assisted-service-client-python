# coding: utf-8

"""
    AssistedInstall

    Assisted installation  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest

import openshift_assisted_service
from openshift_assisted_service.api.operators_api import OperatorsApi  # noqa: E501
from openshift_assisted_service.rest import ApiException


class TestOperatorsApi(unittest.TestCase):
    """OperatorsApi unit test stubs"""

    def setUp(self):
        self.api = openshift_assisted_service.api.operators_api.OperatorsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_v2_list_of_cluster_operators(self):
        """Test case for v2_list_of_cluster_operators

        """
        pass

    def test_v2_list_operator_properties(self):
        """Test case for v2_list_operator_properties

        """
        pass

    def test_v2_list_supported_operators(self):
        """Test case for v2_list_supported_operators

        """
        pass

    def test_v2_report_monitored_operator_status(self):
        """Test case for v2_report_monitored_operator_status

        """
        pass


if __name__ == '__main__':
    unittest.main()
