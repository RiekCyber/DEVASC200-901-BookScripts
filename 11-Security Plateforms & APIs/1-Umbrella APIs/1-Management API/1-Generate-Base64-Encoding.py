""" Generate Base64 Encoding """
import base64
encoded = base64.b64encode('dc1cd18fd2a94cd3b02899e406a19a19:0460e224723646389782d0556e66f9dc'.encode('UTF-8')).decode('ASCII')
print(encoded)
