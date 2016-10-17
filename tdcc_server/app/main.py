# !/usr/bin/env python
# !-*- encoding= utf-8 -*-

import datetime
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


# 收檔自動化檔案要求
@app.route('/fpc/MsgHandler.asmx', methods=['POST'])
def file_in_place():
    data = request.data
    # 過濾字元
    data = re.sub(u"[\x00-\x08\x0b-\x0c\x0e-\x1f]+", u"", data)
    # 移除tag 多餘空白
    data = re.sub(r'</\s+',u'</', data)
    # 將收到的XML字串轉成json object
    json_root = xmltodict.parse(data)
    bluestar = json_root["soap:Envelope"]["soap:Body"]["SubmitXmlSync"]["BlueStar"]
    RqUid = bluestar['@RqUid']
    autoftpfun = bluestar['autoftpfun']
    TxCod = bluestar['TxCod']
    BrkCod = bluestar['BrkCod']
    TxnTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    StatusCode = '0'
    Severity = 'FTP'
    StatusDesc = 'FTP TEST'

    soap_ok='''<?xml version="1.0" ?>
    <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
        <soap:Body>
            < SubmitXmlSyncResponse xmlns="http://www.cedar.com.tw/bluestar/">
                <BlueStar MsgName="Auto_FTP" xmlns="http://www.cedar.com.tw/bluestar/"
                    RqUid="{0}" Status="0">
                    <autoftpfun>{1}</autoftpfun>
                    <TxCod>{2}</TxCod>
                    <BrkCod>{3}</BrkCod>
                    <TxnTime>{4}</TxnTime>
                    <StatusCode>{5}</StatusCode>
                    <Severity>{6}</Severity>
                    <StatusDesc>{7}</StatusDesc>
                </BlueStar>
            </SubmitXmlSyncResponse>
        </soap:Body>
    </soap:Envelope>'''

    return soap_ok.format(RqUid, autoftpfun, TxCod, BrkCod, TxnTime, StatusCode, Severity, StatusDesc)
    # return 'xml'


# STP 服務訊息
@app.route('/stp/MsgHandler.asmx', methods=['GET','POST'])
def straight_through_processing():
    data = request.data
    # 過濾字元
    data = re.sub(u"[\x00-\x08\x0b-\x0c\x0e-\x1f]+", u"", data)
    # 移除tag 多餘空白
    data = re.sub(r'</\s+',u'</', data)
    # 將收到的XML字串轉成json object
    json_root = xmltodict.parse(data)
    # print json.dumps(json_root)
    bluestar = json_root["soap:Envelope"]["soap:Body"]["SubmitXmlSync"]["BlueStar"]
    # print json.dumps(bluestar)
    MsgName = bluestar['@MsgName']
    RqUid = bluestar['@RqUid']
    Date = datetime.datetime.now().strftime("%Y%m%d")
    Time = datetime.datetime.now().strftime("%H%M%S")
    ExeCod = bluestar['ExeBrkCod']
    TxnSeqNo = '0000000001'
    TxCod = bluestar['TxCod']
    StkCod = bluestar['StockNo']
    OpMsg = '作業完成'

    soap_ok='''<?xml version="1.0" ?>
        <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
            <soap:Body>
                < SubmitXmlSyncResponse xmlns="http://www.cedar.com.tw/bluestar/">
                    <BlueStar MsgName="{0}" xmlns="http://www.cedar.com.tw/bluestar/"
                        RqUid="{1}" Status="0">
                        <TxnStatus>0</TxnStatus>
                        <Date>{2}</Date>
                        <Time>{3}</Time>
                        <ExeCod>{4}</ExeCod >
                        <TxnSeqNo>{5}</TxnSeqNo>
                        <TxCod>{6}</TxCod>
                        <StkCod>{7}</StkCod>
                        <OpMsg>{8}</<OpMsg>>
                    </BlueStar>
                </SubmitXmlSyncResponse>
            </soap:Body>
        </soap:Envelope>'''
    #bluestar = json_root["soap:Envelope"]["soap:Body"]["SubmitXmlSync"]["BlueStar"]
    #print xmltodict.unparse(json_root, pretty=True)
    #print bluestar['BrokerNo']
    #print bluestar['SourcePath'] + '/' + bluestar['Filename']
    #return 'file in place receive data:' + bluestar['BrokerNo']
    # return 'xml'
    # 模擬TDCC 回覆訊息
    return soap_ok.format(MsgName, RqUid, Date, Time, ExeCod, TxnSeqNo, TxCod, StkCod, OpMsg)


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
