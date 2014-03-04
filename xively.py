#!/usr/bin/env python

import urllib2, json, time

spark_id = ""
spark_access_token = ""
xively_id = ""
xively_api_key = ""

def update():
    rh = json.loads(urllib2.urlopen('https://api.spark.io/v1/devices/{}/rh?access_token={}'.format(spark_id, spark_access_token)).read())
    
    print rh   

    temp = json.loads(urllib2.urlopen('https://api.spark.io/v1/devices/{}/temp?access_token={}'.format(spark_id, spark_access_token)).read())

    print temp

    req = {
        "version":"1.0.0",
        "datastreams" : [ {
            "id" : "Temperature",
            "current_value" : temp['result']
        },{ 
            "id" : "Humidity",
            "current_value" : rh['result']
        }]
    }

    r=urllib2.Request('https://api.xively.com/v2/feeds/{}.json'.format(xively_id), json.dumps(req), {'X-ApiKey': xively_api_key})
    r.get_method = lambda: 'PUT'
    r=urllib2.urlopen(r)
    print r


while True:

    try:
        update()
    except Exception, e:
        print e
    time.sleep(60)
