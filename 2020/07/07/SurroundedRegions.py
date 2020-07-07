'''
130. Surrounded Regions - Medium
https://leetcode.com/problems/surrounded-regions/

Given a 2D board containing 'X' and 'O' (the letter O), 
capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's 
in that surrounded region.

X X X X 
X O O X
X X O X
X O X X

-> run ->

X X X X
X X X X
X X X X
X O X X

Explanation:

Surrounded regions shouldn’t be on the border, which means 
that any 'O' on the border of the board are not flipped to 'X'. 
Any 'O' that is not on the border and it is not connected to 
an 'O' on the border will be flipped to 'X'. Two cells are 
connected if they are adjacent cells connected horizontally 
or vertically.

'''
from random import random
from collections import deque

class Board:
	def __init__(self, rows, cols):
		board = []
		for i in range(cols):
			row = []
			for j in range(rows):
				row.append('X' if random()<=0.67 else 'O')
			board.append(row)
		self.board = board

	def __init__(self, board):
		self.board = board

	def print(self):
		for row in self.board:
			print(row)
		print()

#Board(4,4).print()

test = [["X","X","X","X"],
		 ["X","O","O","X"],
		 ["X","X","O","X"],
		 ["X","O","X","X"]]

board = Board(test)

'''
format -> [(i,j)->[(i-1,j),(i+1,j),(i,j-1),(i,j+1)],
O1: [(1,1)->[(0,1),(1,0),(2,1),(1,2)],
	 (1,2)->[(0,2),(2,2),(1,1),(1,3)],
	 (2,2)->]
O2: [(3,1)]
'''

def solve(board) -> None:
	# for/for approach: O(R*C), R=rows, C=cols
	board = board.board

	if not any(board): return

	def neighbors(tup):
		i, j = tup
		return (i-1,j),(i+1,j),(i,j-1),(i,j+1)

	rows, cols = len(board), len(board[0])
	border = [tup for k in range(max(rows,cols)) for tup in ((0, k), 
															 (rows-1, k), 
															 (k, 0), 
															 (k, cols-1))]
	while border:
		i, j = border.pop()
		if 0 <= i < rows and 0 <= j < cols and board[i][j]=='O':
			board[i][j] = 'S'
			border += neighbors((i,j))

	board[:] = [['XO'[c == 'S'] for c in row] for row in board]

	'''
	os = deque([])
	for i in range(rows):
		for j in range(cols):
			if board[i][j] == 'O':
				os.append((i,j))
	print('o-locations:\n{}'.format(os))
	check = deque({})
	while os:
		for t in neighbors(os.popleft()): check.appendleft(t)
		#check.appendleft(t for t in neighbors(os.popleft()))
		print(check)
		#while check:
		node = check.popleft()
		#print(check)
		i, j = node
		if i >= rows or i < 0: continue
		elif j >= cols or j < 0: continue

		if node in os:
			for t in neighbors(node): check.appendleft(t)
			print('o-locations:\n{}'.format(os),end="\n\n")
			#print(os)
	print(check)
	'''

solve(board)
board.print()