'''
171. Excel Sheet Column Number - Easy
https://leetcode.com/problems/excel-sheet-column-number/

Given a column title as appear in an Excel sheet, return 
its corresponding column number.
'''
def title_to_number(s: str) -> int:
    '''
    excel_column = s.upper()[::-1] # reverse for ease

    def base26(letter) -> int:
        return ord(letter) - 64 # ASCII convention

    column_number = 0
    number_place = 0
    for char in excel_column:
        column_number += base26(char) * 26 ** number_place
        number_place += 1

    return column_number
    '''
    return reduce(lambda x, y : x * 26 + y, [ord(c) - 64 for c in list(s)])


print(title_to_number('AA'))
print(title_to_number('A'))
print(title_to_number('AZ'))
print(title_to_number('BD'))
print(title_to_number('BZ'))
print(title_to_number('ABCD'))
print(title_to_number('ZAZA'))
print(title_to_number('YKFODA'))