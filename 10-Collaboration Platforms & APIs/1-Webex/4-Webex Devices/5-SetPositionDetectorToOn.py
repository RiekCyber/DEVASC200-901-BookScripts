""" Webex Devices - Set Position Detector To ON """
import requests

URL = "https://10.10.20.155/putxml"

PAYLOAD = (
    '<Configuration>' +
    ' <RoomAnalytics>' +
    '   <PeoplePresenceDetector>On</PeoplePresenceDetector>' +
    ' </RoomAnalytics>' +
    '</Configuration>'
    )

HEADERS = {
            'Content-Type' : "application/xml",
            'Cookie' : "SecureSessionId=ac0f7ac3cb785122f5f7d1ca0f4961e2bd021de260950f15103a3e48d8b4e82f"
        }

RESPONSE = requests.request("POST", URL, data=PAYLOAD, headers=HEADERS, verify = False)

print(RESPONSE.text)
