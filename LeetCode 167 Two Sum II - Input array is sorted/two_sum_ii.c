/**
 * @author tian_hy
 * LeetCode link: https://leetcode.com/problems/sort-colors/
 * Time Complexity: O(n) 对撞指针
 * Space Complexity: O(1)
 */

#include <stdio.h>
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* numbers, int numbersSize, int target, int* returnSize){
    int * returnNums = (int *)malloc(sizeof(int) * numbersSize);
    int i=0, j=numbersSize-1;
    int sum;
    *returnSize = 2;
    while (i<j){
        sum = numbers[i] + numbers[j];
        if (sum < target)
            i++;
        else if (sum == target){
            returnNums[0] = i+1;
            returnNums[1] = j+1;
            return returnNums;
        }
        else
            j--;
    }
    *returnSize = 0;
    return returnNums;
}

void main(){
    int nums[] = {2, 7, 11, 15};
    int numsSize = sizeof(nums)/sizeof(int);
    int target = 9;
    int *returnSize;
    int *returnNums = twoSum(nums, numsSize, target, returnSize);

    for (int i=0; i<*returnSize; i++){
        printf("%d ", returnNums[i]);
    }
    puts("");

    free(returnNums);
}
