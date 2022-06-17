/**
 * @author tian_hy
 * LeetCode link: https://leetcode.cn/problems/minimum-size-subarray-sum/
 * Time Complexity: O(n) 滑动窗口
 * Space Complexity: O(1)
 */

#include <stdio.h>

int minSubArrayLen(int target, int* nums, int numsSize){
    int i = 0, j = 0, len = numsSize+1;
    if (numsSize == 0)
        return 0;
    int sum = nums[0]; // 这里假设长度>=1，初始sum=nums[0]，也可以假设初始没有元素
    while (i < numsSize){
        if (sum >= target){
            len = (j-i+1 < len)? j-i+1: len;
            sum -= nums[i++];
        }
        else 
            if (++j < numsSize){
                sum += nums[j];
            }
            else{
                // 既然j已经超出numsSize了，而且sum<target，之后sum一直在减少
                // 不可能有再出现sum>target的情况出现，直接break了
                break;
            }
    }
    return (len <= numsSize)? len: 0;
}

void main(){
    int target = 11;
    int nums[] = {1, 1, 1, 1, 1, 1, 1, 1};
    int numsSize = sizeof(nums)/sizeof(int);
    int len = minSubArrayLen(target, nums, numsSize);

    printf("%d\n", len);
}