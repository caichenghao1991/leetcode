# 151. Reverse Words in a String
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.strip().split(' ')
        words.reverse()
        while "" in words:
            words.remove("")
        return ' '.join(words)
