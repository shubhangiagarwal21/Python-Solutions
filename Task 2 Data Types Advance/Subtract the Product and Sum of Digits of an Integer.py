class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod=1
        sum1=0
        while(n>0):
            prod*=(n%10)
            sum1+=(n%10)
            n=n//10
        return (prod-sum1)