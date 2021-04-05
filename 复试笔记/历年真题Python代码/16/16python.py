def read_file():
    with open("input.txt", 'r') as fp:
        words = fp.read().split()
    word = sorted(set(words), key=words.index)
    res = []
    for i in word:
        res.append(words.count(i))
    with open("output.txt", 'w')as fp:
        for i in range(len(res)):
            if res[i] > 1:
                fp.write(str(word[i])+':'+str(res[i])+'\n')


def main():
    read_file()


if __name__ == "__main__":
    main()
    with open("output.txt", 'r')as fq:
        print(fq.read())
