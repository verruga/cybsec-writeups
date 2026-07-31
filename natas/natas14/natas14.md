# Natas Level 14 → 15

## Objective
Find the password for the next level 

## Vulnerability
SQL injection

## Reconnaissance
The page shows a login form with a username and a password field. The source code shows that the query often uses a double quote, that can be bypassed using input + ", for example natas15".

## Exploitation

### Steps
1. Insert natas15" OR 1=1 # on the username field
2. Hit enter

### Payload / Method
```
Since the query often uses double quotes, so when I insert natas15", the query should work as "SELECT * from users WHERE username = "natas15"". Without the ", the injection wouldn't work. Because the other " would exclude the rest of the query, and the # makes the rest of the query get ignored.
```

## Why It Works
This method works because the query uses double quotes that can be bypassed with conditions that are always true
## What I Learned
Double quotes can actually be bypassed using a quote when inserting something on a field.