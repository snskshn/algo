# 1.1
def fact_iter(n):
	result = 1
	for i in range(1, n + 1):
		result *= i
	return result

def fact(n):
	if n == 1:
		return 1
	return n * fact(n - 1)

# 1.2
def print_files(path = '/'):
	import os
	for dirname, dirnames, filenames in os.walk(path):
		for subdirname in dirnames:
			print(os.path.join(dirname, subdirname))
		for filename in filenames:
			print(os.path.join(dirname, filename))

# 1.3
def combination(n, r):
	if r == 0 or n == r:
		return 1
	return combination(n - 1, r - 1) + combination(n - 1, r)

memo = {}
def combination_fast(n, r):
        if r == 0 or n == r:
                return 1
        if not (n, r) in memo:
                memo[(n, r)] = combination_fast(n - 1, r - 1) + combination_fast(n - 1, r)
        return memo[(n, r)]
        
# 1.4
def valid_binary(n):
        if n == 1:
                return 1
        return int(not bin(n).count('00')) + valid_binary(n - 1)

def steps(n):
        if n < 2:
                return 1
        return steps(n - 1) + steps(n - 2)
