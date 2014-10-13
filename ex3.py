#-*- coding: utf-8 -*-

from osmxapi.xapiquery import XapiQuery
from osmxapi import OsmXapi

if __name__ == '__main__':
    from osmxapi import bbox

    xapi = OsmXapi(api="overpass.osm.rambler.ru", base="cgi", debug = True)

    denmark = XapiQuery(boundary="administrative")
    denmark['name'] = 'Danmark'
    denmark['admin_level'] = '2'

    A = xapi.relationGet(denmark)
    print A
#.

