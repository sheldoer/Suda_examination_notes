def _2016():
    """
     `2016`年复试上机题
    **要求：**
    文本文件`input.txt`由若干英文单词和分隔符(空格，回车，换行)构成. 根据如下
    说明编写程序统计不同单词出现的次数(频度).
    将统计结果按出现频度从高到低排序，并将出现频度大于`5`的单词及
    其频度输出到文件`output.txt`中. 文件格式如图所示
    ![format](E:\Markdown\img\format.png)
    * 多个连续的分隔符被视为一个分隔符.
    * 大小写敏感.
    * 每个单词的长度不超过`20`个字符.
    * 单词的数量未知. 如使用定义静态大数组的方式来统计，将被扣除`5`分.
    **程序：**
    :return:
    """
    file = open('input.txt', encoding='utf-8')
    txt = file.read()
    file.close()
    import re
    res = re.split(r'\s+', txt)
    print(res)
    dic = {}
    for word in res:
        dic[word] = dic.get(word, 0) + 1
    ans = []
    for k in dic:
        if dic.get(k) > 1:
            ans.append('{}: {}'.format(k, dic.get(k)))
    with open('output.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(ans))


_2016()
with open("output.txt", 'r')as fp:
    print(fp.read())
