""" Delete domain using the Enforcement API """

import requests

url = "https://s-platform.api.opendns.com/1.0/domains/looksfake.com"

querystring = {"customerKey":"e667960b-4c24-4a15-9f4e-684c882c1ee8"}

response = requests.request("DELETE",url ,params=querystring)

print(response.text)
