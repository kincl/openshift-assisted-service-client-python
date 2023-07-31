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
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr
from openshift_assisted_service.models.container_image_availability_result import ContainerImageAvailabilityResult

class ContainerImageAvailability(BaseModel):
    """
    ContainerImageAvailability
    """
    name: Optional[StrictStr] = Field(None, description="A fully qualified image name (FQIN).")
    size_bytes: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="Size of the image in bytes.")
    time: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="Seconds it took to pull the image.")
    download_rate: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="The rate of size/time in seconds MBps.")
    result: Optional[ContainerImageAvailabilityResult] = None
    __properties = ["name", "size_bytes", "time", "download_rate", "result"]

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
    def from_json(cls, json_str: str) -> ContainerImageAvailability:
        """Create an instance of ContainerImageAvailability from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ContainerImageAvailability:
        """Create an instance of ContainerImageAvailability from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ContainerImageAvailability.parse_obj(obj)

        _obj = ContainerImageAvailability.parse_obj({
            "name": obj.get("name"),
            "size_bytes": obj.get("size_bytes"),
            "time": obj.get("time"),
            "download_rate": obj.get("download_rate"),
            "result": obj.get("result")
        })
        return _obj


