# 编写一个算法来判断一个数 n 是不是快乐数。
#
# 「快乐数」定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。如果 可以变为  1，那么这个数就是快乐数。
#
# 如果 n 是快乐数就返回 True ；不是，则返回 False 。
#
#  
#
# 示例：
#
# 输入：19
# 输出：true
# 解释：
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/happy-number
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 使用集合记录 （容易超时 要严格控制变量）
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        arr = set()
        while n != 1 and n not in arr:
            arr.add(n)
            temp = 0
            while n > 0:
                temp += ((n % 10) ** 2)
                n = n // 10
            n = temp

        return n == 1

# 判断循环用快慢指针
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        slow = n
        fast = n
        while 1:
            slow  = self.help(slow)
            # 走两步
            fast = self.help(self.help(fast))
            if slow == fast:
                return slow == 1

    def help(self, n):
        temp = 0
        while n > 0 :
            temp += ((n % 10)**2)
            n = n // 10
        return temp