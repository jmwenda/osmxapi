# -*- coding: utf-8 -*-

from osmxapi.xapiquery import XapiQuery

bb = XapiQuery ()
bb.box(7.1,51.2,7.2,51.3)
print bb
wup = XapiQuery()
wup['name'] = 'Wuppertal-Barmen'
print wup
halt = XapiQuery()
halt['railway'] = 'halt'
print wup+halt
rail = XapiQuery (railway = '*')
print wup+rail
wupo = XapiQuery (name = 'Wuppertal-Barmen|Wuppertal-Oberbarmen')
print wupo
print bb
bus = XapiQuery(highway="bus_stop")
print bb + bus
print bb+wup+halt
bus = XapiQuery(highway="bus_stop|traffic_signals")
print bb+bus
print bb+XapiQuery(highway='*')
fischer = XapiQuery(name="Fischertal")
print fischer
print XapiQuery(name=u"Südstraße|Fischertal")
bridge=XapiQuery(bridge="yes")
print fischer+bridge
sstrasse = XapiQuery(name = u"Südstraße")
print bb+sstrasse
print bb+sstrasse+bridge
print bb+XapiQuery(name=u'Südstraße|Weststraße')
print bb+XapiQuery(maxspeed=u'*')
r603 = XapiQuery(ref='603')
r613 = XapiQuery(ref='613')
print r603
print r603+r613
network = XapiQuery(network="VRR")
print network+r603
print bb+r603
print bb+network+r603
print bb+r603+r613
bb[u'meta'] = True
print bb
print bus+bb
motorway = XapiQuery(highway='motorway')
print motorway+bb

import datetime

dd = datetime.datetime(2012,1,1,23,59)
janfirst = XapiQuery(newer=dd)
print bb+janfirst
