# 实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。
#
# 示例:
#
# Trie trie = new Trie();
#
# trie.insert("apple");
# trie.search("apple");   // 返回 true
# trie.search("app");     // 返回 false
# trie.startsWith("app"); // 返回 true
# trie.insert("app");
# trie.search("app");     // 返回 true
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/implement-trie-prefix-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# 字典的每层是每个在当前字母不同的字典 举例 例如 appc 和apple  字典为
# {a:{p:{p:{l:{e:{'end'= 1}},c:{'end' = 1}}}}
# end表示到这里为一个完整单词
class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        dic = self.dic
        for _ in word:
            if _ not in dic:
                dic[_] = {}
                dic = dic[_]
            else:
                dic = dic[_]
        dic['end'] = 1

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        tree = self.dic
        for _ in word:
            if _ in tree:
                tree = tree[_]
            else:
                return False

        if 'end' not in tree:
            return False
        return True

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        tree = self.dic
        for _ in prefix:
            if _ in tree:
                tree = tree[_]
            else:
                return False
        return True