# Natas Level 12 → 13

## Objective
Find the password for the next level 

## Vulnerability
Unrestricted file upload.

## Reconnaissance
The page only shows a file input and an upload button. But, the source code didn't specify which type of file that can or can't be uploaded. They specified the type manually using a hidden input on the HTML code.

## Exploitation

### Steps
1. Do the ctrl + U command to view the source code
2. Take a careful look at the php code
3. Since the code didn't specify the file type and it was already specified on the HTML code, we can just make a simple PHP file and upload it


### Payload / Method
The file should consist a simple reading script
```
<?php
system("cat /etc/natas_webpass/natas13");
?>
```

## Why It Works
This method works because the hidden input on the HTML code can be freely manipulated by anyone who accesses the website.

## What I Learned
Apparently, if a website doesn't specify which type of file that can be uploaded, you can just upload a PHP file to run a script.
