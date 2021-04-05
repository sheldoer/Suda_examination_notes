def _by_2016():
    """
    ##### `2016`年保研上机题
    ** 要求： **
    *请从服务器将两个数据文件 `input.txt` 和 `words.txt`   下载到本地电脑的 `D`  盘根文件夹。
    *在  `D`  盘根文件夹的  `words.txt`  中存储了不超过  `30000`条的英文单词，每个单词占一行。单词的最大长度为`20`，
    且单词内部没有空格，文件中无重复单词。
    *在D盘根文件夹的 `input.txt` 中存储了一个「丢失」了空格和标点符号的英文文章。每行不超过 `128`个字符，请编写程序把
    该文章中第一行和最后一行显示在屏幕上。
     *编写程序将 `words.txt`中的最后三行显示在屏幕上； *编写程序利用 `words.txt`    中的单词作为词典，采用正向最大
     匹配切分单词算法对   `input.txt`    中的文本进行单词切分。切分时单词区分大小写， 切分分割标记采用空格，并将切分
     后的结果写入到`out.txt` 中。
    所谓正向最大匹配切分就是从左向右扫描待切分字符串，尽量取长词。 下面举一个简单例子：现有待切分字符串`ABCDEFGHIJ`，
    设词典中最大单词长度为`5`。那么按照算法首先取出`ABCDE`判断是否是单词， 如果是则切分到一个单词，否则舍弃最后一个字母接着判断，
    也就是判断`ABCD`是否是单词，依此类推，当只有一个字母时可以直接认定为是单词。 在成功切分出一个单词后对待切分字符串余下的部分
    再次执行上述过程。 *编写程序实现步骤`2`、`3` 描述的要求，并通过如下所示的主函数对进行验证，注意：除了指定添加的代码之外，不得修改
    `main` 函数其余部分。对  `main` 函数每修改一处，总分扣 `3` 分，最多扣    `10` 分。
    *本次考试考核
    `C` 语言程序设计，因此不可以使用`C + +`的` STL
    `的任何功能，如果需要添加下面样例之外的程序头文件，请举手得到监考老师批准。
    ** 程序： **
    '"""

    def read_file():
        with open('words.txt', encoding='utf-8') as f:
            words = f.read().split('\n')
        with open('input.txt', encoding='utf-8') as f:
            txt = f.read().split('\n')
        print(txt[0])
        print(txt[-1])
        i = -3
        if len(words) > 2:
            print(words[i])
            i += 1
        w = {}
        m = 0
        for word in words:
            le = len(word)
            if le > m:
                m = le
            w[word] = 1
        w['max_length'] = m
        return w, txt

    def txt_split(dictionary: dict, txt: str):
        width = dictionary.get('max_length')
        start = 0
        end = start + width
        length = len(txt)
        answer = []
        while start < length:
            if end > length:
                end = length
            if end == start + 1:
                answer.append(txt[start])
                start = end
                end = start + width
            s = txt[start:end]
            if dictionary.get(s):
                start = end
                end = start + width
                answer.append(s)
            else:
                end -= 1
        return ' '.join(answer)

    def write_to_file(txt):
        with open('output.txt', 'w', encoding='utf-8') as f:
            f.write(txt)
