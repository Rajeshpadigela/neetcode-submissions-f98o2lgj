from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)              # count frequencies
        return [num for num, _ in freq.most_common(k)]