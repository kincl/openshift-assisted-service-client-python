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





class OperatorStatus(str, Enum):
    """
    Represents the operator state.
    """

    """
    allowed enum values
    """
    FAILED = 'failed'
    PROGRESSING = 'progressing'
    AVAILABLE = 'available'

    @classmethod
    def from_json(cls, json_str: str) -> OperatorStatus:
        """Create an instance of OperatorStatus from a JSON string"""
        return OperatorStatus(json.loads(json_str))


