class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_count = {}
        t_count = {}

        for i in range(len(s)):
            if s[i] not in s_count:
                s_count[s[i]] = 1
            else:
                s_count[s[i]] += 1
            if t[i] not in t_count:
                t_count[t[i]] = 1
            else:
                t_count[t[i]] += 1

        for elem in s_count:
            if elem not in t_count or elem not in s_count or t_count[elem] != s_count[elem]:
                return False

        return True
        