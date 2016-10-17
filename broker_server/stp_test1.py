import requests
import json


#url = "http://localhost:5100/stp"
stp_url = "http://localhost:5100/stp/MsgHandler.asmx"
fpc_url = "http://localhost:5100/fpc/MsgHandler.asmx"
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
data['TxCod'] = '127'
data['BrkCod'] = '7000'
data['ExeBrkCod'] = '7000'
data['AccountNoLen'] = '0B'
data['AccountNo'] = '70001234567'
data['StockNoLen'] = '06'
data['StockNo'] = '2303  '
data['StkShrLen'] = '0F'
data['StkShr'] = '1234567890123.12'
data['IdNoLen'] = '0A'
data['IdNo'] = 'F123456789'
data['RepNoLen'] = '01'
data['YesNoLen'] = '01'
data['YesNo'] = 'N'
data['TelNoLen'] = '0A'
data['TelNo'] = '0233933009'

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
response = requests.post(url, data=json.dumps(data))
# response = requests.get(url, params=json.dumps(data))
print response.content
