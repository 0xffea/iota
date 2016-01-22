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

import pecan

from oslo_config import cfg
from paste import deploy
from werkzeug import serving

CONF = cfg.CONF


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
    host, port = '0.0.0.0', 9999

    serving.run_simple(host, port, app, 1)


def app_factory(global_config, **local_conf):
    return setup_app()
