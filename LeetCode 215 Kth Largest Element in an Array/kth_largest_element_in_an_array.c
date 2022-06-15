/**
 * @author tian_hy
 * LeetCode link: https://leetcode.cn/problems/kth-largest-element-in-an-array/
 * Time Complexity: O(nlgn) 用了快排
 * Space Complexity: O(1)
 */

#include <stdio.h>

int partition(int* nums, int low, int high){
    int tmp = nums[low];

    while (low < high){
        while (low < high && tmp <= nums[high])
            high--;
        nums[low] = nums[high];
        while (low < high && tmp >= nums[low])
            low++;
        nums[high] = nums[low];
    }
    nums[low] = tmp;
    return low;
}

void findk(int* nums, int low, int high, int pos){
    int mid;
    if (low >= high){
        return; 
    }

    mid = partition(nums, low, high);

    if (mid == pos)
        return;

    if (low <= pos && pos < mid)
        findk(nums, low, mid-1, pos);
    if (mid < pos && pos <= high)
        findk(nums, mid+1, high, pos);
}

int findKthLargest(int* nums, int numsSize, int k){
    int pos = numsSize-k;
    int low = 0, high = numsSize-1;
    findk(nums, low, high, pos);
    return nums[pos];
}

void main(){
    int nums[] = {1, 3, 2, 6, 4, 7, 3};
    int numsSize = sizeof(nums)/sizeof(int);
    int pos = 3;

    printf("%d\n", findKthLargest(nums, numsSize, pos));
}