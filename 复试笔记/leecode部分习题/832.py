def _832(lst):
    length=len(lst)
    for i in range(length):
        lst[i].reverse()
        for j in range(len(lst[0])):
            if lst[i][j]==0:
                lst[i][j]=1
            else:
                lst[i][j]=0
    return lst
if __name__=='__main__':
    lst= [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
    print(_832(lst))
