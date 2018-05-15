from numpy import *
import operator
def classify0(inX,dataSet,labels,k):
    dataSetSize=dataSet.shape[0]
    X=tile(inX,(dataSetSize,1))
    distance=X-dataSet
    sqdistance=distance**2
    sumaqdistance=sqdistance.sum(axis=1)
    fdistance=sqrt(sumaqdistance)
    sorteddistance=fdistance.argsort()
    notedlabels={}
    for i in range(k):
        votelabel=labels[sorteddistance[i]]
        notedlabels[votelabel]=notedlabels.get(votelabel,0)+1       #字典.get()方法的意思是有votelabel的话返回对应的键值没有的话返回0
        sorednotedlabels=sorted(notedlabels.items(),key=operator.itemgetter(1),reverse=True)
        return sorednotedlabels[0][0]