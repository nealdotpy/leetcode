'''
198. House Robber - Easy
https://leetcode.com/problems/house-robber/
'''
def rob(nums):
    # dynamic_sol = [(nums[0], 0)] * (len(nums) + 1)
    # for i, dollar_amt in enumerate(nums):
    #     if i - dynamic_sol[i][1] >= 2: # !neighbors
    #         dynamic_sol[i + 1] = (dynamic_sol[i][0] + dollar_amt, i)
    #     else: # neighbors
    #         dynamic_sol[i + 1] = (max(nums[dynamic_sol[i][1]], dollar_amt), i)
    # print(dynamic_sol)
    # return 0
    aggregate_memory = [-1] * (len(nums) + 1)
    def rob(value_for_each_house, current_house):
        if current_house < 0:
            return 0
        if aggregate_memory[current_house] >= 0:
            return aggregate_memory[current_house]

        max_money_up_to_current = max(rob(value_for_each_house, current_house - 2) + \
                value_for_each_house[current_house], \
                rob(value_for_each_house, current_house - 1))
        aggregate_memory[current_house] = max_money_up_to_current
        return max_money_up_to_current

    return rob(nums, len(nums) - 1)

print(rob([1, 2, 3, 1]))
print(rob([2, 7, 9, 3, 1]))


