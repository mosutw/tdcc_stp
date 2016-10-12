from flask import Flask
from flask_spyne import Spyne
from spyne.protocol.soap import Soap11
from spyne.model.primitive import Unicode, Integer, Float, DateTime
from spyne.model.complex import Iterable

app = Flask(__name__)
spyne = Spyne(app)

class dotazNaOracleDB(spyne.Service):
    __service_url_path__ = '/soap/oracleservice';
    __in_protocol__ = Soap11(validator='lxml');
    __out_protocol__ = Soap11();

    @spyne.srpc(DateTime, DateTime, _returns="What to put here?")
    def oracle(DATE_INCOME, DATE_ISSUE):
        #from OracleDB_Procedure import UlozeniDoXML
        #UlozeniDoXML(DATE_INCOME, DATE_ISSUE);
        s = open("Databaze.xml");
        return s;


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=8000);

