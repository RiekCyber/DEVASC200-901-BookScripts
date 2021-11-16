""" Update and Retrieve Client Details """
from zeep import Client
from zeep.cache import SqliteCache
from zeep.transports import Transport
from requests import Session
from requests.auth import HTTPBasicAuth
import urllib3
from urllib3.exceptions import InsecureRequestWarning

urllib3.disable_warnings(InsecureRequestWarning)

USERNAME = 'administrator'
PASSWORD = 'ciscopsdt'
IP_ADDRESS = "10.10.20.1"
WSDL = 'axlsqltoolkit/schema//12.5//AXLAPI.wsdl'
BINDING_NAME = "{http://www.cisco.com/AXLAPIService/}AXLAPIBinding"

ADDRESS = "https://{ip}:8443/axl/".format(ip=IP_ADDRESS)

def update_phone_by_name(client, name, description):
    """ Update Phone by Name """
    return client.updatePhone(**{'name': name, 'description': description})

def get_phone_by_name(client, name):
    """ Get Phone by Name """
    return client.getPhone(name=name)

def main():

    """ Main """
    session = Session()
    session.verify = False
    session.auth = HTTPBasicAuth(USERNAME, PASSWORD)
    transport = Transport(cache=SqliteCache(), session=session, timeout=60)

    client = Client(wsdl=WSDL,transport=transport)
    axl = client.create_service(BINDING_NAME, ADDRESS)

    update_phone_by_name(axl,"TABUSER008", "DevAsc: Éric's just added a new description")
    print(get_phone_by_name(axl, "TABUSER008"))

if __name__ == '__main__':
    main()
