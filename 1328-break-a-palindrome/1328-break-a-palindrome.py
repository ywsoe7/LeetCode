class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) < 2:
            return ''
        for i in range(int(len(palindrome)//2)):
            if palindrome[i] != 'a':
                palindrome =  palindrome[:i] + 'a' + palindrome[i+1:]
                return palindrome
        return palindrome[:-1] + 'b'