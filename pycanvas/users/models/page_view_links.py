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


class PageViewLinks(BaseModel):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, user=None, context=None, asset=None, real_user=None, account=None):
        """
        PageViewLinks - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'user': 'int',
            'context': 'int',
            'asset': 'int',
            'real_user': 'int',
            'account': 'int'
        }

        self.attribute_map = {
            'user': 'user',
            'context': 'context',
            'asset': 'asset',
            'real_user': 'real_user',
            'account': 'account'
        }

        self._user = user
        self._context = context
        self._asset = asset
        self._real_user = real_user
        self._account = account

    @property
    def user(self):
        """
        Gets the user of this PageViewLinks.
        The ID of the user for this page view

        :return: The user of this PageViewLinks.
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this PageViewLinks.
        The ID of the user for this page view

        :param user: The user of this PageViewLinks.
        :type: int
        """

        self._user = user

    @property
    def context(self):
        """
        Gets the context of this PageViewLinks.
        The ID of the context for the request (course id if context_type is Course, etc)

        :return: The context of this PageViewLinks.
        :rtype: int
        """
        return self._context

    @context.setter
    def context(self, context):
        """
        Sets the context of this PageViewLinks.
        The ID of the context for the request (course id if context_type is Course, etc)

        :param context: The context of this PageViewLinks.
        :type: int
        """

        self._context = context

    @property
    def asset(self):
        """
        Gets the asset of this PageViewLinks.
        The ID of the asset for the request, if any

        :return: The asset of this PageViewLinks.
        :rtype: int
        """
        return self._asset

    @asset.setter
    def asset(self, asset):
        """
        Sets the asset of this PageViewLinks.
        The ID of the asset for the request, if any

        :param asset: The asset of this PageViewLinks.
        :type: int
        """

        self._asset = asset

    @property
    def real_user(self):
        """
        Gets the real_user of this PageViewLinks.
        The ID of the actual user who made this request, if the request was made by a user who was masquerading

        :return: The real_user of this PageViewLinks.
        :rtype: int
        """
        return self._real_user

    @real_user.setter
    def real_user(self, real_user):
        """
        Sets the real_user of this PageViewLinks.
        The ID of the actual user who made this request, if the request was made by a user who was masquerading

        :param real_user: The real_user of this PageViewLinks.
        :type: int
        """

        self._real_user = real_user

    @property
    def account(self):
        """
        Gets the account of this PageViewLinks.
        The ID of the account context for this page view

        :return: The account of this PageViewLinks.
        :rtype: int
        """
        return self._account

    @account.setter
    def account(self, account):
        """
        Sets the account of this PageViewLinks.
        The ID of the account context for this page view

        :param account: The account of this PageViewLinks.
        :type: int
        """

        self._account = account

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