class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tally = defaultdict(int)
        for num in nums:
            tally[num] += 1
        
        inverted_tally = defaultdict(list)
        for key, count in tally.items():
            inverted_tally[count].append(key)

        curr = len(nums)
        results = []
        while len(results) < k:
            if curr in inverted_tally:
                results.extend(inverted_tally[curr])
            curr -= 1

        return results
