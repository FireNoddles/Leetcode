import numpy as np
import math

def initDataSet():
    '''
    初始化单词表
    :return:
    '''
    # 准备单词库
    postingList = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                   ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                   ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                   ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                   ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                   ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    # 对应词汇是否为侮辱性
    classVec = [0, 1, 0, 1, 0, 1]

    return postingList, classVec

def createVocabList(dataSet):
    '''
    创建单词库
    :param dataSet:
    :return:
    '''
    vocabSet = set([])
    for docement in dataSet:
        # 求并集 要用set函数 否则无法求并
        vocabSet = vocabSet | set(docement)
    # 再次转换成列表形式返回
    return list(vocabSet)

def setWordList(vocabList, inputList):
    '''
    对传入的文章进行检查是否包含词库单词的操作
    :param vocabList: 词库
    :param inputList: 传入文章
    :return: 返回单词向量
    '''
    # 初始化单位向量 描绘文章是否含有词汇表中的单词
    wordVec = [0] * len(vocabList)
    for singleWord in inputList:
        if singleWord in vocabList:
            wordVec[vocabList.index(singleWord)] = 1
        else:
            print("no this word in vocabList")

    return wordVec

def trainNavieBayes(trainVec, trainCategory):
    # 在利用贝叶斯分类器对文档进行分类时，要计算多个概率的乘积以获得文档属于某个类别的概率，即计算
    # p(w0 | 1) * p(w1 | 1) * p(w2 | 1)。如果其中一个概率值为0，那么最后的乘积也为
    # 0。为降低这种影响，可以将所有词的出现数初始化为1，并将分母初始化为2 （取1或2的目的主要是为了
    # 保证分子和分母不为0，大家可以根据业务需求进行更改）。
    # 另一个遇到的问题是下溢出，这是由于太多很小的数相乘造成的。当计算乘积
    # p(w0 | ci) * p(w1 | ci) * p(w2 | ci)...p(wn | ci)
    # 时，由于大部分因子都非常小，所以程序会下溢出或者得到不正确的答案。（用Python
    # 尝试相乘许多很小的数，最后四舍五入后会得到0）。一种解决办法是对乘积取自然对数。在代数中有
    # ln(a * b) = ln(a) + ln(b), 于是通过求对数可以避免下溢出或者浮点数舍入导致的错误。同时，
    # 采用自然对数进行处理不会有任何损失。

    # P（C_i|w) = [P(w|c_i)*P(c_i)]/P(w)
    #           = [P(X_1|C_i)*P(X_2|C_i)*..*P(c_i)]/P(x_1)P(x_2)*..
    # 传入文件数（文章数）
    '''
    原始版本算法
    numOfTrain = len(trainVec)
    # 单词库单词数量
    numOfVocab = len(trainVec[0])
    # 求出侮辱性文件出现的概率
    probOfDirty = np.sum(trainCategory)/numOfTrain
    # 单词出现的次数
    _0OfWord = [0] * len(trainVec[0])
    _1OfWord = [0] * len(trainVec[0])
    p1Demo = 0.0
    p0Demo = 0.0
    for i in range(numOfTrain):
        if trainCategory[i] == 1:
            # 在侮辱性分类下每个单词各出现多少次
            _1OfWord += trainVec[i]
            # 在侮辱性分类下总共有多少单词出现
            p1Demo += np.sum(trainVec[i])
        else:
            _0OfWord += trainVec[i]
            p0Demo += np.sum(trainVec[i])

    # 在是侮辱性的文章中每个单词出现的次数概率
    # 在不是侮辱性的文章中每个单词出现的次数概率
    p1Vect = _1OfWord / p1Demo
    p0Vect = _0OfWord / p0Demo

    return p0Vect, p1Vect, probOfDirty
    '''
    # 总文件数
    numTrainDocs = len(trainVec)
    # 总单词数
    numWords = len(trainVec[0])
    # 侮辱性文件的出现概率
    pAbusive = sum(trainCategory) / float(numTrainDocs)
    # 构造单词出现次数列表
    # p0Num 正常的统计
    # p1Num 侮辱的统计
    p0Num = [1] * numWords  # [0,0......]->[1,1,1,1,1.....]
    p1Num = [1] * numWords

    # 整个数据集单词出现总数，2.0根据样本/实际调查结果调整分母的值（2主要是避免分母为0，当然值可以调整）
    # p0Denom 正常的统计
    # p1Denom 侮辱的统计
    p0Denom = 2.0
    p1Denom = 2.0
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            # 累加辱骂词的频次
            p1Num += trainVec[i]
            # 对每篇文章的辱骂的频次 进行统计汇总
            p1Denom += sum(trainVec[i])
        else:
            p0Num += trainVec[i]
            p0Denom += sum(trainVec[i])
    # 类别1，即侮辱性文档的[log(P(F1|C1)),log(P(F2|C1)),log(P(F3|C1)),log(P(F4|C1)),log(P(F5|C1))....]列表
    p1Vect = np.log(p1Num / p1Denom)
    # 类别0，即正常文档的[log(P(F1|C0)),log(P(F2|C0)),log(P(F3|C0)),log(P(F4|C0)),log(P(F5|C0))....]列表
    p0Vect = np.log(p0Num / p0Denom)
    return p0Vect, p1Vect, pAbusive

def classifyNB(vec2Classify, p0Vec, p1Vec, Pclass1):
    p1 = np.sum(vec2Classify * p1Vec) +math.log(Pclass1)
    p0 = np.sum(vec2Classify * p0Vec) + math.log(1-Pclass1)

    if p1 > p0:
        return 1
    else:
        return 0

def test():
    listOPosts, listClasses = initDataSet()
    vobal = createVocabList(listOPosts)

    # 3. 计算单词是否出现并创建数据矩阵
    trainMat = []
    for postinDoc in listOPosts:
        # 返回m*len(myVocabList)的矩阵， 记录的都是0，1信息
        trainMat.append(setWordList(vobal, postinDoc))
    # 4. 训练数据
    p0V, p1V, pAb = trainNavieBayes(np.array(trainMat), np.array(listClasses))
    # 5. 测试数据
    testEntry = ['love', 'my', 'dalmation']
    thisDoc = np.array(setWordList(vobal, testEntry))
    print(testEntry, 'classified as: ', classifyNB(thisDoc, p0V, p1V, pAb))
    testEntry = ['stupid', 'garbage']
    thisDoc = np.array(setWordList(vobal, testEntry))
    print(testEntry, 'classified as: ', classifyNB(thisDoc, p0V, p1V, pAb))


test()