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





class LogsType(str, Enum):
    """
    LogsType
    """

    """
    allowed enum values
    """
    HOST = 'host'
    CONTROLLER = 'controller'
    ALL = 'all'
    EMPTY = ''

    @classmethod
    def from_json(cls, json_str: str) -> LogsType:
        """Create an instance of LogsType from a JSON string"""
        return LogsType(json.loads(json_str))


