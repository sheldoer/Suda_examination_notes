def find_use(A):
    res=[]
    for i in A[0]:
        flag=1
        for j in A:
            if i not in j:
                flag=0
                break
        if flag==1:
            res.append(i)
        
                
    return res

if __name__=="__main__":
    A=["bella","label","roller"]
    print(find_use(A))
