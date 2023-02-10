""" Get Customer details given a customerID """

import requests
url = "https://management.api.umbrella.com/v1/organizations/7944995/roamingcomputers"
headers = {'accept': "application/json",'authorization': "Basic OGJjNjI5MjQ1NGI3NGY2MWFjZDM1MDcyNTNjM2Y0ZTM6NTg4ZDhlMDQ0N2VjNGNkYmFjZjliYjliYTNkZTA5Njg="}
response = requests.request("GET", url, headers=headers)
print(response.text)
