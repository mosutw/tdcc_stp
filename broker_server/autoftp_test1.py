import requests
import json


url = "http://localhost:5100/fsr"
#<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
#xmlns:xsd="http://www.w3.org/2001/XMLSchema"
#xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
#<soap:Body>
#<SubmitXmlSync xmlns="http://www.cedar.com.tw/bluestar/">'''
#
#soap_body = '''<BlueStar MsgName="Auto_FTP"
#xmlns="http://www.cedar.com.tw/bluestar/" App="XML">
# <FunCod>Notice</FunCod>
# <TxnId> </TxnId >
# <BrokerNo>7000</BrokerNo >
# <TxnTime></TxnTime>
# <SourceIP> </SourceIP>
# <SourcePath> </SourcePath>
# <Filename> </Filename>
# </BlueStar>'''
#
#soap_tailor = '''</SubmitXmlSync>
#</soap:Body>
#</soap:Envelope>'''

#body = soap_header + soap_body + soap_tailor

data = {}
data['autoftpfun'] = '167F_FTP'
data['TxCod'] = '167'
data['BrkCod'] = '7000'
data['BrokerNoLen'] = '04'
data['BrokerNo'] = '7000'
data['TakeBorrowDateLen'] = '07'
data['TakeBorrowDate'] = '20161010'
data['Option1Len'] = '01'
data['Option1'] = '1'
data['FileNo'] = '00001'

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
response = requests.post(url, data=json.dumps(data))
# response = requests.get(url, params=json.dumps(data))
print response.content
