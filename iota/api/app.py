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

import logging
import os

import pecan

from oslo_config import cfg
from oslo_log import log
from paste import deploy
from werkzeug import serving

LOG = log.getLogger(__name__)
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


def setup_app():
    pecan_config = {
        'app': {
            'root': 'iota.api.controllers.root.RootController',
            'modules': [],
        }
    }

    pecan.configuration.set_config(dict(pecan_config), overwrite=True)

    app = pecan.make_app(
        pecan_config['app']['root'],
        debug=True,
        hooks=[],
        guess_content_type_from_ext=False
    )

    return app


def load_app():
    return deploy.loadapp('config:/etc/iota/api_paste.ini')


def build_server():
    app = load_app()
    host, port = CONF.api.host, CONF.api.port

    LOG.info('Starting server with PID %s' % os.getpid())
    LOG.info('Configuration:')
    CONF.log_opt_values(LOG, logging.INFO)

    serving.run_simple(host, port, app, 1)


def app_factory(global_config, **local_conf):
    return setup_app()
