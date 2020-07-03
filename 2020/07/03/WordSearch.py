

def exist(board, word) -> bool:
	def dfs(board, i, j, word):
		if len(word) == 0: 
			return True # we got em
		if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
			return False
		tmp = board[i][j]
		board[i][j] = '*'
		ans = dfs(board, i+1, j, word[1:]) or dfs(board, i-1, j, word[1:]) or \
				dfs(board, i, j+1, word[1:]) or dfs(board, i, j-1, word[1:])
		board[i][j] = tmp
		return ans

	
	for i in range(len(board)): # find starting points for DFS or BFS
		for j in range(len(board[0])):
			if dfs(board, i, j, word):
				return True
	return False

	'''
	def dfs(board, word, tup):
		up = board[tup[0]-1][tup[1]] if tup[0] > 0 else 'na'
		down = board[tup[0]+1][tup[1]] if tup[0] < len(board)-1 else 'na'
		left = board[tup[0]][tup[1]-1] if tup[1] > 0 else 'na'
		right = board[tup[0]][tup[1]+1] if tup[1] < len(board[0])-1 else 'na'


		if up == word[0]:
			dfs(board, word[1:], (tup[0]+1, tup[1]))
		elif down == word[0]:
			dfs(board, word[1:], (tup[0]-1, tup[1]))
		elif left == word[0]:
			dfs(board, word[1:], (tup[0], tup[1]-1))
		elif right == word[0]:
			dfs(board, word[1:], (tup[0], tup[1]+1))
		else:
			return False

		if word == '':
			return True
		else:
			return False

	for tup in init:
		if dfs(board, word, tup) == True:
			return True
		else: 
			print('BLNT')

	return False
	'''


board = [
	['A','B','C','E'],
	['S','F','C','S'],
	['A','D','E','E']]

'''
Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
'''

print(exist(board, 'ABCCED'))
print(exist(board, 'SEE'))
print(exist(board, 'ABCB'))