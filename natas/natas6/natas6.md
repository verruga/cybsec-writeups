# Natas Level 6 → 7

## Objective
Find the hidden password for the next level 

## Vulnerability
Exposed directories

## Reconnaissance
The page requires the user to input the secret code and will give the password as an output. The page intentionally reveals its directories in the source code. That means i'll have to manipulate the web URL parameter to view its content.


## Exploitation

### Steps
1. Manipulate the web URL parameter by adding the revealed directories at the end of the URL
2. The directory contains the secret code that is going to be used at the front page
3. Submit the secret code

### Payload / Method

```
View the source code to look for clues. The source code contains a directory. Manually change the URL parameter by adding the directory at the end of the URL. The directory contains a secret code that is going to be submitted at the front page.
```

## Why It Works
This method works because the directory was intentionally exposed in the source code.

## What I Learned
Always look for source code to look for clues
