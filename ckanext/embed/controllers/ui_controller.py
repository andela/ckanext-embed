# -*- coding: utf-8 -*-

# Copyright (c) 2015-2016 CoNWeT Lab., Universidad Politécnica de Madrid

# This file is part of CKAN Data Requests Extension.

# CKAN Data Requests Extension is free software: you can redistribute it and/or
# modify it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# CKAN Data Requests Extension is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with CKAN Data Requests Extension. If not, see <http://www.gnu.org/licenses/>.

import logging

import ckan.lib.base as base
import ckan.lib.helpers as h
import ckan.model as model
import ckan.plugins as plugins
import ckanext.embed.constants as constants
import functools
import re

from ckan.common import request, _, g, c
from urllib import urlencode


_link = re.compile(r'(?:(https?://)|(www\.))(\S+\b/?)([!"#$%&\'()*+,\-./:;<=>?@[\\\]^_`{|}~]*)(\s|$)', re.I)

log = logging.getLogger(__name__)
tk = plugins.toolkit
c = tk.c


class EmbedUI(base.BaseController):

    def index(self):
        # package search
        context = {'model': model, 'session': model.Session,
                    'user': c.user, 'auth_user_obj': c.userobj}
        organization = str(request.GET.get('organization', None))
        q = request.GET.get('q', '*:*')
        print(organization)
        print(q)
        data_dict = {
            'q': q,
            'facet.field': g.facets,
            'rows': 4,
            'start': 0,
            'sort': 'views_recent desc',
            'fq': 'organization:'+organization
        }

        results = tk.get_action(constants.EMBED_INDEX)(context, data_dict)

        return base.render('embed/index.html', extra_vars={'datasets': results.datasets}, cache_force=True)
