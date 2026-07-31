# Natas Level 9 → 10

## Objective
Find the hidden password for the next level 

## Vulnerability
Command injection on the search bar

## Reconnaissance
The page showed a search bar to find words containing "blabla". Any output will be originated from the dictionary.txt, because there is a function that will automatically gain information from the dictionary.txt based on the key input.

## Exploitation

### Steps
1. Every password is contained in the same directory /etc/natas_webpass/natasX'
2. Type the function that is used in the source code and add a "|", so that a second command can be run
3. Type "cat /etc/natas_webpass/natas9" after the "|"

### Payload / Method

```
Look for the source code for clues. The source code contains a "grep -i $key dictionary.txt" command. Slightly alter the command by adding "| cat /etc/natas_webpass/natas9" to read the natas9 password. Put the altered command on the search bar then hit enter.
```

## Why It Works
This method works because a command injection was possible to be done on the search bar

## What I Learned
Always look for source code to look for clues
