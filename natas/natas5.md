# Natas Level 5 → 6

## Objective
Find the hidden password for the next level 

## Vulnerability
Cookie manipulation

## Reconnaissance
The page showed "Access disallowed. You are not logged in". This means that the cookie might be able to be manipulated by the client.


## Exploitation

### Steps
1. Click F12 to check the cookies
2. Look for the "loggedin" variable
3. Modify its value into "1"
4. Refresh the page

### Payload / Method

```
Used F12 to access cookies. Slightly manipulate the value of the loggedin value. The value was 0. That is why the clue said "Access disallowed. You are not logged in". The value flagged that the client haven't logged in yet. It can be solved by changing the 0 into 1, then refresh the page.
```

## Why It Works
This method works because the cookie value can be freely manipulated by the client.

## What I Learned
Cookies are also worth checking since it might contain manipulable variables
