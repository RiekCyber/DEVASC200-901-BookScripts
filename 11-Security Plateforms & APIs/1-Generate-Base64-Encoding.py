""" Generate Base64 Encoding """
import base64
ENCODED = base64.b64encode('8bc6292454b74f61acd3507253c3f4e3:588d8e0447ec4cdbacf9bb9ba3de0968'.encode('UTF-8'))
print(ENCODED.decode('utf-8'))