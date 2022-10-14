class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = sum(nums[:3])
        
        for i in range(len(nums)):
            left, right = i+1, len(nums)-1
        
            while left < right:
                total = sum((nums[i], nums[left], nums[right]))
                if abs(total - target) < abs(result - target):
                    result = total
                elif total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    return result
                
        return result
    
    