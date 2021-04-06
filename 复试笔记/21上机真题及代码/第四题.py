'''
第四题题目:给定一些列集合的数组，从中找到所有数字的出现率高于出现一半的数字，
并以集合的形式返回该数字，如果没有，则返回None
'''
def find_major(L):
    length=len(L)
    lst=[]
    res=set()
    for i in L:
        for j in list(i):
            lst.append(j)
    for i in set(lst):
        if lst.count(i)>length/2:
            res.add(i)
    if len(res)>0:
        return res


if __name__=='__main__':
    L=[{1},{1,2},{1}]
    #L=[{1},{2,3}]
    print(find_major(L))
    
