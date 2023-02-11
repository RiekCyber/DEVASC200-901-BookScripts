
""" Get Server Version """
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://fmcrestapisandbox.cisco.com/api/fmc_platform/v1/info/serverversion"
headers = {'X-auth-access-token': "a5852ff7-c284-41b8-ba80-311cb5a4f81b"}

response = requests.request("GET", url, headers=headers, verify=False)
print(response.text)