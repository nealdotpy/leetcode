'''
17. Letter Combinations of a Phone Number - Medium
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
'''
class Solution:

    MAPPINGS = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }

    def letter_combinations(self, digits: str, y_dictionary=None):
        # len(digits) -> determines lenght of any 1 combination
        # l_c('33') -> dd, de, df ... fd, fe, ff
        # l_c('334') = lc('33'U'4') -> ddg, ddh, ddi, ... ffg, ffh, ffi 
        # print(digits)
        if not digits: return []
        if len(digits) == 1: return self.MAPPINGS[digits[0]]


        y_dictionary = self.letter_combinations(digits[:len(digits)-1], y_dictionary)
        # '23', yd = [abc]

        # print(digits)

        result_dictionary = []
        if y_dictionary:
            x_dictionary = self.MAPPINGS[digits[-1]]
            # print(y_dictionary, x_dictionary)
            for perm_y in y_dictionary:
                for perm_x in x_dictionary:
                    result_dictionary.append(perm_y + perm_x)
            # print(result_dictionary)


        return result_dictionary

s = Solution()

print(s.letter_combinations('23'))
print(s.letter_combinations('234'))



