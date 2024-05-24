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
        if ($count % 2 == 1){
            return $num[$count / 2];
        }
        else{
            return ( $num[$count / 2] + $num[$count / 2 - 1] ) / 2;
        }
    }
}

//tối ưu
function findMedianSortedArrays($nums1, $nums2) {
    $m = count($nums1);
    $n = count($nums2);

    // Đảm bảo nums1 là mảng nhỏ hơn
    if ($m > $n) {
        return findMedianSortedArrays($nums2, $nums1);
    }

    $imin = 0;
    $imax = $m;
    $half_len = intval(($m + $n + 1) / 2);

    while ($imin <= $imax) {
        $i = intval(($imin + $imax) / 2);
        $j = $half_len - $i;

        if ($i < $m && $nums2[$j - 1] > $nums1[$i]) {
            // i quá nhỏ, phải tăng lên
            $imin = $i + 1;
        } elseif ($i > 0 && $nums1[$i - 1] > $nums2[$j]) {
            // i quá lớn, phải giảm xuống
            $imax = $i - 1;
        } else {
            // i là hoàn hảo
            if ($i == 0) {
                $max_of_left = $nums2[$j - 1];
            } elseif ($j == 0) {
                $max_of_left = $nums1[$i - 1];
            } else {
                $max_of_left = max($nums1[$i - 1], $nums2[$j - 1]);
            }

            if (($m + $n) % 2 == 1) {
                return $max_of_left;
            }

            if ($i == $m) {
                $min_of_right = $nums2[$j];
            } elseif ($j == $n) {
                $min_of_right = $nums1[$i];
            } else {
                $min_of_right = min($nums1[$i], $nums2[$j]);
            }

            return ($max_of_left + $min_of_right) / 2;
        }
    }

    throw new Exception("Input arrays are not sorted or have invalid length.");
}


?>