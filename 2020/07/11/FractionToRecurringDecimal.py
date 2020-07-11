'''
166. Fraction to Recurring Decimal - Medium
https://leetcode.com/problems/fraction-to-recurring-decimal/

Given two integers representing the numerator and denominator of a fraction, 
return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

Example 1:
	Input: numerator = 1, denominator = 2
	Output: "0.5"

Example 2:
	Input: numerator = 2, denominator = 1
	Output: "2"

Example 3:
	Input: numerator = 2, denominator = 3
	Output: "0.(6)"
'''

def ftd(numer: int, denom: int) -> str:
	'''
	NUMER, DENOM = numer, denom
	whole = numer // denom # e.g. 61/12 -> whole=5
	r = numer % denom
	#numer -= whole*denom # 61-60 = 1 | 60/12 + 1/12 = 61/12 = 5.08(33)
	L = len(str(denom)) # determines period of repetend; 1/12 -> 0.[08](33)

	quo = [whole] #+ [0 for x in range(L*3)]
	div = [numer] #+ [0 for x in range(L*3)]
	#print('{}{}\n{}{} r={}'.format(' '*L, quo, denom, div, r))

	print('{} / {}'.format(NUMER, DENOM), end=' ')
	if not r: # clean decimals (53.0, 3.0, 1.0, etc)
		return str(quo[0])

	numer = r
	LONG, i = False, 0 # non terminating track
	CAP = (denom-1) * 2
	#for i in range(1, len(quo), 1):
	while numer != 0:
		# if i >= CAP:
		# 	LONG = True
		# 	break
		if len(quo)>L*2 and quo[len(quo)-L:] == quo[len(quo)-L*2:len(quo)-L]:
			# repeating case
			break
		numer *= 10 # dropping the 0
		if numer < denom: # e.g. 1/12 -> True, since 1 % 12 == 12
			quo.append(0)
			continue
		#print(quo[i])
		quo.append(numer // denom)
		#print(quo[i])
		numer %= denom
		i += 1
		#print(quo)


	if numer == 0: # repeating, but with 0s so a "perfect" solution
		return '{}.{}'.format(quo[0],''.join(map(str,quo[1:])))
	
	#print('{}{}\n{}{} r={}'.format(' '*L, quo, denom, div, numer))

	end = quo[len(quo)-L:] 
	mid = quo[len(quo)-L*2:len(quo)-L]
	start = quo[1:1+L]
	res = '{}.'.format(whole)

	# if LONG:
	# 	
	#print('{}->e,m,s:{},{},{}'.format(quo, end, mid, start))


	if end == mid == start: # 0.[6][6][6]
		return res + '({})'.format(''.join(map(str, end)))
	elif end == mid: # 0.[08][33][33]
		for i in quo[1:L+1]:
			res += str(i)
		return res + '({})'.format(''.join(map(str, end)))

	return res + '({})'.format(''.join(map(str, quo[1:denom])))
	#return res
	'''
	n, remainder = divmod(abs(numer), abs(denom))
	sign = '-' if numer*denom < 0 else ''
	result = [sign+str(n), '.']
	stack = []
	while remainder not in stack:
		stack.append(remainder)
		n, remainder = divmod(remainder*10, abs(denom))
		result.append(str(n))

	idx = stack.index(remainder)
	result.insert(idx+2, '(')
	result.append(')')
	return ''.join(result).replace('(0)', '').rstrip('.')



print('= {}'.format(ftd(1,2))) # "0.5"
print('= {}'.format(ftd(2,1))) # "2"
print('= {}'.format(ftd(2,3))) # "0.(6)"
# print('ans={}'.format(ftd(100,20))) # "5"
print('= {}'.format(ftd(61,12))) # "0.08(33)"
print('= {}'.format(ftd(55,1111))) # "0.(0495)"
# print('ans={}'.format(ftd(0,1))) # "0"
# print('ans={}'.format(ftd(1,1))) # "1"
# print('ans={}'.format(ftd(1,17))) # "1"
# print('ans={}'.format(ftd(1,31))) # "1"
print('= {}'.format(ftd(1,81))) # "1"
#print('lalalallalalalal')
#print('ans={}'.format(ftd(601,23031))) # "?"