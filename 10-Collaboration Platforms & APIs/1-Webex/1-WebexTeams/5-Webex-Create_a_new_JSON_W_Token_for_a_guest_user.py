""" Generate JWT """
import base64
import time
import math
import jwt

EXPIRATION = math.floor(time.time()) + 3600 # 1hour from now

PAYLOAD = {"sub": "devASC",
 "name": "devASC-guest",
 "iss": "Y2lzY29zcGFyazovL3VybjpURUFNOmV1LWNlbnRyYWwtMV9rL09SR0FOSVpBVElPTi8xY2Q4ZjQ1OC01ZGEyLTQyOTQtODAyNi0xYTRmOWVlNGFmNDg",
 "exp": EXPIRATION}

SECRET = base64.b64decode('SS0AGbU9gfzuGG/tv1CNC//CE5jnHbWhsJXIH7sENUo=')

TOKEN = jwt.encode(PAYLOAD, SECRET)

# print(TOKEN.decode('utf-8'))
print (TOKEN)

# HEADERS = {'Authorization': 'Bearer ' + TOKEN.decode('utf-8')}
HEADERS = {'Authorization': 'Bearer ' + TOKEN }
