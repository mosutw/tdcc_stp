#! /usr/bin/python
 
import sys
from SOAPpy import SOAPProxy
 
option = sys.argv[1]
 
serverUrl='http://localhost:9000'
namespace='urn:/Date'
server = SOAPProxy(serverUrl, namespace)
response = server.dateInfo(option)
 
# read out the response
if (response == None):
    print "Call returned error."
    sys.exit(1)
    
if (option == "date"):
    print "Current server date is " + response[0]
elif (option == "time"):
    print "Current server time is " + response[0]
elif (option == "all"):
    print "Currently server date is " + response[0]
    print "Currently server time is " + response[1]
