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
from openshift_assisted_service.api.versions_api import VersionsApi  # noqa: E501
from openshift_assisted_service.rest import ApiException


class TestVersionsApi(unittest.TestCase):
    """VersionsApi unit test stubs"""

    def setUp(self):
        self.api = openshift_assisted_service.api.versions_api.VersionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_v2_list_component_versions(self):
        """Test case for v2_list_component_versions

        """
        pass

    def test_v2_list_supported_openshift_versions(self):
        """Test case for v2_list_supported_openshift_versions

        """
        pass


if __name__ == '__main__':
    unittest.main()
