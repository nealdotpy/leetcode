'''
204. Count Primes - Easy
https://leetcode.com/problems/count-primes/
'''
from functools import reduce

class Solution:
    def count_primes(self, n: int) -> int:
        if n <= 1: return 0
        sieve = dict()
        for number in range(2, n): # O(n)
            sieve[number] = True

        number = 2
        while number**2 < n:
            if not sieve[number]: number += 1; continue;
            for i in range(number**2, n, number):
                sieve[i] = False
            number += 1
        # print(sieve)
        return sum(sieve.values())#reduce(lambda total, value: [total, total + 1][value], sieve.values(), 0)



S = Solution()
print(S.count_primes(10)) # 4 {2,3,5,7}
print(S.count_primes(122)) # 
print(S.count_primes(10000)) # 1229