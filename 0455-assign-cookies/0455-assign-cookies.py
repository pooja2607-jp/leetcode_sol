class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        c=0
        g.sort()
        s.sort()
        i=0
        for j in range(len(s)):
            if i<len(g) and s[j]>=g[i]:
                c+=1
                i+=1
        return c