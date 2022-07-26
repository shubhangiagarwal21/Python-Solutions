class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        lst=[]
        for i in nums:
            count=0
            for j in range(0,len(nums)):
                if i>nums[j]:
                    count+=1
            lst.append(count)
        return lst