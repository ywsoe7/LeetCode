class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
     
        hash_map = {0:0}
        sub_total = 0
        
        for i in range(len(nums)):
            sub_total += nums[i]
            
            remainder_key = sub_total % k
            if remainder_key not in hash_map:
                hash_map[remainder_key] = i + 1
            elif hash_map[remainder_key] < i:
                return True
        return False
        
        