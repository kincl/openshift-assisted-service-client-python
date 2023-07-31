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


from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictStr

class Usage(BaseModel):
    """
    Usage
    """
    id: Optional[StrictStr] = Field(None, description="Unique idenftifier of the feature")
    name: Optional[StrictStr] = Field(None, description="name of the feature to track")
    data: Optional[Dict[str, Dict[str, Any]]] = Field(None, description="additional properties of the feature")
    __properties = ["id", "name", "data"]

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
    def from_json(cls, json_str: str) -> Usage:
        """Create an instance of Usage from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Usage:
        """Create an instance of Usage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Usage.parse_obj(obj)

        _obj = Usage.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "data": obj.get("data")
        })
        return _obj


