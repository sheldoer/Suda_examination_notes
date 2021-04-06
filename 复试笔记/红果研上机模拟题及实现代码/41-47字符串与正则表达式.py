import re
def func_41():
    #按要求输出字串
    s=input('input a string:')    #输入指定字符串
    if len(s)<2:                  #字数小于2则返回空
        print('')
    else:                         #或者按要求输出
        print(s[0:2]+s[-2:])
def func_42():
    #删除指定字符的第n位
    s=input('input a string:')    #输入指定字符串
    n=int(input("delete byte:"))
    print(s.replace(s[n-1],''))        #将第n位替换为空字符
def func_43():
    #对给定句子倒置
    s=input('input a string:')    #输入指定字符串
    words=s.split()[::-1]
    print(' '.join(words))
def func_44():
    #统计一个字符串中所有字符出现的次数
    s=input('input a string:')    #输入指定字符串
    keys=list(set(s))              #建立关键词列表
    values=[s.count(i) for i in keys] #建立值列表
    print(dict(zip(keys,values)))
def func_45():
    #动词的第三人称单数形式
    s=input('input a string:')    #输入一个动词
    spe=['o','s','x','z']         #单个特殊字母结尾的列表
    sep=['c','s']                 #多个特殊字母结尾的列表
    if s[-1]=='y':               #情况a
        print(s[:-1]+'ies')
    elif s[-1]in spe:             #情况b1
        print(s+'es')
    elif s[-1]=='h' and s[-2]in sep: #情况b2
        print(s+'es')
    else:                           #情况c
        print(s+'s')
def func_46():
    #
    s=input('input a string:')    #输入指定字符串
    s=re.sub('\s+',' ',s)
    s=s.replace(',',', ')
    s=s.replace('.','. ')
    print(s)
    
def func_47():
    #
    pass
def main():
    #func_41()
    #func_42()
    #func_43()
    #func_44()
    #func_45()
    func_46()
    
    pass
if __name__=='__main__':
    main()
