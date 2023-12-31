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

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr
from openshift_assisted_service.models.operator_status import OperatorStatus
from openshift_assisted_service.models.operator_type import OperatorType

class MonitoredOperator(BaseModel):
    """
    MonitoredOperator
    """
    cluster_id: Optional[StrictStr] = Field(None, description="The cluster that this operator is associated with.")
    name: Optional[StrictStr] = Field(None, description="Unique name of the operator.")
    version: Optional[StrictStr] = Field(None, description="Operator version")
    namespace: Optional[StrictStr] = Field(None, description="Namespace where to deploy an operator. Only some operators require a namespace.")
    subscription_name: Optional[StrictStr] = Field(None, description="The name of the subscription of the operator.")
    operator_type: Optional[OperatorType] = None
    properties: Optional[StrictStr] = Field(None, description="Blob of operator-dependent parameters that are required for installation.")
    timeout_seconds: Optional[StrictInt] = Field(None, description="Positive number represents a timeout in seconds for the operator to be available.")
    status: Optional[OperatorStatus] = None
    status_info: Optional[StrictStr] = Field(None, description="Detailed information about the operator state.")
    status_updated_at: Optional[datetime] = Field(None, description="Time at which the operator was last updated.")
    __properties = ["cluster_id", "name", "version", "namespace", "subscription_name", "operator_type", "properties", "timeout_seconds", "status", "status_info", "status_updated_at"]

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
    def from_json(cls, json_str: str) -> MonitoredOperator:
        """Create an instance of MonitoredOperator from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MonitoredOperator:
        """Create an instance of MonitoredOperator from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MonitoredOperator.parse_obj(obj)

        _obj = MonitoredOperator.parse_obj({
            "cluster_id": obj.get("cluster_id"),
            "name": obj.get("name"),
            "version": obj.get("version"),
            "namespace": obj.get("namespace"),
            "subscription_name": obj.get("subscription_name"),
            "operator_type": obj.get("operator_type"),
            "properties": obj.get("properties"),
            "timeout_seconds": obj.get("timeout_seconds"),
            "status": obj.get("status"),
            "status_info": obj.get("status_info"),
            "status_updated_at": obj.get("status_updated_at")
        })
        return _obj


