from random import randint
def productRndNum():
    # ----产生随机整数-------
    rnd=randint(100,200)          #产生一个随机整数
    numlst=[randint(100,500) for i in range(rnd)]  #产生随机rnd个数的列表
    return numlst
def getDigNumber(numlst, dlst):
    # ----找出包含数字2或6的整数，其中digLst包含数字2和6-----
    n26lst=[]
    for i in numlst:
        for j in dlst:
            if str(j) in str(i):  #如果该数字出现dlst里的数字，则加入目标列表
                n26lst.append(i)
                break
    return n26lst
def printOut(n26lst,n):
    #输出n26lst列表
    for i in range(int(len(n26lst)/n)+1):
        for j in range(n):
            if i*n+j<len(n26lst):
                print('{:5}'.format(n26lst[i*n+j]),end='')
        print()
def getDivisorNum(n26lst):
    #-----找出所有整数的因子-----
    rlst=[]                                 #建立一个因子列表
    for i in n26lst:                        #依次遍历列表中的每一个数
        for j in range(2,int(i**0.5)+1):
            if i%j==0:                      #将因子加入集合中
                rlst.append(j)
                rlst.append(int(i/j))
    return rlst
def staticResult(rlst):
    #-----统计每个因子出现的次数-----
    keys=list(set(rlst))                   #建立关键字列表
    values=[rlst.count(i) for i in keys]   #建立值列表
    dic=dict(zip(keys,values))             #根据关键字和值组成字典
    rdic=sorted(dic.items(),key=lambda x:x[1],reverse=True)  #对字典进行出现频次排序
    #print(rdic)
    return rdic
def printMax5Out(rdic):
    #输出频次出现高的五个数字
    for i in range(5):     #只输出列表的前五位即可
        print('{:5}:{:5}'.format(rdic[i][0],rdic[i][1]))
def delMultiDivisor(rlst):
    # ----删除resultLst中重复因子的多余份数，只保留一份-----
    rs=set(rlst)
    rlst.clear()      #将rlst清空
    for i in rs:
        rlst.append(i) #将无重复的数字添加到列表

def printDivisorToFile(url, rlst):
    #输出去重后的因子
    fp=open(url,'w')
    for i in range(int(len(rlst)/8)+1):   #总共输出几行
        for j in range(8):                #每行输出8个
            if i*8+j<len(rlst):           #如果该位置有数就输出
                fp.write('{:5}'.format(rlst[i*8+j]))
                print('{:5}'.format(rlst[i*8+j]),end='')
        fp.write('\n')
        print()
    fp.close()
    
if __name__ == "__main__":
    # ----产生随机整数-------
    numberLst = productRndNum()
    
    # ----找出包含数字2或6的整数，其中digLst包含数字2和6-----
    digLst=[2,6]
    num26Lst = getDigNumber(numberLst, digLst)
    printOut(num26Lst, 8)

    #-----找出所有整数的因子-----
    resultLst = getDivisorNum(num26Lst)
    #-----统计每个因子出现的次数-----
    resultStatic = staticResult(resultLst)
    printMax5Out(resultStatic)

    # ----删除resultLst中重复因子的多余份数，只保留一份-----
    print(resultLst)
    delMultiDivisor(resultLst)
    print(resultLst)

    print("===出现次数最多的数字===")
    printDivisorToFile("result.txt", resultLst)
