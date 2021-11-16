""" Webex Devices - Set Position Detector To ON """
import requests

URL = "https://10.10.20.152/putxml"

PAYLOAD = (
    '<Configuration>' +
    ' <RoomAnalytics>' +
    '   <PeoplePresenceDetector>On</PeoplePresenceDetector>' +
    ' </RoomAnalytics>' +
    '</Configuration>'
    )

HEADERS = {
            'Content-Type' : "application/xml",
            'Cookie' : "SecureSessionId=f53174106455df192ba11e004c196f084afe08133bafbddca1707fc37df9f21a"
        }

RESPONSE = requests.request("POST", URL, data=PAYLOAD, headers=HEADERS, verify = False)

print(RESPONSE.text)
