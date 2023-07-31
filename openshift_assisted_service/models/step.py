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
from pydantic import BaseModel, StrictStr, conlist
from openshift_assisted_service.models.step_type import StepType

class Step(BaseModel):
    """
    Step
    """
    step_type: Optional[StepType] = None
    step_id: Optional[StrictStr] = None
    args: Optional[conlist(StrictStr)] = None
    __properties = ["step_type", "step_id", "args"]

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
    def from_json(cls, json_str: str) -> Step:
        """Create an instance of Step from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Step:
        """Create an instance of Step from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Step.parse_obj(obj)

        _obj = Step.parse_obj({
            "step_type": obj.get("step_type"),
            "step_id": obj.get("step_id"),
            "args": obj.get("args")
        })
        return _obj

