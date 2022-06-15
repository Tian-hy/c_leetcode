/**
 * @author tian_hy
 * LeetCode link: https://leetcode.com/problems/reverse-string/
 * Time Complexity: O(n) 对撞指针
 * Space Complexity: O(1)
 */

#include <stdio.h>

void reverseString(char* s, int sSize){
    int i = 0, j = sSize-1;
    char tmp;

    while(i < j){
        tmp = s[i];
        s[i++] = s[j];
        s[j--] = tmp;
    }
}

void main(){
    char s[] = "hello";
    reverseString(s, 5);
    puts(s);
}