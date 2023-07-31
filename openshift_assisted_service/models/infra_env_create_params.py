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
from pydantic import BaseModel, Field, StrictStr, conlist, constr, validator
from openshift_assisted_service.models.host_static_network_config import HostStaticNetworkConfig
from openshift_assisted_service.models.image_type import ImageType
from openshift_assisted_service.models.kernel_argument import KernelArgument
from openshift_assisted_service.models.proxy import Proxy

class InfraEnvCreateParams(BaseModel):
    """
    InfraEnvCreateParams
    """
    name: StrictStr = Field(..., description="Name of the infra-env.")
    proxy: Optional[Proxy] = None
    additional_ntp_sources: Optional[StrictStr] = Field(None, description="A comma-separated list of NTP sources (name or IP) going to be added to all the hosts.")
    ssh_authorized_key: Optional[StrictStr] = Field(None, description="SSH public key for debugging the installation.")
    pull_secret: StrictStr = Field(..., description="The pull secret obtained from Red Hat OpenShift Cluster Manager at console.redhat.com/openshift/install/pull-secret.")
    static_network_config: Optional[conlist(HostStaticNetworkConfig)] = None
    image_type: Optional[ImageType] = None
    ignition_config_override: Optional[StrictStr] = Field(None, description="JSON formatted string containing the user overrides for the initial ignition config.")
    cluster_id: Optional[StrictStr] = Field(None, description="If set, all hosts that register will be associated with the specified cluster.")
    openshift_version: Optional[StrictStr] = Field(None, description="Version of the OpenShift cluster (used to infer the RHCOS version - temporary until generic logic implemented).")
    cpu_architecture: Optional[StrictStr] = Field('x86_64', description="The CPU architecture of the image (x86_64/arm64/etc).")
    kernel_arguments: Optional[conlist(KernelArgument)] = Field(None, description="List of kernel arugment objects that define the operations and values to be applied.")
    additional_trust_bundle: Optional[constr(strict=True, max_length=65535)] = Field(None, description="PEM-encoded X.509 certificate bundle. Hosts discovered by this infra-env will trust the certificates in this bundle. Clusters formed from the hosts discovered by this infra-env will also trust the certificates in this bundle.")
    __properties = ["name", "proxy", "additional_ntp_sources", "ssh_authorized_key", "pull_secret", "static_network_config", "image_type", "ignition_config_override", "cluster_id", "openshift_version", "cpu_architecture", "kernel_arguments", "additional_trust_bundle"]

    @validator('cpu_architecture')
    def cpu_architecture_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('x86_64', 'aarch64', 'arm64', 'ppc64le', 's390x'):
            raise ValueError("must be one of enum values ('x86_64', 'aarch64', 'arm64', 'ppc64le', 's390x')")
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
    def from_json(cls, json_str: str) -> InfraEnvCreateParams:
        """Create an instance of InfraEnvCreateParams from a JSON string"""
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

        # set to None if cluster_id (nullable) is None
        # and __fields_set__ contains the field
        if self.cluster_id is None and "cluster_id" in self.__fields_set__:
            _dict['cluster_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> InfraEnvCreateParams:
        """Create an instance of InfraEnvCreateParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return InfraEnvCreateParams.parse_obj(obj)

        _obj = InfraEnvCreateParams.parse_obj({
            "name": obj.get("name"),
            "proxy": Proxy.from_dict(obj.get("proxy")) if obj.get("proxy") is not None else None,
            "additional_ntp_sources": obj.get("additional_ntp_sources"),
            "ssh_authorized_key": obj.get("ssh_authorized_key"),
            "pull_secret": obj.get("pull_secret"),
            "static_network_config": [HostStaticNetworkConfig.from_dict(_item) for _item in obj.get("static_network_config")] if obj.get("static_network_config") is not None else None,
            "image_type": obj.get("image_type"),
            "ignition_config_override": obj.get("ignition_config_override"),
            "cluster_id": obj.get("cluster_id"),
            "openshift_version": obj.get("openshift_version"),
            "cpu_architecture": obj.get("cpu_architecture") if obj.get("cpu_architecture") is not None else 'x86_64',
            "kernel_arguments": [KernelArgument.from_dict(_item) for _item in obj.get("kernel_arguments")] if obj.get("kernel_arguments") is not None else None,
            "additional_trust_bundle": obj.get("additional_trust_bundle")
        })
        return _obj

