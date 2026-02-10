from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        tally: dict[int, int] = defaultdict(int)
        for num in nums:
            tally[num] += 1
        
        inverted_tally = defaultdict(list)
        for key, count in tally.items():
            inverted_tally[count].append(key)

        curr = len(nums)
        results: list[int] = []
        while len(results) < k:
            if curr in inverted_tally:
                results.extend(inverted_tally[curr])
            curr -= 1

        return results
