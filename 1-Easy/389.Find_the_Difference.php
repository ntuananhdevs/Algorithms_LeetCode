<?php
class Solution {
/**
 * @param String $s
 * @param String $t
 * @return String
 */
function findTheDifference($s, $t) {
    $arr = [];
    for ($i = 0; $i < strlen($t); $i++){
        if(!isset($arr[$s[$i]])) $arr[$s[$i]] = 0;
        $arr[$s[$i]]++;
    }
    for ($i = 0; $i < strlen($s); $i++){
        if(empty($arr[$t[$i]])) return $t [$i];
        $arr[$t[$i]]--;
    }
}
}
?>