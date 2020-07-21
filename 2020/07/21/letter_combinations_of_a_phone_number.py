'''
17. Letter Combinations of a Phone Number - Medium
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
'''
from timeit import default_timer as timer
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

class Solution:

    MAPPINGS = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }

    def letter_combinations(self, digits: str, y_dictionary=None):
        # len(digits) -> determines lenght of any 1 combination
        # l_c('33') -> dd, de, df ... fd, fe, ff
        # l_c('334') = lc('33'U'4') -> ddg, ddh, ddi, ... ffg, ffh, ffi 
        # print(digits)
        if not digits: return []
        if len(digits) == 1: return self.MAPPINGS[digits[0]]


        y_dictionary = self.letter_combinations(digits[:len(digits) - 1], y_dictionary)
        # '23', yd = [abc]
        # print(digits)

        result_dictionary = []
        if y_dictionary:
            x_dictionary = self.MAPPINGS[digits[-1]]
            # print(y_dictionary, x_dictionary)
            for permutation_y in y_dictionary:
                for permutation_x in x_dictionary:
                    result_dictionary.append(permutation_y + permutation_x)
            # print(result_dictionary)


        return result_dictionary

s = Solution()

print(s.letter_combinations(''))
print(s.letter_combinations('2'))
print(s.letter_combinations('23'))
print(s.letter_combinations('234'))


test_cases = ['', '2', '23', '234', '2756', 
    '74523', '394933', '8568563', '994384337',
    '756568977', '7765687437', '75756897457', '757656894357', '7576568974357',
    '75765689743575', '757656899743557']

# solution_large = s.letter_combinations()
# print(solution_large)
# print(len(len(solution_large))

len_perms = []
len_time = []

for case in test_cases:
    start = timer()
    ord_pair = (len(case), len(s.letter_combinations(case)))
    end = timer()

    len_perms.append(ord_pair)
    len_time.append((len(case), end - start))

    # print('({}, {})'.format(len(case), len(s.letter_combinations(case))))

# print(len_perms)
# print(len_time)



fig, (ax1, ax2) = plt.subplots(2, 1)
fig.suptitle('the biggest of the O\'s')

ax1.plot([x[0] for x in len_perms], [x[1] for x in len_perms], 'o-')
# ax1.set_xlabel('len(n)')
ax1.set_ylabel('perm(n)')

ax2.plot([x[0] for x in len_time], [x[1] for x in len_time], '.-')
ax2.set_xlabel('len(n)')
ax2.set_ylabel('time (s)')

plt.show()