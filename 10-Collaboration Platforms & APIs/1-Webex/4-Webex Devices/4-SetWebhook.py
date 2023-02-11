""" Webex Devices - Set Webhook """
import requests

URL = "https://10.10.20.155/putxml"

PAYLOAD = (
    '<Command>' +
    ' <HttpFeedback>' +
    '  <Register command="True">' +
    '   <FeedbackSlot>1</FeedbackSlot>' +
    '   <ServerUrl>http://127.0.0.1/devasc-webhook</ServerUrl>' +
    '   <Format>JSON</Format>' +
    '   <Expression item="1">/Configuration</Expression>' +
    '   <Expression item="2">/Event/CallDisconnect</Expression>' +
    '   <Expression item="3">/Status/Call</Expression>' +
    '  </Register>' +
    ' </HttpFeedback>' +
    '</Command> '
    )

HEADERS = {
            'Content-Type' : "application/xml",
            'Cookie' : "SecureSessionId=ac0f7ac3cb785122f5f7d1ca0f4961e2bd021de260950f15103a3e48d8b4e82f"
        }

RESPONSE = requests.request("POST", URL, data=PAYLOAD, headers=HEADERS, verify = False)

print(RESPONSE.text)

