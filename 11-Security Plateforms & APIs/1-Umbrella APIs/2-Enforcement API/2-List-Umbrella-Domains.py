""" List domain using the Enforcement API """

#import json
import requests

url = "https://s-platform.api.opendns.com/1.0/domains"

querystring = {"customerKey":"e667960b-4c24-4a15-9f4e-684c882c1ee8"}

response = requests.request("GET", url, params=querystring)

print(response.text)
