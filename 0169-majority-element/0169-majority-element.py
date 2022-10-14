class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        count = 0
        majority = 0
        
        for num in nums:
            if count == 0:
                majority = num
                count += 1
            elif majority == num:
                count += 1
            else:
                count -= 1
                
        return majority 
        
        # for num in nums:
        #     count = nums.count(num)
        #     if count >= len(nums) // 2:
        #         return num