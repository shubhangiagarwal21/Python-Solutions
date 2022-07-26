class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        lst=[]
        for i in range(0,len(nums)):
            sum1=0
            for j in range(0,i+1):
                sum1+=nums[j]
            lst.append(sum1)
        return lst