<?php
//Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
// The overall run time complexity should be O(log (m+n)).

// Example 1:
// Input: nums1 = [1,3], nums2 = [2]
// Output: 2.00000
// Explanation: merged array = [1,2,3] and  median is 2.

// Example 2:
// Input: nums1 = [1,2], nums2 = [3,4]
// Output: 2.50000
// Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
class Solution {
/**
 * @param Integer[] $nums1
 * @param Integer[] $nums2
 * @return Float
 */
    function findMedianSortedArrays($nums1, $nums2) {
        $num = array_merge($nums1, $nums2);
        sort ($num);
        $count = count($num);
        if ($count % 2 == 1) {
            return $num[$count / 2];
        } 
        else {
            return ($num[$count / 2] + $num[$count / 2 - 1]) / 2;
        }
    }
}
?>