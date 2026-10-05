class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen=set()
        while n!=1:
            if n in seen:
                return False
            seen.add(n)
            sum=0
            while(n>0):
                 rem=n%10
                 sum=sum+rem*rem
                 n=n//10
            n=sum
        return True