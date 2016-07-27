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

from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ...base_api import BaseApi
from ...configuration import Configuration
from ..api_client import ApiClient


class LoginsApi(BaseApi):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    # OPERATIONID: create_user_login
    def create_user_login(self, account_id, user_id, login_unique_id, **kwargs):
        """
        Create a user login
        Create a new login for an existing user in the given account.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_user_login_with_http_info(account_id, user_id, login_unique_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str account_id: ID (required)
        :param str user_id: The ID of the user to create the login for. (required)
        :param str login_unique_id: The unique ID for the new login. (required)
        :param str login_password: The new login's password.
        :param str login_sis_user_id: SIS ID for the login. To set this parameter, the caller must be able to manage SIS permissions on the account.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'user_id', 'login_unique_id', 'login_password', 'login_sis_user_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('per_page')
        all_params.append('page')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_user_login" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params) or (params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `create_user_login`")
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `create_user_login`")
        # verify the required parameter 'login_unique_id' is set
        if ('login_unique_id' not in params) or (params['login_unique_id'] is None):
            raise ValueError("Missing the required parameter `login_unique_id` when calling `create_user_login`")

        resource_path = '/v1/accounts/{account_id}/logins'.replace('{format}', 'json')
        path_params = {}
        if 'account_id' in params:
            path_params['account_id'] = params['account_id']

        query_params = {}
        if 'per_page' in params:
            query_params['per_page'] = params['per_page']
        if 'page' in params:
            query_params['page'] = params['page']

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'user_id' in params:
            form_params.append(('user[id]', params['user_id']))
        if 'login_unique_id' in params:
            form_params.append(('login[unique_id]', params['login_unique_id']))
        if 'login_password' in params:
            form_params.append(('login[password]', params['login_password']))
        if 'login_sis_user_id' in params:
            form_params.append(('login[sis_user_id]', params['login_sis_user_id']))

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['canvas']

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    # OPERATIONID: delete_user_login
    def delete_user_login(self, user_id, id, **kwargs):
        """
        Delete a user login
        Delete an existing login.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_user_login_with_http_info(user_id, id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str user_id: ID (required)
        :param str id: ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('per_page')
        all_params.append('page')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_user_login" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `delete_user_login`")
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_user_login`")

        resource_path = '/v1/users/{user_id}/logins/{id}'.replace('{format}', 'json')
        path_params = {}
        if 'user_id' in params:
            path_params['user_id'] = params['user_id']
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}
        if 'per_page' in params:
            query_params['per_page'] = params['per_page']
        if 'page' in params:
            query_params['page'] = params['page']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['canvas']

        return self.api_client.call_api(resource_path, 'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    # OPERATIONID: edit_user_login
    def edit_user_login(self, account_id, id, **kwargs):
        """
        Edit a user login
        Update an existing login for a user in the given account.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.edit_user_login_with_http_info(account_id, id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str account_id: ID (required)
        :param str id: ID (required)
        :param str login_unique_id: The new unique ID for the login.
        :param str login_password: The new password for the login. Can only be set by an admin user if admins are allowed to change passwords for the account.
        :param str login_sis_user_id: SIS ID for the login. To set this parameter, the caller must be able to manage SIS permissions on the account.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'id', 'login_unique_id', 'login_password', 'login_sis_user_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('per_page')
        all_params.append('page')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method edit_user_login" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params) or (params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `edit_user_login`")
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `edit_user_login`")

        resource_path = '/v1/accounts/{account_id}/logins/{id}'.replace('{format}', 'json')
        path_params = {}
        if 'account_id' in params:
            path_params['account_id'] = params['account_id']
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}
        if 'per_page' in params:
            query_params['per_page'] = params['per_page']
        if 'page' in params:
            query_params['page'] = params['page']

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'login_unique_id' in params:
            form_params.append(('login[unique_id]', params['login_unique_id']))
        if 'login_password' in params:
            form_params.append(('login[password]', params['login_password']))
        if 'login_sis_user_id' in params:
            form_params.append(('login[sis_user_id]', params['login_sis_user_id']))

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['canvas']

        return self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    # OPERATIONID: list_user_logins_accounts
    def list_user_logins_accounts(self, account_id, **kwargs):
        """
        List user logins
        Given a user ID, return that user's logins for the given account.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_user_logins_accounts_with_http_info(account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str account_id: ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('per_page')
        all_params.append('page')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_user_logins_accounts" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params) or (params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `list_user_logins_accounts`")

        resource_path = '/v1/accounts/{account_id}/logins'.replace('{format}', 'json')
        path_params = {}
        if 'account_id' in params:
            path_params['account_id'] = params['account_id']

        query_params = {}
        if 'per_page' in params:
            query_params['per_page'] = params['per_page']
        if 'page' in params:
            query_params['page'] = params['page']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['canvas']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    # OPERATIONID: list_user_logins_users
    def list_user_logins_users(self, user_id, **kwargs):
        """
        List user logins
        Given a user ID, return that user's logins for the given account.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_user_logins_users_with_http_info(user_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str user_id: ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('per_page')
        all_params.append('page')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_user_logins_users" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `list_user_logins_users`")

        resource_path = '/v1/users/{user_id}/logins'.replace('{format}', 'json')
        path_params = {}
        if 'user_id' in params:
            path_params['user_id'] = params['user_id']

        query_params = {}
        if 'per_page' in params:
            query_params['per_page'] = params['per_page']
        if 'page' in params:
            query_params['page'] = params['page']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['canvas']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))