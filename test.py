import multiprocessing,time

def out(index,c):
    # print('index ',index)
    a = c.recv()
    print('index ', index, a)
    for i in range(index):

        c.send(i)
        print(c.recv())

def print_double_num():
    i = 2
    try:
        while i<1000:
            print(i)
            i+=2
            yield
    except StopIteration:
        pass

def print_add_num():
    i =1
    while i<1000:
        print(i)
        i += 2
        yield
if __name__ == '__main__':
    # import threading
    # c = threading.Lock()
    # t1 = threading.Thread(target=print_add_num,args=(c,))
    # t2 = threading.Thread(target=print_double_num, args=(c,))
    # t2.start()
    # t1.start()
    a = print_add_num()
    b = print_double_num()
    while 1:
        try:
            next(a)
            next(b)
        except StopIteration:
            break

    # con1, con2 = multiprocessing.Pipe(False)
    # con1.send(1)
    # a = con1.recv()
    # print(a)
    # for i in range(4):
    #     p = multiprocessing.Process(target=out, args=(i,con1))
    #     con2.send('000')
    #     p.start()
    # p.join()
    # for i in range(6):
    #     data = con2.recv()
    #     print(data)
    # a = 'sss'
    # import copy
    # b = copy.deepcopy(a)
    # b = a[:]
    # print(id(a),id(b))
    # b = b+a
    # print(id(a), id(b))
    # a = [1,2,3]
    # b = [4,5,6]
    # print(type(zip(a,b)))
    # while 1:
    #     a = input()
    #     temp = list(map(int, a.split()))
    #     print(temp)
    #     N = temp[0]
    #     M = temp[1]
    #     print(N,M)

