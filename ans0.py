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
