""" Domains categorization using the
Investigate API """

import requests
url ="https://investigate.api.umbrella.com/domains/categorization/cisco.com.json"

querystring = {"showLabels":""}

headers = {
'authorization': "Bearer 85b2fdb5-c091-45ca-b107-1196d01edd4f",
'cache-control': "no-cache",
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
