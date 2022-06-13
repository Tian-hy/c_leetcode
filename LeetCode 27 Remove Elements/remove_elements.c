/**
 * @file remove_elements.c
 * @author tian_hy
 * LeetCode link: https://leetcode.com/problems/remove-element/
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 */

#include <stdio.h>

int removeElement(int* nums, int numsSize, int val){
    int j = 0;
    for (int i=0; i<numsSize; i++){
        if(nums[i] != val)
            nums[j++] = nums[i];
    }
    return j;
}

int main(){
    int data[]={1, 2, 3, 3, 4, 1, 2}, numsSize=7, val=3;
    int j=removeElement(data, numsSize, val);

    for (int i=0; i<j; i++){
        printf("%d ", data[i]);
    }
    puts("");
}