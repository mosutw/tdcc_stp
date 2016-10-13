import requests
url="http://localhost:5000/xml"
#headers = {'content-type': 'application/soap+xml'}
headers = {'content-type': 'text/xml'}

soap_header='''<?xml version="1.0" ?> 
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
<soap:Body>
<SubmitXmlSync xmlns="http://www.cedar.com.tw/bluestar/">'''

soap_body='''<BlueStar MsgName="Auto_FTP" xmlns="http://www.cedar.com.tw/bluestar/" App="XML">
 <FunCod>Notice</FunCod>
 <TxnId> </TxnId >
 <BrokerNo>7000</BrokerNo >
 <TxnTime></TxnTime>
 <SourceIP> </SourceIP>
 <SourcePath> </SourcePath>
 <Filename> </Filename>
 </BlueStar>'''

soap_tailor='''</SubmitXmlSync>
</soap:Body>
</soap:Envelope>'''

body = soap_header + soap_body + soap_tailor

response = requests.post(url,data=body,headers=headers)
print response.content
