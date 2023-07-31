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

class FreeNetworkAddresses(BaseModel):
    """
    FreeNetworkAddresses
    """
    network: Optional[constr(strict=True)] = None
    free_addresses: Optional[conlist(StrictStr)] = None
    __properties = ["network", "free_addresses"]

    @validator('network')
    def network_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^([0-9]{1,3}\.){3}[0-9]{1,3}\/[0-9]|[1-2][0-9]|3[0-2]?$", value):
            raise ValueError(r"must validate the regular expression /^([0-9]{1,3}\.){3}[0-9]{1,3}\/[0-9]|[1-2][0-9]|3[0-2]?$/")
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
    def from_json(cls, json_str: str) -> FreeNetworkAddresses:
        """Create an instance of FreeNetworkAddresses from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FreeNetworkAddresses:
        """Create an instance of FreeNetworkAddresses from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FreeNetworkAddresses.parse_obj(obj)

        _obj = FreeNetworkAddresses.parse_obj({
            "network": obj.get("network"),
            "free_addresses": obj.get("free_addresses")
        })
        return _obj

