#""" Users List"""
import requests

URL = "https://hq-uccx.abc.inc:8445/finesse/api/Users"

HEADERS = {'authorization': "Basic YWRtaW5pc3RyYXRvcjpjaXNjb3BzZHQ="}

RESPONSE = requests.request("GET", URL, headers=HEADERS, verify = False)

print(RESPONSE.text)

print(RESPONSE.status_code)
