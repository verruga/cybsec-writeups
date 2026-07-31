# Natas Level 8 → 9

## Objective
Find the hidden password for the next level 

## Vulnerability
Exposed secret code

## Reconnaissance
The page requires the user to submit a secret code to the input field in order to gain the password to the next level. A secret code was found in the source code, but it was encrypted multiple times with bin2hex, strrev, and base64. That means the decryption have to be done in reverse.

## Exploitation

### Steps
1. View the source code by doing the ctrl + U command
2. The source code gives contains a secret code that needs to be decrypted using bin2hex, strrev, and base64 in order.
3. Submit the decrypted code

### Payload / Method

```
Used 3 online decryption tools; bin2hex, strrev, and base64.
```

## Why It Works
This method works because the secret code was exposed in the source code.

## What I Learned
Always look for source code to look for clues
