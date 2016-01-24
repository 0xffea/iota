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

from iota.db import migration
from iota import version


CONF = cfg.CONF


class DBCommand(object):

    @staticmethod
    def upgrade():
        migration.upgrade(CONF.command.revision)

    @staticmethod
    def downgrade():
        migration.downgrade(CONF.command.revision)

    @staticmethod
    def revision():
        migration.revision(CONF.command.message, CONF.command.autogenerate)

    @staticmethod
    def stamp():
        migration.stamp(CONF.command.revision)

    @staticmethod
    def version():
        print(migration.version())

    @staticmethod
    def create_schema():
        migration.create_schema()


def add_command_parsers(subparsers):
    parser = subparsers.add_parser('db_version')
    parser.set_defaults(func=DBCommand.version)

    parser = subparsers.add_parser('create_schema')
    parser.set_defaults(func=DBCommand.create_schema)


command_opt = cfg.SubCommandOpt('command',
                                title='Commands',
                                help='Show available commands.',
                                handler=add_command_parsers)


def main():
    logging.register_options(CONF)
    logging.setup(CONF, 'iota-manage')
    CONF.register_cli_opt(command_opt)

    try:
        default_config_files = cfg.find_config_files('iota', 'iota-manage')
        CONF(sys.argv[1:], project='iota', prog='iota-manage',
             version=version.version_info.version_string(),
             default_config_files=default_config_files)
    except RuntimeError as e:
        sys.exit("ERROR: %s" % e)

    try:
        CONF.command.func()
    except Exception as e:
        sys.exit("ERROR: %s" % e)
