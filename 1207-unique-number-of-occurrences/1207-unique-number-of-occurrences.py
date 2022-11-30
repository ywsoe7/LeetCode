class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count_nums = {}
        for num in arr:
            if num not in count_nums:
                count_nums[num] = 1
            else:
                count_nums[num] += 1
                
        if len(set(count_nums.values())) != len(set(arr)):
            return False
        
        return True