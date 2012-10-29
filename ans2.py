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
