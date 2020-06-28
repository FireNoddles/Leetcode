# 写一个程序，输出从 1 到 n 数字的字符串表示。
#
# 1. 如果 n 是3的倍数，输出“Fizz”；
#
# 2. 如果 n 是5的倍数，输出“Buzz”；
#
# 3.如果 n 同时是3和5的倍数，输出 “FizzBuzz”。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/fizz-buzz
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 去除法
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = [str(i) for i in range(1,n+1)]
        i = 3
        while i <=n :
            ans[i-1] = 'Fizz'
            i = i + 3
        i = 5
        while i <=n:
            ans[i-1] = 'Buzz'
            i = i + 5
        i = 15
        while i <=n:
            ans[i-1] = 'FizzBuzz'
            i = i + 15
        return ans