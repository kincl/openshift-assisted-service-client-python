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
from pydantic import BaseModel, Field, StrictInt, StrictStr

class DiskSpeedCheckResponse(BaseModel):
    """
    DiskSpeedCheckResponse
    """
    io_sync_duration: Optional[StrictInt] = Field(None, description="The 99th percentile of fdatasync durations in milliseconds.")
    path: Optional[StrictStr] = Field(None, description="The device path.")
    __properties = ["io_sync_duration", "path"]

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
    def from_json(cls, json_str: str) -> DiskSpeedCheckResponse:
        """Create an instance of DiskSpeedCheckResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DiskSpeedCheckResponse:
        """Create an instance of DiskSpeedCheckResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DiskSpeedCheckResponse.parse_obj(obj)

        _obj = DiskSpeedCheckResponse.parse_obj({
            "io_sync_duration": obj.get("io_sync_duration"),
            "path": obj.get("path")
        })
        return _obj

