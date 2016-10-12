import requests
# url="http://ladonize.org/python-demos/AlbumService/soap/description/?WSDL"
url="http://ladonize.org/python-demos/AlbumService/soap/listAlbums"
#headers = {'content-type': 'application/soap+xml'}
headers = {'content-type': 'text/xml'}
body = """<?xml version='1.0'?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV='http://schemas.xmlsoap.org/soap/envelope/' xmlns:SOAP-ENC='http://schemas.xmlsoap.org/soap/encoding/' xmlns:SOAP='http://schemas.xmlsoap.org/wsdl/soap/' xmlns:ns2='urn:AlbumService' xmlns:tns='urn:AlbumService' xmlns:xsd='http://www.w3.org/2001/XMLSchema' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance'>
   <SOAP-ENV:Body>
      <ns1:listAlbums SOAP-ENV:encodingStyle='http://schemas.xmlsoap.org/soap/encoding/' xmlns:ns1='urn:AlbumService'>
         <search-frase xsi:type='xsd:string'>
            ZOO
         </search-frase>
      </ns1:listAlbums>
   </SOAP-ENV:Body>
</SOAP-ENV:Envelope>"""

response = requests.post(url,data=body,headers=headers)
print response.content
