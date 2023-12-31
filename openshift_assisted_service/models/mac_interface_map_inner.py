# coding: utf-8

"""
    AssistedInstall

    Assisted installation  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr, constr, validator

class MacInterfaceMapInner(BaseModel):
    """
    MacInterfaceMapInner
    """
    mac_address: Optional[constr(strict=True)] = Field(None, description="mac address present on the host")
    logical_nic_name: Optional[StrictStr] = Field(None, description="nic name used in the yaml, which relates 1:1 to the mac address")
    __properties = ["mac_address", "logical_nic_name"]

    @validator('mac_address')
    def mac_address_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^([0-9A-Fa-f]{2}[:]){5}([0-9A-Fa-f]{2})$", value):
            raise ValueError(r"must validate the regular expression /^([0-9A-Fa-f]{2}[:]){5}([0-9A-Fa-f]{2})$/")
        return value

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> MacInterfaceMapInner:
        """Create an instance of MacInterfaceMapInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MacInterfaceMapInner:
        """Create an instance of MacInterfaceMapInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MacInterfaceMapInner.parse_obj(obj)

        _obj = MacInterfaceMapInner.parse_obj({
            "mac_address": obj.get("mac_address"),
            "logical_nic_name": obj.get("logical_nic_name")
        })
        return _obj


