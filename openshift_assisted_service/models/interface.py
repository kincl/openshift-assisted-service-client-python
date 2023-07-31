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
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr, conlist

class Interface(BaseModel):
    """
    Interface
    """
    ipv6_addresses: Optional[conlist(StrictStr)] = None
    vendor: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    has_carrier: Optional[StrictBool] = None
    product: Optional[StrictStr] = None
    mtu: Optional[StrictInt] = None
    ipv4_addresses: Optional[conlist(StrictStr)] = None
    biosdevname: Optional[StrictStr] = None
    client_id: Optional[StrictStr] = None
    mac_address: Optional[StrictStr] = None
    flags: Optional[conlist(StrictStr)] = None
    speed_mbps: Optional[StrictInt] = None
    type: Optional[StrictStr] = None
    __properties = ["ipv6_addresses", "vendor", "name", "has_carrier", "product", "mtu", "ipv4_addresses", "biosdevname", "client_id", "mac_address", "flags", "speed_mbps", "type"]

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
    def from_json(cls, json_str: str) -> Interface:
        """Create an instance of Interface from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Interface:
        """Create an instance of Interface from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Interface.parse_obj(obj)

        _obj = Interface.parse_obj({
            "ipv6_addresses": obj.get("ipv6_addresses"),
            "vendor": obj.get("vendor"),
            "name": obj.get("name"),
            "has_carrier": obj.get("has_carrier"),
            "product": obj.get("product"),
            "mtu": obj.get("mtu"),
            "ipv4_addresses": obj.get("ipv4_addresses"),
            "biosdevname": obj.get("biosdevname"),
            "client_id": obj.get("client_id"),
            "mac_address": obj.get("mac_address"),
            "flags": obj.get("flags"),
            "speed_mbps": obj.get("speed_mbps"),
            "type": obj.get("type")
        })
        return _obj


