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