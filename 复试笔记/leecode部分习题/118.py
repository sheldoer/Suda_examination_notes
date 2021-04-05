def gene_tri(num):
    if num==1:
        return [[1]]
    if num==2:
        return [[1],[1,1]]
    res=[[1],[1,1]]
    for i in range(2,num):
        nrow=[1]
        for j in range(i-1):
            nrow.append(res[i-1][j]+res[i-1][j+1])
        nrow.append(1)
        res.append(nrow)
    return res
if __name__=='__main__':
    print(gene_tri(5))
