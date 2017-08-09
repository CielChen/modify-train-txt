'''
Function：将原始训练集改为libsvm所需的训练集格式
Date: 08/09/2017
Author: Ciel
'''

#打开原始训练集rawtrain.txt
rawtrainFile=open("F:\Code\libsvm\Data\\trainData\\rawtrain.txt","r")
#rawtrainFile=open("F:\Code\modify-train-txt\\test.txt","r")  #测试文件

#新建格式满足libsvm的训练集
newtrainFile=open("F:\Code\libsvm\Data\\trainData\\train.txt","w")
#newtrainFile=open("F:\Code\modify-train-txt\\modify.txt","w")  #测试文件

#逐行读取
fileEnd=0  #fileEnd：读到txt文件结尾的标志。0表示没有到结尾，1到了结尾
#rowNum=0  #rowNum：txt的行数
while not fileEnd:
    lineContent=rawtrainFile.readline()  #lineContent：每行内容

    if(lineContent != ''):
        #rowNum=rowNum+1

        #默认分隔符为空格（不管有几个空格），进行分割字符串lineContent，存入splitLine中
        splitLine=lineContent.split()
        colNum=len(splitLine)  #colNum=列数，下标0~n-1
        #print(colNum)
        '''
        修改格式为libsvm的训练集，即
        <label> <index1>:<value1> <index2>:<value2> ...
        rawtrain.txt中，每行有344列
        第2列为label，第3-344列为342个特征的value
        '''
        for i in range(1, colNum):
            if(i==1):
                newtrainFile.write(splitLine[i])
                newtrainFile.write(' ')
            else:  #<index>:<value>
                newtrainFile.write(str(i-1))
                newtrainFile.write(':')
                newtrainFile.write(splitLine[i])
                newtrainFile.write(' ')
            if(i==colNum-1):  #此行结束，换行
                newtrainFile.write('\n')
            
    else:
        fileEnd=1

#print(rowNum)

rawtrainFile.close()
newtrainFile.close()
