""" Add domain using the Enforcement API """

import json
import requests

url = "https://s-platform.api.opendns.com/1.0/events"

querystring = {"customerKey":"61597426-46f0-4beb-b4a0-9f6586c18b03"}

dict =     {
                "deviceId": "liveriek-e692-4724-ba36-c28132c761de",
                "deviceVersion": "13.7a",
                "eventTime": "2020-01-01T09:33:21.0Z",
                "alertTime": "2020-01-01T09:33:21.0Z",
                "dstDomain": "looksfake1.com",
                "dstUrl": "http://looksfake.com/badurl",
                "protocolVersion": "1.0a",
                "providerName": "Security Platform"
            }

payload2 =  {
                "alertTime": "2013-02-08T11:14:26.0Z",
                "deviceId": "ba6a59f4-e692-4724-ba36-c28132c761de",
                "deviceVersion": "13.7a",
                "dstDomain": "internetbadguys.com",
                "dstUrl": "http://internetbadguys.com/a-bad-url",
                "eventTime": "2013-02-08T09:30:26.0Z",
                "protocolVersion": "1.0a",
                "providerName": "Security Platform"
            }

#payload3 = str (payload3)
#print (payload3)
#payload3 = payload3.replace('\'', '"')
#print (payload3)
#payload3 = json.dumps(payload3)
#print(payload3)
#payload2 = json.loads(payload2)
#print(payload2)
#payload3 = payload3.replace('\'', '"')
#print (payload3)
#print (payload3)

payload3 = [
                {
                    "deviceId": "deadbeaf-e692-4724-ba36-c28132c761de",
                    "deviceVersion": "13.7a",
                    "eventTime": "2020-01-01T09:33:21.0Z",
                    "alertTime": "2020-01-01T09:33:21.0Z",
                    "dstDomain": "looksfake1.com",
                    "dstUrl": "http://looksfake.com/badurl",
                    "protocolVersion": "1.0a",
                    "providerName": "Security Platform" },

                {
                    "alertTime": "2013-02-08T11:14:26.0Z",
                    "deviceId": "ba6a59f4-e692-4724-ba36-c28132c761de",
                    "deviceVersion": "13.7a",
                    "dstDomain": "internetbadguys1.com",
                    "dstUrl": "http://internetbadguys.com/a-bad-url",
                    "eventTime": "2013-02-08T09:30:26.0Z",
                    "protocolVersion": "1.0a",
                    "providerName": "Security Platform"
                }
            ]


payload = []
for i in range (10,20) :
    payload.append(dict)
    dict['dstDomain'] = dict['dstDomain']+str(i)
    print(payload)
    print()






headers = { 'Content-Type': "application/json",
            'Accept': "application/json",
            'Cache-Control': "no-cache",
            'Host': "s-platform.api.opendns.com",
            'Accept-Encoding': "gzip, deflate",
            'Connection': "keep-alive",
            }

response = requests.request("POST", url, data=json.dumps(payload2), headers=headers, params=querystring)


print ()
print(response.text)
print()
#print(payload3)
#print()
