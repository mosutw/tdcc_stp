# !/usr/bin/env python
# !-*- encoding= utf-8 -*-


import re
import uuid

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


@app.route('/fsr')
def file_p_place():
    headers = {'content-type': 'text/xml'}
    soap_header = '''<?xml version="1.0" ?>
    <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:xsd="http://www.w3.org/2001/XMLSchema"
    xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
    <soap:Body>
    <SubmitXmlSync xmlns="http://www.cedar.com.tw/bluestar/">'''

    soap_body = '''<BlueStar MsgName="Auto_FTP"
    xmlns="http://www.cedar.com.tw/bluestar/" RqUid=%s App="XML">'''

    req_data = {}
    req_data['autoftpfunc'] = '167F_FTP'
    json_data = {'data':req_data}
    print dict2xml(json_data)

    '''
    <autoftpfun>167F_FTP</autoftpfun>
    <TxCod>交易代號</TxCod>
    <BrkCod>參加人代號</BrkCod>
    <BrokerNoLen>02~04</BrokerNoLen>
    <BrokerNo>證商代號</BrokerNo>
    <StockNoStartLen>00</StockNoStartLen>
    <StockNoStart>證券代號區間起</StockNoStart>
    <StockNoEndLen>06</StockNoEndLen>
    <StockNoEnd>證券代號區間迄</StockNoEnd>
    <InqTxnIdLen >00</InqTxnIdLen >
    <InqTxnId>查詢交易代號</InqTxnId>
    <InqDateLen>07</ InqDateLen >
    <InqDate>查詢日期</ InqDate >
    <Option1Len>01</ Option1Len>
    <Option1>查詢類別</ Option1>
    <StockKindLen >01</StockKindLen >
    <StockKind>證券類型</StockKind>
    <FileNo>XXXXXX</FileNo>
    </BlueStar>
    '''

    soap_tailor = '''</BlueStar></SubmitXmlSync>
    </soap:Body>
    </soap:Envelope>'''

    rquid = uuid.uuid1()

    print soap_header + soap_body + soap_tailor % (rquid)
    return 'file send request'


@app.route('/fip')
def file_in_place():
    return 'file_in place site'


@app.route('/stp')
def straight_through_processing():
    return 'stp service'


@app.route('/xml', methods=['POST'])
def xml_test():
    data = request.data
    data = re.sub(u"[\x00-\x08\x0b-\x0c\x0e-\x1f]+", u"", data)
    # print data
    xml_root = ET.fromstring(data)
    # xml_root = tree.getroot()
    # ns='{http://www.cedar.com.tw/bluestar/}BlueStar'
    # namespaces={'http://www.cedar.com.tw/bluestar/'}
    # ns='BlueStar'
    print xml_root.findall('{http://www.cedar.com.tw/bluestar/}BlueStar')
    print xml_root[0][0][0].tag
    print xml_root[0][0][0].attrib
    root1 = xml_root[0][0][0]
    for child in root1:
        print child.tag
    for child in xml_root:
        print child
        for subchild in child:
            print subchild
            for subchild1 in subchild:
                print subchild1

    # print xml_root.findall('{http://schemas.xmlsoap.org/soap/envelope/}Body/{http://www.cedar.com.tw/bluestar/}SubmitXmlSync/BlueStar')
    # items = xml_root.findall('.')
    # print len(items)

    json_root = xmltodict.parse(data)
    print json.dumps(json_root)
    # print json.dumps(json_root["soap:Envelope"]["soap:Body"]["SubmitXmlSync"]["BlueStar"])
    bluestar = json_root["soap:Envelope"]["soap:Body"]["SubmitXmlSync"]["BlueStar"]
    print bluestar['BrokerNo']
    return bluestar['BrokerNo']


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
