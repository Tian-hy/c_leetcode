/**
 * @author tian_hy
 * LeetCode link: https://leetcode.com/problems/sort-colors/
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 */

#include <stdio.h>

void merge(int* nums1, int nums1Size, int m, int* nums2, int nums2Size, int n){
    int k = (--m)+(n--);

    for (;k>=0; k--){
        if (m>=0 && n>=0){
            if (nums1[m] < nums2[n])
                nums1[k] = nums2[n--];
            else
                nums1[k] = nums1[m--];
        }
        else if (m < 0)
            nums1[k] = nums2[n--];
    }
}

void main(){
    int nums1[] = {2, 0};
    int nums1Size = sizeof(nums1)/sizeof(int);
    int nums2[] = {1};
    int nums2Size = sizeof(nums2)/sizeof(int);
    int m = 1, n = nums2Size;

    merge(nums1, nums1Size, m, nums2, nums2Size, n);

    for (int i=0; i<nums1Size; i++)
        printf("%d ", nums1[i]);
    puts("");
}