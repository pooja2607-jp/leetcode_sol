class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        seen=('a','e','i','o','u','A','E','I','O','U')
        i=0
        j=len(s)-1
        st=list(s)
        while i<j:
            if st[i] not in seen :
                i+=1
            elif st[j]  not in seen:
                j-=1
            else:
                 st[i],st[j]=st[j],st[i]
                 i+=1
                 j-=1
        return "".join(st)
            
            
