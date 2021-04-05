def is_prime(n):
    #判断是不是素数
    edg=int(n**0.5)+1  #设定除数的上限,该数的开平方向下取整加一
    for i in range(2,edg):
        if n%i==0:
            return False
    return True

def main():
    #实现主函数
    fp=open('result.txt','w')
    for j in range(10,1000):
        if is_prime(j) and is_prime(int(str(j)[::-1])): #判断数字与反数是否为素数
            fp.write(str(j)+'\n')
    fp.close()

if __name__=="__main__":
    main()
    
