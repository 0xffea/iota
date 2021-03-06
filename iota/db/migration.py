#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""Database setup and migration commands."""

from oslo_config import cfg
from stevedore import driver
from oslo_db import options

_IMPL = None


def get_backend():
    global _IMPL
    if not _IMPL:
        # TODO(0xffea): Fix conf file import
        # cfg.CONF.import_opt('backend', 'oslo_db.options', group='database')
        _IMPL = driver.DriverManager(
                    namespace="iota.database.migration_backend",
                    name='sqlalchemy',
                    invoke_on_load=True).driver
    return _IMPL


def upgrade(version=None):
    """Migrate the database to `version` or the most recent version."""
    return get_backend().upgrade(version)


def downgrade(version=None):
    return get_backend().downgrade(version)


def version():
    return get_backend().version()


def stamp(version):
    return get_backend().stamp(version)


def revision(message, autogenerate):
    return get_backend().revision(message, autogenerate)
