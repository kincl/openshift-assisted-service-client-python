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
from openshift_assisted_service.api.managed_domains_api import ManagedDomainsApi  # noqa: E501
from openshift_assisted_service.rest import ApiException


class TestManagedDomainsApi(unittest.TestCase):
    """ManagedDomainsApi unit test stubs"""

    def setUp(self):
        self.api = openshift_assisted_service.api.managed_domains_api.ManagedDomainsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_v2_list_managed_domains(self):
        """Test case for v2_list_managed_domains

        """
        pass


if __name__ == '__main__':
    unittest.main()
