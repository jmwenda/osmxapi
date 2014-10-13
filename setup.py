# -*- coding: utf-8 -*-

from distutils.core import setup
from osmxapi import __version__

setup(name = "osmxapi",
    version = __version__,
    description = "python interface to the Overpass API",
    author = "Morten Kjeldgaard",
    author_email = "mok@bioxray.dk",
    url = "https://launchpad.net/osmxapi",
    license="GPL-3",
    package_dir={'osmxapi': 'osmxapi'},
    packages=["osmxapi"],
    long_description = """This package contains a python module
    implementing the Overpass API for querying OpenStreetMap map data.
    The module allows read only access the OSM database, and provides
    full featured manipulation of data using Python."""
) 
