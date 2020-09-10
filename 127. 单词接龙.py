class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        flag = len(wordList)
        ans = self.help(beginWord, endWord, wordList)
        if ans >= flag+1:
            return 0
        return ans+1

    def help(self, beginWord, endWord, wordList):
        re = []
        print(wordList)
        for _ in wordList:
            i = 0
            for __ in beginWord:
                if __ in _:
                    i += 1
            if i == len(beginWord) - 1:
                if _ == endWord:
                    return 1
                else:
                    re.append(_)
        if len(re) == 0:
            return 99
        else:
            min_num = len(wordList) + 1
            temp = wordList[:]
            for _ in re:
                wordList.remove(_)
                a = 1 + self.help(_, endWord, wordList)
                wordList = temp[:]
                min_num = min(a, min_num)
            return min_num
a  = Solution()
print(a.ladderLength("hot",
"dog",
["hot","cog","dog","tot","hog","hop","pot","dot"]))