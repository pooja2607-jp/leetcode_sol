class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words=[]
        words=s.split()
        words.reverse()
        s=" ".join(words)
        return s