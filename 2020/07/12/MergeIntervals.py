'''
56. Merge Intervals - Medium
https://leetcode.com/problems/merge-intervals/

Given a collection of intervals, merge all overlapping intervals.

Example 1:
	Input: [[1,3],[2,6],[8,10],[15,18]]
	Output: [[1,6],[8,10],[15,18]]
	Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:
	Input: [[1,4],[4,5]]
	Output: [[1,5]]
	Explanation: Intervals [1,4] and [4,5] are considered overlapping.

NOTE: input types have been changed on April 15, 2019. 
Please reset to default code definition to get new method signature.
'''

def merge(slots):
	'''
	if not len(slots): return []
	elif len(slots) == 1: return slots
	res = []
	i = 0
	slots = sorted(slots, key=lambda i: i[0])
	while len(slots)-1 > i:
		l1, r1 = slots[i][0], slots[i][1]
		l2, r2 = slots[i+1][0], slots[i+1][1]
		print('looking at: [{}, {}] -> [{}, {}]'.format(l1,r1,l2,r2))
		if l1 == l2 and r1 == r2: 
			res.append([l1, r1])
			i += 1
			continue
		r1a, l2a = r1, l2
		while r1a >= l2a:
			i += 1
			r1a = slots[i][1]
			if i+1 < len(slots):
				l2a = slots[i+1][0]
			else:
				break

		if r1a > r1: # shifted to the right for sure
			res.append([l1, r1a])
		elif r1a == r1:
			res += [[l1, r1], [l2, r2]]

		i += 1
	return res
	'''
	res = []
	print(len(slots))
	if len(slots) == 1: return slots
	for slot in sorted(slots, key=lambda L: L[0]): # sort (L, R) so L->L+
		#print(slot)
		if res and slot[0] <= res[-1][1]: # end of res, R value
			res[-1][1] = max(res[-1][1], slot[1])
		else:
			res += [slot]
	return res

print(merge([[1,3],[2,6],[8,10],[15,18]]))
print(merge([[1,4],[4,5]]))
print(merge([[1,4],[4,5],[5,7],[7,9],[11,20],[14,21],[15,22]]))
print(merge([[1,4],[1,4]]))
print(merge([[]]))
print(merge([[1,4]]))
