# 0.1: max & min
def min(x, y):
	return x if x < y else y

def max(x, y):
	return x if x > y else y

def max3(x, y, z):
	return max(x, y) if max(x, y) > z else z

def max_arr(a):
	max = 0
	for i in a:
		if i > max:
			max = i
	return max

def max_arr2(a):
	if len(a) == 1:
		return a.pop()
	else:
		return max(a.pop(), max_arr2(a))

# 0.2: swap
def swap(x, y):
	return y, x

def swap_arr(L, i, j):
	L[i], L[j] = L[j], L[i]

# 0.3: rotate array
def right_rotate(L, s, t, k = 1):
	from collections import deque
	d = deque(L[s:t+1])
	d.rotate(k)
	L[s:t+1] = list(d)

def left_rotate(L, s, t, k = 1):
	right_rotate(L, s, t, -k)

# 0.4: bank queue
class Queue(list):
	capacity = 8

	def enqueue(self, item):
		if len(self) >= Queue.capacity:
			raise AttributeError
		self.append(item)

	def dequeue(self):
		return self.pop(0)

class Stack(list):
	push = list.append

# 0.a
def print_arr(L):
	for i in L:
		print(i)

# 0.b
def all_is(L, k):
	return L.count(k) == len(L)

# 0.c
def binary_count(num):
	return list(bin(num)).count('1')

# 0.e
class StackQueue:
	def __init__(self):
		self.inStack = Stack()
		self.outStack = Stack()
	
	def enqueue(self, item):
		self.inStack.push(item)
	
	def dequeue(self):
		if len(self.outStack) == 0:
			while len(self.inStack) != 0:
				self.outStack.push(self.inStack.pop())
		return self.outStack.pop()

# 0.f: 220

# 0.g
def dec2bin(num):
	return bin(num)

# 0.h
def maxsum(L, p):
	if not 0 <= p < len(L):
		raise IndexError

	maxI = maxJ = p
	maxValue = 0
	for i in range(0, p):
		if sum(L[i:p]) > maxValue:
			print("sum: %d" % sum(L[i:p]))
			maxI = i
			maxValue = sum(L[i:p])
	maxValue = 0
	for j in range(p, len(L) - 1):
		if sum(L[p:j]) > maxValue:
			maxJ = j - 1
			maxValue = sum(L[p:j])
	return maxI, maxJ
