# Natas Level 7 → 8

## Objective
Find the hidden password for the next level 

## Vulnerability
Exposed directories

## Reconnaissance
The page showed "Home" and "About" as the only clue. Each button shows a different URL parameter. For example, when the "Home" button is clicked, the URL shows as http://natas7.natas.labs.overthewire.org/index.php?page=about. 


## Exploitation

### Steps
1. View the source code by doing the ctrl + U command
2. The source code gives a hint: 
<!-- hint: password for webuser natas8 is in /etc/natas_webpass/natas8 -->
3. Manually alter the URL parameter by adding the said directory.

### Payload / Method
Manually change the URL paramter by adding the said directory
```
http://natas7.natas.labs.overthewire/etc/natas_webpass/natas8
```

## Why It Works
This method works because the directory was intentionally exposed in the source code.

## What I Learned
Always look for source code to look for clues
