""" Webex Devices - Endpoint Status """
import requests

URL = "https://10.10.20.152/status.xml"

HEADERS = { 'Cookie' : "SecureSessionId=f53174106455df192ba11e004c196f084afe08133bafbddca1707fc37df9f21a" }

RESPONSE = requests.request("GET", URL, headers=HEADERS, verify = False)

print(RESPONSE.text)
