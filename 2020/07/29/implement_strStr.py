'''
28. Implement strStr() - Easy
https://leetcode.com/problems/implement-strstr/
'''

# 32 ms (73.81%) | 13.8MB (94.13%)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle: return 0 # consistent with strstr(), indexOf() [C, Java]
        if not haystack: return -1 # small optimization
        increment = len(needle) - 1
        left_ptr, right_ptr = 0, increment
        while right_ptr < len(haystack):
            if haystack[left_ptr:right_ptr + 1] == needle:
                return left_ptr
            left_ptr, right_ptr = left_ptr + 1, right_ptr + 1
        return -1

S = Solution()
print(S.strStr('hello', '')) # 0
print(S.strStr('', 'll')) # -1
print(S.strStr('hello', 'll')) # 2
print(S.strStr('aaaaa', 'bba')) # -1
print(S.strStr('aaaaaaabbaa', 'bba')) # 
print(S.strStr(' bfdjkl23b jbfjbjsjbgjsgsdfsdf sfdsd f sdf', 'gj')) # 

