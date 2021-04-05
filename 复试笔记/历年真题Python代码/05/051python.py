def count_nums():
    #实现函数
    fp=open('word.txt','r',encoding='utf-8')
    txt=''.join(fp.readlines())
    fp.close()
    dic={}
    for w in txt:
        if 'a'<=w<='z' or 'A'<=w<='Z':
            dic[w]=dic.get(w,0)+1
    
    ls=list(dic.items())
    ls.sort(key=lambda c:c[1])
    for i,j in ls:
        print("%3s:%3d"%(i,j))
def main():
    count_nums()

if __name__=="__main__":
    main()
