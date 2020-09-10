# 一条包含字母 A-Z 的消息通过以下方式进行了编码：
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# 给定一个只包含数字的非空字符串，请计算解码方法的总数。
#
# 示例 1:
#
# 输入: "12"
# 输出: 2
# 解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
# 示例 2:
#
# 输入: "226"
# 输出: 3
# 解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/decode-ways
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
#
# # 递归超时
# class Solution(object):
#     def __init__(self):
#         self.ans = []
#     def numDecodings(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         arr= []
#         if s[0]=='0':
#             return 0
#         self.help(s,arr)
#         return len(self.ans)
#     def help(self,s,arr):
#         arr = arr[:]
#         if len(s)==0:
#             self.ans.append(arr)
#             return
#         if s[0]=='0':
#             return
#         elif len(s) == 1:
#             arr.append(int(s[0]))
#             self.ans.append(arr)
#             return
#         else:
#             arr.append(int(s[0]))
#             self.help(s[1:],arr)
#             if int(s[0])==1:
#                 del arr[-1]
#                 arr.append(int(s[0]+s[1]))
#                 self.help(s[2:],arr)
#             if int(s[0])==2 and int(s[1])<=6:
#                 del arr[-1]
#                 arr.append(int(s[0]+s[1]))
#                 self.help(s[2:],arr)


# 动态规划 每一项与前两项有关
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s[0]=='0':
            return 0
        i = 1
        cur = 1
        for _ in range(1,len(s)):
            temp = cur
            if s[_] == '0':
                if s[_-1]=='1' or s[_-1]=='2':
                    cur = i
                else:
                    return 0
            else:
                if s[_-1] == '1' or (s[_-1] == '2' and 0<=int(s[_])<=6):
                    cur = cur + i
            i = temp
        return cur
a = Solution()
a.numDecodings("12120")