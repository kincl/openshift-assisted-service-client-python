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


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt

class ClusterHostRequirementsDetails(BaseModel):
    """
    ClusterHostRequirementsDetails
    """
    cpu_cores: Optional[StrictInt] = Field(None, description="Required number of CPU cores")
    ram_mib: Optional[StrictInt] = Field(None, description="Required number of RAM in MiB")
    disk_size_gb: Optional[StrictInt] = Field(None, description="Required disk size in GB")
    installation_disk_speed_threshold_ms: Optional[StrictInt] = Field(None, description="Required installation disk speed in ms")
    network_latency_threshold_ms: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="Maximum network average latency (RTT) at L3 for role.")
    packet_loss_percentage: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="Maximum packet loss allowed at L3 for role.")
    tpm_enabled_in_bios: Optional[StrictBool] = Field(None, description="Whether TPM module should be enabled in host's BIOS.")
    __properties = ["cpu_cores", "ram_mib", "disk_size_gb", "installation_disk_speed_threshold_ms", "network_latency_threshold_ms", "packet_loss_percentage", "tpm_enabled_in_bios"]

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
    def from_json(cls, json_str: str) -> ClusterHostRequirementsDetails:
        """Create an instance of ClusterHostRequirementsDetails from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if network_latency_threshold_ms (nullable) is None
        # and __fields_set__ contains the field
        if self.network_latency_threshold_ms is None and "network_latency_threshold_ms" in self.__fields_set__:
            _dict['network_latency_threshold_ms'] = None

        # set to None if packet_loss_percentage (nullable) is None
        # and __fields_set__ contains the field
        if self.packet_loss_percentage is None and "packet_loss_percentage" in self.__fields_set__:
            _dict['packet_loss_percentage'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ClusterHostRequirementsDetails:
        """Create an instance of ClusterHostRequirementsDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ClusterHostRequirementsDetails.parse_obj(obj)

        _obj = ClusterHostRequirementsDetails.parse_obj({
            "cpu_cores": obj.get("cpu_cores"),
            "ram_mib": obj.get("ram_mib"),
            "disk_size_gb": obj.get("disk_size_gb"),
            "installation_disk_speed_threshold_ms": obj.get("installation_disk_speed_threshold_ms"),
            "network_latency_threshold_ms": obj.get("network_latency_threshold_ms"),
            "packet_loss_percentage": obj.get("packet_loss_percentage"),
            "tpm_enabled_in_bios": obj.get("tpm_enabled_in_bios")
        })
        return _obj


