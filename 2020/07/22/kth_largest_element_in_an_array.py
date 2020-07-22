'''
215. Kth Largest Element in an Array - Medium
https://leetcode.com/problems/kth-largest-element-in-an-array/

Find the kth largest element in an unsorted array. Note that it is the
 kth largest element in the sorted order, not the kth distinct element.
'''
class Solution:
    def find_kth_largest(self, array, k):
        # distinct:
        # kth_largest_array = list(reversed(list(set(list(sorted(array))))))
        kth_largest_array = list(reversed(sorted(array)))
        print(kth_largest_array)
        return kth_largest_array[k - 1]


S = Solution()
print(S.find_kth_largest([3, 2, 1, 5, 6, 4], 2)) # 5
print(S.find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)) # 4