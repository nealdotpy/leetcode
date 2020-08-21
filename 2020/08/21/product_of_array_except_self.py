class Solution:
    def productExceptSelf(self, numbers: List[int]) -> List[int]:
        len_list = len(numbers)
        prefix = [1] * len_list
        postfix = [1] * len_list
        for i in range(1, len_list): # (1, 2, 3)
            prefix[i] *= numbers[i-1] * prefix[i-1]
        numbers.reverse()# = numbers[::-1]
        for i in range(1, len_list): # (1, 2, 3)
            postfix[i] *= numbers[i-1] * postfix[i-1]
        #for i in range(len_list, 0, -1): # (3, 2, 1)
        #postfix[i] *= numbers[i+1] * postfix[i+1]
        prefix.reverse()
        for i in range(len_list):
            numbers[i] = prefix[i] * postfix[i]

        return numbers[::-1]