class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        my_dict = defaultdict(int)
        i = 0
        while i < len(s):
            my_dict[s[i]] += 1
            my_dict[t[i]] -= 1
            i += 1

        return any(my_dict.values()) == False
