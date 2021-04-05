def sort_army(mat,k):
    res=[]
    for i in range(len(mat)):
        res.append((mat[i].count(1),i))
    res.sort(key=lambda x:x[0])
    row=[res[i][1] for i in range(k)]
    return row
mat=[[1,1,0,0,0],
     [1,1,1,1,0],
     [1,0,0,0,0],
     [1,1,0,0,0],
     [1,1,1,1,1]]
print(sort_army(mat,3))
        
mat = [[1,0,0,0], [1,1,1,1], [1,0,0,0], [1,0,0,0]]
print(sort_army(mat,2))
