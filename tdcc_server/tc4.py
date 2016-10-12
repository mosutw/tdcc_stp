import requests
url="http://localhost:7789?WSDL"
#headers = {'content-type': 'application/soap+xml'}
headers = {'content-type': 'text/xml'}
body = """<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope xmlns:ns0="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns1="tns" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
   <SOAP-ENV:Header/>
   <ns0:Body>
      <ns1:say_hello>
         <ns1:name>Dave</ns1:name>
         <ns1:times>5</ns1:times>
      </ns1:say_hello>
   </ns0:Body>
</SOAP-ENV:Envelope>"""

response = requests.post(url,data=body,headers=headers)
print response.content
