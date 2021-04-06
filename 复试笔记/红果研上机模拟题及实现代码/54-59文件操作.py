def func_54():
    #复制文件
    fp=open('copy.txt','r')
    fq=open('new.txt','w')
    res=fp.readlines()        #读取copy文件
    #print(res)
    '''
    for i in res:
        fq.write(i)       
        #print(i)'''
    fq.writelines(res)  #写new文件
    fp.close()
    fq.close()
def func_55():
    #对文件里的数字进行处理，写入新文件
    fp=open('numbers.txt','r')
    fq=open('Sort.txt','w')
    res=list(map(eval,fp.read().split()))   #将读取的字符列表转换为数字列表
    res.sort()
    for i in res:
        fq.write(str(i)+'\n')               #从小到大依次写入文件
    aver=sum(res)/len(res)
    fq.write(str(aver)+'\n')                #写入平均数    
    vari=0
    for i in res:
        vari+=(i-aver)**2                   #计算方差
    fq.write(str(vari/len(res)))            #写入方差
    fp.close()
    fq.close()
def func_56():
    #文件合并
    fp1=open('folder/file1.txt','r')
    fp2=open('folder/file2.txt','r')
    fp3=open('folder/file3.txt','r')
    fp4=open('folder/file4.txt','r')
    fq=open('folder/merge.txt','w')
    f1=fp1.readlines()
    f2=fp2.readlines()
    f3=fp3.readlines()
    f4=fp4.readlines()
    fq.writelines(f1)
    fq.write('\n')
    fq.writelines(f2)
    fq.write('\n')
    fq.writelines(f3)
    fq.write('\n')
    fq.writelines(f4)
    fp1.close()
    fp2.close()
    fp3.close()
    fp4.close()
    fq.close()
def func_57():
    #找出文件中的所有非以元音开头的单词，输入到新文件中
    fp=open('word.txt','r')
    fq=open('new_word.txt','w')
    f=fp.readlines()
    vo=['a','e','i','o','u']          #构建元音字列表
    for i in range(len(f)-1,-1,-1):   #从索引逆序查找
        if f[i].lower()[0] in vo:     #判断小写的首字母是否为元音字母，是则删除
            del f[i]
    fq.writelines(f)         
    fq.close()
    fp.close()
def func_58():
    #按字母排序向名字列表里插入名字
    fp=open('names.txt','r')
    fq=open('new_names.txt','w')
    names=fp.read().split()                 #读取文件里的名字生成列表
    names.append(input('input new name:'))  #输入添加的新名字
    names.sort()                            #利用列表内置排序
    for i in names:
        fq.write(i+'\n')                    #依次写入文件
    fq.close()
    fp.close()
def func_59():
    #
    pass                           #不会
def main():
    #func_54()
    #func_55()
    #func_56()
    #func_57()
    #func_58()
    #func_59()                      #未作出
    pass
if __name__=='__main__':
    main()
