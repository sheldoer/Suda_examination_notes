def _to_num():
    """
     `2009`年复试上机题
    **要求：**
    * 用`IE`浏览器从`FTP`上下载`org.dat`，并保存在`D`盘的根目录下.
    * 此文件中按文本方式存放了一段其他文章，其中有若干长度小于`15`
      的十进制或八进制数字，数字之间用`,`分开，数字内部存在且仅存在空格.
    * 八进制数以起始位`0`作为标示与十进制数区分.
    * 顺序读取这些数字将他们转变为十进制数后按从大到小的顺序排序后，
      输出到`D`盘根目录下`new.txt`，每个数字一行.
      `eg`：`_235_,34__2,_043_1_,1_3`，分别是：十进制`235`，十进制`342`，
       八进制`431`，十进制`13`，`_`代表空格.
    **程序：**
    """
    source = open('org.dat', encoding='utf-8')
    words = [x.strip() for x in ','.join(source.readlines()).split(',')]
    source.close()
    ans = []
    for word in words:
        word = word.replace(' ', '')
        if word[0] == '0':
            n = '0o' + word[1:]
            ans.append(str(eval(n)))
        else:
            ans.append(word)
    file = open('new.txt', 'w', encoding='utf-8')
    file.write('\n'.join(ans))
    file.close()
_to_num()
