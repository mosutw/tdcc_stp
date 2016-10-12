import urllib2 
import sys, httplib 
def SendHostName(hostName): 
    SENDTPL = \
    '''<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <GetWhoIS xmlns="http://www.webservicex.net">
      <HostName>%s</HostName>
    </GetWhoIS>
  </soap:Body>
</soap:Envelope>'''
    SoapMessage = SENDTPL % (hostName) 
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
