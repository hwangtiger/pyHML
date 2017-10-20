# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class SbtNgs(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, locus: str=None, test_id: str=None, test_id_source: str=None):
        """
        SbtNgs - a model defined in Swagger

        :param locus: The locus of this SbtNgs.
        :type locus: str
        :param test_id: The test_id of this SbtNgs.
        :type test_id: str
        :param test_id_source: The test_id_source of this SbtNgs.
        :type test_id_source: str
        """
        self.swagger_types = {
            'locus': str,
            'test_id': str,
            'test_id_source': str
        }

        self.attribute_map = {
            'locus': 'locus',
            'test_id': 'test_id',
            'test_id_source': 'test_id_source'
        }

        self._locus = locus
        self._test_id = test_id
        self._test_id_source = test_id_source

    @classmethod
    def from_dict(cls, dikt) -> 'SbtNgs':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SbtNgs of this SbtNgs.
        :rtype: SbtNgs
        """
        return deserialize_model(dikt, cls)

    @property
    def locus(self) -> str:
        """
        Gets the locus of this SbtNgs.

        :return: The locus of this SbtNgs.
        :rtype: str
        """
        return self._locus

    @locus.setter
    def locus(self, locus: str):
        """
        Sets the locus of this SbtNgs.

        :param locus: The locus of this SbtNgs.
        :type locus: str
        """

        self._locus = locus

    @property
    def test_id(self) -> str:
        """
        Gets the test_id of this SbtNgs.

        :return: The test_id of this SbtNgs.
        :rtype: str
        """
        return self._test_id

    @test_id.setter
    def test_id(self, test_id: str):
        """
        Sets the test_id of this SbtNgs.

        :param test_id: The test_id of this SbtNgs.
        :type test_id: str
        """

        self._test_id = test_id

    @property
    def test_id_source(self) -> str:
        """
        Gets the test_id_source of this SbtNgs.

        :return: The test_id_source of this SbtNgs.
        :rtype: str
        """
        return self._test_id_source

    @test_id_source.setter
    def test_id_source(self, test_id_source: str):
        """
        Sets the test_id_source of this SbtNgs.

        :param test_id_source: The test_id_source of this SbtNgs.
        :type test_id_source: str
        """

        self._test_id_source = test_id_source
