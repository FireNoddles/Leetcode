class Solution(object):
    def __init__(self,N):
        self.__name = N
    @property
    def name(self):
        print(666)
        return self.__name
    @name.setter
    def name(self,N):
        self.__name = N


# 前序和中序的区别是一个是边入栈边访问 第二个是出栈在访问
def previsit(head):
    arr = []
    stack = []
    p = head
    while p != None or stack:
        while p:
            arr.append(p.val)
            stack.append(p)
            p = p.left
        p = stack.pop().right


def midvisit(head):
    arr = []
    stack = []
    p = head
    while p != None or stack:
        while p:
            stack.append(p)
            p=p.left
        temp = stack.pop()
        arr.append(temp.val)
        p = temp.right


def lasvisit(head):
    arr = []
    stack = []
    p = head
    while p != None or stack:
        while p:
            stack.append(p)
            p = p.left if p.left else p.right
        temp = stack.pop()
        arr.append(temp.val)
        # 判断出来的是左还是右 如果是左则访问右
        if stack and stack[-1].left == temp:
            p = stack[-1].right
        #如果是右就可以访问上一层
        else:
            p = None





# arr = list(input().split())
# n = int(arr[0])
# p = int(arr[1])
# q = int(arr[2])
# p_arr = set(map(int,input().split()))
# q_arr = set(map(int,input().split()))
#
# common = p_arr.intersection(q_arr)
# p_arr -= common
# q_arr -= common
#
#
# print(len(p_arr),len(q_arr), len(common))

# arr = input()
# dic = {'upper':0, 'lower':0}
# for _ in arr:
#     if _.isupper():
#         dic['upper'] +=1
#     else:
#         dic['lower'] += 1
# print(int(abs(dic['upper']- dic['lower'])/2))


# n = int(input())
# arr = list(map(int,input().split()))
# flag = 0
# positive = []
# t = arr[:]
# for _ in arr:
#     if _ == 1:
#         positive.append(_)
#         t.remove(_)
# if len(positive) < 2:
#     flag = 1
# while len(positive)>1:
#     a1 = min(positive)
#     positive.remove(a1)
#     a2 = min(positive)
#     positive.remove(a2)
#     temp = a1+a2
#     if temp+1 not in t or len(t)==0:
#         flag = 1
#         break
#     else:
#         positive.append(temp+1)
#         t.remove(temp+1)
#     if len(t) == 0:
#         break
# if flag==1:
#     print('NO')
# else:
#     print('YES')
#
#
# n = int(input())
#
# if n < 0: print(0)
# arr = list(map(int,input().split()))
#
# def help(n,i):
#     ret = i % 1
#     for j in range(2,n+1):
#         ret = ret ^ (i%j)
#     return ret
#
# ans = help(n, 1) ^ arr[0]
# if n==1:
#     print(ans)
#
# else:
#     for j in range(1,n):
#         ans = ans ^ help(n,j+1) ^ arr[j]
#     print(ans)





# 单例
class Animal(object):
    __isinstance = None
    def __new__(cls, *args, **kwargs):
        if cls.__isinstance == None:
            cls.__isinstance = super().__new__(cls)
            return cls.__isinstance
        else:
            return cls.__isinstance

a = Animal()
b = Animal()
print(id(a),id(b))