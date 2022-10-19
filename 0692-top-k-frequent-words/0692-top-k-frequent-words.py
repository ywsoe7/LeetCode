class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dictionary = defaultdict(int)
        result = []
        for word in words:
            dictionary[word] += 1
            sorted_dict = sorted(dictionary.items(), key = lambda x: (-x[1], x[0]))
            
        for i in sorted_dict[:k]:
            result.append(i[0])
            
        return result