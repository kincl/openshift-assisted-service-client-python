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
from pydantic import BaseModel, Field, StrictStr

class IgnitionEndpoint(BaseModel):
    """
    Explicit ignition endpoint overrides the default ignition endpoint.
    """
    url: Optional[StrictStr] = Field(None, description="The URL for the ignition endpoint.")
    ca_certificate: Optional[StrictStr] = Field(None, description="base64 encoded CA certficate to be used when contacting the URL via https.")
    __properties = ["url", "ca_certificate"]

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
    def from_json(cls, json_str: str) -> IgnitionEndpoint:
        """Create an instance of IgnitionEndpoint from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if url (nullable) is None
        # and __fields_set__ contains the field
        if self.url is None and "url" in self.__fields_set__:
            _dict['url'] = None

        # set to None if ca_certificate (nullable) is None
        # and __fields_set__ contains the field
        if self.ca_certificate is None and "ca_certificate" in self.__fields_set__:
            _dict['ca_certificate'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> IgnitionEndpoint:
        """Create an instance of IgnitionEndpoint from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return IgnitionEndpoint.parse_obj(obj)

        _obj = IgnitionEndpoint.parse_obj({
            "url": obj.get("url"),
            "ca_certificate": obj.get("ca_certificate")
        })
        return _obj

