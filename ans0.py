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
