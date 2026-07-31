# Natas Level 4 → 5

## Objective
Find the hidden password for the next level 

## Vulnerability
HTTP Referer Header Manipulation

## Reconnaissance
The page showed "Access disallowed. You are visiting from x while authorized users should come only from "http://natas5.natas.labs.overthewire.org/"". This means the server checks the Referer HTTP header to determine where the request originated.

## Exploitation

### Steps
1. It was identified that the server reads the Referer header to validate access
2. Use the curl command to alter the referer as natas5, so that the server will read natas5 as the one who submitted the request

### Payload / Method
Used curl -u command in terminal:
```
curl -u natas4:[password] -H "Referer: http://natas5.natas.labs.overthewire.org/" http://natas4.natas.labs.overthewire.org/
```

## Why It Works
This method works because the server blindly trusts the Referer to validate the request access without having any server-side verification. HTTP headers can be freely manipulated by the client. 

## What I Learned
HTTP headers can be freely manipulated by the client
