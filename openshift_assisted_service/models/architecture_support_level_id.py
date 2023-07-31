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





class ArchitectureSupportLevelId(str, Enum):
    """
    ArchitectureSupportLevelId
    """

    """
    allowed enum values
    """
    X86_64_ARCHITECTURE = 'X86_64_ARCHITECTURE'
    ARM64_ARCHITECTURE = 'ARM64_ARCHITECTURE'
    PPC64_LE_ARCHITECTURE = 'PPC64LE_ARCHITECTURE'
    S390_X_ARCHITECTURE = 'S390X_ARCHITECTURE'
    MULTIARCH_RELEASE_IMAGE = 'MULTIARCH_RELEASE_IMAGE'

    @classmethod
    def from_json(cls, json_str: str) -> ArchitectureSupportLevelId:
        """Create an instance of ArchitectureSupportLevelId from a JSON string"""
        return ArchitectureSupportLevelId(json.loads(json_str))

