
import rrdtool

def createBase(comunidad):
    ret = rrdtool.create(comunidad + ".rrd",
                         "--start",'N',
                         "--step",'40',
                         "DS:inoctets:COUNTER:600:U:U",
                         "DS:outoctets:COUNTER:600:U:U",
                         "RRA:AVERAGE:0.2:1:10",
                         "RRA:AVERAGE:0.2:1:10")

    if ret:
        print (rrdtool.error())
