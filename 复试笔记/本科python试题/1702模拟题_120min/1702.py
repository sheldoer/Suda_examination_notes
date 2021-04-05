def readWordsFromFile(url):
    # ----从data.txt文件中读取所有单词-------
    with open(url,'r')as fp:
        lst=fp.read().split()    #将读取的文件存入列表
    for i in range(len(lst)):
        lst[i]=lst[i].strip(',') #去除逗号
        lst[i]=lst[i].strip('.') #去除句号
    fp.close()
    return lst
def findMultiAlphaWords(lst, n):
     # ----找出单词中，存在某个字母重复num次的单词-----
    wlst=[]
    #clst=[]
    #lst=list(set(lst))
    for i in lst:
        word=i.lower()             #将单词所有字母小写，以便检测出现频率
        #if word not in clst:
            #clst.append(word)
        for j in word:
            if word.count(j)>=n:   #检查单词里出现频次大于n的
                wlst.append(i)
                break               
    return wlst
def delMultiData(wlst):
    # ----删除wordResultLst中重复单词的多余份数，只保留一份-----
    for i in wlst:
        if wlst.count(i)>1:         #将出现频次单词重复的单词逐个去除
            wlst.remove(i)
def printWordLst(wlst, n):
    #输出所有单词，每行输出4个单词
    for i in range(int(len(wlst)/n)+1):  #先分行输出
        for j in range(n):               #每行输出n个单词
            m=i*4+j
            if m<len(wlst):
                print('{:20}'.format(wlst[m]),end='') #格式化输出
        print()                                       #每行结束换行
def getNumberOfWords(wlst):
    # ----将wordResultLst中的所有单词转换为整数------
    numlst=[]
    for i in wlst:
        num=0
        for j in i:
            num+=ord(j)         #利用ord函数将字母转换为数字并累加
        numlst.append(num)
    return numlst

def sortByDigitalSum(numlst):
    # ----对numlst中的所有整数进行根据数字累加和进行降序排序----
    selst=[]
    for i in numlst:
        se=0
        for j in str(i):
            se+=int(j)
        selst.append(se)           #将每个数字进行累加，组成排序相同的列表
    dic=dict(zip(numlst,selst))    #建立成字典
    new=sorted(dic.items(),key=lambda x:x[1],reverse=True) #根据要求排序
    numlst.clear()                 
    for i in new:
        numlst.append(i[0])     #重组numlst
    #print(numlst)
def printNumLst(wlst, n):
    #输出整数列表，每行输出5个整数
    for i in range(int(len(wlst)/n)+1): #先分行输出
        for j in range(n):               #每行输出n个单词
            m=i*n+j
            if m<len(wlst):
                print('{:8}'.format(wlst[m]),end='')
        print()                            #每行结束换行
def staticDigitalTimes(numlst):
    # ----统计数字出现的次数----------
    s=''
    for i in numlst:         #将所有数字组成字符串，方便计数
        s+=str(i)
    keys=list(set(s))            #去重得到关键字列表
    values=[s.count(i) for i in keys]   #利用count函数建立值列表
    rdic=dict(zip(keys,values))
    #print(rdic)
    return rdic
def printDicToFile(url, rdic):
    #输出出现频率最大的数字到文件
    mnum=max(rdic.items(),key=lambda x:x[1])
    fp=open(url,'w')
    fp.write('{:<2}:{:3}'.format(mnum[0],mnum[1]))   #根据要求输出
    fp.close()
    print('{:<2}:{:3}'.format(mnum[0],mnum[1]))         
    
def main():
    pass
if __name__ == "__main__":
    # ----从data.txt文件中读取所有单词-------
    wordlst = readWordsFromFile("data.txt")
    print("文件中单词个数:", len(wordlst))  # 输出单词个数

    # ----找出单词中，存在某个字母重复num次的单词-----
    wordResultLst = findMultiAlphaWords(wordlst, 2)
    print("至少含有重复2次的字母的单词：", len(wordResultLst))

    # ----删除wordResultLst中重复单词的多余份数，只保留一份-----
    delMultiData(wordResultLst)
    print("===删除重复单词的多余单词后的结果===")
    printWordLst(wordResultLst, 4)  #输出所有单词，每行输出4个单词
    
    # ----将wordResultLst中的所有单词转换为整数------
    numlst = getNumberOfWords(wordResultLst)

    # ----对numlst中的所有整数进行根据数字累加和进行降序排序----
    sortByDigitalSum(numlst)
    #print(numlst)
    print("===整数降序排序的结果===")
    printNumLst(numlst, 5)    #输出整数列表，每行输出5个整数 
    
    # ----统计数字出现的次数----------
    resultDic = staticDigitalTimes(numlst)
    print("===出现次数最多的数字===")
    printDicToFile("result.txt", resultDic)
