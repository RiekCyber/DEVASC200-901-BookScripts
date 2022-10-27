""" Generate JWT """
import base64
import time
import math
import jwt

EXPIRATION = math.floor(time.time()) + 3600 # 1hour from now

PAYLOAD = {"sub": "devASC",
 "name": "devASC-guest",
 "iss": "Y2lzY29zcGFyazovL3VybjpURUFNOmV1LWNlbnRyYWwtMV9rL09SR0FOSVpBVElPTi8xY2Q4ZjQ1OC01ZGEyLTQyOTQtODAyNi0xYTRmOWVlNGFmNDg",
 "exp": EXPIRATION}

SECRET = base64.b64decode('SS0AGbU9gfzuGG/tv1CNC//CE5jnHbWhsJXIH7sENUo=')

TOKEN = jwt.encode(PAYLOAD, SECRET)

# print(TOKEN.decode('utf-8'))
print (TOKEN)

# HEADERS = {'Authorization': 'Bearer ' + TOKEN.decode('utf-8')}



""" Send Webex Message """
import json
import requests
import pprint

URL = "https://webexapis.com/v1/messages"

PAYLOAD = {"roomId" :"Y2lzY29zcGFyazovL3VybjpURUFNOmV1LWNlbnRyYWwtMV9rL1JPT00vYTQ0Yjg5YTAtNzYwNS0xMWViLTkzYTMtYzUxMTI3YzE5YTkz",
"text" : "This is a test message"}

HEADERS = {"Authorization": 'Bearer ' + TOKEN,
"Content-Type": "application/json",}



RESPONSE = []
for i in range (10) :
    print(i)
    RESPONSE.append(requests.request("POST", URL, data=json.dumps(PAYLOAD), headers=HEADERS))
    pprint.pprint(json.loads(RESPONSE[i].text))
