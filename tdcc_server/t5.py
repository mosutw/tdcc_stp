import urllib2 
import sys, httplib 
def SendHostName(album): 
    SENDTPL = \
    """<?xml version='1.0'?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV='http://schemas.xmlsoap.org/soap/envelope/' xmlns:SOAP-ENC='http://schemas.xmlsoap.org/soap/encoding/' xmlns:SOAP='http://schemas.xmlsoap.org/wsdl/soap/' xmlns:ns2='urn:AlbumService' xmlns:tns='urn:AlbumService' xmlns:xsd='http://www.w3.org/2001/XMLSchema' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance'>
   <SOAP-ENV:Body>
      <ns1:listBands SOAP-ENV:encodingStyle='http://schemas.xmlsoap.org/soap/encoding/' xmlns:ns1='urn:AlbumService'>
       <search-frase xsi:type='xsd:string'>
            %s
       </search-frase>
      </ns1:listBands>
   </SOAP-ENV:Body>
</SOAP-ENV:Envelope>"""

    SoapMessage = SENDTPL % (album) 
    webservice = httplib.HTTP("ladonize.org")
    webservice.putrequest("POST", "/python-demos/AlbumService/soap/listBands")
    webservice.putheader("Host", "ladonize.org") 
    webservice.putheader("User-Agent", "Python Post") 
    webservice.putheader("Content-type", "text/xml; charset=\"UTF-8\"") 
    webservice.putheader("Content-length", "%d" % len(SoapMessage)) 
    webservice.putheader("SOAPAction", "\"http://ladonize.org/python-demos/AlbumService/soap/listBands\"") 
    webservice.endheaders() 
    webservice.send(SoapMessage) 
    # get the response 
    statuscode, statusmessage, header = webservice.getreply() 
    print "Response: ", statuscode, statusmessage 
    print "headers: ", header 
    print webservice.getfile().read() 
SendHostName('')
