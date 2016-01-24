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

import sys

from oslo_config import cfg
from oslo_db.sqlalchemy import session as db_session

from iota.db import migration

CONF = cfg.CONF

_facade = None


def get_facade():
    global _facade

    if not _facade:
        _facade = db_session.EngineFacade.from_config(CONF)
    return _facade

get_engine = lambda: get_facade().get_engine()
get_session = lambda: get_facade().get_session()


def get_backend():
    """The backend is this module itself."""
    return sys.modules[__name__]


def db_sync(engine, version=None):
    """Migrate the database to `version` or the most recent version."""
    return migration.db_sync(engine, version=version)


def db_version(engine):
    """Display the current database version."""
    return migration.db_version(engine)
