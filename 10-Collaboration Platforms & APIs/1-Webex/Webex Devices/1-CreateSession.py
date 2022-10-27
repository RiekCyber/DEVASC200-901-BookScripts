""" Webex Devices - Get Session Cookie """
import requests

URL = "https://10.10.20.152/xmlapi/session/begin"

HEADERS = {
            'authorization': "Basic YWRtaW46QzFzY28xMjM0NQ=="
            }

RESPONSE = requests.request("POST", URL, headers=HEADERS, verify = False)

print(RESPONSE.headers["Set-Cookie"])
