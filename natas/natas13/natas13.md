# Natas Level 13 → 14

## Objective
Find the password for the next level 

## Vulnerability
File upload bypass

## Reconnaissance
The page only shows a file input and an upload button. But, the source code didn't specify which type of file that can or can't be uploaded. This time, they added exif_imagetype() on the code that serves as a failsafe. The thing is, exif_imagetype can be easily be bypassed since they only check the first bytes of an image file to check its signature and determine its image type.

## Exploitation

### Steps
1. Do the ctrl + U command to view the source code
2. Look at the exif_imagetype function
3. Create a php file that consists magic bytes of an image, for example GIF89a
4. Save the file then upload the file on the website

### Payload / Method
The file should consist a simple reading script
```
GIF89a
<?php system("cat /etc/natas_webpass/natas13"); ?>
```

## Why It Works
This method works because the code uses a exif_imagetype function that can be bypassed by putting magic bytes of an image file on the code.

## What I Learned
This time the website did specify the file type that can be uploaded, but its guarded by exif_imagetype function that can be easily be bypassed.
