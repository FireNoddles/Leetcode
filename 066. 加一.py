class Solution(object):
    @classmethod
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = -1
        while 1:
            if i == -len(digits)-1:
                digits.insert(0,1)
                return digits
            if digits[i] < 9:
                digits[i]+=1
                return digits
            else:
                digits[i] = 0
                i-=1
print(Solution.plusOne([9,9,9]))