# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

"""
Iota Management Utility
"""

import sys

from oslo_config import cfg
from oslo_log import log as logging

from iota import version
from iota import service
from iota.db import migration


CONF = cfg.CONF


def do_db_version():
    '''Print database's current migration level.'''
    print(migration.version())


def do_db_sync():
    '''Place a database under migration control and upgrade.

    DB is created first if necessary.
    '''
    #api.db_sync(api.get_engine(), CONF.command.version)
    pass


def add_command_parsers(subparsers):
    parser = subparsers.add_parser('db_version')
    parser.set_defaults(func=do_db_version)

    parser = subparsers.add_parser('create_schema')
    parser.set_defaults(func=do_db_sync)


def main():
    command_opt = cfg.SubCommandOpt('command',
                                    title='Commands',
                                    help='Show available commands.',
                                    handler=add_command_parsers)

    CONF.register_cli_opt(command_opt)

    #service.prepare_service(default_config_files=['/etc/iota/iota.conf'])
    service.prepare_service()
    CONF.command.func()
