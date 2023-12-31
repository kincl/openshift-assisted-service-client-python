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
from openshift_assisted_service.models.container_image_availability_request import ContainerImageAvailabilityRequest  # noqa: E501
from openshift_assisted_service.rest import ApiException

class TestContainerImageAvailabilityRequest(unittest.TestCase):
    """ContainerImageAvailabilityRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ContainerImageAvailabilityRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ContainerImageAvailabilityRequest`
        """
        model = openshift_assisted_service.models.container_image_availability_request.ContainerImageAvailabilityRequest()  # noqa: E501
        if include_optional :
            return ContainerImageAvailabilityRequest(
                timeout = 56, 
                images = [
                    'A9LCS/o81.h5loqtqj-h9xz3do70@_i714-_@842en7idxm6i75z1t7di1ja.orkmt.8vv6f-n615ro.d3hvck0LlJwL5CTL'
                    ]
            )
        else :
            return ContainerImageAvailabilityRequest(
                images = [
                    'A9LCS/o81.h5loqtqj-h9xz3do70@_i714-_@842en7idxm6i75z1t7di1ja.orkmt.8vv6f-n615ro.d3hvck0LlJwL5CTL'
                    ],
        )
        """

    def testContainerImageAvailabilityRequest(self):
        """Test ContainerImageAvailabilityRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
