class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        return [i for i in nums if nums.count(i)==1][0]
        