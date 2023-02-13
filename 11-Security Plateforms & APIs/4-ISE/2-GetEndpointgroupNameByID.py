import json
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://10.10.20.77/ers/config/endpointgroup/name/RiekCyberDevNetAssociateGroup"
#payload = { "EndPointGroup": { "name": "RiekCyberDevNetAssociateGroup", "description": "RiekCyberDevNetAssociateGroup"}}
headers = { 'content-type': "application/json", 'accept': "application/json", 'authorization': "Basic YWRtaW46QzFzY28xMjM0NQ==", 'cache-control': "no-cache",}

response = requests.request( "Get", url, headers=headers, verify=False)
print(response.status_code)
print(response.text)