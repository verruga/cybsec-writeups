# Natas Level 3 → 4

## Objective
Find the hidden password for the next level

## Vulnerability
Exposed robots.txt file that contains the password for the next level

## Reconnaissance
The page showed "There is nothing on this page" that doesn't help much as a clue. The source code doesn't contain any passwords. So this time the website could have an exposed robots.txt file

## Exploitation

### Steps
1. [Slightly alter the web URL by adding /robots.txt at the end of the URL]
2. [It showed a hidden directory named "/s3cr3t/]
3. [I slightly altered the web URL by adding the directory /s3cr3t/ at the end of the URL]
4. [There is a "users.txt" file that is stored inside the directory]
5. [The file contains the password of natas4]

### Payload / Method
Manually changed the URL parameter in the browser address bar:
```
http://natas3.natas.labs.overthewire.org/robots.txt
http://natas3.natas.labs.overthewire.org/s3cr3t/users.txt
```

## Why It Works
There is an exposed robots.txt file that contains a hidden directory that contains a users.txt file

## What I Learned
A website might have one or many hidden directories that could contain important files
