""" Send Webex Message """
import json
import requests
import pprint

URL = "https://webexapis.com/v1/messages"

PAYLOAD = {"roomId" :" Y2lzY29zcGFyazovL3VzL1JPT00vYzQ2OTk3NTAtZGIyNy0xMWU1LWI0ZjQtZmJmMjI3Y2ZmYWYz",
"text" : "This is a test message"}

HEADERS = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkZXZBU0MiLCJuYW1lIjoiZGV2QVNDLWd1ZXN0IiwiaXNzIjoiWTJselkyOXpjR0Z5YXpvdkwzVnlianBVUlVGTk9tVjFMV05sYm5SeVlXd3RNVjlyTDA5U1IwRk9TVnBCVkVsUFRpOHhZMlE0WmpRMU9DMDFaR0V5TFRReU9UUXRPREF5TmkweFlUUm1PV1ZsTkdGbU5EZyIsImV4cCI6MTY2Njg4OTk3N30.kX2yjOpK0H7e927DJn-S6rD5MntevwDMefhqowq4sII",
"Content-Type": "application/json",}

RESPONSE = []
for i in range (10) :
    print(i)
    RESPONSE.append(requests.request("POST", URL, data=json.dumps(PAYLOAD), headers=HEADERS))
    pprint.pprint(json.loads(RESPONSE[i].text))
