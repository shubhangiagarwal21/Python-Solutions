class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        return len([(i,j) for i in range(0,len(nums)) for j in range(i+1,len(nums)) if nums[i]==nums[j]])
                  