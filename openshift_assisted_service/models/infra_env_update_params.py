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
from pydantic import BaseModel, Field, StrictStr, conlist, constr
from openshift_assisted_service.models.host_static_network_config import HostStaticNetworkConfig
from openshift_assisted_service.models.image_type import ImageType
from openshift_assisted_service.models.kernel_argument import KernelArgument
from openshift_assisted_service.models.proxy import Proxy

class InfraEnvUpdateParams(BaseModel):
    """
    InfraEnvUpdateParams
    """
    proxy: Optional[Proxy] = None
    additional_ntp_sources: Optional[StrictStr] = Field(None, description="A comma-separated list of NTP sources (name or IP) going to be added to all the hosts.")
    ssh_authorized_key: Optional[StrictStr] = Field(None, description="SSH public key for debugging the installation.")
    pull_secret: Optional[StrictStr] = Field(None, description="The pull secret obtained from Red Hat OpenShift Cluster Manager at console.redhat.com/openshift/install/pull-secret.")
    static_network_config: Optional[conlist(HostStaticNetworkConfig)] = None
    image_type: Optional[ImageType] = None
    ignition_config_override: Optional[StrictStr] = Field(None, description="JSON formatted string containing the user overrides for the initial ignition config.")
    kernel_arguments: Optional[conlist(KernelArgument)] = Field(None, description="List of kernel arugment objects that define the operations and values to be applied.")
    additional_trust_bundle: Optional[constr(strict=True, max_length=65535)] = Field(None, description="Allows users to change the additional_trust_bundle infra-env field")
    __properties = ["proxy", "additional_ntp_sources", "ssh_authorized_key", "pull_secret", "static_network_config", "image_type", "ignition_config_override", "kernel_arguments", "additional_trust_bundle"]

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
    def from_json(cls, json_str: str) -> InfraEnvUpdateParams:
        """Create an instance of InfraEnvUpdateParams from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of proxy
        if self.proxy:
            _dict['proxy'] = self.proxy.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in static_network_config (list)
        _items = []
        if self.static_network_config:
            for _item in self.static_network_config:
                if _item:
                    _items.append(_item.to_dict())
            _dict['static_network_config'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in kernel_arguments (list)
        _items = []
        if self.kernel_arguments:
            for _item in self.kernel_arguments:
                if _item:
                    _items.append(_item.to_dict())
            _dict['kernel_arguments'] = _items
        # set to None if additional_ntp_sources (nullable) is None
        # and __fields_set__ contains the field
        if self.additional_ntp_sources is None and "additional_ntp_sources" in self.__fields_set__:
            _dict['additional_ntp_sources'] = None

        # set to None if ssh_authorized_key (nullable) is None
        # and __fields_set__ contains the field
        if self.ssh_authorized_key is None and "ssh_authorized_key" in self.__fields_set__:
            _dict['ssh_authorized_key'] = None

        # set to None if additional_trust_bundle (nullable) is None
        # and __fields_set__ contains the field
        if self.additional_trust_bundle is None and "additional_trust_bundle" in self.__fields_set__:
            _dict['additional_trust_bundle'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> InfraEnvUpdateParams:
        """Create an instance of InfraEnvUpdateParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return InfraEnvUpdateParams.parse_obj(obj)

        _obj = InfraEnvUpdateParams.parse_obj({
            "proxy": Proxy.from_dict(obj.get("proxy")) if obj.get("proxy") is not None else None,
            "additional_ntp_sources": obj.get("additional_ntp_sources"),
            "ssh_authorized_key": obj.get("ssh_authorized_key"),
            "pull_secret": obj.get("pull_secret"),
            "static_network_config": [HostStaticNetworkConfig.from_dict(_item) for _item in obj.get("static_network_config")] if obj.get("static_network_config") is not None else None,
            "image_type": obj.get("image_type"),
            "ignition_config_override": obj.get("ignition_config_override"),
            "kernel_arguments": [KernelArgument.from_dict(_item) for _item in obj.get("kernel_arguments")] if obj.get("kernel_arguments") is not None else None,
            "additional_trust_bundle": obj.get("additional_trust_bundle")
        })
        return _obj


