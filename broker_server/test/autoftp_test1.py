import requests
import json
import xmltodict
import re
import collections

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


url = "http://localhost:5100/fsr"
fpc_str = '{"autoftpfun":"167F_FTP","TxCod":"167","BrkCod":"7000","BrokerNoLen":"04","BrokerNo":"7000","TakeBorrowDateLen":"07","TakeBorrowDate":"20161010","Option1Len":"01","Option1":"1","FileNo":"00001"}'

#
# data = {}
# data["autoftpfun"] = "167F_FTP"
# data["TxCod"] = "167"
# data["BrkCod"] = "7000"
# data["BrokerNoLen"] = "04"
# data["BrokerNo"] = "7000"
# data["TakeBorrowDateLen"] = "07"
# data["TakeBorrowDate"] = "20161010"
# data["Option1Len"] = "01"
# data["Option1"] = "1"
# data["FileNo"] = "00001"
#
headers = {"Content-type": "application/json", "Accept": "text/plain"}
response = requests.post(url, data=fpc_str)
# response = requests.post(url, data=json.dumps(data))
result = response.content
result = re.sub(u"[\x00-\x08\x0b-\x0c\x0e-\x1f]+", u"", result)
result = re.sub(r'</\s+',u'</', result)
result = re.sub(r'<\s+',u'<', result)
result = json.loads(json.dumps((xmltodict.parse(result))))
print json.dumps(result["soap:Envelope"]["soap:Body"]["SubmitXmlSyncResponse"]["BlueStar"])
# result = xmltodict.parse(ET.fromstring(response.content))
# print json.dumps(result)
