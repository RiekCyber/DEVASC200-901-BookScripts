""" Finesse - User Login"""
import requests

URL = "https://hq-uccx.abc.inc:8445/finesse/api/User/Agent001"

PAYLOAD = ("<User>" + "<state>LOGIN</state>" + "<extension>6001</extension>" +"</User>")

HEADERS = {'authorization': "Basic QWdlbnQwMDE6Y2lzY29wc2R0",'content-type': "application/xml",}

RESPONSE = requests.request("PUT", URL, data=PAYLOAD, headers=HEADERS, verify = False)

print(RESPONSE.text)

print(RESPONSE.status_code)
