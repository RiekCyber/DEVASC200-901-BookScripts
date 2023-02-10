""" Delete domain using the Enforcement API """

import requests

url = "https://s-platform.api.opendns.com/1.0/domains/internetbadguys.com"

querystring = {"customerKey":"61597426-46f0-4beb-b4a0-9f6586c18b03"}

response = requests.request("DELETE",url ,params=querystring)

print(response.text)
