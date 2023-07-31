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


from typing import List
from pydantic import BaseModel, Field, conlist
from openshift_assisted_service.models.domain_resolution_request_domains_inner import DomainResolutionRequestDomainsInner

class DomainResolutionRequest(BaseModel):
    """
    DomainResolutionRequest
    """
    domains: conlist(DomainResolutionRequestDomainsInner) = Field(...)
    __properties = ["domains"]

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
    def from_json(cls, json_str: str) -> DomainResolutionRequest:
        """Create an instance of DomainResolutionRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in domains (list)
        _items = []
        if self.domains:
            for _item in self.domains:
                if _item:
                    _items.append(_item.to_dict())
            _dict['domains'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DomainResolutionRequest:
        """Create an instance of DomainResolutionRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DomainResolutionRequest.parse_obj(obj)

        _obj = DomainResolutionRequest.parse_obj({
            "domains": [DomainResolutionRequestDomainsInner.from_dict(_item) for _item in obj.get("domains")] if obj.get("domains") is not None else None
        })
        return _obj

