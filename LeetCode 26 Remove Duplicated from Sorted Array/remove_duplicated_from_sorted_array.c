/**
 * @file remove_elements.c
 * @author tian_hy
 * LeetCode link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 */

#include <stdio.h>

int removeDuplicates(int* nums, int numsSize){
    int j=1;
    if (numsSize < 2){
        return 1;
    }
    for (int i=1; i<numsSize; i++){
        if (nums[i] != nums[i-1]){
            if (i != j)
                nums[j] = nums[i];
            j++;
        }
    }
    return j;
}

void main(){
    int nums[] = {3, 4, 4, 5};
    int numsSize = sizeof(nums)/sizeof(int);
    int len = removeDuplicates(nums, numsSize);

    for (int i=0; i<len; i++){
        printf("%d ", nums[i]);
    }
    puts("");
}