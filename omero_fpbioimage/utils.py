#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#
# Copyright (c) 2017 University of Dundee.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the Creative Commons Attribution,
# ShareAlike 4.0 International license.
# FPBioimage was originally published in
# <https://www.nature.com/nphoton/journal/v11/n2/full/nphoton.2016.273.html>.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the Creative Commons Attribution,
# ShareAlike 4.0 International license along with this program.
# If not, see <https://creativecommons.org/licenses/by-sa/4.0/>.
#
# Version: 1.0
#


def get_version(version=None):

    """
    Returns a PEP 386-compliant version number.
    See https://www.python.org/dev/peps/pep-0440/
    """

    version = get_full_version(version)
    parts = 2 if version[2] == 0 else 3
    res = '.'.join(str(x) for x in version[:parts])
    if len(version) > 3:
        res = "%s%s" % (res, version[3])
    return str(res)


def get_full_version(value=None):

    """
    Returns a tuple of the version.
    """

    if value is None:
        from version import VERSION as value  # noqa
    return value
