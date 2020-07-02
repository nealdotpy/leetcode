import math

'''
5. Longest Palindromic Substring - Medium
https://leetcode.com/problems/longest-palindromic-substring/

Given a string s, find the longest palindromic substring in s. 
You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:

Input: "cbbd"
Output: "bb"
'''

def longestPalindrome(s) -> str:
    def helper(s, l, r):
        # step through all possible middles and stop when palindrome breaks
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return s[l+1:r]

    res = ""
    for i in range(len(s)):
        # odd case, like "aba"
        tmp = helper(s, i, i)
        if len(tmp) > len(res):
            res = tmp

        # even case, like "abba"
        #print('<{}>'.format(tmp))
        tmp = helper(s, i, i+1)
        if len(tmp) > len(res):
            res = tmp
        #print('<{}>'.format(tmp))
    return res

print(longestPalindrome('hbabbad'))