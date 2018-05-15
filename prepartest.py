from numpy import *                       #如果是import numpy 则每次使用numpy属性都需要加上去numpy,但是from numpy import *可以不用加上numpy
import operator
from os import listdir
def file2matrix(filename):
    fr = open(filename)
    arrayOLines=fr.readlines()                    #这里千万不能把readlines()函数写成readline()函数
    numberlines=len(arrayOLines)
    returnMat=zeros((numberlines,3))
    classlabelvector=[]       #创建一个数组[]
    index=0
    for line in arrayOLines:
        line=line.strip()
        listFormLine = line.split('\t')  # s使用spilt()函数将得到的一整行数据分割成一个具有三个元素的元素列表
        returnMat[index,:]=listFormLine[0:3]
        classlabelvector.append(int(listFormLine[-1]))
        index+=1
    return returnMat,classlabelvector