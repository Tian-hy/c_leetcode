/**
 * @author tian_hy
 * LeetCode link: https://leetcode.cn/problems/minimum-window-substring/
 * Time Complexity: O(n) 滑动窗口
 * Space Complexity: O(1)
 */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int is_win_substring(int *freq_s, int *freq_t){
    for (int i=0; i<'z'-'A'+1; i++){
        if (freq_s[i] < freq_t[i]){
            return 0;
        }
    }
    return 1;
}

char * minWindow(char * s, char * t){
    int i = 0, j = -1;
    int len = strlen(s), res_len = strlen(s)+1;
    int freq_s['z'-'A'+1] = {0};
    int freq_t['z'-'A'+1] = {0};
    int idx[2] = {0};

    for (; i<strlen(t); i++){
        freq_t[t[i]-'A']++;
    }
    i = 0;
    while (i < len){
        if (j+1 < len && !is_win_substring(freq_s, freq_t)){
            freq_s[s[++j]-'A']++;
        }
        else{
            freq_s[s[i++]-'A']--;
        }
        if (is_win_substring(freq_s, freq_t))
            if (res_len > j-i+1){
                res_len = j-i+1;
                idx[0] = i;
                idx[1] = j;
            }
    }

    if (res_len == strlen(s)+1){
        return "";
    }
    else{
        char *res = (char *)malloc(sizeof(char)*(idx[1]-idx[0]+2));

        for (int i=0; i<idx[1]-idx[0]+1; i++){
            res[i] = s[i+idx[0]];
        }
        res[idx[1]-idx[0]+1] = '\0';
        return res;
    }
}

void main(){
    char *s = "ADOBECODEBANC";
    char *t = "ABC";
    char *res = minWindow(s, t);
    puts(res);
}