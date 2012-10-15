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

def fib(n):
        if n < 3:
                return 1
        return fib(n - 1) + fib(n - 2)

memo_fib = {}
def fib_memo(n):
        if n < 3:
                return 1
        if not n in memo_fib:
                memo_fib[n] = fib_memo(n - 1) + fib_memo(n - 2)
        return memo_fib[n]

def fib_iter(n):
        p, pp, result = 0, 1, 0
        
        for i in range(2, n + 2):
                result = pp + p
                pp = p
                p = result

        return result
