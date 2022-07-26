class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        lst=[]
        lst1=[nums[i] for i in range(0,len(nums)//2)]
        lst2=[nums[i] for i in range(len(nums)//2,len(nums))]
        for i,j in zip(lst1,lst2):
            lst.append(i)
            lst.append(j)
        return lst