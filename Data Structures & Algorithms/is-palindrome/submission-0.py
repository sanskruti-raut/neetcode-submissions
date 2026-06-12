class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = s.lower()
        # s = s.replace(" ", "")
        s = ''.join(char.lower() for char in s if char.isalnum())
        reverse = s[::-1]
        if s == reverse:
            return True
        else:
            return False    

            
        