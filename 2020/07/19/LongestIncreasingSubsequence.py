'''


'''
def lengthOfLIS(nums) -> int:
	'''
	up_to_point_LIS = []

	for value in nums:
		if not up_to_point_LIS:
			up_to_point_LIS.append(value)
			continue
		elif len(up_to_point_LIS) < 2 and value < up_to_point_LIS[0]:
			up_to_point_LIS.pop()
			up_to_point_LIS.append(value)	
		
		if len(up_to_point_LIS) == 1 and value > up_to_point_LIS[-1]:
			up_to_point_LIS.append(value)
		elif len(up_to_point_LIS) > 1 and value > up_to_point_LIS[-2] and value < up_to_point_LIS[-1]:
			up_to_point_LIS.pop()
			up_to_point_LIS.append(value)
		elif len(up_to_point_LIS) > 1 and value > up_to_point_LIS[-2] and value > up_to_point_LIS[-1]:
			up_to_point_LIS.append(value)

		print(up_to_point_LIS)
	return len(up_to_point_LIS)
	'''
	tails = [0] * len(nums)
	size = 0
	for x in nums:
		print('evaluating x={}'.format(x))
		print('current size->{}'.format(size))
		i, j = 0, size
		print(tails)
		if i != j: print('starting binary search...')
		while i != j:
			print('looking in the range [i={}, j={}]'.format(i, j))
			m = (i + j) // 2
			if tails[m] < x:
				print('tails[{}] < x={}'.format(m, x))
				i = m + 1
			else:
				print('tails[{}] >= x={}'.format(m, x))				
				j = m
		print('setting tails[i={}] to x={}'.format(i, x))
		tails[i] = x
		print('setting size to max({}+1, size={})'.format(i, size))
		size = max(i + 1, size)
	return size

	

A = []#[10,9,2,5,3,7,101,18]
B = []#[-1,-5,-123,3,4,5,923,1202]
C = [9,10,11,12,2,42,23,3,4,5]#,7,8,120]

print(lengthOfLIS(A))
print(lengthOfLIS(B))
print(lengthOfLIS(C))