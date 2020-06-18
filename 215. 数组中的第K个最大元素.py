# 在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

# Onlogn
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = sorted(nums, reverse = True)
        return nums[k-1]


# 堆排序 OnlogK
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 首先建立并调整堆
        # 只需要管建立的k个结点的堆有序 并且要从非叶子结点开始（节点序号k/2） 从小往上调整
        for i in range(k / 2, -1, -1):
            self.help(i, k, nums)

        # 处理后续结点 当结点大于堆顶（此时堆顶为当前最小的第k个元素）时，替换堆顶，并调整
        for i in range(k, len(nums)):
            if nums[i] > nums[0]:
                nums[0] = nums[i]
                self.help(0, k, nums)
        # 返回堆顶
        return nums[0]

    def help(self, i, k, nums):
        # 只需要管建立的k个结点的堆有序，判断现在调整的结点 它的子节点是否已经超过k个结点的树
        while i * 2 + 1 < k:
            # t的作用是找到第i个结点和其两个孩子之间 三个结点哪个最小
            t = i
            if nums[i * 2 + 1] < nums[i]:
                t = i * 2 + 1
            if i * 2 + 2 < k and nums[t] > nums[i * 2 + 2]:
                t = i * 2 + 2
            # 如果i是最小的 说明调整完毕 跳出
            if i == t:
                break
            # 交换 使父节点最小 形成最小堆
            else:
                nums[i], nums[t] = nums[t], nums[i]
                # 调整移动后的后续的结点 从上往下
                i = t