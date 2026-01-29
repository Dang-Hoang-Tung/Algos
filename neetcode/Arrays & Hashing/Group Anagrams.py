class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = defaultdict(list)
        for string in strs:
            signature = [0] * 26 # alphabet length
            for char in string:
                position = ord(char) - ord('a')
                signature[position] += 1
            my_dict[tuple(signature)].append(string)
        return list(my_dict.values())
