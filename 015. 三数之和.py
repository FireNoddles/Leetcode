# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组。
#
#  
#
# 示例：
#
# 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
#
# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/3sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 变成两个数求和 tips（因为3数求和需要On^2 所以用了排序Onlogn 再双指针 而没有哈希 如果用哈希相当于时间要On2 空间要On）关键点在去除重复 开始的时候先排序
# 如果一个数等于前面一个数 则计算时直接跳过 因为之前已经算过了 避免重复
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums = sorted(nums)
        if len(nums) < 1 or nums[0]>0:# 如果最小的数都大于0 则肯定无法完成目标
            return res
        for _ in range(len(nums)):
           if _==0 or nums[_]!=nums[_-1]: # 如果一个数等于前面一个数 则计算时直接跳过 因为之前已经算过了 避免重复
               c = self.help(-nums[_],nums[_+1:])
               if c:
                   res.extend(c)
        return res
    def help(self,target,arr):
        res = []
        i = 0
        j = len(arr)-1
        while i<j:
            if arr[i] + arr[j] < target:
                i+=1
            elif arr[i] + arr[j] > target:
                j-=1
            else:
                if [-target, arr[i],arr[j]] not in res:
                    res.append([-target, arr[i],arr[j]])
                j-=1
                i+=1
        if len(res) == 0:
            return False
        return res

a = Solution()
print(a.threeSum(
[-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]))