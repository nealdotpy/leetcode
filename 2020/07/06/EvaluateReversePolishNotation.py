'''
150. Evaluate Reverse Polish Notation - Medium
https://leetcode.com/problems/evaluate-reverse-polish-notation/

Evaluate the value of an arithmetic expression in 
Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an 
integer or another expression.

Example 1:
	Input: ["2", "1", "+", "3", "*"]
	Output: 9
	Explanation: ((2 + 1) * 3) = 9

Example 2:
	Input: ["4", "13", "5", "/", "+"]
	Output: 6
	Explanation: (4 + (13 / 5)) = 6

Example 3:
	Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
	Output: 22
	Explanation: 
	  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
	= ((10 * (6 / (12 * -11))) + 17) + 5
	= ((10 * (6 / -132)) + 17) + 5
	= ((10 * 0) + 17) + 5
	= (0 + 17) + 5
	= 17 + 5
	= 22
'''

def evalRPN(tokens) -> int:
	''' --> passed 19/20 test cases with time being factor on last one
	def calc(x, y, o):
		print('reducing {}{}{}'.format(x,o,y))
		x = int(x); y = int(y)
		if o == '+':
			return x+y
		elif o == '-':
			return x-y
		elif o == '*':
			return x*y
		else:
			return round(x/y,1)

	res = 0
	ops = ['+', '-', '*', '/']
	new = []
	i = 0
	while i+2 < len(tokens):
		#print('i = {}'.format(i))
		if (not (tokens[i] in ops or tokens[i+1] in ops)) and tokens[i+2] in ops:
			#print(tokens[i], tokens[i+1], tokens[i+2])
			res = calc(tokens[i], tokens[i+1], tokens[i+2])
			tokens = tokens[:i] + [res] + tokens[i+3:]
			#print('tokens[{}] = {}'.format(i, tokens[i]))
			print(tokens)
			i = 0
			continue
		i += 1

	return int(tokens[0])
	'''
	stack = []
	for t in tokens:
		if t not in ["+", "-", "*", "/"]:
			stack.append(int(t))
		else:
			r, l = stack.pop(), stack.pop()
			if t == "+":
				stack.append(l+r)
			elif t == "-":
				stack.append(l-r)
			elif t == "*":
				stack.append(l*r)
			else:
				stack.append(int(l/r))
	return stack.pop()



print(evalRPN(["2", "1", "+", "3", "*"]))
print(evalRPN(["4", "13", "5", "/", "+"]))
print(evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))