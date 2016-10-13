#!/usr/bin/env python
#!-*- encoding= utf-8 -*-
import re
from flask import Flask
from flask import request
import base64
import xmltodict, json

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
    data=re.sub(u"[\x00-\x08\x0b-\x0c\x0e-\x1f]+",u"",data)
    # print data
    xml_root = ET.fromstring(data)
    #xml_root = tree.getroot()
    print xml_root.find('BlueStar')
    # json_root = xmltodict.parse(data)
    return 'xml'

def getConfig():
    config = ConfigParser()
    # 加這行回寫時key才會區分大小寫
    config.optionxform = str  #reference: http://docs.python.org/library/configparser.html
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


