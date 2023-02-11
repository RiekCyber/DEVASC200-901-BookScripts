""" Generate the session token for FMC """
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://fmcrestapisandbox.cisco.com/api/fmc_platform/v1/auth/generatetoken"
headers = {'Content-Type': "application/xml", 'Authorization': "Basic ZS5zZWJlcnQ6eENlM1FtbWI=",}

response = requests.request("POST", url, headers=headers, verify=False)
print(response.headers)