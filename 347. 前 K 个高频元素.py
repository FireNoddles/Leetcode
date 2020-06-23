class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic = {}
        for _ in nums:
            if _ not in dic:
                dic[_] = 1
            else:
                dic[_]+=1
        if k>len(dic):
            return False
        keys = list(dic.keys())

        for _ in range(k//2,-1,-1):
            self.help(_,keys,k,dic)
        for _ in range(k, len(keys)):
            if dic[keys[_]] >  dic[keys[0]]:
                keys[0] = keys[_]
                self.help(0,keys,k,dic)
        return keys[:k]
    def help(self, index, arr, k, dic):
        while index * 2 + 1 < k:
            t = index
            if dic[arr[index * 2 + 1]] < dic[arr[t]]:
                t = index * 2 + 1
            if index * 2 + 2 < k and dic[arr[index * 2 + 2]] < dic[arr[t]]:
                t = index * 2 + 2
            if t != index:
                arr[t], arr[index] = arr[index], arr[t]
                index = t
            else:
                break