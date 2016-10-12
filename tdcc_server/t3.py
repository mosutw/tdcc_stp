import urllib2 
import sys, httplib 
def SendHostName(hostName): 
    SENDTPL = \
    '''<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope xmlns:ns0="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns1="tns" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
   <SOAP-ENV:Header/>
   <ns0:Body>
      <ns1:say_hello>
         <ns1:name>%s</ns1:name>
         <ns1:times>%s</ns1:times>
      </ns1:say_hello>
   </ns0:Body>
</SOAP-ENV:Envelope>'''

    SoapMessage = SENDTPL % (name,times) 
    webservice = httplib.HTTP("www.webservicex.net") 
    webservice.putrequest("POST", "/whois.asmx") 
    webservice.putheader("Host", "www.webservicex.net") 
    webservice.putheader("User-Agent", "Python Post") 
    webservice.putheader("Content-type", "text/xml; charset=\"UTF-8\"") 
    webservice.putheader("Content-length", "%d" % len(SoapMessage)) 
    webservice.putheader("SOAPAction", "\"http://www.webservicex.net/GetWhoIS\"") 
    webservice.endheaders() 
    webservice.send(SoapMessage) 
    # get the response 
    statuscode, statusmessage, header = webservice.getreply() 
    print "Response: ", statuscode, statusmessage 
    print "headers: ", header 
    print webservice.getfile().read() 
SendHostName('www.google.com')
