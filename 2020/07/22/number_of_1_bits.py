'''
191. Number of 1 Bits - Easy
https://leetcode.com/problems/number-of-1-bits/
'''

class Solution:
    def hamming_weight(self, unsigned_int: int) -> int:
        hamming_count = 0
        while unsigned_int != 0:
            if unsigned_int & 1:
                hamming_count += 1
            unsigned_int >>= 1
        return hamming_count

S = Solution()
print(S.hamming_weight(11))
print(S.hamming_weight(3))
print(S.hamming_weight(21))
print(S.hamming_weight(8))
print(S.hamming_weight(2))
print(S.hamming_weight(32))