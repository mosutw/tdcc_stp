import logging
logging.basicConfig(level=logging.DEBUG)

from spyne import Application, rpc, ServiceBase, \
    Integer, Unicode

from spyne import Iterable

from spyne.protocol.xml import XmlDocument
from spyne.protocol.soap import Soap11

from spyne.server.wsgi import WsgiApplication

class HelloWorldService(ServiceBase):
    @srpc(Unicode, Integer, _returns=Iterable(Unicode))
    def say_hello(name, times):
        for i in range(times):
            yield 'Hello, %s' % name

application = Application([HelloWorldService],
    tns='spyne.examples.hello',
    in_protocol=XmlDocument(validator='lxml'),
    out_protocol=Soap11()
)

if __name__ == '__main__':
    # You can use any Wsgi server. Here, we chose
    # Python's built-in wsgi server but you're not
    # supposed to use it in production.
    from wsgiref.simple_server import make_server

    wsgi_app = WsgiApplication(application)
    server = make_server('0.0.0.0', 8000, wsgi_app)
    server.serve_forever()


