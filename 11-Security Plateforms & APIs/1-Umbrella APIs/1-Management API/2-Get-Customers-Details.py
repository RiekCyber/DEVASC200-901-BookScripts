""" Get Customer details given a customerID """

import requests
url = "https://management.api.umbrella.com/v1/organizations/5325945/roamingcomputers"
headers = {'accept': "application/json",'authorization': "Basic ZGMxY2QxOGZkMmE5NGNkM2IwMjg5OWU0MDZhMTlhMTk6MDQ2MGUyMjQ3MjM2NDYzODk3ODJkMDU1NmU2NmY5ZGM="}
response = requests.request("GET", url, headers=headers)
print(response.text)
