def func_48():
    #计算一组数的方差
    res=(65.5,70.2,100.5,45.5,88.8,55.5,73.5,67.8)
    aver=sum(res)/len(res)       #先求出平均数
    variance=0
    for i in res:
        variance+=(i-aver)**2     #将每个方差累加起来
    print(variance/len(res))
def func_49():
    #在程序中创建两个字典，找出并显示两个字典中相同的键。
    a={'x':1,'y':2,'z':3}
    b={'o':2,'p':3,'x':4}
    print(a.keys()&b.keys())
    #print(a.values()& b.values())    #报错
def func_50():
    #在程序中创建两个字典，找出并显示两个字典中具有相同值
    a={'x':1,'y':2,'z':3}
    b={'o':2,'p':3,'x':4}
    for i in a.items():
        if i[1] in b.values():          
            print(i[0])
def func_51():
    #
    name=0
    dic={}
    while name!='q':
        name=input("name:",end=':')
        eid=eval(input("id:"))
        
        dic[name]=eid
    
    for i,j in dic.items():
        print(i)
        print("id:name:{}{}".format(j,i))
def print_lst(lst:list,n:int):
    for i in range(int(len(lst)/n)):
        for j in range(n):
            if n*i+j<len(lst):
                print('{:5}'.format(lst[i*n+j]),end='')
        print()
def func_52():
    #求两个集合的相同数据与不同数据
    from random import randint
    res1=set(randint(0,500) for i in range(201))
    res2=set(randint(0,500) for i in range(201))
    same=res1&res2            #先求交集
    dif=(res1|res2)-same       #后利用并集减去交集，求不同的数据
    same=list(same)
    dif=list(dif)              #转换为列表，方便索引
    print_lst(same,10)
    print()
    print_lst(dif,10)
def func_53():
    #
    pass
    
    
def main():
    #func_48()
    #func_49()                  #little wrong
    #func_50()                  #little wrong
    #func_51()                  #未作出
    #func_52()
    func_53()
    pass
if __name__=='__main__':
    main()
