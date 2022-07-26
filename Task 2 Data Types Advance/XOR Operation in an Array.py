from functools import reduce
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        lst = [start+2*i for i in range(n)]
        return reduce(lambda i, j: i ^ j, lst)