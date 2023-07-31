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

class DhcpAllocationRequest(BaseModel):
    """
    DhcpAllocationRequest
    """
    interface: StrictStr = Field(..., description="The network interface (NIC) to run the DHCP requests on.")
    api_vip_mac: StrictStr = Field(..., description="MAC address for the API virtual IP.")
    ingress_vip_mac: StrictStr = Field(..., description="MAC address for the Ingress virtual IP.")
    api_vip_lease: Optional[StrictStr] = Field(None, description="Contents of lease file to be used for API virtual IP.")
    ingress_vip_lease: Optional[StrictStr] = Field(None, description="Contents of lease file to be used for for Ingress virtual IP.")
    __properties = ["interface", "api_vip_mac", "ingress_vip_mac", "api_vip_lease", "ingress_vip_lease"]

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
    def from_json(cls, json_str: str) -> DhcpAllocationRequest:
        """Create an instance of DhcpAllocationRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DhcpAllocationRequest:
        """Create an instance of DhcpAllocationRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DhcpAllocationRequest.parse_obj(obj)

        _obj = DhcpAllocationRequest.parse_obj({
            "interface": obj.get("interface"),
            "api_vip_mac": obj.get("api_vip_mac"),
            "ingress_vip_mac": obj.get("ingress_vip_mac"),
            "api_vip_lease": obj.get("api_vip_lease"),
            "ingress_vip_lease": obj.get("ingress_vip_lease")
        })
        return _obj


