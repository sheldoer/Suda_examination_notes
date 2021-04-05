def count_1(lst):
    mcnt=0
    length=len(lst)
    for i in range(length):
        if lst[i]==1:
            cnt=1
            for j in range(i+1,length):
                if lst[j]!=1:
                    break
                cnt+=1
            if cnt>mcnt:
                mcnt=cnt
    return mcnt
if __name__=='__main__':
    print(count_1([1,1,0,1,1,1]))
            
