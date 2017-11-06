# -*- coding: utf-8 -*-

# Copyright (c) 2015-2016 CoNWeT Lab., Universidad Politécnica de Madrid

# This file is part of CKAN Embed Extension.

# CKAN Embed Extension is free software: you can redistribute it and/or
# modify it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# CKAN Embed Extension is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with CKAN Embed Extension. If not, see <http://www.gnu.org/licenses/>.


import logging

import ckan.logic.action.get as get_core
import ckan.plugins as plugins
import ckan.lib.search as search
from ckan.common import _, c

c = plugins.toolkit.c
log = logging.getLogger(__name__)
tk = plugins.toolkit

# Avoid user_show lag
USERS_CACHE = {}


def embed_index(context, data_dict):
    '''
    Returns a list with the existing datasets to be embedded. Rights access
    will not be checked before returning the results.

    :param organization_id: This parameter is optional and allows users
        to filter the results by organization
    :type organization_id: string

    :param user_id: This parameter is optional and allows users
        to filter the results by user
    :type user_id: string

    :param closed: This parameter is optional and allows users to filter
        the result by the dataset status (open or closed)
    :type closed: bool

    :param q: This parameter is optional and allows users to filter
        datasets based on a free text
    :type q: string

    :param sort: This parameter is optional and allows users to sort
        datasets. You can choose 'desc' for retrieving datasets
        in descending order or 'asc' for retrieving datasets in
        ascending order. Datasets are returned in ascending order
        by default.
    :type sort: string

    :param offset: The first element to be returned (0 by default)
    :type offset: int

    :param limit: The max number of datasets to be returned (10 by
        default)
    :type limit: int

    :returns: A dict with three fields: result (a list of datasets),
        facets (a list of the facets that can be used) and count (the total
        number of existing datasets)
    :rtype: dict
    '''

    try:
        # Call the function to fetch the datasets
        query = get_core.package_search(context, data_dict)
        c.search_facets = query['search_facets']
        c.package_count = query['count']
        c.datasets = query['results']
        c.facet_titles = {
                    'organization': _('Organizations'),
                    'groups': _('Groups'),
                    'tags': _('Tags'),
                    'res_format': _('Formats'),
                    'license': _('Licenses'),
                }

    except search.SearchError:
        c.package_count = 0

    return c


def embed_show(context, data_dict):
    '''
    Action to retrieve the information of a dataset. The only required
    parameter is the id of the dataset. A NotFound exception will be
    risen if the given id is not found.

    :param id: the id or name of the dataset
    :type id: string

    :param use_default_schema: use default package schema instead of
        a custom schema defined with an IDatasetForm plugin (default: False)
    :type use_default_schema: bool
    :param include_tracking: add tracking information to dataset and
        resources (default: False)
    :type include_tracking: bool
    :rtype: dictionary
    '''

    try:
        # Call the function to fetch the dataset from core ckan
        dataset = get_core.package_show(context, data_dict)
        dataset['follower_count'] = get_core.dataset_follower_count(context, data_dict)
        dataset['activity_stream'] = get_core.package_activity_list_html(context, data_dict)
    except search.SearchError:
        dataset = {}
    
    return dataset
