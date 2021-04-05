def order_sequence(words:list,order:str):
    '''length=min(len(i) for i in words)    #找到最小长度
    for i in range(length):
        words[0][i]>words[1][i]'''
    length=len(words)
    for i in range(length):
        A=words[i]
        for j in range(i+1,length):
            B=words[j]
            n=0
            mlen=min(len(A),len(B))
            while n<mlen and words[i][n]==words[j][n]:
                    n+=1
            if n==mlen==len(B):
                return False
            else:
                continue
            if order.index(A[n])<order.index(B[n]):
                continue
            else:
                return False

    return True
    
def main():
    words = ["ap","app",'joim']
    order = "abcdefghijklmnopqrstuvwxyz"
    print(order_sequence(words,order))
if __name__=='__main__':
    main()
    
