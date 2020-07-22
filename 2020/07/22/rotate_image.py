'''
48. Rotate Image - Medium
https://leetcode.com/problems/rotate-image/

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).
'''
class Solution:

    # INPLACE ROTATION
    def rotate(self, A):
        pass

    def rotate_pythonic(self, A):
        A[:] = zip(*A[::-1])

    def rotate_pythonic_resulting_in_list(self, A):
        A[:] = map(list, zip(*A[::-1]))

    def rotate_most_direct(self, A) -> None:
        dimension = len(A) # n x n implies square
        for i in range(dimension//2):
            for j in range(dimension - dimension//2):
                A[i][j], A[~j][i], A[~i][~j], A[j][~i] = \
                    A[~j][i], A[~i][~j], A[j][~i], A[i][j]

    def rotate_flip_flip(self, A):
        # print('A:\n{}'.format(A))
        A.reverse()
        # print('A\':\n{}'.format(A))
        for i in range(len(A)):
            for j in range(i):
                A[i][j], A[j][i] = A[j][i], A[i][j]
                # print('i={}, j={}\n{}'.format(i, j, A))



S = Solution()

A = [[1,2,3],
    [4,5,6],
    [7,8,9]]

B = [[ 5, 1, 9,11],
    [ 2, 4, 8,10],
    [13, 3, 6, 7],
    [15,14,12,16]]

C = [[]]


print(S.rotate(A))
print(S.rotate_flip_flip(B))
print(S.rotate(C))