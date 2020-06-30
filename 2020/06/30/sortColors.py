import math

'''
75. Sort Colors - Medium
https://leetcode.com/problems/sort-colors/

Given an array with n objects colored red, white or blue, 
sort them in-place so that objects of the same color are adjacent, 
with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent 
the color red, white, and blue respectively.

Other References: Dutch Flag Problem
'''
def sortColors(nums) -> None:
    red, white, blue = 0, 0, len(nums)-1
    
    while white <= blue:
        print(nums)
        if nums[white] == 0:
            nums[red], nums[white] = nums[white], nums[red]
            white += 1
            red += 1
        elif nums[white] == 1:
            white += 1
        else:
            nums[white], nums[blue] = nums[blue], nums[white]
            blue -= 1

    print(nums)

sortColors([2,0,2,1,1,0])