'''
371. Sum of Two Integers - Easy
https://leetcode.com/problems/sum-of-two-integers/

Calculate the sum of two integers a and b, but you are
not allowed to use the operator + and -.
'''
def get_sum(a: int, b: int) -> int:
    MAX = 0x7FFFFFFF
    MIN = 0x80000000
    MASK = 0xFFFFFFFF

    while b != 0:
        a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK
        
    return [a, ~(a ^ MASK)][a > MAX]


print(get_sum(4,7))
print(get_sum(4,0))
print(get_sum(-1,7))