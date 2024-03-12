# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class NBService(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, service_name: str=None, ip: str=None, port: int=None, description: str=None, props: str=None):  # noqa: E501
        """NBService - a model defined in Swagger

        :param service_name: The service_name of this NBService.  # noqa: E501
        :type service_name: str
        :param ip: The ip of this NBService.  # noqa: E501
        :type ip: str
        :param port: The port of this NBService.  # noqa: E501
        :type port: int
        :param description: The description of this NBService.  # noqa: E501
        :type description: str
        :param props: The props of this NBService.  # noqa: E501
        :type props: str
        """
        self.swagger_types = {
            'service_name': str,
            'ip': str,
            'port': int,
            'description': str,
            'props': str
        }

        self.attribute_map = {
            'service_name': 'service_name',
            'ip': 'ip',
            'port': 'port',
            'description': 'description',
            'props': 'props'
        }
        self._service_name = service_name
        self._ip = ip
        self._port = port
        self._description = description
        self._props = props

    @classmethod
    def from_dict(cls, dikt) -> 'NBService':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NBService of this NBService.  # noqa: E501
        :rtype: NBService
        """
        return util.deserialize_model(dikt, cls)

    @property
    def service_name(self) -> str:
        """Gets the service_name of this NBService.

        Name of the exposed service in the MEC  # noqa: E501

        :return: The service_name of this NBService.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name: str):
        """Sets the service_name of this NBService.

        Name of the exposed service in the MEC  # noqa: E501

        :param service_name: The service_name of this NBService.
        :type service_name: str
        """
        if service_name is None:
            raise ValueError("Invalid value for `service_name`, must not be `None`")  # noqa: E501

        self._service_name = service_name

    @property
    def ip(self) -> str:
        """Gets the ip of this NBService.

        IP of the service  # noqa: E501

        :return: The ip of this NBService.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip: str):
        """Sets the ip of this NBService.

        IP of the service  # noqa: E501

        :param ip: The ip of this NBService.
        :type ip: str
        """
        if ip is None:
            raise ValueError("Invalid value for `ip`, must not be `None`")  # noqa: E501

        self._ip = ip

    @property
    def port(self) -> int:
        """Gets the port of this NBService.

        Port of the service  # noqa: E501

        :return: The port of this NBService.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port: int):
        """Sets the port of this NBService.

        Port of the service  # noqa: E501

        :param port: The port of this NBService.
        :type port: int
        """
        if port is None:
            raise ValueError("Invalid value for `port`, must not be `None`")  # noqa: E501

        self._port = port

    @property
    def description(self) -> str:
        """Gets the description of this NBService.

        Description of the service  # noqa: E501

        :return: The description of this NBService.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this NBService.

        Description of the service  # noqa: E501

        :param description: The description of this NBService.
        :type description: str
        """

        self._description = description

    @property
    def props(self) -> str:
        """Gets the props of this NBService.

        JSON with extra information of the service  # noqa: E501

        :return: The props of this NBService.
        :rtype: str
        """
        return self._props

    @props.setter
    def props(self, props: str):
        """Sets the props of this NBService.

        JSON with extra information of the service  # noqa: E501

        :param props: The props of this NBService.
        :type props: str
        """

        self._props = props
