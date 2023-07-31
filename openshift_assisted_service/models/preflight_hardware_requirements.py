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
from pydantic import BaseModel, Field, conlist
from openshift_assisted_service.models.host_type_hardware_requirements_wrapper import HostTypeHardwareRequirementsWrapper
from openshift_assisted_service.models.operator_hardware_requirements import OperatorHardwareRequirements

class PreflightHardwareRequirements(BaseModel):
    """
    PreflightHardwareRequirements
    """
    operators: Optional[conlist(OperatorHardwareRequirements)] = Field(None, description="Preflight operators hardware requirements")
    ocp: Optional[HostTypeHardwareRequirementsWrapper] = None
    __properties = ["operators", "ocp"]

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
    def from_json(cls, json_str: str) -> PreflightHardwareRequirements:
        """Create an instance of PreflightHardwareRequirements from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in operators (list)
        _items = []
        if self.operators:
            for _item in self.operators:
                if _item:
                    _items.append(_item.to_dict())
            _dict['operators'] = _items
        # override the default output from pydantic by calling `to_dict()` of ocp
        if self.ocp:
            _dict['ocp'] = self.ocp.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PreflightHardwareRequirements:
        """Create an instance of PreflightHardwareRequirements from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PreflightHardwareRequirements.parse_obj(obj)

        _obj = PreflightHardwareRequirements.parse_obj({
            "operators": [OperatorHardwareRequirements.from_dict(_item) for _item in obj.get("operators")] if obj.get("operators") is not None else None,
            "ocp": HostTypeHardwareRequirementsWrapper.from_dict(obj.get("ocp")) if obj.get("ocp") is not None else None
        })
        return _obj


