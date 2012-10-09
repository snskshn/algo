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
	memo = [[0]*n for _ in [0]*r]
	if r == 0 or n == r:
		return 1
	return combination(n - 1, r - 1) + combination(n - 1, r)
