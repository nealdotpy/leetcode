'''
412. Fizz Buzz - Easy
https://leetcode.com/problems/fizz-buzz/
'''

def fizzBuzz(n: int):

	def naive(n):
		output_array = []
		for value in range(1,n+1):
			if not value % 15:
				output_array.append('FizzBuzz')
			elif not value % 5:
				output_array.append('Buzz')
			elif not value % 3:
				output_array.append('Fizz')
			else:
				output_array.append('{}'.format(value))
		return output_array
	
	def better(n):
		return ['Fizz' * (not value % 3) + 'Buzz' * (not value % 5) or str(value) \
				for value in range(1,n+1)]


	return better(n)


print(fizzBuzz(100))
print(fizzBuzz(10))
print(fizzBuzz(29))