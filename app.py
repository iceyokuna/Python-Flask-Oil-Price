from flask import Flask
from zeep import Client
from lxml import etree
import json

app = Flask(__name__)


@app.route("/")
def index():
    response_message = ""
    client = Client('http://www.pttplc.com/webservice/pttinfo.asmx?WSDL')
    result = client.service.CurrentOilPrice("en")

    root = etree.fromstring(result)

    for r in root.xpath('DataAccess'):
        product = r.xpath('PRODUCT/text()')[0]
        price = r.xpath('PRICE/text()') or [0]
        if(int(float(price[0])) == 0):
            continue
        response_message += str(product) + " [" +  str(float(price[0])) + "฿] , "
        
    return response_message

if __name__ == "__main__":
    app.run()

