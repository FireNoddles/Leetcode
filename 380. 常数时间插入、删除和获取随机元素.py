# 设计一个支持在平均 时间复杂度 O(1) 下，执行以下操作的数据结构。
#
# insert(val)：当元素 val 不存在时，向集合中插入该项。
# remove(val)：元素 val 存在时，从集合中移除该项。
# getRandom：随机返回现有集合中的一项。每个元素应该有相同的概率被返回。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/insert-delete-getrandom-o1
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

import random
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []


    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.arr:
            self.arr.append(val)
            return True
        else:
            return False


    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.arr:
            self.arr.remove(val)
            return True
        else:
            return False


    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        index = random.sample(range(0,len(self.arr)),1)
        return self.arr[index[0]]



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()