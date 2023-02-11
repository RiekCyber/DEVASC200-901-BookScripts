""" Webex Devices - Get Session Cookie """
import requests

URL = "https://10.10.20.155/xmlapi/session/begin"

HEADERS = {
            'authorization': "Basic YWRtaW46QWRtIW4xMjM0NTY3OTkm"
            }

RESPONSE = requests.request("POST", URL, headers=HEADERS, verify = False)

print(RESPONSE.headers["Set-Cookie"])