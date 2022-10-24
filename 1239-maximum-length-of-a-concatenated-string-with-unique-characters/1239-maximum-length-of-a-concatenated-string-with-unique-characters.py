class Solution:
    def maxLength(self, arr: List[str]) -> int:
        result = ['']
        max_length = 0
        
        for i in range(len(arr)):
            for j in range(len(result)):
                subset = arr[i] + result[j]  # 'un'
                if len(subset) == len(set(subset)):
                    result.append(subset)
                    max_length = max(max_length, len(subset)) # 2
                    
        return max_length