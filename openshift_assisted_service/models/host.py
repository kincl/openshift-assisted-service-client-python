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
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist, validator
from openshift_assisted_service.models.host_progress_info import HostProgressInfo
from openshift_assisted_service.models.host_role import HostRole
from openshift_assisted_service.models.host_stage import HostStage
from openshift_assisted_service.models.logs_state import LogsState

class Host(BaseModel):
    """
    Host
    """
    kind: StrictStr = Field(..., description="Indicates the type of this object. Will be 'Host' if this is a complete object or 'HostLink' if it is just a link, or 'AddToExistingClusterHost' for host being added to existing OCP cluster, or ")
    id: StrictStr = Field(..., description="Unique identifier of the object.")
    href: StrictStr = Field(..., description="Self link.")
    cluster_id: Optional[StrictStr] = Field(None, description="The cluster that this host is associated with.")
    infra_env_id: Optional[StrictStr] = Field(None, description="The infra-env that this host is associated with.")
    status: StrictStr = Field(...)
    status_info: StrictStr = Field(...)
    validations_info: Optional[StrictStr] = Field(None, description="JSON-formatted string containing the validation results for each validation id grouped by category (network, hardware, etc.)")
    logs_info: Optional[LogsState] = None
    status_updated_at: Optional[datetime] = Field(None, description="The last time that the host status was updated.")
    progress: Optional[HostProgressInfo] = None
    stage_started_at: Optional[datetime] = Field(None, description="Time at which the current progress stage started.")
    stage_updated_at: Optional[datetime] = Field(None, description="Time at which the current progress stage was last updated.")
    progress_stages: Optional[conlist(HostStage)] = None
    connectivity: Optional[StrictStr] = None
    api_vip_connectivity: Optional[StrictStr] = Field(None, description="Contains a serialized api_vip_connectivity_response")
    tang_connectivity: Optional[StrictStr] = None
    inventory: Optional[StrictStr] = None
    free_addresses: Optional[StrictStr] = None
    ntp_sources: Optional[StrictStr] = Field(None, description="The configured NTP sources on the host.")
    disks_info: Optional[StrictStr] = Field(None, description="Additional information about disks, formatted as JSON.")
    role: Optional[HostRole] = None
    suggested_role: Optional[HostRole] = None
    bootstrap: Optional[StrictBool] = None
    logs_collected_at: Optional[datetime] = None
    logs_started_at: Optional[datetime] = None
    installer_version: Optional[StrictStr] = Field(None, description="Installer version.")
    installation_disk_path: Optional[StrictStr] = Field(None, description="Contains the inventory disk path, This field is replaced by installation_disk_id field and used for backward compatability with the old UI.")
    installation_disk_id: Optional[StrictStr] = Field(None, description="Contains the inventory disk id to install on.")
    updated_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    checked_in_at: Optional[datetime] = Field(None, description="The last time the host's agent communicated with the service.")
    registered_at: Optional[datetime] = Field(None, description="The last time the host's agent tried to register in the service.")
    discovery_agent_version: Optional[StrictStr] = None
    requested_hostname: Optional[StrictStr] = None
    user_name: Optional[StrictStr] = None
    media_status: Optional[StrictStr] = 'connected'
    deleted_at: Optional[Dict[str, Any]] = Field(None, description="swagger:ignore")
    ignition_config_overrides: Optional[StrictStr] = Field(None, description="Json formatted string containing the user overrides for the host's pointer ignition")
    installer_args: Optional[StrictStr] = None
    timestamp: Optional[StrictInt] = Field(None, description="The time on the host as seconds since the Unix epoch.")
    machine_config_pool_name: Optional[StrictStr] = None
    images_status: Optional[StrictStr] = Field(None, description="Array of image statuses.")
    domain_name_resolutions: Optional[StrictStr] = Field(None, description="The domain name resolution result.")
    ignition_endpoint_token_set: Optional[StrictBool] = Field(None, description="True if the token to fetch the ignition from ignition_endpoint_url is set.")
    node_labels: Optional[StrictStr] = Field(None, description="Json containing node's labels.")
    disks_to_be_formatted: Optional[StrictStr] = Field(None, description="A comma-separated list of disks that will be formatted once installation begins, unless otherwise set to be skipped by skip_formatting_disks. This means that this list also includes disks that appear in skip_formatting_disks. This property is managed by the service and cannot be modified by the user.")
    skip_formatting_disks: Optional[StrictStr] = Field(None, description="A comma-seperated list of host disks that the service will avoid formatting.")
    __properties = ["kind", "id", "href", "cluster_id", "infra_env_id", "status", "status_info", "validations_info", "logs_info", "status_updated_at", "progress", "stage_started_at", "stage_updated_at", "progress_stages", "connectivity", "api_vip_connectivity", "tang_connectivity", "inventory", "free_addresses", "ntp_sources", "disks_info", "role", "suggested_role", "bootstrap", "logs_collected_at", "logs_started_at", "installer_version", "installation_disk_path", "installation_disk_id", "updated_at", "created_at", "checked_in_at", "registered_at", "discovery_agent_version", "requested_hostname", "user_name", "media_status", "deleted_at", "ignition_config_overrides", "installer_args", "timestamp", "machine_config_pool_name", "images_status", "domain_name_resolutions", "ignition_endpoint_token_set", "node_labels", "disks_to_be_formatted", "skip_formatting_disks"]

    @validator('kind')
    def kind_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('Host', 'AddToExistingClusterHost'):
            raise ValueError("must be one of enum values ('Host', 'AddToExistingClusterHost')")
        return value

    @validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('discovering', 'known', 'disconnected', 'insufficient', 'disabled', 'preparing-for-installation', 'preparing-failed', 'preparing-successful', 'pending-for-input', 'installing', 'installing-in-progress', 'installing-pending-user-action', 'resetting-pending-user-action', 'installed', 'error', 'resetting', 'added-to-existing-cluster', 'cancelled', 'binding', 'unbinding', 'unbinding-pending-user-action', 'known-unbound', 'disconnected-unbound', 'insufficient-unbound', 'disabled-unbound', 'discovering-unbound', 'reclaiming', 'reclaiming-rebooting'):
            raise ValueError("must be one of enum values ('discovering', 'known', 'disconnected', 'insufficient', 'disabled', 'preparing-for-installation', 'preparing-failed', 'preparing-successful', 'pending-for-input', 'installing', 'installing-in-progress', 'installing-pending-user-action', 'resetting-pending-user-action', 'installed', 'error', 'resetting', 'added-to-existing-cluster', 'cancelled', 'binding', 'unbinding', 'unbinding-pending-user-action', 'known-unbound', 'disconnected-unbound', 'insufficient-unbound', 'disabled-unbound', 'discovering-unbound', 'reclaiming', 'reclaiming-rebooting')")
        return value

    @validator('media_status')
    def media_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('connected', 'disconnected'):
            raise ValueError("must be one of enum values ('connected', 'disconnected')")
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
    def from_json(cls, json_str: str) -> Host:
        """Create an instance of Host from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of progress
        if self.progress:
            _dict['progress'] = self.progress.to_dict()
        # set to None if cluster_id (nullable) is None
        # and __fields_set__ contains the field
        if self.cluster_id is None and "cluster_id" in self.__fields_set__:
            _dict['cluster_id'] = None

        # set to None if progress_stages (nullable) is None
        # and __fields_set__ contains the field
        if self.progress_stages is None and "progress_stages" in self.__fields_set__:
            _dict['progress_stages'] = None

        # set to None if media_status (nullable) is None
        # and __fields_set__ contains the field
        if self.media_status is None and "media_status" in self.__fields_set__:
            _dict['media_status'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Host:
        """Create an instance of Host from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Host.parse_obj(obj)

        _obj = Host.parse_obj({
            "kind": obj.get("kind"),
            "id": obj.get("id"),
            "href": obj.get("href"),
            "cluster_id": obj.get("cluster_id"),
            "infra_env_id": obj.get("infra_env_id"),
            "status": obj.get("status"),
            "status_info": obj.get("status_info"),
            "validations_info": obj.get("validations_info"),
            "logs_info": obj.get("logs_info"),
            "status_updated_at": obj.get("status_updated_at"),
            "progress": HostProgressInfo.from_dict(obj.get("progress")) if obj.get("progress") is not None else None,
            "stage_started_at": obj.get("stage_started_at"),
            "stage_updated_at": obj.get("stage_updated_at"),
            "progress_stages": obj.get("progress_stages"),
            "connectivity": obj.get("connectivity"),
            "api_vip_connectivity": obj.get("api_vip_connectivity"),
            "tang_connectivity": obj.get("tang_connectivity"),
            "inventory": obj.get("inventory"),
            "free_addresses": obj.get("free_addresses"),
            "ntp_sources": obj.get("ntp_sources"),
            "disks_info": obj.get("disks_info"),
            "role": obj.get("role"),
            "suggested_role": obj.get("suggested_role"),
            "bootstrap": obj.get("bootstrap"),
            "logs_collected_at": obj.get("logs_collected_at"),
            "logs_started_at": obj.get("logs_started_at"),
            "installer_version": obj.get("installer_version"),
            "installation_disk_path": obj.get("installation_disk_path"),
            "installation_disk_id": obj.get("installation_disk_id"),
            "updated_at": obj.get("updated_at"),
            "created_at": obj.get("created_at"),
            "checked_in_at": obj.get("checked_in_at"),
            "registered_at": obj.get("registered_at"),
            "discovery_agent_version": obj.get("discovery_agent_version"),
            "requested_hostname": obj.get("requested_hostname"),
            "user_name": obj.get("user_name"),
            "media_status": obj.get("media_status") if obj.get("media_status") is not None else 'connected',
            "deleted_at": obj.get("deleted_at"),
            "ignition_config_overrides": obj.get("ignition_config_overrides"),
            "installer_args": obj.get("installer_args"),
            "timestamp": obj.get("timestamp"),
            "machine_config_pool_name": obj.get("machine_config_pool_name"),
            "images_status": obj.get("images_status"),
            "domain_name_resolutions": obj.get("domain_name_resolutions"),
            "ignition_endpoint_token_set": obj.get("ignition_endpoint_token_set"),
            "node_labels": obj.get("node_labels"),
            "disks_to_be_formatted": obj.get("disks_to_be_formatted"),
            "skip_formatting_disks": obj.get("skip_formatting_disks")
        })
        return _obj


