class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.helper(s) == self.helper(t)
        
        
    def helper(self, string):
        result = []
        
        for char in string:
            if char != '#':
                result.append(char)
            else:
                if result:
                    result.pop()
                
        return result