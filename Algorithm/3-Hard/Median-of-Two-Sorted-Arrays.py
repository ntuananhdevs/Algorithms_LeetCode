# Intuition :To find median we need to add the two given sorted arrays into one array (or) a newarray and find its median.
# Approach:
# 1)take an newarray and assign two variables i,j to traverse the nums1,nums2 let m=len(nums1) and n=len)nums2
# 2) execute the while loop until i<=m and j<=n for traversal and adding the elements into the new array
# 3)if nums1[i]<nums2[j] implies the nums1[i] is less than nums2[j]
# we add the smaller element into the new array(the concepty which we use to merge two arrays in merge sort)
# 4)after completing the while loop there may be a chance for len(nums1)<len(nums2) or len(nums2)>len(num1) cosider as case1,case2

# so we had used two more while loops one for case 1 and other for case 2
# 6)after the loops we get the sorted newarray.find the median of the sorted array if len(newarray) is odd return(newarray[mid]/2)
# 7)if len(newarray) is even return median by return((newarray[mid-1]=newarray[mid],2))
# FINALLY WE GOT THE REQUIRED RESULT BUT THIS IS NOT THE ASKED ONE WE NEED TO SOLVE THIS BY O(LOG(m+N))
# TAKE THIS AS A BRUTE FORCE APPROACH WE SOLVE THIS BY USING TWO POINTERS(OPTIMIZED)


def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m=len(nums1)-1
        n=len(nums2)-1
        new=[]
        i,j=0,0
        while i<=m and j<=n:
            if nums1[i]<nums2[j]:
                new.append(nums1[i])
                i=i+1
            else:
                new.append(nums2[j])
                j=j+1
        while(i<=m):
            new.append(nums1[i])
            i=i+1
        while(j<=n):
            new.append(nums2[j])
            j=j+1
        median=len(new)
        i=median//2
        if median%2==0:
            median=(new[i-1]+new[i])/2
        else:
            median=new[i]
        return median