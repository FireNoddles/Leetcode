# 给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？
#
# 示例:
#
# 输入: 3
# 输出: 5
# 解释:
# 给定 n = 3, 一共有 5 种不同结构的二叉搜索树:
#
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/unique-binary-search-trees
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 标签：动态规划
# 假设n个节点存在二叉排序树的个数是G(n)，令f(i)为以i为根的二叉搜索树的个数，则
# G(n) = f(1) + f(2) + f(3) + f(4) + ... + f(n)G(n)=f(1)+f(2)+f(3)+f(4)+...+f(n)
#
# 当i为根节点时，其左子树节点个数为i-1个，右子树节点为n-i，则
# f(i) = G(i-1)*G(n-i)f(i)=G(i−1)∗G(n−i)
#
# 综合两个公式可以得到 卡特兰数 公式
# G(n) = G(0)*G(n-1)+G(1)*(n-2)+...+G(n-1)*G(0)G(n)=G(0)∗G(n−1)+G(1)∗(n−2)+...+G(n−1)∗G(0
#
# 作者：guanpengchn
# 链接：https://leetcode-cn.com/problems/unique-binary-search-trees/solution/hua-jie-suan-fa-96-bu-tong-de-er-cha-sou-suo-shu-b/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


# (2n)! / (n!(n+1)!)
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        temp = 1

        for i in range(1, 2 * n + 1):
            temp = temp * i
            if i == n:
                a = temp
            if i == n + 1:
                b = temp
            if i == 2 * n:
                c = temp
        return c / (a * b)

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0 for i in range(n+1)]
        dp[0]=1
        dp[1] = 1
        for i in range(2, n+1):
            for j in range(1, i+1):
                dp[i]+= dp[j-1] * dp[i-j]
        return dp[n]