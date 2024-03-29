import unittest

# 2.2
이상해씨마을 = [
    [1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1]]
궁금해씨마을 = [
    [1, 1, 1, 1, 1],
    [1, 1, 0, 0, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 1, 1, 1]]

def makeVillage(n, m):
    return [[1]*n for _ in [0]*m]

def findPath(L, i, j):
    if i < 0 or j < 0:
        return 0
    if i == j == 0:
        return 1
    if L[i][j] == 0:
        return 0
    return findPath(L, i - 1, j) + findPath(L, i, j - 1)

def findPathDynamic(L):
    from copy import deepcopy
    return _findPathDynamic(deepcopy(L))
def _findPathDynamic(L, i = 1, j = 1):
    if L[i][j] != 0:
        L[i][j] = L[i-1][j] + L[i][j-1]
    if i == j == len(L) - 1:
        return L[i][j]
    if j >= len(L) - 1:
        return _findPathDynamic(L, i + 1, 1)
    else:
        return _findPathDynamic(L, i, j + 1)
    
class testFindPath(unittest.TestCase):
    def testFindPath(self):
        self.assertEqual(findPath(이상해씨마을, 4, 4), 53)
        self.assertEqual(findPath(궁금해씨마을, 4, 4), 11)
        self.assertEqual(findPathDynamic(이상해씨마을), 53)
        self.assertEqual(findPathDynamic(궁금해씨마을), 11)
        self.assertEqual(findPathDynamic(makeVillage(30, 30)),
                         30067266499541040)

# 2.3
즐거워씨마을 = [
    [1, 2, 2, 1, 5],
    [1, 4, 4, 3, 1],
    [2, 1, 1, 1, 2],
    [1, 3, 5, 1, 1],
    [1, 5, 1, 2, 2]]
def joy(L, i = None, j = None):
    if i == j == None:
        i = len(L) - 1
        j = len(L[0]) - 1
    if i == j == 0:
        return L[0][0]
    if i < 0 or j < 0:
        return 0
    return max(joy(L, i - 1, j), joy(L, i, j - 1)) + L[i][j]

def joyDynamic(L):
    from copy import deepcopy
    return _joyDynamic(deepcopy(L))
def _joyDynamic(L):
    if len(L) != len(L[0]):
        raise IndexError
    for i in range(1, len(L)):
        L[0][i] += L[0][i-1]
        L[i][0] += L[i-1][0]
    for i in range(1, len(L)):
        for j in range(1, len(L[0])):
            if L[i][j] == 0:
                continue
            L[i][j] += max(L[i-1][j], L[i][j-1])

    # print path
    i = j = len(L) - 1
    result = []
    while not i == j == 0:
        result.append((i, j))
        if i == 0:
            j -= 1
        elif j == 0:
            i -= 1
        elif L[i-1][j] > L[i][j-1]:
            i -= 1
        else:
            j -= 1
    result.reverse()
    print(result)
    
    return L.pop().pop()

# 2.4
def subset_sum(L, n, result = []):
    if n == 0:
        #print(result, sum(result))
        return 1
    if n < 0 or len(L) == 0:
        return 0
    result2 = result[:]
    result2.append(L[0])
    return max(subset_sum(L[1:], n, result),
               subset_sum(L[1:], n - L[0], result2))

class TestSubsetSum(unittest.TestCase):
    def testSubsetSum(self):    
        self.L1 = [6, 9, 13, 14, 20, 21, 22, 30, 49, 55]
        self.L2 = list(range(10, 110, 10))
        self.L3 = [2, 4, 6, 9, 12, 14, 15]

        self.assertEqual(subset_sum(self.L1, 100), 1)
        self.assertEqual(subset_sum(self.L1, 110), 1)
        self.assertEqual(subset_sum(self.L1, 90), 1)
        self.assertEqual(subset_sum(self.L2, 101), 0)
        self.assertEqual(subset_sum(self.L3, 32), 1)
