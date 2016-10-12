#!/usr/bin/env python
#!-*- encoding= utf-8 -*-
from flask import Flask
from configparser import ConfigParser
import base64

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
    app.run(host=host, port=int(port))

if __name__ == "__main__":
    main()


