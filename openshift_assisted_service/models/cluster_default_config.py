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
from pydantic import BaseModel, Field, StrictInt, StrictStr, conint, conlist, constr, validator
from openshift_assisted_service.models.cluster_network import ClusterNetwork
from openshift_assisted_service.models.service_network import ServiceNetwork

class ClusterDefaultConfig(BaseModel):
    """
    ClusterDefaultConfig
    """
    cluster_network_cidr: Optional[constr(strict=True)] = None
    cluster_network_host_prefix: Optional[conint(strict=True, le=32, ge=1)] = None
    inactive_deletion_hours: Optional[StrictInt] = None
    service_network_cidr: Optional[constr(strict=True)] = None
    ntp_source: Optional[StrictStr] = None
    cluster_networks_ipv4: Optional[conlist(ClusterNetwork)] = None
    cluster_networks_dualstack: Optional[conlist(ClusterNetwork)] = None
    service_networks_ipv4: Optional[conlist(ServiceNetwork)] = None
    service_networks_dualstack: Optional[conlist(ServiceNetwork)] = None
    forbidden_hostnames: Optional[conlist(StrictStr)] = Field(None, description="This provides a list of forbidden hostnames. If this list is empty or not present, this implies that the UI should fall back to a hard coded list.")
    __properties = ["cluster_network_cidr", "cluster_network_host_prefix", "inactive_deletion_hours", "service_network_cidr", "ntp_source", "cluster_networks_ipv4", "cluster_networks_dualstack", "service_networks_ipv4", "service_networks_dualstack", "forbidden_hostnames"]

    @validator('cluster_network_cidr')
    def cluster_network_cidr_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)[\/]([1-9]|[1-2][0-9]|3[0-2]?)$", value):
            raise ValueError(r"must validate the regular expression /^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)[\/]([1-9]|[1-2][0-9]|3[0-2]?)$/")
        return value

    @validator('service_network_cidr')
    def service_network_cidr_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)[\/]([1-9]|[1-2][0-9]|3[0-2]?)$", value):
            raise ValueError(r"must validate the regular expression /^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)[\/]([1-9]|[1-2][0-9]|3[0-2]?)$/")
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
    def from_json(cls, json_str: str) -> ClusterDefaultConfig:
        """Create an instance of ClusterDefaultConfig from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in cluster_networks_ipv4 (list)
        _items = []
        if self.cluster_networks_ipv4:
            for _item in self.cluster_networks_ipv4:
                if _item:
                    _items.append(_item.to_dict())
            _dict['cluster_networks_ipv4'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in cluster_networks_dualstack (list)
        _items = []
        if self.cluster_networks_dualstack:
            for _item in self.cluster_networks_dualstack:
                if _item:
                    _items.append(_item.to_dict())
            _dict['cluster_networks_dualstack'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in service_networks_ipv4 (list)
        _items = []
        if self.service_networks_ipv4:
            for _item in self.service_networks_ipv4:
                if _item:
                    _items.append(_item.to_dict())
            _dict['service_networks_ipv4'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in service_networks_dualstack (list)
        _items = []
        if self.service_networks_dualstack:
            for _item in self.service_networks_dualstack:
                if _item:
                    _items.append(_item.to_dict())
            _dict['service_networks_dualstack'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ClusterDefaultConfig:
        """Create an instance of ClusterDefaultConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ClusterDefaultConfig.parse_obj(obj)

        _obj = ClusterDefaultConfig.parse_obj({
            "cluster_network_cidr": obj.get("cluster_network_cidr"),
            "cluster_network_host_prefix": obj.get("cluster_network_host_prefix"),
            "inactive_deletion_hours": obj.get("inactive_deletion_hours"),
            "service_network_cidr": obj.get("service_network_cidr"),
            "ntp_source": obj.get("ntp_source"),
            "cluster_networks_ipv4": [ClusterNetwork.from_dict(_item) for _item in obj.get("cluster_networks_ipv4")] if obj.get("cluster_networks_ipv4") is not None else None,
            "cluster_networks_dualstack": [ClusterNetwork.from_dict(_item) for _item in obj.get("cluster_networks_dualstack")] if obj.get("cluster_networks_dualstack") is not None else None,
            "service_networks_ipv4": [ServiceNetwork.from_dict(_item) for _item in obj.get("service_networks_ipv4")] if obj.get("service_networks_ipv4") is not None else None,
            "service_networks_dualstack": [ServiceNetwork.from_dict(_item) for _item in obj.get("service_networks_dualstack")] if obj.get("service_networks_dualstack") is not None else None,
            "forbidden_hostnames": obj.get("forbidden_hostnames")
        })
        return _obj


