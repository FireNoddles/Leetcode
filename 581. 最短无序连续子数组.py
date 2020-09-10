# 给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。
#
# 你找到的子数组应是最短的，请输出它的长度。
#
# 示例 1:
#
# 输入: [2, 6, 4, 8, 10, 9, 15]
# 输出: 5
# 解释: 你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# 寻找右边界：
# 从前往后遍历的过程中，用max记录遍历过的最大值，如果max大于当前的nums[i]，说明nums[i]的位置不正确，属于需要排序的数组，因此将右边界更新为i，然后更新max；这样最终可以找到需要排序的数组的右边界，右边界之后的元素都大于max；
# 寻找左边界：
# 从后往前遍历的过程中，用min记录遍历过的最小值，如果min小于当前的nums[j]，说明nums[j]的位置不正确，应该属于需要排序的数组，因此将左边界更新为j，然后更新min；这样最终可以找到需要排序的数组的左边界，左边界之前的元素都小于min；
#
# 作者：zackqf
# 链接：https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray/solution/shi-jian-chao-guo-100de-javajie-fa-by-zackqf/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
# On
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = nums[0]
        l = 0
        for i in range(len(nums)):
            if nums[i] < m:
                l = i
            m = max(m, nums[i])
        m_in = nums[-1]
        r = len(nums) - 1
        for j in range(len(nums) - 1, -1, -1):
            if nums[j] > m_in:
                r = j
            m_in = min(m_in, nums[j])
        return 0 if l <= r else l - r + 1
from multiprocessing import Process, Pipe

def help(lock):
    while 1:
        a = lock.recv()
        print('help2'+str(a))
def help2(lock):
    for _ in range(10):
        lock.send('help2'+str(_))

if __name__ == '__main__':
    # l1,l2 = Pipe()
    # l1.send('111')
    #
    # p1 = Process(target=help,args = (l2,))
    # p2 = Process(target=help2, args = (l1,))
    # p1.start()
    # p2.start()
    def quick_sort(arr, left, right):
        if left>=right:
            return
        mid = arr[left]
        l = left
        r = right

        while l<r:
            # 小于等于很重要
            while l<r and arr[r] >= mid:
                r-=1
            arr[l] = arr[r]
            while l<r and arr[l] <= mid:
                l+=1
            arr[r] = arr[l]
        arr[l] = mid
        quick_sort(arr,left,l-1)
        quick_sort(arr,l+1,right)

    a = [5,4,3,5,7,9,10,21]
    quick_sort(a,0,len(a)-1)
    print(a)


