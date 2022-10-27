""" Webex Devices - Set Camera Position """
import requests

URL = "https://10.10.20.152/putxml"

PAYLOAD = (
    ' <Command> ' +
    '   <Camera> ' +
    '       <PositionSet command="True">' +
    '           <CameraId>1</CameraId>' +
    '           <Pan>150</Pan>' +
    '           <Tilt>150</Tilt>' +
    '       </PositionSet>' +
    '   </Camera>' +
    ' </Command>'
    )

HEADERS = {
            'Content-Type' : "application/xml",
            'Cookie' : "SecureSessionId=f53174106455df192ba11e004c196f084afe08133bafbddca1707fc37df9f21a"
        }

RESPONSE = requests.request("POST", URL, data=PAYLOAD, headers=HEADERS, verify = False)

print(RESPONSE.text)
