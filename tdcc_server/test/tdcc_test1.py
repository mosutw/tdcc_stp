#!/usr/bin/env python
#!-*- encoding=utf-8 -*-

# 測試集保檔案到位通知
import requests


url = "http://localhost:5100/fip"
# headers = {'content-type': 'application/soap+xml'}
headers = {'content-type': 'text/xml'}

soap_header = '''<?xml version="1.0" ?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xmlns:xsd="http://www.w3.org/2001/XMLSchema"
xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
<soap:Body>
<SubmitXmlSync xmlns="http://www.cedar.com.tw/bluestar/">'''

soap_body = '''<BlueStar MsgName="Auto_FTP"
xmlns="http://www.cedar.com.tw/bluestar/" App="XML">
 <FunCod>Notice</FunCod>
 <TxnId>167</TxnId >
 <BrokerNo>7000</ BrokerNo >
 <TxnTime>20161015</TxnTime>
 <SourceIP>127.0.0.1</SourceIP>
 <SourcePath>/ftp/7000 </SourcePath>
 <Filename>167FTX_1.TXT</Filename>
 </BlueStar>'''

soap_tailor = '''</SubmitXmlSync>
</soap:Body>
</soap:Envelope>'''

body = soap_header + soap_body + soap_tailor

response = requests.post(url, data=body, headers=headers)
print response.content
