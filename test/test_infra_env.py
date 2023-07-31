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
from openshift_assisted_service.models.infra_env import InfraEnv  # noqa: E501
from openshift_assisted_service.rest import ApiException

class TestInfraEnv(unittest.TestCase):
    """InfraEnv unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InfraEnv
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InfraEnv`
        """
        model = openshift_assisted_service.models.infra_env.InfraEnv()  # noqa: E501
        if include_optional :
            return InfraEnv(
                kind = 'InfraEnv', 
                id = '', 
                href = '', 
                openshift_version = '', 
                name = '', 
                user_name = '', 
                org_id = '', 
                email_domain = '', 
                proxy = openshift_assisted_service.models.proxy.proxy(
                    http_proxy = '', 
                    https_proxy = '', 
                    no_proxy = '', ), 
                additional_ntp_sources = '', 
                ssh_authorized_key = '', 
                pull_secret_set = True, 
                static_network_config = '', 
                type = 'full-iso', 
                ignition_config_override = '', 
                cluster_id = '', 
                size_bytes = 0, 
                download_url = '', 
                generator_version = '', 
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                expires_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                cpu_architecture = 'x86_64', 
                kernel_arguments = '', 
                additional_trust_bundle = ''
            )
        else :
            return InfraEnv(
                kind = 'InfraEnv',
                id = '',
                href = '',
                name = '',
                type = 'full-iso',
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testInfraEnv(self):
        """Test InfraEnv"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()