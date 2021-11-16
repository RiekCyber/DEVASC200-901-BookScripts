""" Create Webex Room """

import json
import requests
import pprint

URL = "https://webexapis.com/v1/rooms"
PAYLOAD = {"title": "DevAsc Team Room"}
HEADERS = {"Authorization": "Bearer N2VkNzYwZmUtYmU3Mi00ZTJlLTgxOTYtNDdhMDZmM2EyZmEyYWMyZTM0MWEtOGQz_PE93_cb22bf91-b84e-4c50-ab49-cd704940b921",
            "Content-Type": "application/json"}

RESPONSE = requests.request("POST", URL, data=json.dumps(PAYLOAD), headers=HEADERS)

pprint.pprint(json.loads(RESPONSE.text))
