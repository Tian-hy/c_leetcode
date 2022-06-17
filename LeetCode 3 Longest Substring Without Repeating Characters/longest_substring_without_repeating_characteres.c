/**
 * @author tian_hy
 * LeetCode link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
 * Time Complexity: O(n) 滑动窗口
 * Space Complexity: O(1)
 */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int lengthOfLongestSubstring(char * s){
    int freq[256] = {0};
    int i = 0, j = -1;
    int len = 0, max = 0;

    while (i < strlen(s)){
        if (j+1 < strlen(s) && freq[s[j+1]] == 0){
            freq[s[++j]]++;
            len++;
            max = (max<len)? len: max;
        }
        else{
            freq[s[i++]]--;
            len--;
        }
    }
    return max;
}

void main(){
    char *s = "pwwkew";
    printf("%d\n", lengthOfLongestSubstring(s));
}