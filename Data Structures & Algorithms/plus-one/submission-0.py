class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        digits.reverse()
        digits.append(0)
        digits[0] += 1
        i = 0

        while i < len(digits):
            if digits[i] >= 10:
                temp = digits[i]
                digits[i] = temp % 10
                digits[i + 1] += (temp // 10)
            i += 1
  
        if digits[-1] == 0:
            digits.pop()
            
        digits.reverse()
        
        return digits 