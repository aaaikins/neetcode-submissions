class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            else:
                left_char= s[l].lower()
                right_char = s[r].lower()

                if left_char != right_char:
                    return False
                else:
                    l += 1
                    r -= 1
        
        return True
            
        
        