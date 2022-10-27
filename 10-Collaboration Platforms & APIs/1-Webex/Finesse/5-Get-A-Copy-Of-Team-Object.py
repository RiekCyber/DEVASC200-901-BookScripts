""" Finesse - User to Ready State"""
import requests

URL = "https://hq-uccx.abc.inc:8445/finesse/api/Team/2"

HEADERS = {'authorization': "Basic QWdlbnQwMDE6Y2lzY29wc2R0",}

RESPONSE = requests.request("GET", URL, headers=HEADERS, verify = False)

print(RESPONSE.text)

print(RESPONSE.status_code)
