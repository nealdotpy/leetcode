'''
127. Word Ladder - Medium
https://leetcode.com/problems/word-ladder/

Given two words (beginWord and endWord), and a dictionary's word list, 
find the length of shortest transformation sequence from beginWord 
to endWord, such that:
	1. Only one letter can be changed at a time.
	2. Each transformed word must exist in the word list.

Note:
	* Return 0 if there is no such transformation sequence.
	* All words have the same length.
	* All words contain only lowercase alphabetic characters.
	* You may assume no duplicates in the word list.
	* You may assume beginWord and endWord are non-empty and are not the same.


Example 1: 
	Input:
		beginWord = "hit",
		endWord = "cog",
		wordList = ["hot","dot","dog","lot","log","cog"]

	Output: 5

	Explanation: As one shortest transformation is 
				"hit" -> "hot" -> "dot" -> "dog" -> "cog", 
				return its length 5.
Example 2:
	Input:
		beginWord = "hit"
		endWord = "cog"
		wordList = ["hot","dot","dog","lot","log"]

	Output: 0

	Explanation: The endWord "cog" is not in wordList, 
					therefore no possible transformation.
'''
from queue import Queue
import collections

class Graph:
	def __init__(self):
		self.edges = {}
	
	def neighbors(self, id):
		return self.edges[id]

def ladderLength(begin: str, end: str, wl):
	'''Time Limit Exceeded
	if not (end in wl): return 0 # if end isn't in word list then not possible
	
	def make_graph(wl) -> Graph:
		#print(wl)
		def diff(r, s):
			return sum(r[i] != s[i] for i in range(len(s)))

		g = Graph()
		for i in range(len(wl)):
			edges = list(map(lambda x: diff(wl[i], x), wl))
			valid_edges = []
			for j in range(len(edges)):
				if edges[j] == 1:
					valid_edges.append(wl[j])
			#print('{}.edges: {}'.format(wl[i], valid_edges))
			g.edges[wl[i]] = valid_edges 

		return g

	graph = make_graph(wl+[begin])

	frontier = Queue()
	frontier.put(begin)
	came_from = {}
	came_from[begin] = None

	while not frontier.empty():
		current = frontier.get()
		if current == end: break
		for next in graph.neighbors(current):
			if next not in came_from:
				frontier.put(next)
				came_from[next] = current

	jumps = 0
	curr = end
	while curr in came_from and [curr] != None:
		if came_from[curr] == begin: 
			jumps += 2
			break
		curr = came_from[curr]
		jumps += 1

	#print(came_from[curr])
	return jumps
	'''
	# Space Efficient, Somewhat 'Slow':
	wl = set(wl)
	queue = collections.deque([(begin, 1)])
	while queue:
		print(queue)
		word, length = queue.popleft()
		print('word: {} [{}]'.format(word, length))
		if word == end:
			return length
		for i in range(len(word)):
			for c in 'abcdefghijklmnopqrstuvwxyz':
				next_word = word[:i] + c + word[i+1:]
				if next_word in wl:
					wl.remove(next_word)
					queue.append((next_word, length + 1))
	return 0


print(ladderLength('hit', 'cog', ["hot","dot","dog","lot","log","cog"]))
print(ladderLength('hit', 'cog', ["hot","dot","dog","lot","log"]))