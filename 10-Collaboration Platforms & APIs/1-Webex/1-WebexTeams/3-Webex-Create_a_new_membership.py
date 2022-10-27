""" Add new Member to a Webex Room """
import json
import requests
import pprint

URL = "https://webexapis.com/v1/memberships"

PAYLOAD = {"roomId": "Y2lzY29zcGFyazovL3VybjpURUFNOmV1LWNlbnRyYWwtMV9rL1JPT00vMDJiZTJkNTAtNzZiOC0xMWViLThmZmEtNjU4ZGNlYTg4MTMx",
    "personEmail": "newUser@devasc.com",
    "personDisplayName": "Cisco DevNet",
    "isModerator": "false"}

HEADERS = {"Authorization": "Bearer N2VkNzYwZmUtYmU3Mi00ZTJlLTgxOTYtNDdhMDZmM2EyZmEyYWMyZTM0MWEtOGQz_PE93_cb22bf91-b84e-4c50-ab49-cd704940b921", "Content-Type": "application/json"}

RESPONSE = requests.request("POST", URL, data=json.dumps(PAYLOAD), headers=HEADERS)

pprint.pprint(json.loads(RESPONSE.text))
