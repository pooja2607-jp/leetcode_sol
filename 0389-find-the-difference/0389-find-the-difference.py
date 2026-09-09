class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for i in range(len(t)):
            if t[i] not in s:
                return t[i]
            s=s.replace(t[i],"",1)
        return 0