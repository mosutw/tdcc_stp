  	

#! /usr/bin/python
 
from SOAPpy import SOAPServer
import sys, time
 
class Date:
    def dateInfo(self, option) :
        tm = time.localtime()
        year = tm.tm_year
        month = tm.tm_mon
        day = tm.tm_mday
        hour = tm.tm_hour
        min = tm.tm_min
        sec = tm.tm_sec
        
        if (option == "date"):
            return ["%02d/%02d/%04d" % (month, day, year)]
        elif (option == "time"):
            return ["%02d:%02d:%02d" % (hour, min, sec)]
        elif (option == "all"):
            return ["%02d/%02d/%04d" % (month, day, year),
                "%02d:%02d:%02d" % (hour, min, sec)]
        else:
            return "Error - unrecognized option"
        
server = SOAPServer(("localhost", 9000))
server.registerObject(Date(), "urn:/Date")
server.serve_forever()
