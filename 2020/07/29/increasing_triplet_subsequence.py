'''
334. Increasing Triplet Subsequence - Medium
https://leetcode.com/problems/increasing-triplet-subsequence/
'''

class Solution:
    def increasing_triplet(self, nums) -> bool:
        if len(nums) < 3: return False
        tier1 = tier2 = float('inf')
        for number in nums:
            if number <= tier1:
                tier1 = number
            elif number <= tier2:
                tier2 = number
            else:
                return True
        return False
        



SOL = Solution()
print(SOL.increasing_triplet([1, 2])) # false
print(SOL.increasing_triplet([])) # false
print(SOL.increasing_triplet([1, 2, 3, 4, 5])) # true
print(SOL.increasing_triplet([5, 4, 3, 2, 1])) # false
print(SOL.increasing_triplet([1, 3, 1, 2, 1, 5, 7, 5, 7, 192, 1])) # true
print(SOL.increasing_triplet([1341, 332, 1, -202, 155, 56, 7, 57, 87, 51, 21])) # true

# for myself and some random curiosity
class Paper:
    def __init__(self, length=0.30, width=0.30, thickness=0.0001): # in meters
        self.length = length
        self.width = width
        self.thickness = thickness
        self.folds = 0

    def fold(self, num_of_folds=1):
        for i in range(num_of_folds):
            if self.folds % 2: # 1 -> length-wise fold
                self.length /= 2
            else: # 0 -> width-wise fold
                self.width /= 2
            self.thickness *= 2
            self.folds += 1

    def dimensions(self):
        return 'folds: {} | l: {}m, w: {}m, t: {}m'.format(self.folds, self.length, self.width, self.thickness)

# DIST_TO_SUN_IN_METERS = 149.6 * 10 ** 9
# P = Paper(1, 1)
# while P.thickness < DIST_TO_SUN_IN_METERS:
#     P.fold()
#     print(abs(P.thickness - DIST_TO_SUN_IN_METERS))
# print(P.dimensions())