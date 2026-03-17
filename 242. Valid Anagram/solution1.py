class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = sorted(s)
        sorted_s_str = "".join(sorted_s)

        sorted_t = sorted(t)
        sorted_t_str = "".join(sorted_t)

        if sorted_s_str == sorted_t_str:
            return True
            
        return False