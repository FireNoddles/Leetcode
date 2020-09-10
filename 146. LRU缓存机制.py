#运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。

# 获取数据 get(key) - 如果关键字 (key) 存在于缓存中，则获取关键字的值（总是正数），否则返回 -1。
# 写入数据 put(key, value) - 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字/值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/lru-cache
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


import collections
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.dic = collections.OrderedDict()


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.dic:
            return -1
        else:
            temp  = self.dic[key]
            del self.dic[key]
            self.dic[key] = temp
            return temp

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.dic:
            del self.dic[key]
        if len(self.dic)==self.capacity:
            keys = self.dic.keys()
            del self.dic[keys[0]]
            self.dic[key] = value
        else:
            self.dic[key] = value