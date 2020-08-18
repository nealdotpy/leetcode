from functools import reduce

'''
class Solution:
    def decode_string(self, string: str) -> str:
        encoded_stack = string.split(']')
        print(encoded_stack)
        decoded_stack = []
        # O(n) | n = len(qstring)
        def string_has_brackets(qstring: str) -> bool: 
            # CODE HERE
            for char in qstring:
                if char_is_bracket(char):
                    return True
            return False

        def char_is_bracket(qstring: str) -> int:
            # [ -> return -1
            # ] -> return 1
            if ord(qstring) == 91:
                return -1
            elif ord(qstring) == 93:
                return 1
            else:
                return 0

        def char_is_number(qstring: str) -> bool:
            # CODE HERE
            return 47 <= ord(qstring) <= 57

        def compress_encoded_stack(aggregate, element):
            if not char_is_number(element):
                aggregate = element + aggregate
            else:
                aggregate *= int(element)
            return aggregate

        if not string_has_brackets(string): return string

        for part in encoded_stack: # O(ES)
            if len(part) == 0: continue # don't process any ''
            part = part.split('[')
            if len(part) == 2:
                prefix = ''.join([i for i in part[0] if i.isalpha()])
                number = ''.join([i for i in part[0] if i.isdigit()])
                part = prefix + int(number) * part[1]
            else:
                part = list(''.join(part))
                part = reduce(compress_encoded_stack, part[::-1], "") # O(p)
            decoded_stack.append(part)
            # print(decoded_stack)
        
        return ''.join(decoded_stack)
'''
class Solution:
    def decode_string(self, s: str) -> str:
        stack = []
        stack.append(["", 1])
        num = ""
        for ch in s:
            if ch.isdigit():
              num += ch
            elif ch == '[':
                stack.append(["", int(num)])
                num = ""
            elif ch == ']':
                st, k = stack.pop()
                stack[-1][0] += st*k
            else:
                stack[-1][0] += ch
        return stack[0][0]



s = "3[a]2[bc]"
s2 = "3[a2[c]]"
smine = "2[abc]3[c2[d]]ef"
s3 = "ziz10[abc]3[c2[d]]ef"
s4 = "3[a]2[b4[F]c]"
S = Solution()
print(S.decode_string(s))
print(S.decode_string(s2))
print(S.decode_string(smine))
print(S.decode_string(s3))
print(S.decode_string(s4))