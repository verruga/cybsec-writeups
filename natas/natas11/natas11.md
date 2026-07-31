# Natas Level 11 → 12

## Objective
Decrypt the cookie to gain password 

## Vulnerability
Exposed cookie data & source code.

## Reconnaissance
The page says that cookies are protected with XOR encryption. But the source code itself is actually exposed.

## Exploitation

### Steps
1. Click F12 to look for the cookie data
2. Do ctrl + U to view the source code
3. The cookie is encrypted with base64 and XOR, so the decryption have to be done reversed.
4. Create a script based on the source code, you can reuse some of its functions and variables
5. Put the URL-encoded raw cookie data into the script, then hit run to get the pattern
6. Put the pattern as the key in the other script, then hit run to get the new cookie

### Payload / Method
Two scripts were used in order to get the cookie data.
```
First script:
<?php
$defaultdata = array("showpassword"=>"no", "bgcolor"=>"#ffffff");

function xor_encrypt($in) {
    $key= base64_decode("EGAgHwQ1IxYYMSQYGSZxTUksPFVHYDEQCC0%2FGBlgaVVIJDURDSQ1VRY=");
    $text = $in;
    $outText = '';

    for($i=0;$i<strlen($text);$i++) {
        $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }
    return $outText;
}
$b = xor_encrypt(json_encode($defaultdata));
print($b);
?>
```

```
Second script:
<?php
$defaultdata = array("showpassword"=>"yes", "bgcolor"=>"#ffffff");

function xor_encrypt($in) {
    $key= "kBSw";
    $text = $in;
    $outText = '';

    for($i=0;$i<strlen($text);$i++) {
        $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }
    return $outText;
}
$new = base64_encode(xor_encrypt(json_encode($defaultdata)));
print($new);
?>
```

## Why It Works
This method works because the source code exposed its method to encrypt the cookie data. So the cookie encryption can be decrypted by anyone who sees the source code.

## What I Learned
Cookie encryption can be reversed with online tools.
