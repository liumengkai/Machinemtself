from numpy import *
import operator
def Classify0(inX,dataSet,labels,k):
    dataSetSize=dataSet.shape[0]           #这里要用方括号
    diffMat=tile(inX,[dataSetSize,1])-dataSet
    sqdiffMat=diffMat**2
    sqDistance=sqdiffMat.sum(axis=1)
    distance=sqDistance**1/2
    sortedDisstance=distance.argsort()                   #argsort()排序会返回被排序的序号不是值
    classCount={}                                  #创建一个字典，键值分别对应标签以及该标签出现的次数
    for i in range (k):
        voteIlabel=labels[sortedDisstance[i]]        #将labels中的前k个标签分别给voteIlabel
        classCount[voteIlabel]=classCount.get(voteIlabel,0)+1
    sortedClassCount=sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]