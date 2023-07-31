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





class HostRole(str, Enum):
    """
    HostRole
    """

    """
    allowed enum values
    """
    AUTO_MINUS_ASSIGN = 'auto-assign'
    MASTER = 'master'
    WORKER = 'worker'
    BOOTSTRAP = 'bootstrap'

    @classmethod
    def from_json(cls, json_str: str) -> HostRole:
        """Create an instance of HostRole from a JSON string"""
        return HostRole(json.loads(json_str))

