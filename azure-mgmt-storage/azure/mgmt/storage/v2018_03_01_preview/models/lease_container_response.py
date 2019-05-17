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


class LeaseContainerResponse(Model):
    """Lease Container response schema.

    :param lease_id: Returned unique lease ID that must be included with any
     request to delete the container, or to renew, change, or release the
     lease.
    :type lease_id: str
    :param lease_time_seconds: Approximate time remaining in the lease period,
     in seconds.
    :type lease_time_seconds: str
    """

    _attribute_map = {
        'lease_id': {'key': 'leaseId', 'type': 'str'},
        'lease_time_seconds': {'key': 'leaseTimeSeconds', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(LeaseContainerResponse, self).__init__(**kwargs)
        self.lease_id = kwargs.get('lease_id', None)
        self.lease_time_seconds = kwargs.get('lease_time_seconds', None)