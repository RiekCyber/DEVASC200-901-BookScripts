""" Webex Devices - Set Webhook """
import requests

URL = "https://10.10.20.152/putxml"

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
            'Cookie' : "SecureSessionId=f53174106455df192ba11e004c196f084afe08133bafbddca1707fc37df9f21a"
        }

RESPONSE = requests.request("POST", URL, data=PAYLOAD, headers=HEADERS, verify = False)

print(RESPONSE.text)
