# -*- encoding: utf-8 -*-
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

from oslo_config import cfg


CONF = cfg.CONF

api_server_opts = [
    cfg.StrOpt('host',
               default='0.0.0.0',
               help='The listen IP for the Iota API server.'),
    cfg.PortOpt('port',
                default=9999,
                help='The port number of the Iota API server.'),
]

api_server_opt_group = cfg.OptGroup(name='api',
                                    title='Parameters for the API server')

CONF.register_group(api_server_opt_group)
CONF.register_opts(api_server_opts, api_server_opt_group)


def list_opts():
    yield api_server_opt_group, api_server_opts
