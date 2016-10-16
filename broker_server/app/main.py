# !/usr/bin/env python
# !-*- encoding= utf-8 -*-


import re
import uuid

import requests
from flask import Flask
from flask import request
import base64
import xmltodict
import json

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

from configparser import ConfigParser
app = Flask(__name__)


@app.route('/')
def welcome_mega():
    return 'mega'


# 收檔自動化要求
# 收到後台要求訊息,將內容組成xml 格式，傳送到TDCC要求
# 檔案名稱由後台決定，所以也許要記錄相關訊息
# @app.route('/fsr/<request_data>')
@app.route('/fsr', methods = ['POST'])
def file_send_request():
    data = request.data
    soap_header = '''<?xml version="1.0" ?>
    <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:xsd="http://www.w3.org/2001/XMLSchema"
    xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
    <soap:Body>
    <SubmitXmlSync xmlns="http://www.cedar.com.tw/bluestar/">'''
    soap_body = '''<BlueStar MsgName="Auto_FTP" xmlns="http://www.cedar.com.tw/bluestar/" RqUid="{0}" App="XML">'''
    soap_tailor = '''</BlueStar></SubmitXmlSync></soap:Body></soap:Envelope>'''

    json_data = {}
    json_data['data'] = json.loads(data)
    xml_root = ET.fromstring(xmltodict.unparse(json_data))
    for e in xml_root:
        soap_body = soap_body + ET.tostring(e)

    rquid = uuid.uuid1()

    print soap_header + soap_body.format(rquid) + soap_tailor 
    return 'file send request'

# 收檔自動化到位通知服務
@app.route('/fip', methods=['POST'])
def file_in_place():
    data = request.data
    # 過濾字元
    data = re.sub(u"[\x00-\x08\x0b-\x0c\x0e-\x1f]+", u"", data)
    # 移除tag 多餘空白
    data = re.sub(r'</\s+',u'</', data)
    # 將收到的XML字串轉成xml element
    # xml_root = ET.fromstring(data)
    # xml_root =xmltodict.parse(data,process_namespaces=True)
    # 將收到的XML字串轉成json object
    json_root = xmltodict.parse(data)
    bluestar = json_root["soap:Envelope"]["soap:Body"]["SubmitXmlSync"]["BlueStar"]
    print xmltodict.unparse(json_root, pretty=True)
    print bluestar['BrokerNo']
    print bluestar['SourcePath'] + '/' + bluestar['Filename']
    return 'file in place receive data:' + bluestar['BrokerNo']
    # return 'xml'


# STP 服務訊息
# 傳送資料為每次為一筆訊息往返
# STP 的做法類似fsr ,差別在xml訊息
# 但fsr回傳訊息較簡單不需處理，STP則需另外處理
@app.route('/stp', methods=['GET','POST'])
def straight_through_processing():
    url = "http://localhost:5100/fip"
    # headers = {'content-type': 'application/soap+xml'}
    headers = {'content-type': 'text/xml'}
    data = request.data
    soap_header = '''<?xml version="1.0" ?> 
    <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
               xmlns:xsd="http://www.w3.org/2001/XMLSchema" 
               xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
      <soap:Body>
         <SubmitXmlSync xmlns="http://www.cedar.com.tw/bluestar/">'''
    soap_body = '''<BlueStar MsgName="{0}" xmlns="http://www.cedar.com.tw/bluestar/" RqUid="{1}" App="">'''
    soap_tailor = '''</BlueStar></SubmitXmlSync></soap:Body></soap:Envelope>'''

    json_data = {}
    json_data['data'] = json.loads(data)
    xml_root = ET.fromstring(xmltodict.unparse(json_data))
    for e in xml_root:
	if e.tag == "TxCod":
		MsgName = e.text
        soap_body = soap_body + ET.tostring(e)

    rquid = uuid.uuid1()
    stp_body = soap_header + soap_body.format(MsgName, rquid) + soap_tailor 
    print stp_body
    # response = requests.post(url, data=stp_body, headers=headers)

    # 模擬TDCC 回覆訊息

    return 'OK'


# 收檔自動化到位測試，之後刪除
@app.route('/xml', methods=['POST'])
def xml_test():
    data = request.data
    # 過濾字元
    data = re.sub(u"[\x00-\x08\x0b-\x0c\x0e-\x1f]+", u"", data)
    # 移除tag 多餘空白
    data = re.sub(r'</\s+',u'</', data)
    # print data
    xml_root = ET.fromstring(data)
    xml_root =xmltodict.parse(data,process_namespaces=True)
    # print xml_root
    # xml_root = tree.getroot()
    # ns='{http://www.cedar.com.tw/bluestar/}BlueStar'
    # namespaces={'http://www.cedar.com.tw/bluestar/'}
    # ns='BlueStar'
    #print xml_root.findall('{http://www.cedar.com.tw/bluestar/}BlueStar')
    #print xml_root[0][0][0].tag
    #print xml_root[0][0][0].attrib
    #root1 = xml_root[0][0][0]
    #for child in root1:
    #    print child.tag
    #for child in xml_root:
    #    print child
    #    for subchild in child:
    #        print subchild
    #        for subchild1 in subchild:
    #            print subchild1

    # print xml_root.findall('{http://schemas.xmlsoap.org/soap/envelope/}Body/{http://www.cedar.com.tw/bluestar/}SubmitXmlSync/BlueStar')
    # items = xml_root.findall('.')
    # print len(items)

    json_root = xmltodict.parse(data)
    print json.dumps(json_root)
    print json.dumps(json_root["soap:Envelope"]["soap:Body"]["SubmitXmlSync"]["BlueStar"])
    bluestar = json_root["soap:Envelope"]["soap:Body"]["SubmitXmlSync"]["BlueStar"]
    print bluestar['BrokerNo']
    print bluestar['SourcePath'] + '/' + bluestar['Filename']
    return bluestar['BrokerNo']
    # return 'xml'


def get_namespace(element):
    m = re.match('\{.*\}', element.tag)
    return m.group(0) if m else ''


def getConfig():
    config = ConfigParser()
    # 加這行回寫時key才會區分大小寫
    config.optionxform = str  # reference: http://docs.python.org/library/configparser.html
    config.read('./config/config.ini')
    return config


def main():
    config = getConfig()
    host = config['setting']['host']
    port = config['setting']['port']
    print base64.b64decode(config['ftp']['password'])
    app.run(host=host, port=int(port), debug=True)

if __name__ == "__main__":
    main()
