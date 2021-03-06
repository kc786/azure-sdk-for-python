# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class UserIdentity(Model):
    """The definition of the user identity under which the task is run.

    Specify either the userName or autoUser property, but not both.

    :param user_name: The name of the user identity under which the task is
     run. The userName and autoUser properties are mutually exclusive; you must
     specify one but not both.
    :type user_name: str
    :param auto_user: The auto user under which the task is run. The userName
     and autoUser properties are mutually exclusive; you must specify one but
     not both.
    :type auto_user: ~azure.mgmt.batch.models.AutoUserSpecification
    """

    _attribute_map = {
        'user_name': {'key': 'userName', 'type': 'str'},
        'auto_user': {'key': 'autoUser', 'type': 'AutoUserSpecification'},
    }

    def __init__(self, user_name=None, auto_user=None):
        self.user_name = user_name
        self.auto_user = auto_user
