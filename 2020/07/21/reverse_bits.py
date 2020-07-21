'''
190. Reverse Bits - Easy
https://leetcode.com/problems/reverse-bits/
'''
def reverse_bits(n: int):
    # bits = []
    # while n > 0:
    #     # bits.insert(0, n % 2)
    #     bits.append(n % 2)
    #     n //= 2
    # leading_zeroes = 32 - len(bits)
    # bits = bits + [0] * leading_zeroes # effective reversal without wasting time
    # print(bits, len(bits))
    # number = 0
    # for i, bit in enumerate(bits):
    #     number += bit * 2 ** (len(bits) - i - 1)
    # return number

    reverse_decimal_integer = 0
    for i in range(32):
        reverse_decimal_integer = (reverse_decimal_integer << 1) + (n & 1)
        n >>= 1
    return reverse_decimal_integer

print(reverse_bits(11))
print(reverse_bits(43261596))
print(reverse_bits(4294967293))