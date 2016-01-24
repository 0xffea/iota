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
SQLAlchemy models for Iota data.
"""

import uuid

import sqlalchemy as sa
from sqlalchemy.ext import declarative

BASE = declarative.declarative_base()


class Thing(BASE):

    __tablename__ = 'thing'

    id = sa.Column('id', sa.String(36), primary_key=True,
                   default=lambda: str(uuid.uuid4()))
    name = sa.Column('name', sa.String(255))
    status = sa.Column(sa.String(255))
