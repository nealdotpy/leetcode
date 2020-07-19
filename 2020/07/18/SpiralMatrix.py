'''
54. Spiral Matrix - Medium
https://leetcode.com/problems/spiral-matrix/

Given a matrix of m x n elements (m rows, n columns), 
return all elements of the matrix in spiral order.

Example 1:

	Input:
	[
	 [ 1, 2, 3 ],
	 [ 4, 5, 6 ],
	 [ 7, 8, 9 ]
	]
	Output: [1,2,3,6,9,8,7,4,5]

Example 2:

	Input:
	[
	  [1, 2, 3, 4],
	  [5, 6, 7, 8],
	  [9,10,11,12]
	]
	Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''
def spiral(matrix):
	'''
	max_i = len(matrix)
	max_j = len(matrix[0])
	end_i = max_i // 2 #+ max_i % 2
	end_j = max_j // 2 #+ max_i % 2
	start_i = 0
	start_j = 0

	queue = []

	if end_j == 0:
		for i in range(max_i):
			queue.append(matrix[i][0])
		return queue

	while max_i > end_i and max_j > end_j:
		print('new while')
		print(queue)
		print('max_i->{}, max_j->{}, end_i->{}, end_j-{}, start_i->{}, start_j->{}'.format(max_i, max_j, end_i,end_j,start_i,start_j))
		
		for j in range(start_j, max_j, 1):
			queue.append(matrix[start_i][j])

		start_j = max_j-1
		print('max_i->{}, max_j->{}, end_i->{}, end_j-{}, start_i->{}, start_j->{}'.format(max_i, max_j, end_i,end_j,start_i,start_j))
		print(queue)
		
		for i in range(start_i+1, max_i-1, 1):
			queue.append(matrix[i][start_j])

		start_i = max_i-1
		print('max_i->{}, max_j->{}, end_i->{}, end_j-{}, start_i->{}, start_j->{}'.format(max_i, max_j, end_i,end_j,start_i,start_j))
		print(queue)
		
		if start_i == end_i or start_j == end_j:
			break

		for j in range(start_j, 0, -1):
			queue.append(matrix[start_i][j])

		start_j = len(matrix[0]) - max_j
		print('max_i->{}, max_j->{}, end_i->{}, end_j-{}, start_i->{}, start_j->{}'.format(max_i, max_j, end_i,end_j,start_i,start_j))
		print(queue)
		
		for i in range(start_i, 0, -1):
			queue.append(matrix[i][start_j])

		start_i = len(matrix) - max_i
		print('max_i->{}, max_j->{}, end_i->{}, end_j-{}, start_i->{}, start_j->{}'.format(max_i, max_j, end_i,end_j,start_i,start_j))
		print(queue)
		
		start_j += 1
		start_i += 1

		max_i -= 1
		max_j -= 1

	return queue
	'''

	if matrix == []:
          return matrix

        l = 0
        r = len(matrix[0]) - 1
        t = 0
        b = len(matrix) - 1

        ret = []
        while l < r and t < b:
        	# top
        	for i in range(l, r):
        		ret.append(matrix[t][i])
        	# right
        	for i in range(t, b):
        		ret.append(matrix[i][r])
        	# bottom
        	for i in range(r, l, -1):
        		ret.append(matrix[b][i])
        	# left
        	for i in range(b, t, -1):
        		ret.append(matrix[i][l])

	        l += 1
	        r -= 1 
	        t += 1
	        b -= 1

	    # single square
        if l == r and t == b:
        	ret.append(matrix[t][l])
        # vertical line
       	elif l == r:
       		for i in range(t, b + 1):
       			ret.append(matrix[i][l])
       	# horizontal line
       	elif t == b:
       		for i in range(l, r + 1):
       			ret.append(matrix[t][i])
       	return ret


Z = [[4,7,6,8], [2,5,3,1], [6,7,10,14]]

A = [[1,2,3,4,5,6,]]

B = [[1,2],[4,3]]

print('A={}'.format(spiral(A)))
print('B={}'.format(spiral(B)))
print('Z={}'.format(spiral(Z)))


