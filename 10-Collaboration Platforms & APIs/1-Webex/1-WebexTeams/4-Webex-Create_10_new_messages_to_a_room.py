""" Send Webex Message """
import json
import requests
import pprint

URL = "https://webexapis.com/v1/messages"

PAYLOAD = {"roomId" :" Y2lzY29zcGFyazovL3VzL1JPT00vYzQ2OTk3NTAtZGIyNy0xMWU1LWI0ZjQtZmJmMjI3Y2ZmYWYz",
"text" : "This is a test message"}

HEADERS = {"Authorization": "Bearer MWVmMDhiM2MtMTgxZi00ZWQwLWI4MDQtYmYyZmExNjQxNDQ1OWRkN2FlMmEtYTU0_PE93_cb22bf91-b84e-4c50-ab49-cd704940b921",
"Content-Type": "application/json",}

RESPONSE = []
for i in range (10) :
    print(i)
    RESPONSE.append(requests.request("POST", URL, data=json.dumps(PAYLOAD), headers=HEADERS))
    pprint.pprint(json.loads(RESPONSE[i].text))
