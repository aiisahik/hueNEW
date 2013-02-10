# -*- compile-command: "python timeline.py" -*-

import os
import simplejson as json
import fileinput

record = []

for line in fileinput.input("cluster.json"):
    x = json.loads(line)
    last = x[1]



for cluster in range(0, 8):
    start = 0
    color = "rgb(%d,%d,%d)" % ((cluster/4)*128+32, ((cluster%4)/2)*128+32, 
                                   ((cluster%2)*128)+32)
    ds = dict([('color', color), 
               ('data', [])
               ])
    
    for line in fileinput.input("cluster.json"):
        x = json.loads(line)
        if x[0] == cluster:

            while start < x[1]:
                ds["data"].append({ "x" : start, "y" : 0 })
                #print "----"
                start += 1

            #print x[1], x[1]
            ds["data"].append({ "x" : x[1], "y" : x[2] })
            start += 1

    while start <= last:
        ds["data"].append({ "x" : start, "y" : 0 })
        #print "=====", start, last
        start += 1

    record.append(ds)
    #print

print json.dumps(record)
