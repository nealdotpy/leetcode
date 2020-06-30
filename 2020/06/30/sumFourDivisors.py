import math

'''
1390. Four Divisions - Medium
https://leetcode.com/problems/four-divisors/

Given an integer array nums, return the sum of divisors of the integers 
in that array that have exactly four divisors.

If there is no such integer in the array, return 0.

Constraints:
    1 <= nums.length <= 10^4
    1 <= nums[i] <= 10^5
'''
def sumFourDivisors(nums) -> int:
        # everything has at least 2 divisors (1 and itself)
        div_sum = 0
        def get_divs(n):
            divs = []
            i = 1
            while i <= math.sqrt(n):
                if (n % i == 0):
                    if (n / i == i):
                        divs.append(i)
                    else:
                        divs.append(i)
                        divs.append(n/i)
                i += 1
                if len(divs) > 4:
                    break
            
            return divs

        for num in nums:
            divs = get_divs(num)
            if len(divs) == 4:
                div_sum += sum(divs)

        return int(div_sum)

print('sum of div_c=4: {}'.format(sumFourDivisors([21,6,33,22,4,7])))

sumFourDivisors([])