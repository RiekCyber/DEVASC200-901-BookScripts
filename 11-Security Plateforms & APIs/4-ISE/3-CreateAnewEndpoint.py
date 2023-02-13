""" create a new endpoint """
import json
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://10.10.20.77/ers/config/endpoint"
payload = { "ERSEndPoint": { "name": "RiekCyberDevNet_Endpoint3", "description": "DevNet Endpoint-1", "mac": "FF:EE:DD:03:04:35", "groupId": " 732696a0-abc1-11ed-8061-1e9282b9a578", "staticGroupAssignment": True}}
headers = { 'content-type': "application/json", 'accept': "application/json", 'authorization': "Basic YWRtaW46QzFzY28xMjM0NQ==", 'cache-control': "no-cache", }
response = requests.request( "POST", url, data=json.dumps(payload), headers=headers, verify=False)

print(response.status_code)
print(response.headers)
print(response.text)
