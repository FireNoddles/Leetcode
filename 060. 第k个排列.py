class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        dic = {}
        temp = 1
        for _ in range(n):
            temp*=_+1
            dic[_+1] = temp
        arr = [i+1 for i in range(n)]
        s = ''
        k = k-1
        while n>1:
            index = k//dic[n-1]
            k = k%dic[n-1]
            s += str(arr[index])
            del arr[index]
            n-=1
        return s+str(arr[0])