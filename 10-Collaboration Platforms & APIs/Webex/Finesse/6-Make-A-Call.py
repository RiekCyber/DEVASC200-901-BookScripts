""" Finesse - User Login"""
import requests

URL = "https://hq-uccx.abc.inc:8445/finesse/api/User/Agent001/Dialogs"

PAYLOAD = (
            "<Dialog>" +
                "<requestedAction>MAKE_CALL</requestedAction>" +
                "<fromAddress>6001</fromAddress>" +
                "<toAddress>6002</toAddress>" +
            "</Dialog>"
)



HEADERS = {
            'authorization': "Basic QWdlbnQwMDE6Y2lzY29wc2R0",
            'content-type': "application/xml",
            'cache-control' : "no-cache",
            }

RESPONSE = requests.request("POST", URL, data=PAYLOAD, headers=HEADERS, verify = False)

print(RESPONSE.text)

print(RESPONSE.status_code)
