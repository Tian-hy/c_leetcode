/**
 * @file move_zeros.c
 * @author tian_hy
 * LeetCode link: https://leetcode.com/problems/move-zeroes/
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 */

#include <stdio.h>

void moveZeroes(int* nums, int numsSize){
    for (int i = 0, j = 0, tmp; i < numsSize; i++){
        if (nums[i]){
            if(i != j){
                tmp = nums[j];
                nums[j++] = nums[i];
                nums[i] = tmp;
            }
            else{
                j++;
            }
        }
    }
}

void main(){
    int nums[] = {0, 1, 2, 0, 3, 1, 0};
    moveZeroes(nums, 7);
    for (int i = 0; i < 7; i++){
        printf("%d ", nums[i]);
    }
    puts("");
}