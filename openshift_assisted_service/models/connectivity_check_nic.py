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


from typing import List, Optional
from pydantic import BaseModel, StrictStr, conlist, constr, validator

class ConnectivityCheckNic(BaseModel):
    """
    ConnectivityCheckNic
    """
    name: Optional[StrictStr] = None
    mac: Optional[StrictStr] = None
    ip_addresses: Optional[conlist(constr(strict=True))] = None
    __properties = ["name", "mac", "ip_addresses"]

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
    def from_json(cls, json_str: str) -> ConnectivityCheckNic:
        """Create an instance of ConnectivityCheckNic from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ConnectivityCheckNic:
        """Create an instance of ConnectivityCheckNic from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ConnectivityCheckNic.parse_obj(obj)

        _obj = ConnectivityCheckNic.parse_obj({
            "name": obj.get("name"),
            "mac": obj.get("mac"),
            "ip_addresses": obj.get("ip_addresses")
        })
        return _obj


