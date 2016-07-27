# coding: utf-8

"""


    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from ...base_model import BaseModel
from pprint import pformat
from six import iteritems
import re


class Day(BaseModel):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, date=None, graders=None):
        """
        Day - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'date': 'Datetime',
            'graders': 'int'
        }

        self.attribute_map = {
            'date': 'date',
            'graders': 'graders'
        }

        self._date = date
        self._graders = graders

    @property
    def date(self):
        """
        Gets the date of this Day.
        the date represented by this entry

        :return: The date of this Day.
        :rtype: Datetime
        """
        return self._date

    @date.setter
    def date(self, date):
        """
        Sets the date of this Day.
        the date represented by this entry

        :param date: The date of this Day.
        :type: Datetime
        """

        self._date = date

    @property
    def graders(self):
        """
        Gets the graders of this Day.
        an array of the graders who were responsible for the submissions in this response. the submissions are grouped according to the person who graded them and the assignment they were submitted for.

        :return: The graders of this Day.
        :rtype: int
        """
        return self._graders

    @graders.setter
    def graders(self, graders):
        """
        Sets the graders of this Day.
        an array of the graders who were responsible for the submissions in this response. the submissions are grouped according to the person who graded them and the assignment they were submitted for.

        :param graders: The graders of this Day.
        :type: int
        """

        self._graders = graders

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other