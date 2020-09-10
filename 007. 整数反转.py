# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。123->321
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ls = list(str(x))
        if len(ls)==1:
            return x
        flag = 0
        if ls[0] == '-':
            del ls[0]
            flag = 1
        i = 0
        j = len(ls) - 1
        while i<j:
            ls[i],ls[j] = ls[j],ls[i]
            i+=1
            j-=1
        result = 0
        for _ in range(len(ls)):
            result += (int(ls[_]) * (10**(len(ls) - _ -1 )))
        if flag:
            result = -result
        if -2**31 <= result <= 2**31 -1:
            return result
        return 0
a = Solution()
print(13 % 10)

-11 % 10