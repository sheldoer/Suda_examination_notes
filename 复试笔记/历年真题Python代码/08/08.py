def _read_word():
    """
    **要求：`2008`年复试上机题**
    * 用`IE`从`FTP`上下载`org.dat`，并保存在`D`盘的根目录中.
    * 此文件中按文本方式存放了一段其他文章，其中有若干长度小于`15`的英文单词，
    单词之间用空格分开，无其他符号.
    * 顺序读取这段文章的不同的单词(大小写敏感)，
    同时在读取的过程中排除所有的单词`THE`以及变形，即这些单词不能出现在读取的结果中.
    * 将读取的所有单词的首字母转大写后，输出`D`根目录下`new.txt`，每个单词一行.
    **程序：**
    """
    source = open('org.dat', encoding='utf-8')
    words = [x.title() for x in ' '.join(source.readlines()).split()]
    source.close()
    word_times = {}
    file = open('new.txt', 'a', encoding='utf-8')
    for word in words:
        if word == 'The':
            continue
        if word_times.get(word):
            continue
        word_times[word] = word_times.get(word, 0) + 1
        file.writelines(word + '\n')
    file.close()
_read_word()
