# 给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
#
# 此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
#
# 注意:
# 不能使用代码库中的排序函数来解决这道题。
#
# 示例:
#
# 输入: [2,0,2,1,1,0]
# 输出: [0,0,1,1,2,2]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/sort-colors
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
#计数排序
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        arr = [0,0,0]
        for _ in nums:
            if _ == 0:
                arr[0]+=1
            elif _==1:
                arr[1]+=1
            else:
                arr[2]+=1
        i = 0
        for _ in range(3):
            for __ in range(arr[_]):
                print(i)
                nums[i] = _
                i+=1
# 三指针 一次遍历

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i =0
        j = len(nums) -1
        m = 0
        while m <= j:
            if nums[m] == 0:
                nums[m],nums[i] = nums[i],nums[m]
                i+=1
                m+=1
            elif nums[m] ==1:
                m+=1
            else:
                nums[m],nums[j] = nums[j],nums[m]
                j-=1
Solution().sortColors(
[2,0,2,1,1,0])