""" Webex Devices - Set Camera Position """
import requests

URL = "https://10.10.20.155/putxml"

PAYLOAD = (
'<Configuration> <SystemUnit> <Name>EricSeb</Name> </SystemUnit> </Configuration>'

#    ' <Command> ' +
#    '   <Camera> ' +
#    '       <PositionSet command="True">' +
#    '           <CameraId>1</CameraId>' +
#    '           <Pan>150</Pan>' +
#    '           <Tilt>150</Tilt>' +
#    '       </PositionSet>' +
#    '   </Camera>' +
#    ' </Command>'
    )

HEADERS = {
            'Content-Type' : "application/xml",
            'Cookie' : "SecureSessionId=ac0f7ac3cb785122f5f7d1ca0f4961e2bd021de260950f15103a3e48d8b4e82f"
        }

RESPONSE = requests.request("POST", URL, data=PAYLOAD, headers=HEADERS, verify = False)

print(RESPONSE.text)