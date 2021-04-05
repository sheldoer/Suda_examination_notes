def _count_():
    """
    2005
     ``统计篇文章中各英文字母的个数，并排序.
    """
    file = open('word.txt','r', encoding='utf-8')
    txt = ''.join(file.readlines())
    file.close()
    dic = {}
    for c in txt:
        if 'a' <= c <= 'z' or 'A' <= c <= 'Z':
            dic[c] = dic.get(c, 0) + 1
    print(dic)
    ls = list(dic.items())
    print(ls)
    ls.sort(key=lambda c: c[1])
    print(ls)
    for i, j in ls:
        print("{} ：{} 次".format(i, j))
    
_count_()
