#-*- coding: utf-8 -*-

from osmxapi.xapiquery import XapiQuery
from osmxapi import OsmXapi

if __name__ == '__main__':
    from osmxapi import bbox

    xapi = OsmXapi(api="overpass.osm.rambler.ru", base="cgi", debug = True)
    #xapi = OsmXapi( debug = True)

    bb_aarhus = bbox.Bbox(latn=56.169842, 
                       lats=56.1391956,
                       lone=10.2131633,
                       lonw=10.1461766)

    bb_holmesyd = bbox.Bbox(lats=56.1012473, 
                         lonw=10.1656151, 
                         latn=56.10881, 
                         lone=10.1810646)

    bb_uniparken = bbox.Bbox (lats=56.1618032,
                           lonw=10.1891327,
                           latn=56.1719343,
                           lone=10.212822)

    bb_mindeparken = bbox.Bbox (lats=56.1249836, 
                             lonw=10.2002907, 
                             latn=56.1339765,
                             lone=10.2150536)

    aarhus = XapiQuery()
    aarhus.bbox(bb_aarhus)

    holmesyd = XapiQuery()
    holmesyd.bbox(bb_holmesyd)

    uniparken = XapiQuery ()
    uniparken.bbox(bb_uniparken)

    mindeparken = XapiQuery ()
    mindeparken.bbox(bb_mindeparken)

    uniparken[u'amenity'] = u'parking'

    raw = xapi.anyGet(uniparken, raw=True)
    print raw

    N = xapi.nodeGet(uniparken)
    print N

    W = xapi.wayGet(uniparken)
    print W

    A = xapi.anyGet(uniparken)
    print A
#.
