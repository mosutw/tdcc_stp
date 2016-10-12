#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# ripped off from soaplib 2.0.0 beta 1 examples and modified to use m2wsgi
#
# N.B. soap appears to be interchangeable with rpc because of rpclib fork
#

import soaplib
from soaplib.core.service import soap, DefinitionBase
from soaplib.core.model.primitive import String, Integer
from soaplib.core.server import wsgi
from soaplib.core.model.clazz import ClassModel, Array
import pymongo
from pymongo import Connection
import string

class LetterStatus(ClassModel):
	__namespace__ = "letterstatus"
	Reference = String
	ServiceNumber = String
	LetterIndex = String
	LetterId = String
	WhenCreated = String
	WhenLodged = String
	Status = String

class ClientService(DefinitionBase):
	@soap(String, Integer, _returns=Array(String))
	def say_hello(self,name,times):
		results = []
		for i in range(0, times):
			results.append('Hello, %s' % name)
		return results

	@soap(String, Array(String), _returns=Array(LetterStatus))
	def RequestLetterStatus(self, Account, LetterReferences):
		results = {}

		for i in range(0, len(LetterReferences)):
			letterstatus = LetterStatus()
			letter = db.letters.find_one({ "account" : Account, "reference" : LetterReferences[i] }, { "id" : 1, "reference" : 1, "dbid" : 1 } )
			if letter == None:
				letterstatus.Reference = LetterReferences[i]
				letterstatus.ServiceNumber = ''
				letterstatus.LetterIndex = ''
				letterstatus.LetterId = ''
				letterstatus.WhenCreated = ''
				letterstatus.WhenLodged = ''
				letterstatus.Status = 'Unknown'
			else:
				letter_id = string.split(letter.get('id', ''), ':')
				letterstatus.Reference = letter.get('reference', '')
				letterstatus.ServiceNumber = letter_id[0]
				letterstatus.LetterIndex = str(int(letter_id[1]) + 1)
				letterstatus.LetterId = str(letter.get('dbid', ''))
				pack = db.packs.find_one({ "id" : letter_id[0] }, { "id" : 1, "reference" : 1, "dbid" : 1, "received" : 1, "processed" : 1, "status" : 1 })
				if pack == None:
					letterstatus.WhenCreated = ''
					letterstatus.WhenLodged = ''
					letterstatus.Status = 'Unknown'
				else:
					letterstatus.WhenCreated = str(pack.get('received', ''))
					letterstatus.WhenLodged = 'Not set yet'
					letterstatus.Status = pack.get('status', 'Not set yet')
			results[i] = letterstatus
		return [v for k, v in results.items()]

if __name__=='__main__':
	try:
		from m2wsgi.io.standard import WSGIHandler
		db = Connection().testdb
		soap_application = soaplib.core.Application([ClientService], 'eas')
		wsgi_application = wsgi.Application(soap_application)
		handler = WSGIHandler(wsgi_application, "tcp://127.0.0.1:9991")
		handler.serve()
	except ImportError:
		print "Error: example server code requires Python >= 2.5"
