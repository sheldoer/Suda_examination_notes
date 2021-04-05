def is_prime(n):
    #判断n是否为素数
    edg=int(n**0.5)+1
    for i in range(2,edg):
        if n%i==0:
            return False
    return True

def write_file():
    #将合适的数字写入result文件中
    with open("result.txt",'w')as fp:
        for i in range(100,1000):
            if is_prime(i) and '9' not in str(i):
                fp.write(str(i)+'\n')
    fp.close()

def main():
    #主函数
    write_file()

if __name__=="__main__":
    main()
