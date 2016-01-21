# -*- encoding: utf-8 -*-
#
# Copyright 2016 OpenStack Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import pecan

from iota.api.controllers.v1 import root as v1

MEDIA_TYPE_JSON = 'application/vnd.openstack.iot-%s+json'


class RootController(object):

    def __init__(self):
        self.v1 = v1.V1Controller()

    @pecan.expose('json')
    def index(self):
        base_url = pecan.request.application_url
        version = 'v1'
        released_on = '2016-01-21T00:00:00Z'
        url = '%s/%s' % (base_url, version)
        versions = {
            'versions': {
                'values': [
                    {'id': version,
                     'links': [
                         {'href': url, 'rel': 'self', }],
                     'media-types': [
                         {'base': 'application/json',
                          'type': MEDIA_TYPE_JSON % version, }],
                     'status': 'stable',
                     'updated': released_on, }]}}
        return versions
