import itertools
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return [list(j) for i in range(len(nums)+1) for j in itertools.combinations(nums, i)]