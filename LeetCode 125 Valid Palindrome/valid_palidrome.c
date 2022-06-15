/**
 * @author tian_hy
 * LeetCode link: https://leetcode.cn/problems/valid-palindrome/
 * Time Complexity: O(n) 对撞指针
 * Space Complexity: O(1)
 */
#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <ctype.h>

bool isPalindrome(char * s){
    int i = 0, j = strlen(s)-1;
    while(i<j){
        if (!isdigit(s[i]) && !isalpha(s[i])){
            i++;
            continue;
        }
        if (!isdigit(s[j]) && !isalpha(s[j])){
            j--;
            continue;
        }
        if (tolower(s[i]) != tolower(s[j]))
            return false;
        else{
            i++;
            j--;
        }
    }
    return true;
}

void main(){
    char *s = "1A man, a plan, a canal: Panama";
    bool flag = isPalindrome(s);
    printf("%d\n", flag);
}