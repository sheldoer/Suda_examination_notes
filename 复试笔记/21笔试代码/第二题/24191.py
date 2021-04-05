def find_number(n):
    res=[]
    for i in range(n+1):
        s=bin(i)[2:]                #remove '0b'
        if s.count('1')>s.count('0'):
            res.append(i)
    return res
if __name__=='__main__':
    print(find_number(15))
        
