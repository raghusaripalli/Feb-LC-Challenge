class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        i = 0
        l = len(s)
        c = 0
        while i < l:
            c ^= ord(s[i]) ^ ord(t[i])
            i += 1
        return chr(c ^ ord(t[-1]))
