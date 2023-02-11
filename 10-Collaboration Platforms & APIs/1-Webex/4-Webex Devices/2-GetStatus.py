""" Webex Devices - Endpoint Status """
import requests

URL = "https://10.10.20.155/status.xml"

HEADERS = { 'Cookie' : "SecureSessionId=ac0f7ac3cb785122f5f7d1ca0f4961e2bd021de260950f15103a3e48d8b4e82f" }

RESPONSE = requests.request("GET", URL, headers=HEADERS, verify = False)

print(RESPONSE.text)
