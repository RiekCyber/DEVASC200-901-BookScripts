""" Generate Base64 Encoding """
import base64
ENCODED = base64.b64encode('e.sebert:xCe3Qmmb'.encode('UTF-8'))
print(ENCODED.decode('utf-8'))