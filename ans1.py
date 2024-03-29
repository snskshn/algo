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

def late(n, p):
        result = 0
        for i in range(1, 2**n + 1):
                if '111' in bin(i):
                        lates = bin(i).count('1')
                        result += p**lates * (1 - p)**(n - lates)
        return 1 - result
def 나졸려생존():
        print(late(20, 1/2))
def 더졸려생존():
        print(late(20, 2/3))

# 1.5
class Pay(list):
        def pay(self, amount, money = 1, L=[], debug = False):
                if amount < 0:
                        return 0
                if amount == 0:
                        if debug:
                                print(L)
                        return 1
                result = 0
                for i in self:
                        if money > i:
                                continue
                        result += self.pay(amount - i, i, L + [i], debug)
                return result

import unittest
class TestPay(unittest.TestCase):
        def testPay(self):
                p = Pay([1,2,5])
                self.assertEqual(p.pay(10, debug=True), 10)
                p1 = Pay([1, 2, 5, 10, 20, 50])
                self.assertEqual(p1.pay(100), 4562)
                p2 = Pay([1, 2, 5, 10, 20, 50, 100])
                #self.assertEqual(p2.pay(300), 466800)

# 1.6
class IntegerPartition:
        memo = {}
        @staticmethod
        def count(n, m, L = []):
                if n == 0:
                        #print('+'.join(map(str, L)))
                        return 1
                if m == 0:
                        return 0
                if (n, m) in memo:
                        return memo[(n, m)]
                if n < m:
                        IntegerPartition.count(n, n, L)

                i = 0
                result = 0
                while n - m * i >= 0:
                        result += IntegerPartition.count(n - m * i, m - 1, L + [m] * i)
                        i += 1
                memo[(n, m)] = result
                        
                return memo[(n, m)]
        def count_seq(n, L=[]):
                if n == 0:
                        #print('+'.join(map(str, L)))
                        return 1
                if n < 0:
                        return 0
                
                result = 0
                for i in range(1, n + 1):
                        result += IntegerPartition.count_seq(n - i, L + [i])
                        
                return result
                
class TestIntegerPartition(unittest.TestCase):
        def testPartition(self):
                self.assertEqual(IntegerPartition.count(3, 3), 3)
                self.assertEqual(IntegerPartition.count(4, 4), 5)
                self.assertEqual(IntegerPartition.count(5, 5), 7)
                self.assertEqual(IntegerPartition.count(5, 2), 3)
                self.assertEqual(IntegerPartition.count(5, 3), 5)

# 1.7
def gray(n, L = ['0', '1']):
        if n == 1:
                return L
        new = ['0'+x for x in L]
        L.reverse()
        new += ['1'+x for x in L]
        L.reverse()
        return gray(n - 1, new)

# 1.a
def sumOfPower(n, k):
        result = 0
        for i in range(1, n + 1):
               result += i**k
        return result
def sumOfPower2(n, k):
        if n == 1:
                return 1
        return sumOfPower2(n - 1, k) + n**k

# 1.b
def pascal(n, k = 0):
        if n == k:
                return
        for i in range(k + 1):
                print(combination(k, i), end=' ')
        print()
        pascal(n, k + 1)

# 1.c
def allSum(n, m, L = []):
        if n == m == 0:
                print(L)
        for i in range(1, n + 1):
                allSum(n - i, m - 1, L + [i])

# 1.d: http://www.geeksforgeeks.org/archives/3968
inverse_count = 0
def merge(left, right):
        L = []
        while len(left) > 0 and len(right) > 0:
                if left[0] < right[0]:
                        L.append(left.pop(0))
                else:
                        global inverse_count
                        L.append(right.pop(0))
                        inverse_count += len(left)
        L.extend(left + right)
        return L

def mergeSort(L):
        if len(L) < 2:
                return L
        left = mergeSort(L[:len(L) // 2])
        right = mergeSort(L[len(L) // 2:])
        return merge(left, right)

class testMerge(unittest.TestCase):
        def testMerge(self):
                global inverse_count
                inverse_count = 0
                mergeSort([1, 3, 5, 4, 2])
                self.assertEqual(inverse_count, 4);
                inverse_count = 0
                mergeSort([4, 3, 1, 5, 2])
                self.assertEqual(inverse_count, 6);

# 1.e
def josephus(L):
        if len(L) == 1:
                return L[0]
        L.pop(1)
        return josephus(L[2:] + L[:2])
def last_person(n):
        L = list(range(1, n + 1))
        return josephus(L)
