# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.geolocation_tile_list import GeolocationTileList  # noqa: F401,E501
from swagger_server.models.mec_creation_resources import MECCreationResources  # noqa: F401,E501
from swagger_server.models.sb_service import SBService  # noqa: F401,E501
from swagger_server import util


class MECInstance(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: str=None, name: str=None, lat: str=None, lng: str=None, organization: str=None, resources: MECCreationResources=None, sb_services: List[SBService]=None, props: object=None, geolocation: List[GeolocationTileList]=None):  # noqa: E501
        """MECInstance - a model defined in Swagger

        :param id: The id of this MECInstance.  # noqa: E501
        :type id: str
        :param name: The name of this MECInstance.  # noqa: E501
        :type name: str
        :param lat: The lat of this MECInstance.  # noqa: E501
        :type lat: str
        :param lng: The lng of this MECInstance.  # noqa: E501
        :type lng: str
        :param organization: The organization of this MECInstance.  # noqa: E501
        :type organization: str
        :param resources: The resources of this MECInstance.  # noqa: E501
        :type resources: MECCreationResources
        :param sb_services: The sb_services of this MECInstance.  # noqa: E501
        :type sb_services: List[SBService]
        :param props: The props of this MECInstance.  # noqa: E501
        :type props: object
        :param geolocation: The geolocation of this MECInstance.  # noqa: E501
        :type geolocation: List[GeolocationTileList]
        """
        self.swagger_types = {
            'id': str,
            'name': str,
            'lat': str,
            'lng': str,
            'organization': str,
            'resources': MECCreationResources,
            'sb_services': List[SBService],
            'props': object,
            'geolocation': List[GeolocationTileList]
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'lat': 'lat',
            'lng': 'lng',
            'organization': 'organization',
            'resources': 'resources',
            'sb_services': 'sb_services',
            'props': 'props',
            'geolocation': 'geolocation'
        }
        self._id = id
        self._name = name
        self._lat = lat
        self._lng = lng
        self._organization = organization
        self._resources = resources
        self._sb_services = sb_services
        self._props = props
        self._geolocation = geolocation

    @classmethod
    def from_dict(cls, dikt) -> 'MECInstance':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MECInstance of this MECInstance.  # noqa: E501
        :rtype: MECInstance
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this MECInstance.


        :return: The id of this MECInstance.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this MECInstance.


        :param id: The id of this MECInstance.
        :type id: str
        """

        self._id = id

    @property
    def name(self) -> str:
        """Gets the name of this MECInstance.


        :return: The name of this MECInstance.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this MECInstance.


        :param name: The name of this MECInstance.
        :type name: str
        """

        self._name = name

    @property
    def lat(self) -> str:
        """Gets the lat of this MECInstance.


        :return: The lat of this MECInstance.
        :rtype: str
        """
        return self._lat

    @lat.setter
    def lat(self, lat: str):
        """Sets the lat of this MECInstance.


        :param lat: The lat of this MECInstance.
        :type lat: str
        """

        self._lat = lat

    @property
    def lng(self) -> str:
        """Gets the lng of this MECInstance.


        :return: The lng of this MECInstance.
        :rtype: str
        """
        return self._lng

    @lng.setter
    def lng(self, lng: str):
        """Sets the lng of this MECInstance.


        :param lng: The lng of this MECInstance.
        :type lng: str
        """

        self._lng = lng

    @property
    def organization(self) -> str:
        """Gets the organization of this MECInstance.


        :return: The organization of this MECInstance.
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization: str):
        """Sets the organization of this MECInstance.


        :param organization: The organization of this MECInstance.
        :type organization: str
        """

        self._organization = organization

    @property
    def resources(self) -> MECCreationResources:
        """Gets the resources of this MECInstance.


        :return: The resources of this MECInstance.
        :rtype: MECCreationResources
        """
        return self._resources

    @resources.setter
    def resources(self, resources: MECCreationResources):
        """Sets the resources of this MECInstance.


        :param resources: The resources of this MECInstance.
        :type resources: MECCreationResources
        """

        self._resources = resources

    @property
    def sb_services(self) -> List[SBService]:
        """Gets the sb_services of this MECInstance.


        :return: The sb_services of this MECInstance.
        :rtype: List[SBService]
        """
        return self._sb_services

    @sb_services.setter
    def sb_services(self, sb_services: List[SBService]):
        """Sets the sb_services of this MECInstance.


        :param sb_services: The sb_services of this MECInstance.
        :type sb_services: List[SBService]
        """

        self._sb_services = sb_services

    @property
    def props(self) -> object:
        """Gets the props of this MECInstance.


        :return: The props of this MECInstance.
        :rtype: object
        """
        return self._props

    @props.setter
    def props(self, props: object):
        """Sets the props of this MECInstance.


        :param props: The props of this MECInstance.
        :type props: object
        """

        self._props = props

    @property
    def geolocation(self) -> List[GeolocationTileList]:
        """Gets the geolocation of this MECInstance.


        :return: The geolocation of this MECInstance.
        :rtype: List[GeolocationTileList]
        """
        return self._geolocation

    @geolocation.setter
    def geolocation(self, geolocation: List[GeolocationTileList]):
        """Sets the geolocation of this MECInstance.


        :param geolocation: The geolocation of this MECInstance.
        :type geolocation: List[GeolocationTileList]
        """

        self._geolocation = geolocation