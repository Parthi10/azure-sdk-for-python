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


class ClosedList(Model):
    """Exported Model - A list entity.

    :param name: Name of the list entity.
    :type name: str
    :param sub_lists: Sublists for the list entity.
    :type sub_lists:
     list[~azure.cognitiveservices.language.luis.authoring.models.SubClosedList]
    :param roles:
    :type roles: list[str]
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'sub_lists': {'key': 'subLists', 'type': '[SubClosedList]'},
        'roles': {'key': 'roles', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(ClosedList, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.sub_lists = kwargs.get('sub_lists', None)
        self.roles = kwargs.get('roles', None)