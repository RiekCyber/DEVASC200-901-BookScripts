""" GET list of all vulnerabilities via API """
import requests
url = "https://api.amp.cisco.com/v1/vulnerabilities"
querystring = {"offset":"0","limit":"1"}
headers = { 'authorization': "Basic ZGVhZGJlZWYxMjM0NDhjY2MwMGQ6WFhYWFhYWFgtWVlZWS1aWlpaL-TAwMDAtZTM4NGVmMmR4eHh4", 'cache-control': "no-cache",}
response = requests.request("GET", url, headers=headers, params=querystring)
print(response.text)