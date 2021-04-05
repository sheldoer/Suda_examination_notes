def _922(lst):
    snum=[x for x in lst if x%2!=0]
    onum=[y for y in lst if y%2==0]
    num=[]
    for i in range(len(lst)//2):
        num.append(onum[i])
        num.append(snum[i])
    return num
if __name__=='__main__':
    print(_922([4,2,5,7]))
    
