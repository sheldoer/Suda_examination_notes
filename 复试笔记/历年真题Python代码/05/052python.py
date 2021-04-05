def is_prime(n):
    #判断n是否为素数
    if n<2:
        return False
    if n==2:
        return True
    top=int(n**0.5)+1
    for i in range(2,top):
        if n%i==0:
            return False
    return True

def n_split(num:int,res:list):
    if num<2:
        return
    if is_prime(num):
        res.append(num)
        return
    for i in range(num,1,-1):
        if is_prime(i) and num-i>1:
            res.append(i)
            n_split(num-i,res)
            return

def main():
    res=[]
    while True:
        num=int(input("请输入待分裂的数字:"))
        n_split(num,res)
        print(res)
        res.clear()

if __name__=='__main__':
    main()
    
    
