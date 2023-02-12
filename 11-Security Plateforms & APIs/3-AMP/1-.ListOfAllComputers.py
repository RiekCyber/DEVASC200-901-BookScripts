""" GET list of all computers via API """

import requests
url = "https://api.amp.cisco.com/v1/computers"
headers = { 'authorization': "Basic ZGVhZGJlZWYxMjM0NDhjY2MwMGQ6WFhYWFhYWFgtWVlZWS1aWlpaLTAwMDAtZTM4NGVmMmR4eHh4", 'cache-control': "no-cache",}
response = requests.request("GET", url, headers=headers)
print(response.text)