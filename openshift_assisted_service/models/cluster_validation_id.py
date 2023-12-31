# coding: utf-8

"""
    AssistedInstall

    Assisted installation  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class ClusterValidationId(str, Enum):
    """
    ClusterValidationId
    """

    """
    allowed enum values
    """
    MACHINE_MINUS_CIDR_MINUS_DEFINED = 'machine-cidr-defined'
    CLUSTER_MINUS_CIDR_MINUS_DEFINED = 'cluster-cidr-defined'
    SERVICE_MINUS_CIDR_MINUS_DEFINED = 'service-cidr-defined'
    NO_MINUS_CIDRS_MINUS_OVERLAPPING = 'no-cidrs-overlapping'
    NETWORKS_MINUS_SAME_MINUS_ADDRESS_MINUS_FAMILIES = 'networks-same-address-families'
    NETWORK_MINUS_PREFIX_MINUS_VALID = 'network-prefix-valid'
    MACHINE_MINUS_CIDR_MINUS_EQUALS_MINUS_TO_MINUS_CALCULATED_MINUS_CIDR = 'machine-cidr-equals-to-calculated-cidr'
    API_MINUS_VIPS_MINUS_DEFINED = 'api-vips-defined'
    API_MINUS_VIPS_MINUS_VALID = 'api-vips-valid'
    INGRESS_MINUS_VIPS_MINUS_DEFINED = 'ingress-vips-defined'
    INGRESS_MINUS_VIPS_MINUS_VALID = 'ingress-vips-valid'
    ALL_MINUS_HOSTS_MINUS_ARE_MINUS_READY_MINUS_TO_MINUS_INSTALL = 'all-hosts-are-ready-to-install'
    SUFFICIENT_MINUS_MASTERS_MINUS_COUNT = 'sufficient-masters-count'
    DNS_MINUS_DOMAIN_MINUS_DEFINED = 'dns-domain-defined'
    PULL_MINUS_SECRET_MINUS_SET = 'pull-secret-set'
    NTP_MINUS_SERVER_MINUS_CONFIGURED = 'ntp-server-configured'
    LSO_MINUS_REQUIREMENTS_MINUS_SATISFIED = 'lso-requirements-satisfied'
    OCS_MINUS_REQUIREMENTS_MINUS_SATISFIED = 'ocs-requirements-satisfied'
    ODF_MINUS_REQUIREMENTS_MINUS_SATISFIED = 'odf-requirements-satisfied'
    CNV_MINUS_REQUIREMENTS_MINUS_SATISFIED = 'cnv-requirements-satisfied'
    LVM_MINUS_REQUIREMENTS_MINUS_SATISFIED = 'lvm-requirements-satisfied'
    MCE_MINUS_REQUIREMENTS_MINUS_SATISFIED = 'mce-requirements-satisfied'
    NETWORK_MINUS_TYPE_MINUS_VALID = 'network-type-valid'
    PLATFORM_MINUS_REQUIREMENTS_MINUS_SATISFIED = 'platform-requirements-satisfied'

    @classmethod
    def from_json(cls, json_str: str) -> ClusterValidationId:
        """Create an instance of ClusterValidationId from a JSON string"""
        return ClusterValidationId(json.loads(json_str))


