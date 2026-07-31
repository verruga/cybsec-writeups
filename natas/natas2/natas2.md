# Natas Level 2 → 3

## Objective
Find the hidden password for the next level

## Vulnerability
Exposed file directory

## Reconnaissance
The page showed "There is nothing on this page" that doesn't help much as a clue. Since the source code doesn't contain any password, I might have to inspect the website's element.

## Exploitation

### Steps
1. Do the F12 command or right click the page and click on "Inspect Element"
2. Click on "Sources"
3. There is a file named "pixel.png" that is placed inside a directory named "files"
4. Slightly alter the web url by adding /files to the end
5. There are 2 files stored in the "files" directory; pixel.png and users.txt
6. Open the users.txt file

### Payload / Method
```
F12 command; Sources
```

## Why It Works
The web has a publicly exposed file directory that contains a file that contains a natas3 password

## What I Learned
A website might have an exposed file directory that is worth checking
