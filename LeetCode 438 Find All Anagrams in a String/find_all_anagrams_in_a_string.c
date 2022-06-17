/**
 * @author tian_hy
 * LeetCode link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
 * Time Complexity: O(n) 滑动窗口
 * Space Complexity: O(1)
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int is_anagrams(int *freq_s, int *freq_p){
    for (int i=0; i<26; i++){
        if (freq_s[i] != freq_p[i]){
            return 0;
        }
    }
    return 1;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findAnagrams(char * s, char * p, int* returnSize){
    int *pos = (int *)malloc(strlen(s)*sizeof(int));
    memset(pos, 0, strlen(s)*sizeof(int));
    int freq_p[26] = {0}; //只考虑小写字母
    int freq_s[26] = {0}; //只考虑小写字母
    int i = 0, j = -1;
    *returnSize = 0;

    for (; i < strlen(p); i++){
        freq_p[p[i] - 'a']++;
    }
    i = 0;
    while(i < strlen(s)){
        if (j+1 < strlen(s) && freq_s[s[j+1]-'a'] < freq_p[s[j+1]-'a']){
            freq_s[s[++j]-'a']++;
            if (is_anagrams(freq_s, freq_p)){
                pos[*returnSize] = i;
                *returnSize += 1;
            }
        }
        else{
            freq_s[s[i++]-'a']--;
        }
    }
    return pos;
}

void main(){
    char *s = "cbaebabacd";
    char *p = "abc";
    int *returnSize;
    int *pos = findAnagrams(s, p, returnSize);

    for (int i=0; i<*returnSize; i++){
        printf("%d ", pos[i]);
    }
    puts("");

    free(pos);
}