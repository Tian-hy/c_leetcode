/**
 * @author tian_hy
 * LeetCode link: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 */

#include <stdio.h>

int removeDuplicates(int* nums, int numsSize){
    int j=2, prev=nums[0];
    if (numsSize < 3){
        return numsSize;
    }
    for (int i=2; i<numsSize; i++){
        if (nums[i] != prev){
            prev = nums[i-1];
            if (i != j)
                nums[j] = nums[i];
            j++;
        }
        else
            prev = nums[i-1];
    }
    return j;
}

void main(){
    // int nums[] = {3, 4, 4, 4, 5, 5, 5, 6};
    int nums[] = {0, 1, 1, 1, 1, 2, 3, 3};
    int numsSize = sizeof(nums)/sizeof(int);
    int len = removeDuplicates(nums, numsSize);

    for (int i=0; i<len; i++){
        printf("%d ", nums[i]);
    }
    puts("");
}