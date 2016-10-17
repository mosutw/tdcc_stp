import requests
import json


url = "http://localhost:5100/stp"
stp_string = '{"TxCod":"127","BrkCod":"7000","ExeBrkCod":"7000","AccountNoLen":"0B","AccountNo":"70001234567", "StockNoLen":"06","StockNo":"2303  ","StkShrLen":"0F","StkShr":"1234567890123.12","IdNoLen":"0A","IdNo":"F123456789","RepNoLen":"01","YesNoLen":"01","YesNo":"N","TelNoLen":"0A","TelNo":"0233933009"}'

# data = {}
# data['TxCod'] = '127'
# data['BrkCod'] = '7000'
# data['ExeBrkCod'] = '7000'
# data['AccountNoLen'] = '0B'
# data['AccountNo'] = '70001234567'
# data['StockNoLen'] = '06'
# data['StockNo'] = '2303  '
# data['StkShrLen'] = '0F'
# data['StkShr'] = '1234567890123.12'
# data['IdNoLen'] = '0A'
# data['IdNo'] = 'F123456789'
# data['RepNoLen'] = '01'
# data['YesNoLen'] = '01'
# data['YesNo'] = 'N'
# data['TelNoLen'] = '0A'
# data['TelNo'] = '0233933009'
#
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
response = requests.post(url, data=stp_string)
#response = requests.post(url, data=json.dumps(data))
result = xmltodict.parse(response.content)
print json.dumps(result)
