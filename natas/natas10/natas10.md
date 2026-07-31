# Natas Level 10 → 11

## Objective
Find the hidden password for the next level 

## Vulnerability
Command injection on the search bar

## Reconnaissance
The page now says that special characters are filtered to avoid any command injections. That means a "|" can no longer be used.

## Exploitation

### Steps
1. Look for clues in the source code
2. It still uses the same command: "grep -i $key dictionary.txt"
3. Try using the command directly instead of adding a "|"
4. Type "$ cat /etc/natas_webpass/natas10" on the search bar, then hit enter

### Payload / Method

```
Instead of altering the command by adding a "|", try using the "$ cat /etc/natas_webpass/natas10" directly on the search bar.
```

## Why It Works
This method works because a command injection was possible to be done on the search bar

## What I Learned
Always look for source code to look for clues
