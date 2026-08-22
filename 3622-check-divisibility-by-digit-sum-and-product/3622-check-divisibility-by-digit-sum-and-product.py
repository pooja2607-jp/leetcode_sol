class Solution:
    def checkDivisibility(self, n: int) -> bool:
        temp=n
        sum=0
        prod=1
        while n>0:
            rem=n%10
            sum=sum+rem
            prod=prod*rem
            n=n//10
       
        return temp%(sum+prod)==0
