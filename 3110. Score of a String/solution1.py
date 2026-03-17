class Solution:
    def scoreOfString(self, s: str) -> int:
        str_length = len(s)
        absolutes = []
        score = 0
        for char in range(str_length):
            if char+1<str_length:
                term1 = ord(s[char])
                term2 = ord(s[char+1])
                diff = term1-term2
                absolute = abs(diff)
                absolutes.append(absolute)
        for ab in absolutes:
            score = score + ab
        return score