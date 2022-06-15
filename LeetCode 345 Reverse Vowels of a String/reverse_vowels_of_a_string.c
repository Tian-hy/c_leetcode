/**
 * @author tian_hy
 * LeetCode link: https://leetcode.cn/problems/reverse-vowels-of-a-string/ 
 * Time Complexity: O(n) 对撞指针
 * Space Complexity: O(1)
 */

#include <stdio.h>
#include <string.h>
#include <ctype.h>

char * reverseVowels(char * s){
    int i = 0, j = strlen(s)-1;
    char tmp;

    while(i < j){
        tmp = tolower(s[i]);
        if (tmp!='a'&&tmp!='e'&&tmp!='i'&&tmp!='o'&&tmp!='u'){
            i++;
            continue;
        }
        tmp = tolower(s[j]);
        if (tmp!='a'&&tmp!='e'&&tmp!='i'&&tmp!='o'&&tmp!='u'){
            j--;
            continue;
        }
        tmp = s[i];
        s[i++] = s[j];
        s[j--] = tmp;
    }
    return s;
}

void main(){
    char s[] = "hello";
    strcpy(s, reverseVowels(s));
    puts(s);
}