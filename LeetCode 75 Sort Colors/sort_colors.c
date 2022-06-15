/**
 * @file move_zeros.c
 * @author tian_hy
 * LeetCode link: https://leetcode.com/problems/sort-colors/
 */

#include <stdio.h>

/**
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 * 需要遍历两遍
 */
void sortColors1(int* nums, int numsSize){
    int counts[3] = {0, 0, 0}; // 存放0，1，2的个数
    int index = 0;
    int i, j;
    for (int i=0; i<numsSize; i++){
        counts[nums[i]]++;
    }
    
    // 重新赋值
    for(i=0; i<3; i++){
        for (j=0; j<counts[i]; j++){
            nums[index++] = i;
        }
    }
}

/**
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 * 三路快排只需要遍历一遍
 */
void sortColors2(int* nums, int numsSize){
    int zero = -1; // nums[0...zero] == 0
    int two = numsSize; // nums[two:n-1] == 2
    int tmp;
    for (int i = 0; i<two; ){
        if (nums[i] == 1)
            i++;
        else if (nums[i] == 2){
            tmp = nums[--two];
            nums[two] = nums[i];
            nums[i] = tmp;
        }
        else{ //nums[i] == 0
            tmp = nums[++zero];
            nums[zero] = nums[i];
            nums[i++] = tmp;
        }
    }
}

void main(){
    int nums[] = {1, 1, 0, 1, 2, 2, 0, 0};
    int numsSize = sizeof(nums)/sizeof(int);
    sortColors2(nums, numsSize);

    for (int i=0; i<numsSize; i++){
        printf("%d ", nums[i]);
    }
    puts("");
}