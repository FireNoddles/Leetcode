# 请根据每日 气温 列表，重新生成一个列表。对应位置的输出为：要想观测到更高的气温，至少需要等待的天数。如果气温在这之后都不会升高，请在该位置用 0 来代替。
#
# 例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/daily-temperatures
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        stack = []
        ans = [0 for i in range(len(T))]
        for i in range(len(T)):
            if len(stack) == 0:
                stack.append([i,T[i]])
            else:
                while stack[-1][1] < T[i]:
                    ans[stack[-1][0]] = i-stack[-1][0]
                    stack.pop()
                    if len(stack) == 0:
                        break
                stack.append([i,T[i]])
        return ans

# import heapq
# s = input().split()
# arr = list(map(int, s))
# m, n, x = (arr[i] for i in range(3))
# # m, n, x  = arr[0], arr[1], arr[2]
# s = input().split()
# data = list(map(int, s))
# heap = []
# for i in data:
#     heapq.heappush(heap, i)
# while n>0:
#     target = heapq.heappop(heap)
#     heapq.heappush(heap, target+x)
#     n-=1
# print(heapq.heappop(heap))



s = input()
n = int(s)
s = input().split()
data = sorted(list(map(int, s)),reverse=True)
i = len(data)-1
while len(set(data))!=len(data) and i > 0:
    if data[i]==data[i-1]:
        while data[i]==data[i-1]:
            i-=1
        data[i+1]+=data[i+1]
        del data[i]
        i = len(data)-1
    else:
        i-=1
print(data)

