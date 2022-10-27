""" Generate Base64 Encoding """
import base64
ENCODED = base64.b64encode('admin:C1sco12345'.encode('UTF-8'))
print(ENCODED.decode('utf-8'))
