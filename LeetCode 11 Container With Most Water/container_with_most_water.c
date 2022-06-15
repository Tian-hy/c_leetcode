/**
 * @author tian_hy
 * LeetCode link: https://leetcode.com/problems/container-with-most-water/
 * Time Complexity: O(n) 对撞指针
 * Space Complexity: O(1)
 */

#include <stdio.h>

int maxArea(int* height, int heightSize){
    int i = 0, j = heightSize-1;
    int wdth, hght, max = 0;

    while(i < j){
        wdth = j - i;
        hght = (height[i] <= height[j])? height[i]: height[j];
        if (max < wdth*hght) {
            max = wdth * hght;
        }

        if (height[i] < height[j])
            i++;
        else
            j--;
    }
    return max;
}

void main(){
    int height[] = {1,8,6,2,5,4,8,3,7};
    int heightSize = sizeof(height)/sizeof(int);

    int max = maxArea(height, heightSize);
    printf("%d\n", max);
}