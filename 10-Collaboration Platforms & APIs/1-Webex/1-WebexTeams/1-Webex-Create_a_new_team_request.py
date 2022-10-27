""" Create Webex Team """

import json
import requests

URL = "https://webexapis.com/v1/teams"

PAYLOAD = {"name": "DevNet Associate Certification Team1"}

HEADERS = {"Authorization": "Bearer OTQxMGEyODAtNzFkZC00ZmU0LWI3NWYtYTRlOTA4YmQ5YmI1ZjAzZGE3MzEtZmNm_PE93_cb22bf91-b84e-4c50-ab49-cd704940b921", "Content-Type" : "application/json"}

RESPONSE = requests.request("POST", URL, data=json.dumps(PAYLOAD), headers=HEADERS)

print(RESPONSE.text)
