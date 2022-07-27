class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maximum=0
        for i in range(0,len(nums)-1):
            for j in range(i,len(nums)):
                if i!=j:
                    if (nums[i]-1)*(nums[j]-1)>=maximum:
                        maximum=(nums[i]-1)*(nums[j]-1)
        return maximum